#Source: https://stackoverflow.com/questions/69028267/tkcalendar-get-date-gets-passed-to-a-function-but-returns-typeerror
from tkinter import *
from tkcalendar import *
import datetime

class test_class():
    
    selected_date = ""
    
    def __init__(self):
        self.window = Tk()
        
        self.stu_cal = Calendar(self.window,selectmode="day",year=int(test_class.get_year()),month=int(test_class.get_month()))
        self.stu_cal.grid(row=9,column=0)
        
        self.b3 = Button(self.window,text="Select this date",bg='#B6BDC4',fg='white',command=self.add_selected_date)
        self.b3.grid(row=9,column=6)
        
        self.window.mainloop()
        
    def add_selected_date(self):
        test_class.selected_date(self.stu_cal.get_date())
        
    @staticmethod    
    def get_year():
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        return date.strftime("%Y")
    
    @staticmethod 
    def get_month():
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        return date.strftime("%m")
    
    @classmethod
    def selected_date(cls,cal_date):
        cls.selected_date = cal_date

test_class()