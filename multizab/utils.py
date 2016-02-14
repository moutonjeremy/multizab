import os
from multizab.zapi import ZabbixAPI
from flask import current_app
import json

types_data = {'5': 'disaster', '4': 'high',
              '3': 'average', '2': 'warning',
              '1': 'information', '0': 'not_classified'}


def get_app_base_path():
    """

    :return:
    """
    return os.path.dirname(os.path.realpath(__file__))


def get_instance_folder_path():
    """

    :return:
    """
    return os.path.join(get_app_base_path(), 'instance')


def get_zabbix_list():
    """

    :return:
    """
    with open(current_app.config['DATABASE_FILE']) as f:
        return json.load(f)['hosts']


def count_type(triggers):
    """

    :param triggers:
    :return:
    """
    types = ['disaster', 'high', 'average', 'warning', 'information', 'not_classified']
    priority_list = [i['priority'] for i in triggers]
    count_types = {}
    for i in types:
        count_types[i] = priority_list.count(i)
    return count_types


class Zabbix:
    """
    Zabbix Class
    """
    def __init__(self, url, username, password):
        """

        :param url:
        :param username:
        :param password:
        :return:
        """
        self.zapi = ZabbixAPI(url)
        self.zapi.timeout = 2
        try:
            self.zapi.login(username, password)
        except ValueError:
            current_app.logger.error('connection error: {0}'.format(url))

    def get_triggers(self):
        """

        :return:
        """
        result = []
        for i in self.zapi.trigger.get(only_true=1,
                                       skipDependent=1,
                                       monitored=1,
                                       active=1,
                                       output='extend',
                                       expandDescription=1,
                                       expandData='host',
                                       withLastEventUnacknowledged=1):
            i['priority'] = i['priority'].replace(i['priority'], types_data[i['priority']])
            result.append(i)
        return result
