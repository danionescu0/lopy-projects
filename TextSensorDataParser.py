import ure

class TextSensorDataParser:
    SENSOR_REGEX = '([A-Z]*)([0-9]*)?\:(\-?[0-9]*\.?[0-9]*]*)'
    SENSOR_SEPARATOR = '|'
    regex = ure.compile(SENSOR_REGEX)

    def is_buffer_parsable(self, buffer):
        return buffer.endswith(self.SENSOR_SEPARATOR)


    def parse(self, text_buffer):
        text_buffer = text_buffer[:-1]
        sensors = []
        for sensor_data in text_buffer.split('|'):
            sensor_components = self.regex.search(sensor_data)
            if not sensor_components:
                continue
            sensors.append((sensor_components.group(1),
                            sensor_components.group(2),
                            sensor_components.group(3)))

        return sensors
