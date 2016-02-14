import os
from multizab.zapi import ZabbixAPI
from flask import current_app

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
