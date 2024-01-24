# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18937994/python-and-tkinter-nameerror-global-name-roomchange-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(369299)

except ImportError:
    pass
try:
    import tkinter.messagebox
    _l_(369301)

except ImportError:
    pass

def displayText():
    _l_(369322)

    """ Display the Entry text value. """

    global roomChange
    _l_(369302)


    if _c_(369307, _a_(369306, _c_(369305, _a_(369304, _n_(369303, "roomChange", lambda: roomChange), "get")), "strip")) == "":
        _l_(369321)

        _c_(369310, _a_(369309, _a_(369308, tkinter, "messagebox"), "showerror"), "Invalid Value", "Please enter a valid classroom name.")
        _l_(369311)
    else:
        _c_(369319, _a_(369313, _a_(369312, tkinter, "messagebox"), "showinfo"), "Temporary Window", "Text value = " + _c_(369318, _a_(369317, _c_(369316, _a_(369315, _n_(369314, "roomChange", lambda: roomChange), "get")), "strip"))) 
        _l_(369320) 

def roomChanger():
    _l_(369381)


    chrm = _c_(369324, _n_(369323, "Tk", lambda: Tk))
    _l_(369325)
    _c_(369328, _a_(369327, _n_(369326, "chrm", lambda: chrm), "title"), "Change Room")
    _l_(369329)
    _c_(369332, _a_(369331, _n_(369330, "chrm", lambda: chrm), "wm_iconbitmap"), './Includes/icon.ico')
    _l_(369333)
    _n_(369334, "chrm", lambda: chrm)["padx"] = 40
    _l_(369335)
    _n_(369336, "chrm", lambda: chrm)["pady"] = 20       
    _l_(369337)       

    # Create a text frame to hold the text Label and the Entry widget
    textFrame = _c_(369340, _n_(369338, "Frame", lambda: Frame), _n_(369339, "chrm", lambda: chrm))
    _l_(369341)

    #Create a Label in textFrame
    roomChangeLabel = _c_(369344, _n_(369342, "Label", lambda: Label), _n_(369343, "textFrame", lambda: textFrame))
    _l_(369345)
    _n_(369346, "roomChangeLabel", lambda: roomChangeLabel)["text"] = "Enter name of classroom: "
    _l_(369347)
    _c_(369351, _a_(369349, _n_(369348, "roomChangeLabel", lambda: roomChangeLabel), "pack"), side=_n_(369350, "LEFT", lambda: LEFT))
    _l_(369352)

    # Create an Entry Widget in textFrame
    roomChange = _c_(369355, _n_(369353, "Entry", lambda: Entry), _n_(369354, "textFrame", lambda: textFrame))
    _l_(369356)
    _n_(369357, "roomChange", lambda: roomChange)["width"] = 50
    _l_(369358)
    _c_(369362, _a_(369360, _n_(369359, "roomChange", lambda: roomChange), "pack"), side=_n_(369361, "LEFT", lambda: LEFT))
    _l_(369363)

    _c_(369366, _a_(369365, _n_(369364, "textFrame", lambda: textFrame), "pack"))
    _l_(369367)

    roomChangeButton = _c_(369371, _n_(369368, "Button", lambda: Button), _n_(369369, "chrm", lambda: chrm), text="Submit", command=_n_(369370, "displayText", lambda: displayText))
    _l_(369372)
    _c_(369375, _a_(369374, _n_(369373, "roomChangeButton", lambda: roomChangeButton), "pack")) 
    _l_(369376) 

    _c_(369379, _a_(369378, _n_(369377, "chrm", lambda: chrm), "mainloop"))
    _l_(369380)


testButton = _c_(369385, _n_(369382, "Button", lambda: Button), _n_(369383, "window", lambda: window), text='Change Room', command=_n_(369384, "roomChanger", lambda: roomChanger))
_l_(369386)
_c_(369389, _a_(369388, _n_(369387, "testButton", lambda: testButton), "place"), x = 825, y = 360)
_l_(369390)