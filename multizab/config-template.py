import os
import logging
import json

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '254496C5-9F6F-4A8D-A60E-219CF83AE015'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'multizab.log'
    LOGGING_LEVEL = logging.DEBUG
    DATABASE_FILE = os.path.join(basedir, 'hosts.json')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = '82B13811-2201-4B8A-B7BC-71FC2A8F7DAF'


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SECRET_KEY = 'E0D82A3C-D954-471B-8772-D762BF746F45'


config = {
    "development": "multizab.config.DevelopmentConfig",
    "testing": "multizab.config.TestingConfig",
    "default": "multizab.config.DevelopmentConfig"
}


def database(path):
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            json.dump({'hosts': []}, f, ensure_ascii=False)


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True)
    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    database(app.config['DATABASE_FILE'])
