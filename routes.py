"""
Routes and views for the bottle application.
"""

from bottle import route, view, abort
from datetime import datetime
from sqlalchemy.orm import Session

import orm

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
def about(code: int = -1):
    """Renders the book page."""
    with Session(db) as session:
        book = session.execute(orm.query_select_book(code)).scalar_one()

        if book is None:
            abort(404)
        else:
            return {
                'title': 'Book',
                'book': book,
                'year': datetime.now().year,
            }


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
def registration():
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
            books = session.execute(orm.query_latest_books_new(20)).scalars().all()
        elif filter == 'popular':
            books = session.execute(orm.query_latest_books_views(20)).scalars().all()
        elif filter == 'rating':
            books = session.execute(orm.query_latest_books_rating(20)).scalars().all()
        else:
            abort(404)

    return {
        'title': 'Каталог',
        'filter': filter,
        'books': books,
        'year': datetime.now().year,
    }
