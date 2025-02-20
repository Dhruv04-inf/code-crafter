# class CINF 308
# Dhruv Amrishbhai Patel
# Assignment - 5

class TimeType:
    
    # __init__ method that will be exected as soon as the program loads this class.
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
    
    #Get methods will returns time that is hour, minute and seconds when needed by the user.
    def get_hours(self):
        return self.hour
    
    def get_minutes(self):
        return self.minute
    
    def get_seconds(self):
        return self.second
    
    #Set methods will set time that is hour, minute and seconds when called by the user. 
    #The hour will set the hours same goes for the minutes and seconds.
    #The set_time will can manipulate all the hour, minutes and seconds simultaneously.
    def set_hours(self, hours):
        if hours >= 0 and hours <= 23:
            self.hour = hours
            return True
        else:
            return False
        
    def set_minutes(self, minutes):
        if minutes >= 0 and minutes <= 59:
            self.minute = minutes
            return True
        else:
            return False
    
    def set_seconds(self, seconds):
        if seconds >= 0 and seconds <= 59:
            self.second = seconds
            return True
        else:
            return False
        
    def set_time(self, hours, minutes, seconds):
        if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <=59:
            self.hour = hours
            self.minute = minutes
            self.second = seconds
            return True
        else: 
            return False

    #The increase and decrease methods will do increement and decreement of the seconds when called.
    #It also changes the minutes and hours as needed.
    def increase_second(self): 
        self.second += 1
        if self.second > 59:
            self.minute += 1
            self.second=0
            if self.minute > 59:
                self.minute = 0
                self.hour += 1
                if self.hour > 23:
                    self.hour == 0
                
    
    def decrease_second(self):
        self.second -= 1
        if self.second < 1:
            self.second = 59
            self.minute -= 1
            if self.minute < 1:
                self.minute = 59
                self.hour -= 1
                if self.hour < 1:
                    self.hour == 23
                

    #The __str__ method will format the data and will print meaningful things rather than the position of object.
    
    def __str__(self):
        period = "AM"  
        hour = self.hour
        
        if self.hour > 12:
            period = "PM"
            if self.hour > 12:
                self.hour -= 12 
        if self.hour == 0:
            self.hour = 12
        
        return (f"{self.hour:02}:{self.minute:02}:{self.second:02} {period}")
        
          
