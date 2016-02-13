from wtforms import StringField, PasswordField
from flask_wtf import Form


class HostForm(Form):
    name = StringField('name')
    uri = StringField('uri')
    username = StringField('username')
    password = PasswordField('password')
