import requests
import json
import uuid


class ZabbixException(Exception):
    """
    Zabbix Exception
    """
    pass


class ZabbixAPI(object):
    def __init__(self, url, timeout=None, session=None):
        """
        :param url: zabbix url
        :param timeout: timeout request
        """
        self.url = url + '/api_jsonrpc.php'
        self.timeout = timeout

        if session:
            self.session = session
        else:
            self.session = requests.Session()
        self.auth = ''

        self.session.headers.update({'Content-Type': 'application/json-rpc'})

    def login(self, user, password):
        """
        :param user: zabbix user
        :param password: zabbix user password
        :return: session
        """
        self.auth = self.user.login(user=user, password=password)

    def do_request(self, method, params=None):
        """
        :param method: zabbix method
        :param params: params for method
        :return: json response
        """
        rq = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params or {},
            'id': str(uuid.uuid4())
        }

        if self.auth:
            rq['auth'] = self.auth

        rp = self.session.post(
            self.url,
            data=json.dumps(rq),
            timeout=self.timeout
        )

        if not len(rp.text):
            raise ZabbixException('No Response')

        try:
            rp_json = json.loads(rp.text)
        except ValueError:
            raise ZabbixException('Parse json error: {0}'.format(rp.text))
        if 'error' in rp_json:
            raise ZabbixException('Error: {0}'.format(rp.text))

        return rp_json

    def __getattr__(self, item):
        """
        :param item:
        :return:
        """
        return ZabbixObject(item, self)


class ZabbixObject(object):
    """
    Send request to zabbix
    """
    def __init__(self, key, value):
        """
        :param key:
        :param value:
        :return:
        """
        self.key = key
        self.value = value

    def __getattr__(self, item):
        """
        :param item:
        :return:
        """
        def fn(*args, **kwargs):
            if args and kwargs:
                raise TypeError("Found both args and kwargs")

            return self.value.do_request(
                '{0}.{1}'.format(self.key, item),
                args or kwargs
            )['result']

        return fn
