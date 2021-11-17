class Clock():
    def __init__(self, hours=0, minutes=0, seconds=0, type=1):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.type = type

    def __str__(self):
        if self.type == 0:
            return ("{:02}:{:02}:{:02}".format(self.hours, self.minutes, self.seconds))
        elif self.type == 1:
            if self.hours == 0:
                return ("{:02}:{:02}:{:02} am".format(self.hours, self.minutes, self.seconds))
            if self.hours > 0 and self.hours <= 12:
                return ("{:02}:{:02}:{:02} am".format(self.hours, self.minutes, self.seconds))
            if self.hours > 12:
                self.hours -= 12
                return ("{:02}:{:02}:{:02} pm".format(self.hours, self.minutes, self.seconds))
        
    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        elif self.seconds == 59:
            self.seconds = 0
            if self.minutes < 59:
                self.minutes += 1
            elif self.minutes == 59:
                self.minutes = 0
                self.hours += 1
    
        