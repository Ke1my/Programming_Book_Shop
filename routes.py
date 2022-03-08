"""
Routes and views for the bottle application.
"""

from bottle import route, view, abort
from datetime import datetime

import store

store = store.Store()

@route('/')
@route('/home')
@view('index')
def home():
    """Home page"""
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
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }

@route('/profile')
@view('profile')
def profile():
    return {
        'title': 'Profile',
        'year': datetime.now().year,
    }

@route('/registration')
@view('registration')
def profile():
    return {
        'title': 'Registration',
        'year': datetime.now().year,
    }

@route('/catalog')
@route('/catalog/<filter>')
@view('catalog')
def catalog(filter: str = 'all'):
    """Filtered catalog page"""

    if filter in ('all', 'popular', 'rating'):
        return {
            'title': 'Каталог',
            'filter': filter,
            'books': store.inner,
            'year': datetime.now().year,
        }
    else:
        abort(404)

