"""
Routes and views for the bottle application.
"""

from collections import deque
from bottle import route, view, abort, response
from datetime import datetime
from sqlalchemy.orm import Session

import orm

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


@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return {
        'title': 'Contact',
        'year': datetime.now().year,
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

        if book is None:
            abort(404)
        else:
            book.views += 1
            session.commit()
            session.refresh(book)

            return {
                'title': 'Book',
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


# Обозначение аргументов
@route('/profile')
@view('profile')
def profile():
    return {
        'title': 'Profile',
        'year': datetime.now().year,
    }


@route('/auth')
@view('auth')
def auth():
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
    }
