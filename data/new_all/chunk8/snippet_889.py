# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52546212/typeerror-start-missing-1-required-positional-argument-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(380120)

except ImportError:
    pass
try:
    from tkinter import PhotoImage
    _l_(380122)

except ImportError:
    pass
try:
    import time
    _l_(380124)

except ImportError:
    pass

class TimeCheck():
    _l_(380239)

    def __init__(self, parent=None, **kw):
        _l_(380131)

        _n_(380125, "self", lambda: self)._start = 0.0        
        _l_(380126)        
        _n_(380127, "self", lambda: self)._elapsedtime = 0.0
        _l_(380128)
        _n_(380129, "self", lambda: self)._running = 0              
        _l_(380130)              

    def trianglemove(move_x, move_y):
        _l_(380139)

        _c_(380137, _a_(380133, _n_(380132, "canvas", lambda: canvas), "move"), _n_(380134, "triangle3", lambda: triangle3), _n_(380135, "move_x", lambda: move_x), _n_(380136, "move_y", lambda: move_y))
        _l_(380138)

    def _update(self):
        _l_(380160)

        _n_(380140, "self", lambda: self)._elapsedtime = _c_(380143, _a_(380142, _n_(380141, "time", lambda: time), "time")) - _a_(380145, _n_(380144, "self", lambda: self), "_start")
        _l_(380146)
        _c_(380151, _a_(380148, _n_(380147, "self", lambda: self), "_setTime"), _a_(380150, _n_(380149, "self", lambda: self), "_elapsedtime"))
        _l_(380152)
        _n_(380153, "self", lambda: self)._timer = _c_(380158, _a_(380155, _n_(380154, "self", lambda: self), "after"), 50, _a_(380157, _n_(380156, "self", lambda: self), "_update"))
        _l_(380159)

    def _setTime(self, elap):
        _l_(380176)

        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = _c_(380163, _n_(380161, "int", lambda: int), _n_(380162, "elap", lambda: elap)/60)
        _l_(380164)
        seconds = _c_(380168, _n_(380165, "int", lambda: int), _n_(380166, "elap", lambda: elap) - _n_(380167, "minutes", lambda: minutes)*60.0)
        _l_(380169)
        hseconds = _c_(380174, _n_(380170, "int", lambda: int), (_n_(380171, "elap", lambda: elap) - _n_(380172, "minutes", lambda: minutes)*60.0 - _n_(380173, "seconds", lambda: seconds))*100)                  
        _l_(380175)                  

    def Start(self):
        _l_(380199)

        """ Start the stopwatch, ignore if running. """
        if not _a_(380178, _n_(380177, "self", lambda: self), "_running"):
            _l_(380198)

            _n_(380179, "self", lambda: self)._start = _c_(380182, _a_(380181, _n_(380180, "time", lambda: time), "time")) - _a_(380184, _n_(380183, "self", lambda: self), "_elapsedtime")
            _l_(380185)
            _c_(380188, _a_(380187, _n_(380186, "self", lambda: self), "_update"))
            _l_(380189)
            _n_(380190, "self", lambda: self)._running = 1
            _l_(380191)
            _c_(380193, _n_(380192, "print", lambda: print), "RECORD")
            _l_(380194)
            #for recordcounter in range(768):
            _c_(380196, _n_(380195, "trianglemove", lambda: trianglemove), 1, 0)
            _l_(380197)

    def Stop(self):
        _l_(380224)

        """ Stop the stopwatch, ignore if stopped. """
        if _a_(380201, _n_(380200, "self", lambda: self), "_running"):
            _l_(380223)

            _c_(380206, _a_(380203, _n_(380202, "self", lambda: self), "after_cancel"), _a_(380205, _n_(380204, "self", lambda: self), "_timer"))            
            _l_(380207)            
            _n_(380208, "self", lambda: self)._elapsedtime = _c_(380211, _a_(380210, _n_(380209, "time", lambda: time), "time")) - _a_(380213, _n_(380212, "self", lambda: self), "_start")    
            _l_(380214)    
            _c_(380219, _a_(380216, _n_(380215, "self", lambda: self), "_setTime"), _a_(380218, _n_(380217, "self", lambda: self), "_elapsedtime"))
            _l_(380220)
            _n_(380221, "self", lambda: self)._running = 0
            _l_(380222)

    def Reset(self):
        _l_(380238)

        """ Reset the stopwatch. """
        _n_(380225, "self", lambda: self)._start = _c_(380228, _a_(380227, _n_(380226, "time", lambda: time), "time"))         
        _l_(380229)         
        _n_(380230, "self", lambda: self)._elapsedtime = 0.0    
        _l_(380231)    
        _c_(380236, _a_(380233, _n_(380232, "self", lambda: self), "_setTime"), _a_(380235, _n_(380234, "self", lambda: self), "_elapsedtime"))    
        _l_(380237)    

root = _c_(380242, _a_(380241, _n_(380240, "tk", lambda: tk), "Tk"))
_l_(380243)
_c_(380246, _a_(380245, _n_(380244, "root", lambda: root), "geometry"), "960x600")
_l_(380247)

timechecker = _c_(380250, _n_(380248, "TimeCheck", lambda: TimeCheck), _n_(380249, "root", lambda: root))
_l_(380251)

recordbutton = _c_(380253, _n_(380252, "PhotoImage", lambda: PhotoImage), file="images/recordbutton.gif")
_l_(380254)
beatbutton = _c_(380256, _n_(380255, "PhotoImage", lambda: PhotoImage), file="images/beatbutton.gif")
_l_(380257)
stopbutton = _c_(380259, _n_(380258, "PhotoImage", lambda: PhotoImage), file="images/stopbutton.gif")
_l_(380260)

label_toptitle = _c_(380264, _a_(380262, _n_(380261, "tk", lambda: tk), "Label"), _n_(380263, "root", lambda: root), text="Program Name", font=(None, 40),)
_l_(380265)
_c_(380268, _a_(380267, _n_(380266, "label_toptitle", lambda: label_toptitle), "grid"), row=0, columnspan=3)
_l_(380269)

description = "To create rhythm, press the red record button. While recording, use the clicked note button to\n create a series of rectangle notes on screen. They can be held to extend the rectangles. \n\n Once you are done, press the red stop button to stop recording"
_l_(380270)

pixel = _c_(380272, _n_(380271, "PhotoImage", lambda: PhotoImage), width=1, height=1)
_l_(380273)
label_desc = _c_(380279, _a_(380275, _n_(380274, "tk", lambda: tk), "Label"), _n_(380276, "root", lambda: root), image=_n_(380277, "pixel", lambda: pixel), compound="center", width=900, font=(None, 14),
                                          padx=20, pady=10, text=_n_(380278, "description", lambda: description))
_l_(380280)

_c_(380283, _a_(380282, _n_(380281, "label_desc", lambda: label_desc), "grid"), row=1, columnspan=3)
_l_(380284)

canvas = _c_(380287, _a_(380286, _n_(380285, "tk", lambda: tk), "Canvas"), width=960, height=300, bg='white')
_l_(380288)
_c_(380291, _a_(380290, _n_(380289, "canvas", lambda: canvas), "grid"), row=2, column=0, columnspan=3)
_l_(380292)

for linecounter in _c_(380294, _n_(380293, "range", lambda: range), 49):
    _l_(380320)

    newtextbit = _n_(380295, "linecounter", lambda: linecounter) + 1
    _l_(380296)
    if (_n_(380297, "newtextbit", lambda: newtextbit) + 3) % 4 == 0 and _n_(380298, "newtextbit", lambda: newtextbit) != 49:
        _l_(380305)

        #print ('x is divisible by 3')
        _c_(380303, _a_(380300, _n_(380299, "canvas", lambda: canvas), "create_text"), (_n_(380301, "linecounter", lambda: linecounter) * 16 + 80), 90,
                                   fill="darkblue",
                                   font="Times 10 bold",
                                   text=_n_(380302, "newtextbit", lambda: newtextbit))
        _l_(380304)
    if (_n_(380306, "newtextbit", lambda: newtextbit) + 3) % 4 == 0:
        _l_(380319)

        _c_(380311, _a_(380308, _n_(380307, "canvas", lambda: canvas), "create_line"), ((_n_(380309, "linecounter", lambda: linecounter) * 16 + 80)), 40, ((_n_(380310, "linecounter", lambda: linecounter) * 16 + 80)), 70,
                                   width=1,
                                   fill="black"
                                   )
        _l_(380312)
    else:
            _c_(380317, _a_(380314, _n_(380313, "canvas", lambda: canvas), "create_line"), ((_n_(380315, "linecounter", lambda: linecounter) * 16 + 80)), 50, ((_n_(380316, "linecounter", lambda: linecounter) * 16 + 80)), 70,
                                       width=1,
                                       fill="black"
                                       )
            _l_(380318)
_c_(380323, _a_(380322, _n_(380321, "canvas", lambda: canvas), "create_line"), 73, 70, 860, 70,
                                   width=2,
                                   fill="black"
                                   )
_l_(380324)
triangle3 = _c_(380327, _a_(380326, _n_(380325, "canvas", lambda: canvas), "create_polygon"), 75, 25, 86, 25, 80, 40, fill ='red')
_l_(380328)

f1 = _c_(380332, _a_(380330, _n_(380329, "tk", lambda: tk), "Frame"), _n_(380331, "root", lambda: root), width=70, height=30)
_l_(380333)
_c_(380336, _a_(380335, _n_(380334, "f1", lambda: f1), "grid"), row=3, column=0, sticky='W')
_l_(380337)

button_record = _c_(380344, _a_(380339, _n_(380338, "tk", lambda: tk), "Button"), _n_(380340, "f1", lambda: f1),
                                                text="Record",
                                                image=_n_(380341, "recordbutton", lambda: recordbutton),
                                                command=_a_(380343, _n_(380342, "TimeCheck", lambda: TimeCheck), "Start"),
                                                compound="top"
                                                )
_l_(380345)
button_beat = _c_(380350, _a_(380347, _n_(380346, "tk", lambda: tk), "Button"), _n_(380348, "f1", lambda: f1),
                                                text="Beat",
                                                image=_n_(380349, "beatbutton", lambda: beatbutton),
                                                #command=tomato,
                                                compound="top"
                                                )
_l_(380351)
button_playstop = _c_(380356, _a_(380353, _n_(380352, "tk", lambda: tk), "Button"), _n_(380354, "f1", lambda: f1),
                                                text="Stop",
                                                image=_n_(380355, "stopbutton", lambda: stopbutton),
                                                #command=potato,
                                                compound="top"
                                                )
_l_(380357)

_c_(380360, _a_(380359, _n_(380358, "button_record", lambda: button_record), "pack"), side='left', padx=140)
_l_(380361)
_c_(380364, _a_(380363, _n_(380362, "button_beat", lambda: button_beat), "pack"), side='left', padx=55)
_l_(380365)
_c_(380368, _a_(380367, _n_(380366, "button_playstop", lambda: button_playstop), "pack"), side='left', padx=140)
_l_(380369)

_c_(380372, _a_(380371, _n_(380370, "root", lambda: root), "mainloop"))
_l_(380373)