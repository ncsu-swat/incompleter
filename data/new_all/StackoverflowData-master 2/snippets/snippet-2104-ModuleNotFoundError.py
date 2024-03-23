#Source: https://stackoverflow.com/questions/63672232/typeerror-currencyconverter-object-is-not-callable
from tkinter import *
from currency_converter import CurrencyConverter

global c
c = CurrencyConverter()
#test converter
# result = c.convert(100, 'USD', 'HKD')
# print(result)
#create window
root = Tk()
root.title("EZ Currency Converter")
root.geometry("350x200")

#create currency option list
currencies = ["USD","EUR","JPY", "GBP","AUD", "CAD", "CHF","HKD","SGD", "MXN", 
"SEK", "PHP", "RUB", "HUF","LTL","MTL", "PLN", "ROL", "SIT", "SKK", 
]

def conversion(clicked, second_clicked, currency_amount):
    result= c(currency_amount, clicked, second_clicked)
    final_conversion = Label(root, text= result)
    final_conversion.grid(row=4, column=1, columnspan=2)
    

#Set what kind of variable to expect
clicked = StringVar()
clicked.set("USD")
second_clicked= StringVar()
second_clicked.set("USD")

#welcome new users
welcome = Label(root, text="Welcome to your new favorite Currency Converter")

#create the dropdown options/ input box /  button
original =OptionMenu(root, clicked, *currencies)
converted =OptionMenu(root, second_clicked, *currencies)
currency_amount= Entry(root, width=30)
convert = Button(root, text="Convert", padx=10, pady=10, command=lambda:conversion(clicked.get(),second_clicked.get(), currency_amount.get()))


#place widgets
welcome.grid(row=0, column=1, columnspan=2)
original.grid(row=1, column= 1, columnspan=1)
converted.grid(row=1, column=2, columnspan=1)
currency_amount.grid(row=2, column=1, columnspan=2)
convert.grid(row=3, column=1, columnspan=2)

root.mainloop()