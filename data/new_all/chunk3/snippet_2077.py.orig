#Source: https://stackoverflow.com/questions/65530677/need-help-for-python-and-sqlite-typeerror-nonetype-object-is-not-subscrip
from tkinter import *
from tkinter import ttk
from datetime import datetime
import sqlite3

class Main:

    db_name = 'materiales.db'
    
    def __init__(self,window):
        self.wind = window
        self.wind.title('Stock App')

        #create frame
        frame = LabelFrame(self.wind, text = 'Add stock')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Name Input
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # Quantity Input
        Label(frame, text = 'Quantity: ').grid(row = 2, column = 0)
        self.quantity = Entry(frame)
        self.quantity.grid(row = 2, column = 1)

        # Button Add Stock
        ttk.Button(frame, text = 'Add Stock', command = self.add_stock).grid(row = 3, columnspan = 2, sticky = W + E)

        #Log Message
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        #Button Search Stocks
        ttk.Button(text = 'Search Stocks', command = self.search_stocks).grid(row = 5, column = 0, columnspan = 3, pady = 20, sticky = W + E) 



    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def validation(self):
        return len(self.name.get()) != 0 and len(self.quantity.get()) !=0
        

    def add_stock(self):
        time = datetime.now().strftime("%B %d, %Y")
        hour = datetime.now().strftime("%I:%M%p")
        query = 'SELECT totalstock FROM stocks WHERE name = ? AND MovementID = ( SELECT max( MovementID ) FROM stocks)'
        parameters = (self.name.get(),)
        lastrecord = self.run_query(query, parameters)
        total = lastrecord.fetchone()[0]
        total += int(self.quantity.get())
        if self.validation():
            query = 'INSERT INTO stocks VALUES(NULL, ?, ?, ?, ?, ?)'
            parameters = (self.name.get(), self.quantity.get(), total, time, hour)
            self.run_query(query, parameters)
            self.message['text'] = 'Stock for {} added succesfully'.format(self.name.get())
            self.name.delete(0, END)
            self.quantity.delete(0, END)
        else:
            self.message['text'] = 'Name and Quantity required'
        self.get_product()

    def search_stocks(self):
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Search Stocks'

        #Name Product
        Label(self.edit_wind, text = 'Name: ').grid(row = 0, column = 1)
        name = Entry(self.edit_wind)
        name.grid(row = 0, column = 2)

        Button(self.edit_wind, text = 'Search', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W)

    def edit_records(self, name):
        query = 'SELECT totalstock FROM stocks WHERE name = ? AND MovementID = ( SELECT max( MovementID ) FROM stocks)'
        parameters = (name)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Total stock is {}'.format(totalstock)
        self.get_product()

        
if __name__ == '__main__':
    window = Tk()
    application = Main(window)
    window.mainloop()