# Flask Internationalization (i18n) and Localization (l10n) Demo

This is a demonstration application showing how to implement internationalization (i18n) and localization (l10n) in a Flask application using Flask-Babel. The application supports multiple languages, automatic language detection based on browser settings, and manual language selection.

## Features

- Multiple language support (English, Spanish, French)
- Automatic language detection based on browser settings
- Manual language selection through UI
- Localized date/time formatting
- Localized number formatting
- Translation of UI elements

## Project Structure

```
├── app/                      # Application package
│   ├── __init__.py           # Flask application initialization
│   ├── babel.py              # Babel configuration
│   ├── routes.py             # Application routes
│   ├── static/               # Static files (CSS, JS, etc.)
│   │   └── css/              # CSS stylesheets
│   ├── templates/            # Jinja2 templates
│   │   ├── base.html         # Base template with language selector
│   │   ├── index.html        # Home page template
│   │   └── about.html        # About page template
│   └── translations/         # Translation files
│       ├── es/               # Spanish translations
│       └── fr/               # French translations
├── babel.cfg                 # Babel extraction configuration
├── requirements.txt          # Project dependencies
├── run.py                    # Application entry point
└── README.md                 # This file
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone or download this repository

2. Create a virtual environment (recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - Windows:
   ```bash
   venv\Scripts\activate
   ```

   - macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Install the required packages:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
python run.py
```

6. Open your browser and navigate to `http://127.0.0.1:5000`

## Translation Workflow

This project uses Flask-Babel for translations. Here's how to add or update translations:

1. Extract translatable strings to a POT file:

```bash
pybabel extract -F babel.cfg -o messages.pot .
```

2. Initialize a new language (if it doesn't exist yet):

```bash
pybabel init -i messages.pot -d app/translations -l <language_code>
```

Replace `<language_code>` with the language code (e.g., 'de' for German).

3. Update existing language translations:

```bash
pybabel update -i messages.pot -d app/translations
```

4. Edit the translation files in `app/translations/<language_code>/LC_MESSAGES/messages.po`

5. Compile the translations:

```bash
pybabel compile -d app/translations
```

## How It Works

### Language Selection

The application selects the language in the following order:

1. User-selected language (stored in session)
2. Browser's preferred language (from Accept-Language header)
3. Default language (English)

You can change the language by clicking on the language links in the header.

### Marking Strings for Translation

- In Python files: Use the `_()` function
  ```python
  from flask_babel import _
  flash(_('Your message has been sent.'))
  ```

- In Jinja2 templates: Use the `{{ _('text') }}` syntax
  ```html
  <h1>{{ _('Welcome') }}</h1>
  ```

### Formatting Dates and Numbers

Flask-Babel provides functions for formatting dates and numbers according to the selected locale:

- `format_datetime()`: Format a datetime object
- `format_date()`: Format a date object
- `format_time()`: Format a time object
- `format_number()`: Format a number
- `format_currency()`: Format a currency value

## Troubleshooting

- **Missing translations**: Make sure you've compiled the translations with `pybabel compile`
- **Language not changing**: Check if cookies are enabled in your browser
- **Babel errors**: Ensure you're using the correct version of Flask-Babel (check requirements.txt)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Flask-Babel](https://python-babel.github.io/flask-babel/)
- [Babel](https://babel.pocoo.org/)