class Duration:
    def __init__(self, seconds, minutes, hours):
        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours
    
    @property
    def seconds(self):
        return self.__seconds
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def hours(self):
        return self.__hours

    @staticmethod
    def from_seconds(amount):
        return Duration(amount, amount/60, amount/3600)
    
    @staticmethod
    def from_minutes(amount):
        return Duration(amount * 60, amount, amount/60)
    
    @staticmethod
    def from_hours(amount):
        return Duration(amount * 3600, amount*60, amount)
    

duration = Duration.from_seconds(60)
print(duration.seconds)
print(duration.minutes)


duration = Duration.from_hours(1)
print(duration.minutes)

print(duration.seconds)