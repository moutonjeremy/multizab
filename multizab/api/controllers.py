from flask import Blueprint, jsonify
from multizab.utils import Zabbix, get_zabbix_list, count_type

api = Blueprint('api', __name__)


@api.route('/alerts')
def alerts():
    """

    :return:
    """
    alerts_data = []
    hosts = get_zabbix_list()
    for i in hosts:
        for j in Zabbix(i['uri'], i['username'], i['password']).get_triggers():
            j['platform'] = i['name']
            alerts_data.append(j)
    return jsonify({'result': alerts_data})


@api.route('/list/zabbix')
def list_zabbix():
    """

    :return:
    """
    return jsonify({'result': [i['name'] for i in get_zabbix_list()]})


@api.route('/count/alerts')
def count_alerts():
    """

    :return:
    """
    alerts_data = {}
    hosts = get_zabbix_list()
    for i in hosts:
        alerts_data[i['name']] = len(Zabbix(i['uri'], i['username'], i['password']).get_triggers())
    return jsonify({'result': alerts_data})


@api.route('/count/types')
def count_types():
    """

    :return:
    """
    hosts = get_zabbix_list()
    triggers = [j for i in hosts for j in Zabbix(i['uri'], i['username'], i['password']).get_triggers()]
    types_data = count_type(triggers)
    return jsonify({'result': types_data})


@api.route('/count/types/<zabbix_name>')
def count_types_zabbix(zabbix_name):
    """
    
    :param zabbix_name:
    :return:
    """
    hosts = get_zabbix_list()
    triggers = [j for i in hosts if zabbix_name == i['name']
                for j in Zabbix(i['uri'], i['username'], i['password']).get_triggers()]
    types_data = count_type(triggers)
    return jsonify({'result': types_data})
