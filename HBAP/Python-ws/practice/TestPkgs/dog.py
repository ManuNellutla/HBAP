""":cvar
  T
"""
from datetime import date, timedelta
from dateutil.relativedelta import *

class Dog():
    """
      constructor for the class
          state objects : name, dob, vocab type
    """
    def __init__(self, name, year, month, day, vocab):
        self.name = name
        self.month = month
        self. day = day
        self. year = year
        self.vocab = vocab

    """
      accessor method : behavior - speak
    """
    def speak(self):
        return self.vocab

    """
       accessor method : get age
    """
    def getAge(self):
        birthDate = date(self.year, self.month, self.day)
        age =  relativedelta(date.today(), birthDate)
        return f"Age of the dog :{age.years} years, {age.months} months, {age.days} days"

    """ change speak """
    def changeBark(self, nBark):
        self.vocab = nBark

    """ 
     Access name 
    """
    def getName(self):
        return f"This dog's name is {self.name}"

