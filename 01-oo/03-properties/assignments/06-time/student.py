class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    @property
    def hours(self):
        return self.__hours
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def seconds(self):
        return self.__seconds

    @hours.setter
    def hours(self, value):
        if not isinstance(value, int):
            raise ValueError('Hours must be an integer')
        if not 0 <= value < 24:
            raise ValueError('Hours must be between 0 and 23')
        self.__hours = value
    
    @minutes.setter
    def minutes(self, value):
        if not isinstance(value, int):
            raise ValueError('Minutes must be an integer')
        if not 0 <= value < 60:
            raise ValueError('Minutes must be between 0 and 59')
        self.__minutes = value

    @seconds.setter
    def seconds(self, value):
        if not isinstance(value, int):
            raise ValueError('Seconds must be an integer')
        if not 0 <= value < 60:
            raise ValueError('Seconds must be between 0 and 59')
        self.__seconds = value
    
time = Time(0, 0, 0)
time.hours = 8
# time.hours = -1
# time.hours = 24