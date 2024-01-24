# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18937994/python-and-tkinter-nameerror-global-name-roomchange-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(366415)

except ImportError:
    pass
try:
    import tkinter.messagebox
    _l_(366417)

except ImportError:
    pass

def displayText():
    _l_(366438)

    """ Display the Entry text value. """

    global roomChange
    _l_(366418)


    if _c_(366423, _a_(366422, _c_(366421, _a_(366420, _n_(366419, "roomChange", lambda: roomChange), "get")), "strip")) == "":
        _l_(366437)

        _c_(366426, _a_(366425, _a_(366424, tkinter, "messagebox"), "showerror"), "Invalid Value", "Please enter a valid classroom name.")
        _l_(366427)
    else:
        _c_(366435, _a_(366429, _a_(366428, tkinter, "messagebox"), "showinfo"), "Temporary Window", "Text value = " + _c_(366434, _a_(366433, _c_(366432, _a_(366431, _n_(366430, "roomChange", lambda: roomChange), "get")), "strip"))) 
        _l_(366436) 

def roomChanger():
    _l_(366497)


    chrm = _c_(366440, _n_(366439, "Tk", lambda: Tk))
    _l_(366441)
    _c_(366444, _a_(366443, _n_(366442, "chrm", lambda: chrm), "title"), "Change Room")
    _l_(366445)
    _c_(366448, _a_(366447, _n_(366446, "chrm", lambda: chrm), "wm_iconbitmap"), './Includes/icon.ico')
    _l_(366449)
    _n_(366450, "chrm", lambda: chrm)["padx"] = 40
    _l_(366451)
    _n_(366452, "chrm", lambda: chrm)["pady"] = 20       
    _l_(366453)       

    # Create a text frame to hold the text Label and the Entry widget
    textFrame = _c_(366456, _n_(366454, "Frame", lambda: Frame), _n_(366455, "chrm", lambda: chrm))
    _l_(366457)

    #Create a Label in textFrame
    roomChangeLabel = _c_(366460, _n_(366458, "Label", lambda: Label), _n_(366459, "textFrame", lambda: textFrame))
    _l_(366461)
    _n_(366462, "roomChangeLabel", lambda: roomChangeLabel)["text"] = "Enter name of classroom: "
    _l_(366463)
    _c_(366467, _a_(366465, _n_(366464, "roomChangeLabel", lambda: roomChangeLabel), "pack"), side=_n_(366466, "LEFT", lambda: LEFT))
    _l_(366468)

    # Create an Entry Widget in textFrame
    roomChange = _c_(366471, _n_(366469, "Entry", lambda: Entry), _n_(366470, "textFrame", lambda: textFrame))
    _l_(366472)
    _n_(366473, "roomChange", lambda: roomChange)["width"] = 50
    _l_(366474)
    _c_(366478, _a_(366476, _n_(366475, "roomChange", lambda: roomChange), "pack"), side=_n_(366477, "LEFT", lambda: LEFT))
    _l_(366479)

    _c_(366482, _a_(366481, _n_(366480, "textFrame", lambda: textFrame), "pack"))
    _l_(366483)

    roomChangeButton = _c_(366487, _n_(366484, "Button", lambda: Button), _n_(366485, "chrm", lambda: chrm), text="Submit", command=_n_(366486, "displayText", lambda: displayText))
    _l_(366488)
    _c_(366491, _a_(366490, _n_(366489, "roomChangeButton", lambda: roomChangeButton), "pack")) 
    _l_(366492) 

    _c_(366495, _a_(366494, _n_(366493, "chrm", lambda: chrm), "mainloop"))
    _l_(366496)


testButton = _c_(366501, _n_(366498, "Button", lambda: Button), _n_(366499, "window", lambda: window), text='Change Room', command=_n_(366500, "roomChanger", lambda: roomChanger))
_l_(366502)
_c_(366505, _a_(366504, _n_(366503, "testButton", lambda: testButton), "place"), x = 825, y = 360)
_l_(366506)