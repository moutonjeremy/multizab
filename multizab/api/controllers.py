from flask import Blueprint, jsonify, current_app
import json
from multizab.zapi import ZabbixAPI

api = Blueprint('api', __name__)


@api.route('/alerts')
def alerts():
    alerts_data = []
    with open(current_app.config['DATABASE_FILE']) as f:
        hosts = json.load(f)['hosts']
    for i in hosts:
        zapi = ZabbixAPI(i['uri'])
        zapi.timeout = 2
        try:
            zapi.login(i['username'], i['password'])
            triggers = zapi.trigger.get(only_true=1,
                                        skipDependent=1,
                                        monitored=1,
                                        active=1,
                                        output='extend',
                                        expandDescription=1,
                                        expandData='host',
                                        withLastEventUnacknowledged=1)
            for j in triggers:
                j['platform'] = i['name']
                alerts_data.append(j)
        except ValueError:
            current_app.logger.error('connection error: {0}'.format(i['name']))
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
        zapi = ZabbixAPI(i['uri'])
        zapi.timeout = 2
        try:
            zapi.login(i['username'], i['password'])
            triggers = zapi.trigger.get(only_true=1,
                                        skipDependent=1,
                                        monitored=1,
                                        active=1,
                                        output='extend',
                                        expandDescription=1,
                                        expandData='host',
                                        withLastEventUnacknowledged=1)
            alerts_data[i['name']] = len(triggers)
        except ValueError:
            current_app.logger.error('connection error: {0}'.format(i['name']))
    return jsonify({'result': alerts_data})


@api.route('/count/types')
def count_types():
    types_data = {'disaster': 0, 'high': 0,
                  'average': 0, 'warning': 0,
                  'information': 0, 'not_classified': 0}
    with open(current_app.config['DATABASE_FILE']) as f:
        hosts = json.load(f)['hosts']
    for i in hosts:
        zapi = ZabbixAPI(i['uri'])
        zapi.timeout = 2
        try:
            zapi.login(i['username'], i['password'])
            triggers = zapi.trigger.get(only_true=1,
                                        skipDependent=1,
                                        monitored=1,
                                        active=1,
                                        output='extend',
                                        expandDescription=1,
                                        expandData='host',
                                        withLastEventUnacknowledged=1)
            for j in triggers:
                if j['priority'] == str(5):
                    types_data['disaster'] += 1
                elif j['priority'] == str(4):
                    types_data['high'] += 1
                elif j['priority'] == str(3):
                    types_data['average'] += 1
                elif j['priority'] == str(2):
                    types_data['warning'] += 1
                elif j['priority'] == str(1):
                    types_data['information'] += 1
                else:
                    types_data['not_classified'] += 1
        except ValueError:
            current_app.logger.error('connection error: {0}'.format(i['name']))
    return jsonify({'result': types_data})


@api.route('/count/types/<zabbix_name>')
def count_types_zabbix(zabbix_name):
    types_data = {'disaster': 0, 'high': 0,
                  'average': 0, 'warning': 0,
                  'information': 0, 'not_classified': 0}
    with open(current_app.config['DATABASE_FILE']) as f:
        hosts = json.load(f)['hosts']
    for i in hosts:
        if zabbix_name == i['name']:
            zapi = ZabbixAPI(i['uri'])
            zapi.timeout = 2
            try:
                zapi.login(i['username'], i['password'])
                triggers = zapi.trigger.get(only_true=1,
                                            skipDependent=1,
                                            monitored=1,
                                            active=1,
                                            output='extend',
                                            expandDescription=1,
                                            expandData='host',
                                            withLastEventUnacknowledged=1)
                for j in triggers:
                    if j['priority'] == str(5):
                        types_data['disaster'] += 1
                    elif j['priority'] == str(4):
                        types_data['high'] += 1
                    elif j['priority'] == str(3):
                        types_data['average'] += 1
                    elif j['priority'] == str(2):
                        types_data['warning'] += 1
                    elif j['priority'] == str(1):
                        types_data['information'] += 1
                    else:
                        types_data['not_classified'] += 1
            except ValueError:
                current_app.logger.error('connection error: {0}'.format(i['name']))
    return jsonify({'result': types_data})