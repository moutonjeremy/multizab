from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect

db = SQLAlchemy()


class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


class Zabbix(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    host = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def serialize(self):
        d = Serializer.serialize(self)
        del d['password']
        return d
