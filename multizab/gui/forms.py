from wtforms import StringField, PasswordField
from flask_wtf import Form


class HostForm(Form):
    hostname = StringField('hostname')
    username = StringField('username')
    password = PasswordField('password')