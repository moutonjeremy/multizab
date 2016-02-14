from flask import Blueprint, jsonify
from multizab.utils import Zabbix, get_zabbix_list, count_type

api = Blueprint('api', __name__)


@api.route('/alerts')
def alerts():
    alerts_data = []
    hosts = get_zabbix_list()
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
    hosts = get_zabbix_list()
    for i in hosts:
        list_name.append(i['name'])
    return jsonify({'result': list_name})


@api.route('/count/alerts')
def count_alerts():
    alerts_data = {}
    hosts = get_zabbix_list()
    for i in hosts:
        zapi = Zabbix(i['uri'], i['username'], i['password'])
        triggers = zapi.get_triggers()
        alerts_data[i['name']] = len(triggers)
    return jsonify({'result': alerts_data})


@api.route('/count/types')
def count_types():
    hosts = get_zabbix_list()
    types_data = {}
    for i in hosts:
        zapi = Zabbix(i['uri'], i['username'], i['password'])
        types_data = count_type(zapi.get_triggers())
    return jsonify({'result': types_data})


@api.route('/count/types/<zabbix_name>')
def count_types_zabbix(zabbix_name):
    types_data = {}
    hosts = get_zabbix_list()
    for i in hosts:
        if zabbix_name == i['name']:
            zapi = Zabbix(i['uri'], i['username'], i['password'])
            types_data = count_type(zapi.get_triggers())
    return jsonify({'result': types_data})
