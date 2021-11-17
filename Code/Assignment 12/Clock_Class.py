class Clock():
    def __init__(self, hours=0, minutes=0, seconds=0, type=1):
        self.hours = hours #setting object values to passed args
        self.minutes = minutes
        self.seconds = seconds
        self.type = type

    def __str__(self): #printing clock info based on clock type
        if self.type == 0:
            return ("{:02}:{:02}:{:02}".format(self.hours, self.minutes, self.seconds)) #24 hour clock
        elif self.type == 1:
            if self.hours == 0: #12 hour clock in am
                return ("{:02}:{:02}:{:02} am".format(self.hours, self.minutes, self.seconds))
            if self.hours > 0 and self.hours <= 12:
                return ("{:02}:{:02}:{:02} am".format(self.hours, self.minutes, self.seconds))
            if self.hours > 12:
                self.hours -= 12 #12 hour clock in pm
                return ("{:02}:{:02}:{:02} pm".format(self.hours, self.minutes, self.seconds))
        
    def tick(self): #adding one second to clock time
        if self.seconds < 59: #if elif ladder associated with clock time overfall
            self.seconds += 1
        elif self.seconds == 59:
            self.seconds = 0
            if self.minutes < 59:
                self.minutes += 1
            elif self.minutes == 59:
                self.minutes = 0
                self.hours += 1
    
        