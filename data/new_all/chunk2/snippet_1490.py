# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51720014/attributeerror-module-multiprocessing-has-no-attribute-event
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import multiprocessing
    _l_(434465)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(434467)

except ImportError:
    pass
try:
    import cv2
    _l_(434469)

except ImportError:
    pass

e = _c_(434472, _a_(434471, _n_(434470, "multiprocessing", lambda: multiprocessing), "Event"))
_l_(434473)
p = None
_l_(434474)

# -------begin capturing and saving video
def startrecording(e,width,height,fourcc,out):
    _l_(434504)


    #width = 1920#window.winfo_screenwidth()
    #height = 500#window.winfo_screenheight()

    #fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    #out = cv2.VideoWriter("output.avi", fourcc, 5.0, (width,height))


    while True:
        _l_(434503)

        img = _c_(434479, _a_(434476, _n_(434475, "ImageGrab", lambda: ImageGrab), "grab"), bbox=(0,0,_n_(434477, "width", lambda: width),_n_(434478, "height", lambda: height)))
        _l_(434480)
        img_np = _c_(434484, _a_(434482, _n_(434481, "np", lambda: np), "array"), _n_(434483, "img", lambda: img))
        _l_(434485)

        frame = _c_(434491, _a_(434487, _n_(434486, "cv2", lambda: cv2), "cvtColor"), _n_(434488, "img_np", lambda: img_np), _a_(434490, _n_(434489, "cv2", lambda: cv2), "COLOR_BGR2RGB"))
        _l_(434492)

        #cv2.imshow('Screen', frame)

        _c_(434496, _a_(434494, _n_(434493, "out", lambda: out), "write"), _n_(434495, "frame", lambda: frame))
        _l_(434497)

        if _c_(434500, _a_(434499, _n_(434498, "cv2", lambda: cv2), "waitKey"), 1) == 27:
            _l_(434502)

            break
            _l_(434501)

def start_recording_proc(width,height,fourcc,out):
    _l_(434520)

    global p
    _l_(434505)
    p = _c_(434514, _a_(434507, _n_(434506, "multiprocessing", lambda: multiprocessing), "Process"), target=_n_(434508, "startrecording", lambda: startrecording), args=(_n_(434509, "e", lambda: e),_n_(434510, "width", lambda: width),_n_(434511, "height", lambda: height),_n_(434512, "fourcc", lambda: fourcc),_n_(434513, "out", lambda: out)))
    _l_(434515)
    _c_(434518, _a_(434517, _n_(434516, "p", lambda: p), "start"))
    _l_(434519)

# -------end video capture and stop tk
def stoprecording(out):
    _l_(434545)

    _c_(434523, _a_(434522, _n_(434521, "e", lambda: e), "set"))
    _l_(434524)
    _c_(434527, _a_(434526, _n_(434525, "p", lambda: p), "join"))
    _l_(434528)
    _c_(434531, _a_(434530, _n_(434529, "out", lambda: out), "release"))
    _l_(434532)
    _c_(434535, _a_(434534, _n_(434533, "cv2", lambda: cv2), "destroyAllWindows"))
    _l_(434536)


    _c_(434539, _a_(434538, _n_(434537, "root", lambda: root), "quit"))
    _l_(434540)
    _c_(434543, _a_(434542, _n_(434541, "root", lambda: root), "destroy"))
    _l_(434544)

if _n_(434546, "__name__", lambda: __name__) == "__main__":
    _l_(434599)

    # -------configure window
    root = _c_(434549, _a_(434548, _n_(434547, "tk", lambda: tk), "Tk"))
    _l_(434550)
    _c_(434553, _a_(434552, _n_(434551, "root", lambda: root), "geometry"), "%dx%d+0+0" % (100, 100))
    _l_(434554)

    width = 1920#window.winfo_screenwidth()
    _l_(434555)#window.winfo_screenwidth()
    height = 500#window.winfo_screenheight()
    _l_(434556)#window.winfo_screenheight()

    fourcc = _c_(434559, _a_(434558, _n_(434557, "cv2", lambda: cv2), "VideoWriter_fourcc"), *'MJPG')
    _l_(434560)
    out = _c_(434566, _a_(434562, _n_(434561, "cv2", lambda: cv2), "VideoWriter"), "output.avi", _n_(434563, "fourcc", lambda: fourcc), 5.0, (_n_(434564, "width", lambda: width),_n_(434565, "height", lambda: height)))
    _l_(434567)


    startbutton=_c_(434577, _a_(434569, _n_(434568, "tk", lambda: tk), "Button"), _n_(434570, "root", lambda: root),width=10,height=1,text='START',command= lambda: _c_(434576, _n_(434571, "start_recording_proc", lambda: start_recording_proc), _n_(434572, "width", lambda: width),_n_(434573, "height", lambda: height),_n_(434574, "fourcc", lambda: fourcc),_n_(434575, "out", lambda: out)))
    _l_(434578)
    stopbutton=_c_(434585, _a_(434580, _n_(434579, "tk", lambda: tk), "Button"), _n_(434581, "root", lambda: root),width=10,height=1,text='STOP', command= lambda: _c_(434584, _n_(434582, "stoprecording", lambda: stoprecording), _n_(434583, "out", lambda: out)))
    _l_(434586)
    _c_(434589, _a_(434588, _n_(434587, "startbutton", lambda: startbutton), "pack"))
    _l_(434590)
    _c_(434593, _a_(434592, _n_(434591, "stopbutton", lambda: stopbutton), "pack"))
    _l_(434594)

    # -------begin
    _c_(434597, _a_(434596, _n_(434595, "root", lambda: root), "mainloop"))
    _l_(434598)