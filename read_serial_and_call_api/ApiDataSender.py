import ujson
import time

import HttpClient as http_client


class ApiDataSender():
    URL = '/sensor/{0}'

    def __init__(self, endpoint):
        self.__endpoint = endpoint

    def send(self, sensors):
        for sensor in sensors:
            self.__send_single(sensor)
            time.sleep(1)

    def __send_single(self, sensor):
        sensor_data = {'type' : sensor['type'], 'value' : sensor['value']}
        full_url = self.__endpoint + self.URL.format(sensor['id'])
        print('[PUT] request to {0} with raw data {1}'.
                    format(full_url, ujson.dumps(sensor_data)))
        http_client.put(full_url, json=sensor_data)
