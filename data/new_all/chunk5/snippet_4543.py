# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55910379/typeerror-not-supported-between-instances-of-int-and-label
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(677044)

except ImportError:
    pass
def animate(frame_number,last_frame,label,framelist):
    _l_(677061)

    #if the frame number is bigger than the last frame
    if _n_(677045, "frame_number", lambda: frame_number) > _n_(677046, "last_frame", lambda: last_frame):
        _l_(677048)

        frame_number = 0
        _l_(677047)
    _c_(677053, _a_(677050, _n_(677049, "label", lambda: label), "config"), image=_n_(677051, "framelist", lambda: framelist)[_n_(677052, "frame_number", lambda: frame_number)]) 
    _l_(677054) 
    _c_(677059, _a_(677056, _n_(677055, "window", lambda: window), "after"), 1500, _n_(677057, "animate", lambda: animate), _n_(677058, "frame_number", lambda: frame_number)+1)
    _l_(677060)
#make mainwindow
window = _c_(677064, _a_(677063, _n_(677062, "tk", lambda: tk), "Tk"))
_l_(677065)
# List to hold all the frames
framelist = [] 
_l_(677066) 
# Frame index
frame_index = 0    
_l_(677067)    

while True:
    _l_(677089)

    try:
        _l_(677082)

        # Read a frame from GIF file
        part = _c_(677071, _a_(677068, 'gif -index {}', "format"), _n_(677069, "frame_index", lambda: frame_index),_n_(677070, "fr", lambda: fr))
        _l_(677072)
        frame = _c_(677076, _a_(677074, _n_(677073, "tk", lambda: tk), "PhotoImage"), file='giphy.gif', format=_n_(677075, "part", lambda: part))
        _l_(677077)
    except:
        _l_(677081)

        # Save index for last frame
        last_frame = _n_(677078, "frame_index", lambda: frame_index) - 1 
        _l_(677079) 
         # Will break when GIF index is reached
        break              
        _l_(677080)              
    _c_(677086, _a_(677084, _n_(677083, "framelist", lambda: framelist), "append"), _n_(677085, "frame", lambda: frame))
    _l_(677087)
     # Next frame index
    frame_index += 1       
    _l_(677088)       


#put the gif into a label
label = _c_(677093, _a_(677091, _n_(677090, "tk", lambda: tk), "Label"), _n_(677092, "window", lambda: window), bg='black')
_l_(677094)
_c_(677097, _a_(677096, _n_(677095, "label", lambda: label), "grid"), column = 1, row = 7)
_l_(677098)

_c_(677103, _n_(677099, "animate", lambda: animate), _n_(677100, "last_frame", lambda: last_frame),_n_(677101, "label", lambda: label),_n_(677102, "framelist", lambda: framelist),0)  # Start animation
_l_(677104)  # Start animation
#window size
_c_(677107, _a_(677106, _n_(677105, "window", lambda: window), "geometry"), "600x600")
_l_(677108)

#end of page
_c_(677111, _a_(677110, _n_(677109, "window", lambda: window), "mainloop"))
_l_(677112)