# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54144305/type-error-missing-required-positional-arguments-with-multiple-py-files
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(572986)

except ImportError:
    pass
try:
    import curses
    _l_(572988)

except ImportError:
    pass
try:
    import Bauklotz_class
    _l_(572990)

except ImportError:
    pass

x1 = 10   #initialise coordinates
_l_(572991)   #initialise coordinates
y1 = 10
_l_(572992)
x2 = 20
_l_(572993)
y2 = 20
_l_(572994)

root = _c_(572996, _n_(572995, "Tk", lambda: Tk)) #create window
_l_(572997) #create window
_c_(573000, _a_(572999, _n_(572998, "root", lambda: root), "wm_title"), "Raspberry Pi GUI") #window title
_l_(573001) #window title
_c_(573004, _a_(573003, _n_(573002, "root", lambda: root), "config"), background = "#FFFFFF") #background color
_l_(573005) #background color

#The whole left frame and widgets involved
leftFrame = _c_(573008, _n_(573006, "Frame", lambda: Frame), _n_(573007, "root", lambda: root), width=200, height = 400)
_l_(573009)
_c_(573012, _a_(573011, _n_(573010, "leftFrame", lambda: leftFrame), "grid"), row=0, column = 0, padx = 10, pady = 3)
_l_(573013)
leftLabel1 = _c_(573016, _n_(573014, "Label", lambda: Label), _n_(573015, "leftFrame", lambda: leftFrame), text = "Platzhalter Text")
_l_(573017)
_c_(573020, _a_(573019, _n_(573018, "leftLabel1", lambda: leftLabel1), "grid"), row = 0, column = 0, padx = 10, pady = 3)
_l_(573021)
leftLabel2 = _c_(573024, _n_(573022, "Label", lambda: Label), _n_(573023, "leftFrame", lambda: leftFrame), text = "Dies ist ein Text\nmit mehreren Zeilen")
_l_(573025)
_c_(573028, _a_(573027, _n_(573026, "leftLabel2", lambda: leftLabel2), "grid"), row = 1, column = 0, padx = 10, pady = 3)
_l_(573029)


#the whole right frame and widgets involved
rightFrame = _c_(573032, _n_(573030, "Frame", lambda: Frame), _n_(573031, "root", lambda: root), width=400, height = 400)
_l_(573033)
_c_(573036, _a_(573035, _n_(573034, "rightFrame", lambda: rightFrame), "grid"), row = 0, column = 1, padx = 10, pady = 3)
_l_(573037)
E1 = _c_(573040, _n_(573038, "Entry", lambda: Entry), _n_(573039, "rightFrame", lambda: rightFrame), width = 50)
_l_(573041)
_c_(573044, _a_(573043, _n_(573042, "E1", lambda: E1), "grid"), row = 0, column = 0, padx = 10, pady = 60)
_l_(573045)

#The two functions for the 2 buttons created
def callback1():
    _l_(573054)

    test = _c_(573048, _a_(573047, _n_(573046, "Bauklotz_class", lambda: Bauklotz_class), "Baustein"), 20, 30, 40, 50, "red")
    _l_(573049)
    _c_(573052, _a_(573051, _n_(573050, "test", lambda: test), "show_new_object"))
    _l_(573053)

def callback2():
    _l_(573058)

    _c_(573056, _n_(573055, "print", lambda: print), 1+1)
    _l_(573057)

buttonFrame = _c_(573061, _n_(573059, "Frame", lambda: Frame), _n_(573060, "rightFrame", lambda: rightFrame))
_l_(573062)
_c_(573065, _a_(573064, _n_(573063, "buttonFrame", lambda: buttonFrame), "grid"), row = 1, column = 0, padx = 10, pady = 60)
_l_(573066)
B1 = _c_(573070, _n_(573067, "Button", lambda: Button), _n_(573068, "buttonFrame", lambda: buttonFrame), text = "Button1", bg = "#FF0000", width = 15, command = _n_(573069, "callback1", lambda: callback1))
_l_(573071)
_c_(573074, _a_(573073, _n_(573072, "B1", lambda: B1), "grid"), row = 0, column = 0, padx = 10, pady = 60)
_l_(573075)
B2 = _c_(573079, _n_(573076, "Button", lambda: Button), _n_(573077, "buttonFrame", lambda: buttonFrame), text = "Button2", bg ="#FFFF00", width = 15, command = _n_(573078, "callback2", lambda: callback2))
_l_(573080)
_c_(573083, _a_(573082, _n_(573081, "B2", lambda: B2), "grid"), row = 0, column = 1, padx = 10, pady = 60)
_l_(573084)

Slider = _c_(573088, _n_(573085, "Scale", lambda: Scale), _n_(573086, "rightFrame", lambda: rightFrame), from_ = 0, to = 100, resolution = 0.1, orient = _n_(573087, "HORIZONTAL", lambda: HORIZONTAL), length = 400)
_l_(573089)
_c_(573092, _a_(573091, _n_(573090, "Slider", lambda: Slider), "grid"), row = 2, column = 0, padx = 10, pady = 3)
_l_(573093)

Display = _c_(573096, _n_(573094, "Canvas", lambda: Canvas), _n_(573095, "rightFrame", lambda: rightFrame), width = 300, height = 300)
_l_(573097)
_c_(573100, _a_(573099, _n_(573098, "Display", lambda: Display), "configure"), background = 'black')
_l_(573101)
_c_(573104, _a_(573103, _n_(573102, "Display", lambda: Display), "grid"), row = 1, column = 3, padx = 10, pady = 3)
_l_(573105)

quadrat = _c_(573108, _a_(573107, _n_(573106, "Display", lambda: Display), "create_rectangle"), 20, 30, 40, 50, fill = "blue")
_l_(573109)
_c_(573117, _a_(573111, _n_(573110, "Display", lambda: Display), "coords"), _n_(573112, "quadrat", lambda: quadrat), _n_(573113, "x1", lambda: x1), _n_(573114, "y1", lambda: y1), _n_(573115, "x2", lambda: x2), _n_(573116, "y2", lambda: y2))
_l_(573118)


#following functions are for coordination of the square
#also you can find here the exceptions so that the object
#cant break out of the display widget

def down(event):
    _l_(573151)

    global x1, y1, x2, y2
    _l_(573119)
    if _n_(573120, "x2", lambda: x2) == 290 or _n_(573121, "y2", lambda: y2) == 300:
        _l_(573150)

        pass
        _l_(573122)
    else:
        y1 += 10
        _l_(573123)
        y2 += 10
        _l_(573124)
        _c_(573132, _a_(573126, _n_(573125, "Display", lambda: Display), "coords"), _n_(573127, "quadrat", lambda: quadrat), _n_(573128, "x1", lambda: x1), _n_(573129, "y1", lambda: y1), _n_(573130, "x2", lambda: x2), _n_(573131, "y2", lambda: y2))
        _l_(573133)
        _c_(573148, _a_(573135, _n_(573134, "leftLabel1", lambda: leftLabel1), "config"), text = "x1: " + _c_(573138, _n_(573136, "str", lambda: str), _n_(573137, "x1", lambda: x1)) + ", x2:" + _c_(573141, _n_(573139, "str", lambda: str), _n_(573140, "x2", lambda: x2)) + ", y1:" + _c_(573144, _n_(573142, "str", lambda: str), _n_(573143, "y1", lambda: y1)) + ", y2:" + _c_(573147, _n_(573145, "str", lambda: str), _n_(573146, "y2", lambda: y2)), width = "40" , )
        _l_(573149)
def up(event):
    _l_(573184)

    global x1, y1, x2, y2
    _l_(573152)
    if _n_(573153, "x2", lambda: x2) == 0 or _n_(573154, "y2", lambda: y2) == 10:
        _l_(573183)

        pass
        _l_(573155)
    else:
        y1 -= 10
        _l_(573156)
        y2 -= 10
        _l_(573157)
        _c_(573165, _a_(573159, _n_(573158, "Display", lambda: Display), "coords"), _n_(573160, "quadrat", lambda: quadrat), _n_(573161, "x1", lambda: x1), _n_(573162, "y1", lambda: y1), _n_(573163, "x2", lambda: x2), _n_(573164, "y2", lambda: y2))
        _l_(573166)
        _c_(573181, _a_(573168, _n_(573167, "leftLabel1", lambda: leftLabel1), "config"), text = "x1: " + _c_(573171, _n_(573169, "str", lambda: str), _n_(573170, "x1", lambda: x1)) + ", x2:" + _c_(573174, _n_(573172, "str", lambda: str), _n_(573173, "x2", lambda: x2)) + ", y1:" + _c_(573177, _n_(573175, "str", lambda: str), _n_(573176, "y1", lambda: y1)) + ", y2:" + _c_(573180, _n_(573178, "str", lambda: str), _n_(573179, "y2", lambda: y2)), width = "40" , )
        _l_(573182)
def left(event):
    _l_(573217)

    global x1, y1, x2, y2
    _l_(573185)
    if _n_(573186, "x1", lambda: x1) == 0 or _n_(573187, "y1", lambda: y1) == 10:
        _l_(573216)

        pass
        _l_(573188)
    else:
        x1 -= 10
        _l_(573189)
        x2 -= 10
        _l_(573190)
        _c_(573198, _a_(573192, _n_(573191, "Display", lambda: Display), "coords"), _n_(573193, "quadrat", lambda: quadrat), _n_(573194, "x1", lambda: x1), _n_(573195, "y1", lambda: y1), _n_(573196, "x2", lambda: x2), _n_(573197, "y2", lambda: y2))
        _l_(573199)
        _c_(573214, _a_(573201, _n_(573200, "leftLabel1", lambda: leftLabel1), "config"), text = "x1: " + _c_(573204, _n_(573202, "str", lambda: str), _n_(573203, "x1", lambda: x1)) + ", x2:" + _c_(573207, _n_(573205, "str", lambda: str), _n_(573206, "x2", lambda: x2)) + ", y1:" + _c_(573210, _n_(573208, "str", lambda: str), _n_(573209, "y1", lambda: y1)) + ", y2:" + _c_(573213, _n_(573211, "str", lambda: str), _n_(573212, "y2", lambda: y2)), width = "40" , )
        _l_(573215)
def right(event):
    _l_(573250)

    global x1, y1, x2, y2
    _l_(573218)
    if _n_(573219, "x1", lambda: x1) == 290 or _n_(573220, "y1", lambda: y1) == 300:
        _l_(573249)

        pass
        _l_(573221)
    else:
        x1 += 10
        _l_(573222)
        x2 += 10
        _l_(573223)
        _c_(573231, _a_(573225, _n_(573224, "Display", lambda: Display), "coords"), _n_(573226, "quadrat", lambda: quadrat), _n_(573227, "x1", lambda: x1), _n_(573228, "y1", lambda: y1), _n_(573229, "x2", lambda: x2), _n_(573230, "y2", lambda: y2))
        _l_(573232)
        _c_(573247, _a_(573234, _n_(573233, "leftLabel1", lambda: leftLabel1), "config"), text = "x1: " + _c_(573237, _n_(573235, "str", lambda: str), _n_(573236, "x1", lambda: x1)) + ", x2:" + _c_(573240, _n_(573238, "str", lambda: str), _n_(573239, "x2", lambda: x2)) + ", y1:" + _c_(573243, _n_(573241, "str", lambda: str), _n_(573242, "y1", lambda: y1)) + ", y2:" + _c_(573246, _n_(573244, "str", lambda: str), _n_(573245, "y2", lambda: y2)), width = "40" , )    
        _l_(573248)    
_c_(573254, _a_(573252, _n_(573251, "root", lambda: root), "bind"), '<a>', _n_(573253, "left", lambda: left))
_l_(573255)
_c_(573259, _a_(573257, _n_(573256, "root", lambda: root), "bind"), '<w>', _n_(573258, "up", lambda: up))
_l_(573260)
_c_(573264, _a_(573262, _n_(573261, "root", lambda: root), "bind"), '<s>', _n_(573263, "down", lambda: down))
_l_(573265)
_c_(573269, _a_(573267, _n_(573266, "root", lambda: root), "bind"), '<d>', _n_(573268, "right", lambda: right))
_l_(573270)


_c_(573273, _a_(573272, _n_(573271, "root", lambda: root), "mainloop"))
_l_(573274)