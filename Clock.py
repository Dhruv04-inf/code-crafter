# class CINF 308
# Dhruv Amrishbhai Patel
# Assignment - 5

#Import TimeType which is the class TimeType in the file Named TimeType.
from TimeType import TimeType 

# The Clock Class inherits the TimeType class.
class Clock (TimeType):
    
    # List if Days in each month that is Jan TO Dec.
    monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]  
    
    #Calls the __init__ method of TimeType class and also creates variable for month,  days, year
    def __init__(self):
        self.day = 1
        self.month = 1 
        self.year = 1980
        super().__init__()
     
    # This determines that the entered year is a leap year or not.
    def leapyear(self, years):
        if (years % 4 == 0 and years % 100 != 0) or (years  % 100 == 0 and years % 400 == 0):
            return True
        else:
            return False

    # setClock method takes 6 arguments and also checks if it is a leap year 
    #This also check the entered date month year sec min and hour is valid or not and returns true or false, accordingly.
    def setClock(self, hours, minutes, seconds, months, days, years):
        if self.leapyear(years)== True :
            self.monthDays[1] = 29
        else:
            self.monthDays[1] = 28
            
        if self.set_time(hours, minutes, seconds):          
            if 1 <= self.day <= self.monthDays[months - 1]:
                self.month = months
                self.day = days
                self.year = years
                return True
            else:
                return False
        else: 
            return False

    #This increase a day and if necessary increase month and year.
    def increaseDay(self):
        self.day += 1
        if self.day > self.monthDays[self.month - 1]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
        
    #This decrease a day and if necessary decrease month and year.
    def decreaseDay(self):
        self.day -= 1
        if self.day < 1:
            self.day = self.monthDays[self.month - 1]
            self.month -= 1 
            if self.month < 1:
                self.month = 12
                self.year -= 1  

    #This method do increase a second and all other aspects if necessary.
    def increaseSecond(self):
        super().increase_second()
        if super().get_seconds() == 0:
            self.increaseDay()
    
    #This method do decrease a second and all other aspects if necessary.
    def decreaseSecond(self):
        super().decrease_second()
        if super().get_seconds() == 59:
            self.decreaseDay()
    
    #This str methods calls the str method of TimeType class and also make formats of the month, day and year.
    def __str__(self):
        timeTypeStr = super().__str__()
        return (f"{self.month:02}/{self.day:02}/{self.year:04} {timeTypeStr}")
    