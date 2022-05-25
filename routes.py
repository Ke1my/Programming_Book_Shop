"""
Routes and views for the bottle application.
"""

from collections import deque
from bottle import route, view, abort, response, post, request, redirect
from datetime import datetime
from sqlalchemy.orm import Session
import argon2

from utils import check_email, check_password_weakness, check_username, check_mark, check_phone, cart_is_valid
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
            reviews = session.execute(
                orm.query_select_book_reviews(code)).scalars().all()
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
    with Session(db) as session:
        user = session.execute(orm.query_select_user_cart_by_password(
            request.get_cookie('userhash', secret=COOKIE_SECRET))).scalar()
        
        return {
            'title': 'Каталог',
            'filter': filter,
            'user': user,
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
    name = request.forms.getunicode('name')
    email = request.forms.getunicode('email')
    password = request.forms.getunicode('pass')

    if not check_email(email):
        return "Bad email"

    if not check_password_weakness(password):
        return "Weak password"

    if not check_username(name):
        return "invalide username"

    with Session(db) as session:
        user = orm.User(name=name, email=email,
                        password=orm.Hasher.hash(password))
        session.add(user)
        session.commit()
    return redirect('/auth')


@route('/auth', method='post')
def auth_post():
    password = request.forms.getunicode('pass')
    email = request.forms.getunicode('email')

    if not check_email(email):
        return "Bad email"

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
    book = request.forms.getunicode('book')

    if password is None:
        return redirect(f"/book/{book}")
    with Session(db) as session:
        user = session.execute(
            orm.query_select_user_by_password(password)).scalar()
        if user is None:
            return redirect('/logout')

    mark = request.forms.getunicode('review-mark')
    content = request.forms.getunicode('review-content')
    if check_username(mark):
        return "invalide mark"
    with Session(db) as session:
        newreview = orm.Review(mark=mark, user=user.id,
                               book=book, content=content,datetime = datetime.now().strftime("%Y-%m-%d %H:%M"))
        session.add(newreview)
        session.commit()
    return redirect(f'/book/{book}')


@route('/confirm', method='post')
def review():
    # Взятие данных из полей страницы
    phone = request.forms.getunicode('phone_number')
    adress = request.forms.getunicode('adress')
    user = request.forms.getunicode('user')

    if (check_phone(phone) and cart_is_valid(phone, adress)): # Проверка на пустые значения и правильный формат телефона
        with Session(db) as session: #Открытие сессии в бд
            user = session.execute(orm.query_select_user_by_password( #Получение пользователя
                request.get_cookie('userhash', secret=COOKIE_SECRET))).scalar()
            user.cart_rel.clear() #Очищение карзины
            session.commit() # Фиксация изменений
        return redirect('/profile') # Переход на страницу с профилем
    else:
        return redirect('/cart') # Переход на страницу с корзиной


@route('/add', method='post')
def add():
    code = request.forms.getunicode('book')# Взятие данных из полей страницы
    with Session(db) as session: #Открытие сессии в бд
        book = session.execute(orm.query_select_book(code)).scalar()  # Получение книги
        user = session.execute(orm.query_select_user_cart_by_password( #Получение пользователя
            request.get_cookie('userhash', secret=COOKIE_SECRET))).scalar()
        user.cart_rel.append(book) # Добавление книги
        session.commit()  # Фиксация изменений
    return redirect("/catalog") # Переход  в каталог


@route('/logout')
def logout():
    if request.get_cookie("userhash") is not None:
        response.delete_cookie("userhash")
    return redirect("/auth")


@route('/active')
@view('active')
def active():
    from orm import User, Review, func
    from sqlalchemy import desc, text

    with Session(db) as session:  # Открытие сессии в бд
        return {
            'title': 'ТОП-10 Активных пользователей',
            # Запрос на получение 10 самых активный пользователей
            'users': session.execute(session.query(User, func.count(Review.id))
                                     .select_from(Review)
                                     .join(User) # Join с таблицей пользователей
                                     .group_by(User) # Группировка отзывов по пользователям
                                     .order_by(desc(text("count_1"))) # Обратная сортировка
                                     .limit(10) # Последние 10 записей
                                     ).fetchall(),
            'year': datetime.now().year,
            'request': request,
        }
