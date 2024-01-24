# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63672232/typeerror-currencyconverter-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(524059)

except ImportError:
    pass
try:
    from currency_converter import CurrencyConverter
    _l_(524061)

except ImportError:
    pass

global c
_l_(524062)
c = _c_(524064, _n_(524063, "CurrencyConverter", lambda: CurrencyConverter))
_l_(524065)
#test converter
# result = c.convert(100, 'USD', 'HKD')
# print(result)
#create window
root = _c_(524067, _n_(524066, "Tk", lambda: Tk))
_l_(524068)
_c_(524071, _a_(524070, _n_(524069, "root", lambda: root), "title"), "EZ Currency Converter")
_l_(524072)
_c_(524075, _a_(524074, _n_(524073, "root", lambda: root), "geometry"), "350x200")
_l_(524076)

#create currency option list
currencies = ["USD","EUR","JPY", "GBP","AUD", "CAD", "CHF","HKD","SGD", "MXN", 
"SEK", "PHP", "RUB", "HUF","LTL","MTL", "PLN", "ROL", "SIT", "SKK", 
]
_l_(524077)

def conversion(clicked, second_clicked, currency_amount):
    _l_(524093)

    result= _c_(524082, _n_(524078, "c", lambda: c), _n_(524079, "currency_amount", lambda: currency_amount), _n_(524080, "clicked", lambda: clicked), _n_(524081, "second_clicked", lambda: second_clicked))
    _l_(524083)
    final_conversion = _c_(524087, _n_(524084, "Label", lambda: Label), _n_(524085, "root", lambda: root), text= _n_(524086, "result", lambda: result))
    _l_(524088)
    _c_(524091, _a_(524090, _n_(524089, "final_conversion", lambda: final_conversion), "grid"), row=4, column=1, columnspan=2)
    _l_(524092)

#Set what kind of variable to expect
clicked = _c_(524095, _n_(524094, "StringVar", lambda: StringVar))
_l_(524096)
_c_(524099, _a_(524098, _n_(524097, "clicked", lambda: clicked), "set"), "USD")
_l_(524100)
second_clicked= _c_(524102, _n_(524101, "StringVar", lambda: StringVar))
_l_(524103)
_c_(524106, _a_(524105, _n_(524104, "second_clicked", lambda: second_clicked), "set"), "USD")
_l_(524107)

#welcome new users
welcome = _c_(524110, _n_(524108, "Label", lambda: Label), _n_(524109, "root", lambda: root), text="Welcome to your new favorite Currency Converter")
_l_(524111)

#create the dropdown options/ input box /  button
original =_c_(524116, _n_(524112, "OptionMenu", lambda: OptionMenu), _n_(524113, "root", lambda: root), _n_(524114, "clicked", lambda: clicked), *_n_(524115, "currencies", lambda: currencies))
_l_(524117)
converted =_c_(524122, _n_(524118, "OptionMenu", lambda: OptionMenu), _n_(524119, "root", lambda: root), _n_(524120, "second_clicked", lambda: second_clicked), *_n_(524121, "currencies", lambda: currencies))
_l_(524123)
currency_amount= _c_(524126, _n_(524124, "Entry", lambda: Entry), _n_(524125, "root", lambda: root), width=30)
_l_(524127)
convert = _c_(524141, _n_(524128, "Button", lambda: Button), _n_(524129, "root", lambda: root), text="Convert", padx=10, pady=10, command=lambda:_c_(524140, _n_(524130, "conversion", lambda: conversion), _c_(524133, _a_(524132, _n_(524131, "clicked", lambda: clicked), "get")),_c_(524136, _a_(524135, _n_(524134, "second_clicked", lambda: second_clicked), "get")), _c_(524139, _a_(524138, _n_(524137, "currency_amount", lambda: currency_amount), "get"))))
_l_(524142)


#place widgets
_c_(524145, _a_(524144, _n_(524143, "welcome", lambda: welcome), "grid"), row=0, column=1, columnspan=2)
_l_(524146)
_c_(524149, _a_(524148, _n_(524147, "original", lambda: original), "grid"), row=1, column= 1, columnspan=1)
_l_(524150)
_c_(524153, _a_(524152, _n_(524151, "converted", lambda: converted), "grid"), row=1, column=2, columnspan=1)
_l_(524154)
_c_(524157, _a_(524156, _n_(524155, "currency_amount", lambda: currency_amount), "grid"), row=2, column=1, columnspan=2)
_l_(524158)
_c_(524161, _a_(524160, _n_(524159, "convert", lambda: convert), "grid"), row=3, column=1, columnspan=2)
_l_(524162)

_c_(524165, _a_(524164, _n_(524163, "root", lambda: root), "mainloop"))
_l_(524166)