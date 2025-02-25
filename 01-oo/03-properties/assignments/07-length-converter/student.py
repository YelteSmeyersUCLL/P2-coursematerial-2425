class LengthConverter:
    def __init__(self):
        self.__distance_in_meter = 0.0

    @property
    def meter(self):
        return self.__distance_in_meter

    @meter.setter
    def meter(self, value):
        self.__distance_in_meter = value

    @property
    def feet(self):
        return self.__distance_in_meter * 3.28084

    @feet.setter
    def feet(self, value):
        self.__distance_in_meter = value / 3.28084

    @property
    def inch(self):
        return self.__distance_in_meter * 39.3701

    @inch.setter
    def inch(self, value):
        self.__distance_in_meter = value / 39.3701

# Example usage:
converter = LengthConverter()

# Set the distance to 100 meter
converter.meter = 100

# Convert the 100 meter into feet
print(converter.feet)  # 328.084

# Convert the 100 meter into inch
print(converter.inch)  # 3937.01

# Convert the 100 meter into meter
print(converter.meter)  # 100

# Set the distance to 5 feet
converter.feet = 5

# Convert 5 feet into inches
print(converter.inch)  # 60

# Set distance to 10 inch
converter.inch = 10

# Converting to meter
print(converter.meter)  # 0.254

# Converting to feet
print(converter.feet)  # 0.833333