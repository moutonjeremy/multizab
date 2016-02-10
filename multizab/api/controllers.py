from flask import Blueprint, jsonify
from pyzabbix import ZabbixAPI
from zabbix_client import ZabbixServerProxy

from multizab.data.models import db, Zabbix

api = Blueprint('api', __name__)


@api.route('/hosts')
def hosts():
    hosts = Zabbix.query.all()
    return jsonify({'result': Zabbix.serialize_list(hosts)})


@api.route('/alerts')
def alerts():
    alerts_data = []
    for i in Zabbix.query.all():
        zapi = ZabbixAPI('http://{0}/zabbix/'.format(i.host))
        zapi.login(i.username, i.password)
        triggers = zapi.trigger.get(only_true=1,
                                    skipDependent=1,
                                    monitored=1,
                                    active=1,
                                    output='extend',
                                    expandDescription=1,
                                    expandData='host',
                                    withLastEventUnacknowledged=1)
        for j in triggers:
            j['platform'] = i.host
            alerts_data.append(j)
    return jsonify({'result': alerts_data})
