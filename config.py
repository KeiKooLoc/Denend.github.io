import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 20

    SESSION_TYPE = 'sqlalchemy'
    CAPTCHA_ENABLE = True
    CAPTCHA_NUMERIC_DIGITS = 5
