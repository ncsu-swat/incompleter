# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42906206/python-module-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(458806)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(458808)

except ImportError:
    pass
try:
    from tkinter.filedialog import askopenfilename
    _l_(458810)

except ImportError:
    pass


def main():
    _l_(458912)

    framevalues = []
    _l_(458811)
    count = 1
    _l_(458812)
    selectedvideo = _c_(458814, _n_(458813, "askopenfilename", lambda: askopenfilename))
    _l_(458815)
    selectedvideostring = _c_(458818, _n_(458816, "str", lambda: str), _n_(458817, "selectedvideo", lambda: selectedvideo))
    _l_(458819)
    cap = _c_(458823, _a_(458821, _n_(458820, "cv2", lambda: cv2), "VideoCapture"), _n_(458822, "selectedvideo", lambda: selectedvideo))
    _l_(458824)
    length = _c_(458831, _n_(458825, "int", lambda: int), _c_(458830, _a_(458827, _n_(458826, "cap", lambda: cap), "get"), _a_(458829, _n_(458828, "cv2", lambda: cv2), "CAP_PROP_FRAME_COUNT")))
    _l_(458832)

    while _c_(458835, _a_(458834, _n_(458833, "cap", lambda: cap), "isOpened")):
        _l_(458903)

        ret, frame = _c_(458838, _a_(458837, _n_(458836, "cap", lambda: cap), "read"))
        _l_(458839)

        # check if read frame was successful
        if _n_(458840, "ret", lambda: ret) == False:
            _l_(458842)

            break
            _l_(458841)
        # show frame first
        _c_(458846, _a_(458844, _n_(458843, "cv2", lambda: cv2), "imshow"), 'frame',_n_(458845, "frame", lambda: frame))
        _l_(458847)

        # then waitKey
        frameclick = _c_(458850, _a_(458849, _n_(458848, "cv2", lambda: cv2), "waitKey"), 0) & 0xFF
        _l_(458851)

        if _n_(458852, "frameclick", lambda: frameclick) == _c_(458854, _n_(458853, "ord", lambda: ord), 'a'):
            _l_(458902)

            _c_(458857, _n_(458855, "swingTag", lambda: swingTag), _n_(458856, "cap", lambda: cap))
            _l_(458858)

        elif _n_(458859, "frameclick", lambda: frameclick) == _c_(458861, _n_(458860, "ord", lambda: ord), 'r'):
            _l_(458901)

            _c_(458864, _n_(458862, "rewindFrames", lambda: rewindFrames), _n_(458863, "cap", lambda: cap))
            _l_(458865)

        elif _n_(458866, "frameclick", lambda: frameclick) == _c_(458868, _n_(458867, "ord", lambda: ord), 's'):
            _l_(458900)

            _c_(458871, _n_(458869, "stanceTag", lambda: stanceTag), _n_(458870, "cap", lambda: cap))
            _l_(458872)

        elif _n_(458873, "frameclick", lambda: frameclick) == _c_(458875, _n_(458874, "ord", lambda: ord), 'd'):
            _l_(458899)

            _c_(458878, _n_(458876, "unsureTag", lambda: unsureTag), _n_(458877, "cap", lambda: cap))
            _l_(458879)

        elif _n_(458880, "frameclick", lambda: frameclick) == _c_(458882, _n_(458881, "ord", lambda: ord), 'q'):
            _l_(458898)

            with _c_(458885, _n_(458883, "open", lambda: open), (_n_(458884, "selectedvideostring", lambda: selectedvideostring) + '.txt'), 'w') as textfile:
                _l_(458895)

                for item in _n_(458886, "framevalues", lambda: framevalues):
                    _l_(458894)

                    _c_(458892, _a_(458888, _n_(458887, "textfile", lambda: textfile), "write"), _c_(458891, _a_(458889, "{}\n", "format"), _n_(458890, "item", lambda: item)))
                    _l_(458893)
            break
            _l_(458896)

        else:
            continue
            _l_(458897)

    _c_(458906, _a_(458905, _n_(458904, "cap", lambda: cap), "release"))
    _l_(458907)
    _c_(458910, _a_(458909, _n_(458908, "cv2", lambda: cv2), "destroyAllWindows"))
    _l_(458911)

def stanceTag(cap):
    _l_(458939)

    _c_(458922, _a_(458914, _n_(458913, "framevalues", lambda: framevalues), "append"), '0' + ' ' + '|' + ' ' + _c_(458921, _n_(458915, "str", lambda: str), _c_(458920, _n_(458916, "int", lambda: int), _c_(458919, _a_(458918, _n_(458917, "cap", lambda: cap), "get"), 1))))
    _l_(458923)
    _c_(458933, _n_(458924, "print", lambda: print), _c_(458931, _n_(458925, "str", lambda: str), _c_(458930, _n_(458926, "int", lambda: int), _c_(458929, _a_(458928, _n_(458927, "cap", lambda: cap), "get"), 1))), '/', _n_(458932, "length", lambda: length)) 
    _l_(458934) 
    _c_(458937, _n_(458935, "print", lambda: print), _n_(458936, "framevalues", lambda: framevalues))
    _l_(458938)

def swingTag(cap):
    _l_(458966)

    _c_(458949, _a_(458941, _n_(458940, "framevalues", lambda: framevalues), "append"), '1' + ' ' + '|' + ' ' + _c_(458948, _n_(458942, "str", lambda: str), _c_(458947, _n_(458943, "int", lambda: int), _c_(458946, _a_(458945, _n_(458944, "cap", lambda: cap), "get"), 1))))
    _l_(458950)
    _c_(458960, _n_(458951, "print", lambda: print), _c_(458958, _n_(458952, "str", lambda: str), _c_(458957, _n_(458953, "int", lambda: int), _c_(458956, _a_(458955, _n_(458954, "cap", lambda: cap), "get"), 1))), '/', _n_(458959, "length", lambda: length))
    _l_(458961)
    _c_(458964, _n_(458962, "print", lambda: print), _n_(458963, "framevalues", lambda: framevalues)) 
    _l_(458965) 

def unsureTag(cap):
    _l_(458993)

    _c_(458976, _a_(458968, _n_(458967, "framevalues", lambda: framevalues), "append"), '-1' + ' ' + '|' + ' ' + _c_(458975, _n_(458969, "str", lambda: str), _c_(458974, _n_(458970, "int", lambda: int), _c_(458973, _a_(458972, _n_(458971, "cap", lambda: cap), "get"), 1))))
    _l_(458977)
    _c_(458987, _n_(458978, "print", lambda: print), _c_(458985, _n_(458979, "str", lambda: str), _c_(458984, _n_(458980, "int", lambda: int), _c_(458983, _a_(458982, _n_(458981, "cap", lambda: cap), "get"), 1))), '/', _n_(458986, "length", lambda: length)) 
    _l_(458988) 
    _c_(458991, _n_(458989, "print", lambda: print), _n_(458990, "framevalues", lambda: framevalues))
    _l_(458992)

def rewindFrames(cap):
    _l_(459020)

    _c_(459001, _a_(458995, _n_(458994, "cap", lambda: cap), "set"), 1,((_c_(459000, _n_(458996, "int", lambda: int), _c_(458999, _a_(458998, _n_(458997, "cap", lambda: cap), "get"), 1)) - 2)))
    _l_(459002)
    _c_(459010, _n_(459003, "print", lambda: print), _c_(459008, _n_(459004, "int", lambda: int), _c_(459007, _a_(459006, _n_(459005, "cap", lambda: cap), "get"), 1)), '/', _n_(459009, "length", lambda: length)) 
    _l_(459011) 
    _c_(459014, _a_(459013, _n_(459012, "framevalues", lambda: framevalues), "pop"))
    _l_(459015)
    _c_(459018, _n_(459016, "print", lambda: print), _n_(459017, "framevalues", lambda: framevalues))  
    _l_(459019)  






if _n_(459021, "__name__", lambda: __name__) == '__main__':
    _l_(459033)

    # this is called if this code was not imported ... ie it was directly run
    # if this is called, that means there is no GUI already running, so we need to create a root
    root = _c_(459024, _a_(459023, _n_(459022, "tk", lambda: tk), "Tk"))
    _l_(459025)
    _c_(459028, _a_(459027, _n_(459026, "root", lambda: root), "withdraw"))
    _l_(459029)
    _c_(459031, _n_(459030, "main", lambda: main))
    _l_(459032)