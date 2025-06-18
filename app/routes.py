from flask import render_template, request, redirect, url_for, session
from flask_babel import _, get_locale, format_datetime, format_number
from datetime import datetime
from app import app

@app.route('/')
def index():
    current_time = datetime.now()
    formatted_time = format_datetime(current_time)
    formatted_number = format_number(12345.67)
    
    return render_template('index.html', 
                          current_time=current_time,
                          formatted_time=formatted_time,
                          formatted_number=formatted_number)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/language/<language>')
def set_language(language):
    session['language'] = language
    return redirect(request.referrer or url_for('index'))

@app.context_processor
def inject_locale():
    return dict(locale=get_locale())