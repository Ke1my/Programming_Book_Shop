"""
Routes and views for the bottle application.
"""

from collections import deque
from bottle import route, view, abort, response, post, request, redirect
from datetime import datetime
from sqlalchemy.orm import Session
import argon2
import utils
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
        'year': datetime.now().year,
        'request': request,
    }


@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return {
        'title': 'О нас',
        'message': 'Все что вы хотите знать о CoolBookShop',
        'year': datetime.now().year,
        'request': request,
    }


@route('/book')
@route('/book/<code>')
@view('book')
def book(code: int = -1):
    """Renders the book page."""
    with Session(db) as session:
        reviews = []
        with Session(db) as session:
            reviews = session.execute(orm.query_latest_books(20)).scalars().all()
        book = session.execute(orm.query_select_book(code)).scalar()
        if book is None:
            abort(404)
        else:
            book.views += 1
            session.commit()
            session.refresh(book)
            return {
                'title': 'Book',
                'book': book,
                'reviews': reviews,
                'year': datetime.now().year,
                'request': request,
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
        books = session.execute(orm.query_latest_books(20)).scalars().all()
        return {
            'title': 'Каталог',
            'filter': filter,
            'books': books,
            'year': datetime.now().year,
            'request': request,
        }


@route('/profile')
@view('profile')
def profile():
    password = request.get_cookie('userhash', secret=COOKIE_SECRET)
    if password is None:
        return redirect('/auth')
    else:
        with Session(db) as session:
            user = session.execute(
                orm.query_select_user_by_password(password)).scalar()
            if user is None:
                response.delete_cookie('userhash')
                return redirect("/auth")
        return {
            'title': 'Profile',
            'user': user,
            'year': datetime.now().year,
            'request': request,
        }


@route('/auth')
@view('auth')
def auth():
    if request.get_cookie('userhash') is not None:
        return redirect('/profile')
    else:
        return {
            'title': 'Authorization',
            'year': datetime.now().year,
            'request': request,
        }

@route('/cart')
@view('cart')
def catalog():
    """Filtered catalog page"""
    books = []
    with Session(db) as session:
        books = session.execute(orm.query_select_cart(orm.query_select_user_by_password(request.get_cookie('userhash', secret=COOKIE_SECRET)).scalar()).scalars().all())
    return {
        'title': 'Каталог',
        'filter': filter,
        'books': books,
        'year': datetime.now().year,
        'request': request,
    }

@route('/catalog')
@route('/catalog/<filter>')
@view('catalog')
def catalog(filter: str = 'recent'):
    """Filtered catalog page"""
    books = []
    with Session(db) as session:
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
        'books': books,
        'year': datetime.now().year,
        'request': request,
    }


@route('/reg', method='post')
def registration():
    name = request.forms.getunicodeunicode('name')
    mail = request.forms.getunicode('email')
    password = request.forms.getunicode('pass')
    with Session(db) as session:
        user = orm.User(name=name, email=mail, password=orm.Hasher.hash(password))
        session.add(user)
        session.commit()
    return redirect('/auth')


@route('/auth', method='post')
def auth_post():
    password = request.forms.getunicode('pass')
    email = request.forms.getunicode('email')
    with Session(db) as session:
        user = session.execute(orm.query_select_user_by_email(email)).scalar()
        if user is None:
            return "Error1111"
        else:
            try:
                orm.Hasher.verify(user.password, password)
                response.set_cookie(
                    'userhash', user.password, secret=COOKIE_SECRET)
                return redirect('/profile')
            except argon2.exceptions.VerifyMismatchError:
                return "Error2222"


@route('/review', method='post')
def review():
    password = request.get_cookie('userhash', secret=COOKIE_SECRET)
    if password is None:
        return redirect(request_uri)
    with Session(db) as session:
        user = session.execute(
            if 
            orm.query_select_user_by_password(password)).scalar()
        if user is None:
            return redirect('/logout')

    mark = request.forms.getunicode('review-mark')
    content = request.forms.getunicode('review-content')
    book = request.forms.getunicode('book')
    with Session(db) as session:
        newreview = orm.Review(mark=mark, user=user.id, book=book, content=content)
        session.add(newreview)
        session.commit()
    return redirect(f'/book/{book}')

@route('/confirm', method='post')
def review():
    user = request.forms.getunicode('user')
    # Try to check something
    with Session(db) as session:
        user = session.execute(orm.query_select_user_by_password(request.get_cookie('userhash', secret=COOKIE_SECRET))
         # TODO DROP
    return redirect('/card')

@route('/add', method='post')
def add():
    code = request.forms.getunicode('book')
    with Session(db) as session:
        book = session.execute(orm.query_select_book(code)).scalar()
        user = session.execute(orm.query_select_user_by_password(request.get_cookie('userhash', secret=COOKIE_SECRET))
        user.card_rel.append(book)
        session.commit()


@route('/logout')
def logout():
    if request.get_cookie("userhash") is not None:
        response.delete_cookie("userhash")
    return redirect("/auth")
