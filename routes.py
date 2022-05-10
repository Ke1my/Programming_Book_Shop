"""
Routes and views for the bottle application.
"""

from collections import deque
from bottle import route, view, abort, response, post, request, redirect
from datetime import datetime
from sqlalchemy.orm import Session
import argon2

import orm

COOKIE_SECRET = 'RZIcY0t8FMsTuHEI6HDm1w$J01bVVqbsXDgAcRj7znMlCQ01Ak51OU21bR+/0qujXk'

book_image_cache = deque(maxlen=30)
db = orm.open_db()


@route('/')
@route('/home')
@view('index')
def home():
    """Главная страница"""
    return {
        'title': 'Main',
        'year': datetime.now().year
    }


@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return {
        'title': 'О нас',
        'message': 'Все что вы хотите знать о CoolBookShop',
        'year': datetime.now().year,
    }


@route('/book')
@route('/book/<code>')
@view('book')
def book(code: int = -1):
    """Renders the book page."""
    with Session(db) as session:
        book = session.execute(orm.query_select_book(code)).scalar()
        user = session.execute(orm.query_select_user_by_password(request.get_cookie('userhash',secret = COOKIE_SECRET))).scalar()
        if book is None:
            abort(404)
        else:
            book.views += 1
            session.commit()
            session.refresh(book)

            return {
                'title': 'Book',
                'user': user,
                'book': book,
                'year': datetime.now().year,
            }



@route('/book/image/<code:int>.jpg')
def book_image(code: int = -1):
    """Returns book image from cache"""

    bytes = None

    for (id, photo) in book_image_cache:
        if id == code:
            bytes = photo
    
    if bytes is None:
        with Session(db) as session:
            book = session.execute(orm.query_select_book(code)).scalar()

            if book is None:
                abort(404)
            else:
                bytes = book.photo
                book_image_cache.append((book.id, bytes))

    response.set_header("Content-Type", "image/jpeg")
    return bytes
@route('/catalog')
@route('/catalog/<filter>')
@view('catalog')
def catalog(filter: str = 'recent'):
    """Filtered catalog page"""
    books = []
    with Session(db) as session:
        user = session.execute(orm.query_select_user_by_password(request.get_cookie('userhash',secret = COOKIE_SECRET))).scalar()
        books = session.execute(orm.query_latest_books(20)).scalars().all()
        return {
        'title': 'Каталог',
        'filter': filter,
        'user': user,
        'books': books,
        'year': datetime.now().year,
    }

@route('/profile')
@view('profile')
def profile():
    password = request.get_cookie('userhash',secret = COOKIE_SECRET)
    if password is None: return redirect('/auth')
    else:
        with Session(db) as session:
            user = session.execute(orm.query_select_user_by_password(password)).scalar()
            if user is None:
                abort(404)
        return {
            'title': 'Profile',
            'user' : user, 
            'year': datetime.now().year,
        }

@route('/auth')
@view('auth')
def auth():
    if request.get_cookie('userhash',) is not None: return redirect('/profile')
    else:
        return {
        'title': 'Authorization',
        'year': datetime.now().year,
        }


@route('/catalog')
@route('/catalog/<filter>')
@view('catalog')
def catalog(filter: str = 'recent'):
    """Filtered catalog page"""
    books = []
    with Session(db) as session:
        user = session.execute(orm.query_select_user_by_password(request.get_cookie('userhash',secret = COOKIE_SECRET))).scalar()
        # TODO: Add book photo
        if filter == 'recent':  # Проверка выбранного фильтра
            books = session.execute(orm.query_latest_books(20)).scalars().all()
        elif filter == 'new':  # Проверка выбранного фильтра
            books = session.execute(
                orm.query_latest_books_new(20)).scalars().all()
        elif filter == 'popular':
            books = session.execute(
                orm.query_latest_books_views(20)).scalars().all()
        elif filter == 'rating':
            books = session.execute(
                orm.query_latest_books_rating(20)).scalars().all()
        else:
            abort(404)

    return {
        'title': 'Каталог',
        'filter': filter,
        'user': user,
        'books': books,
        'year': datetime.now().year,
    }

@post('/reg', method='post')
def registration():
    name = request.forms.get('name')
    mail = request.forms.get('email')
    password = request.forms.get('pass')
    with Session(db) as session:
        newuser = orm.User(name=name,email=mail,password = orm.Hasher.hash(password))
        session.add(newuser)
        session.commit()
    return redirect('/auth')

@post('/auth', method='post')
def authorisation():
    password = request.forms.get('pass')
    email = request.forms.get('email')
    with Session(db) as session:
        user = session.execute(orm.query_select_user_by_email(email)).scalar()
        if user is None:
            return "Error1111"
        else: 
            try:
                orm.Hasher.verify(user.password, password)
                response.set_cookie('userhash',user.password,secret = COOKIE_SECRET)
                return redirect('/profile')
            except argon2.exceptions.VerifyMismatchError: return "Error2222"

@post('/review', method = 'post')
def review():
    mark = request.forms.get('review mark')
    content = request.forms.get('review text')
    user = request.forms.get('user')
    book = request.forms.get('book')
    with Session(db) as session:
        newreview = orm.Review(mark = mark,user = user,book = book,content = content)
        session.add(newreview)
        session.commit()
        session.refresh(Review)
    return redirect('/book')

@post('/confirm', method = 'post')
def review():
    user = request.forms.get('user')
    with Session(db) as session:
        newreview = orm.Review(mark = mark,user = user,book = book,content = content)
        session.add(newreview)
        session.commit()
        session.refresh(Review)
    return redirect('/book')

