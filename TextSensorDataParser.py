import ure


class TextSensorDataParser:
    SENSOR_REGEX = '([A-Z]*)([0-9]*)?\:(\-?[0-9]*\.?[0-9]*]*)'
    SENSOR_SEPARATOR = '|'
    regex = ure.compile(SENSOR_REGEX)

    def __init__(self, sensor_mapping):
        self.__sensor_mapping = sensor_mapping

    def is_buffer_parsable(self, buffer):
        return buffer.endswith(self.SENSOR_SEPARATOR)

    def parse(self, text_buffer):
        text_buffer = text_buffer[:-1]
        sensors = []
        for sensor_data in text_buffer.split('|'):
            sensor_components = self.regex.search(sensor_data)
            if not sensor_components:
                continue
            type = self.__sensor_mapping[sensor_components.group(1)]
            sensors.append({'type' : type,
                            'id' : sensor_components.group(2),
                            'value' : sensor_components.group(3)})

        return sensors
