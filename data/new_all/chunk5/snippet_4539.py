# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55910379/typeerror-not-supported-between-instances-of-int-and-label
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(649815)

except ImportError:
    pass
def animate(frame_number,last_frame,label,framelist):
    _l_(649832)

    #if the frame number is bigger than the last frame
    if _n_(649816, "frame_number", lambda: frame_number) > _n_(649817, "last_frame", lambda: last_frame):
        _l_(649819)

        frame_number = 0
        _l_(649818)
    _c_(649824, _a_(649821, _n_(649820, "label", lambda: label), "config"), image=_n_(649822, "framelist", lambda: framelist)[_n_(649823, "frame_number", lambda: frame_number)]) 
    _l_(649825) 
    _c_(649830, _a_(649827, _n_(649826, "window", lambda: window), "after"), 1500, _n_(649828, "animate", lambda: animate), _n_(649829, "frame_number", lambda: frame_number)+1)
    _l_(649831)
#make mainwindow
window = _c_(649835, _a_(649834, _n_(649833, "tk", lambda: tk), "Tk"))
_l_(649836)
# List to hold all the frames
framelist = [] 
_l_(649837) 
# Frame index
frame_index = 0    
_l_(649838)    

while True:
    _l_(649860)

    try:
        _l_(649853)

        # Read a frame from GIF file
        part = _c_(649842, _a_(649839, 'gif -index {}', "format"), _n_(649840, "frame_index", lambda: frame_index),_n_(649841, "fr", lambda: fr))
        _l_(649843)
        frame = _c_(649847, _a_(649845, _n_(649844, "tk", lambda: tk), "PhotoImage"), file='giphy.gif', format=_n_(649846, "part", lambda: part))
        _l_(649848)
    except:
        _l_(649852)

        # Save index for last frame
        last_frame = _n_(649849, "frame_index", lambda: frame_index) - 1 
        _l_(649850) 
         # Will break when GIF index is reached
        break              
        _l_(649851)              
    _c_(649857, _a_(649855, _n_(649854, "framelist", lambda: framelist), "append"), _n_(649856, "frame", lambda: frame))
    _l_(649858)
     # Next frame index
    frame_index += 1       
    _l_(649859)       


#put the gif into a label
label = _c_(649864, _a_(649862, _n_(649861, "tk", lambda: tk), "Label"), _n_(649863, "window", lambda: window), bg='black')
_l_(649865)
_c_(649868, _a_(649867, _n_(649866, "label", lambda: label), "grid"), column = 1, row = 7)
_l_(649869)

_c_(649874, _n_(649870, "animate", lambda: animate), _n_(649871, "last_frame", lambda: last_frame),_n_(649872, "label", lambda: label),_n_(649873, "framelist", lambda: framelist),0)  # Start animation
_l_(649875)  # Start animation
#window size
_c_(649878, _a_(649877, _n_(649876, "window", lambda: window), "geometry"), "600x600")
_l_(649879)

#end of page
_c_(649882, _a_(649881, _n_(649880, "window", lambda: window), "mainloop"))
_l_(649883)