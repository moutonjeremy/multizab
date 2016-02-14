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


@api.route('/graphics')
def graphics():
    """

    :return:
    """
    result = {'count_alerts': {}, 'count_types': {}, 'count_types_per_zabbix': {}}
    hosts = get_zabbix_list()
    triggers = []
    for i in hosts:
        for j in Zabbix(i['uri'], i['username'], i['password']).get_triggers():
            j['platform'] = i['name']
            triggers.append(j)
    for i in triggers:
        if i['platform'] not in result['count_alerts']:
            result['count_alerts'][i['platform']] = 0
        result['count_alerts'][i['platform']] += 1
    result['count_types'] = count_type(triggers)
    for i in result['count_alerts']:
        result['count_types_per_zabbix'][i] = count_type([j for j in triggers if j['platform'] == i])
    return jsonify({'result': result})

