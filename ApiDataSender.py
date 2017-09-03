import ujson

import HttpClient as http_client


class ApiDataSender():
    URL = '/sensor/{0}'

    def __init__(self, endpoint):
        self.__endpoint = endpoint

    def send(self, sensors):
        for sensor in sensors:
            self.__send_single(sensor)

    def __send_single(self, sensor):
        sensor_data = {'type' : sensor['type'], 'value' : sensor['value']}
        full_url = self.__endpoint + self.URL.format(sensor['id'])
        print('[POST] request to {0} with raw data {1}'.
                    format(full_url, ujson.dumps(sensor_data)))
        response = http_client.put(full_url, json=sensor_data)
        response.raise_for_status()
        print(response.status_code)
