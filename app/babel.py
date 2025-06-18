from flask import request, session
from flask_babel import Babel
from app import app

def get_locale():
    # If the user has selected a language, use it
    if 'language' in session:
        return session['language']
    
    # Otherwise, try to detect the language from the browser
    return request.accept_languages.best_match(['en', 'es', 'fr'])