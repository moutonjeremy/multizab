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
    return jsonify({'result': alerts_data})
