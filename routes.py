"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Home page"""
    return {
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
        'year': datetime.now().year,
    }
    )
