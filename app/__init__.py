from flask import Flask, request, session
from flask_babel import Babel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

# Import get_locale before initializing Babel
from app.babel import get_locale

# Initialize Babel with locale_selector parameter (Flask-Babel 4.0.0+)
babel = Babel(app, locale_selector=get_locale)

from app import routes