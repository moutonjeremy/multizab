from flask import Flask
from utils import get_instance_folder_path
from config import configure_app
from multizab.data.models import db

from multizab.api.controllers import api
from multizab.gui.controllers import gui

app = Flask(__name__,
            instance_path=get_instance_folder_path(),
            instance_relative_config=True,
            template_folder='templates')

configure_app(app)
db.init_app(app)

app.register_blueprint(gui)
app.register_blueprint(api, url_prefix='/api')
