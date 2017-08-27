import HttpClient as http_client

class ApiDataSender():
    URL = '/sensor/{0}'

    def __init__(self, endpoint):
        self.__endpoint = endpoint

    # sensors = list of touples
    def send(self, sensors):
        for sensor in sensors:
            self.__send_single(sensor)

    def __send_single(self, sensor):
        sensor_data = {'type' : sensor[0], 'value' : sensor[2]}
        full_url = self.__endpoint + self.URL.format(sensor[1])
        print(full_url)
        print(sensor_data)
        response = http_client.put(full_url, json=sensor_data)
        response.raise_for_status()
        print(response.status_code)
        print(response.text)
