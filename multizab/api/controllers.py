from flask import Blueprint, jsonify, current_app
from pyzabbix import ZabbixAPI
import json

api = Blueprint('api', __name__)


@api.route('/alerts')
def alerts():
    alerts_data = []
    with open(current_app.config['DATABASE_FILE']) as f:
        hosts = json.load(f)['hosts']
    for i in hosts:
        zapi = ZabbixAPI(i['uri'])
        zapi.session.verify = False
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
        except:
            current_app.logger.error('connection error: {0}'.format(i['name']))
    return jsonify({'result': alerts_data})
