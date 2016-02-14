from flask import Blueprint, jsonify, current_app
import json
from multizab.utils import Zabbix

api = Blueprint('api', __name__)


@api.route('/alerts')
def alerts():
    alerts_data = []
    with open(current_app.config['DATABASE_FILE']) as f:
        hosts = json.load(f)['hosts']
    for i in hosts:
        zapi = Zabbix(i['uri'], i['username'], i['password'])
        triggers = zapi.get_triggers()
        for j in triggers:
            j['platform'] = i['name']
            alerts_data.append(j)
    return jsonify({'result': alerts_data})


@api.route('/list/zabbix')
def list_zabbix():
    list_name = []
    with open(current_app.config['DATABASE_FILE']) as f:
        hosts = json.load(f)['hosts']
    for i in hosts:
        list_name.append(i['name'])
    return jsonify({'result': list_name})


@api.route('/count/alerts')
def count_alerts():
    alerts_data = {}
    with open(current_app.config['DATABASE_FILE']) as f:
        hosts = json.load(f)['hosts']
    for i in hosts:
        zapi = Zabbix(i['uri'], i['username'], i['password'])
        triggers = zapi.get_triggers()
        alerts_data[i['name']] = len(triggers)
    return jsonify({'result': alerts_data})


@api.route('/count/types')
def count_types():
    types_data = {'disaster': 0, 'high': 0,
                  'average': 0, 'warning': 0,
                  'information': 0, 'not_classified': 0}
    priority_list = []
    with open(current_app.config['DATABASE_FILE']) as f:
        hosts = json.load(f)['hosts']
    for i in hosts:
        zapi = Zabbix(i['uri'], i['username'], i['password'])
        triggers = zapi.get_triggers()
        for j in triggers:
            priority_list.append(j['priority'])
        for k in types_data:
            types_data[k] = priority_list.count(k)
    return jsonify({'result': types_data})


@api.route('/count/types/<zabbix_name>')
def count_types_zabbix(zabbix_name):
    types_data = {'disaster': 0, 'high': 0,
                  'average': 0, 'warning': 0,
                  'information': 0, 'not_classified': 0}
    priority_list = []
    with open(current_app.config['DATABASE_FILE']) as f:
        hosts = json.load(f)['hosts']
    for i in hosts:
        if zabbix_name == i['name']:
            zapi = Zabbix(i['uri'], i['username'], i['password'])
            triggers = zapi.get_triggers()
            for j in triggers:
                priority_list.append(j['priority'])
            for k in types_data:
                types_data[k] = priority_list.count(k)
    return jsonify({'result': types_data})