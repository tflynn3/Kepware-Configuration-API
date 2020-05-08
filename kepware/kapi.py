import requests
from collections import Mapping, Sequence, Sized
from dataclasses import dataclass, asdict, replace
from kepware.api_wrapper import *
from random import randint


class Client:
    def __init__(self, address, port, username='administrator', password='', use_ssl=True):
        self.address = address
        self.port = port
        self.username = username
        self.password = password

        if use_ssl:
            self.protocol = 'https://'
        else:
            self.protocol = 'http://'
        self.create_session()

    def create_session(self):
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)

class JsonWrapper(Sized):
    def __len__(self):
        return len(self._data)

    def __init__(self, json):
        self._data = json

    @property
    def raw(self): return self._data

class JsonListWrapper(JsonWrapper, Sequence):
    def __init__(self, json_list):
        if type(json_list) is not list:
            raise TypeError('received type {}, expected list'.format(type(json_list)))
        super().__init__(json_list)

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        raise NotImplementedError('__iter__')

    def get(self, index):
        try:
            return self._data[index]
        except Exception as e:
            print(index)
            raise e

class JsonDictWrapper(JsonWrapper, Mapping):
    def __init__(self, json_dict):
        super().__init__(json_dict)
        if type(self._data) is not dict:
            raise TypeError('received type {}, expected dict'.format(type(json_dict)))

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, key):
        return self._data[key]

    __marker = object()

    def get(self, key, default=__marker):
        try:
            return self._data[key]
        except KeyError:
            if default is self.__marker:
                raise
            else:
                return default



@dataclass
class Channel:
    PROJECT_ID: int
    common_ALLTYPES_NAME: str
    common_ALLTYPES_DESCRIPTION: str
    servermain_MULTIPLE_TYPES_DEVICE_DRIVER: str
    servermain_CHANNEL_DIAGNOSTICS_CAPTURE: bool
    servermain_CHANNEL_UNIQUE_ID: int
    servermain_CHANNEL_WRITE_OPTIMIZATIONS_METHOD: int
    servermain_CHANNEL_WRITE_OPTIMIZATIONS_DUTY_CYCLE: int
    servermain_CHANNEL_NON_NORMALIZED_FLOATING_POINT_HANDLING: int
    
    def _asdict(self):
        return asdict(self)

    def rename(self, new_name):
        self.common_ALLTYPES_NAME = new_name

@dataclass
class OPCDA(Channel):
    opcdaclient_CHANNEL_PROG_ID : str = "Kepware.KEPServerEX.V6"
    opcdaclient_CHANNEL_REMOTE_MACHINE_NAME : str = ""
    opcdaclient_CHANNEL_CONNECTION_TYPE : int = 21
    opcdaclient_CHANNEL_FAILED_CONNECTION_RETRY_INTERVAL_SEC : int = 5
    opcdaclient_CHANNEL_SERVER_STATUS_QUERY_INTERVAL_SEC : int = 5

    def _asdict(self):
        d = asdict(self)
        del d['PROJECT_ID']
        del d['servermain_CHANNEL_UNIQUE_ID']
        d2 = {}
        for k in d.keys():
            if "common_" in k:
                new_k = k.replace("common_", "common.")
                d2[new_k] = d[k]
            elif "servermain_" in k:
                new_k = k.replace("servermain_", "servermain.")
                d2[new_k] = d[k]
            elif "opcdaclient_" in k:
                new_k = k.replace("opcdaclient_", "opcdaclient.")
                d2[new_k] = d[k]
            else:
                d2[k] = d[k]
            

        return d2
    
    def rename(self, new_name):
        self.common_ALLTYPES_NAME = new_name

    def create(self, client):
        print(self._asdict())
        post = post_channels(client, self._asdict())
        return post

    