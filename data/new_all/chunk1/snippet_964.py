# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64304288/opencv-attributeerror-module-cv2-cv2-has-no-attribute-trackerboosting-create
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(384920)

except ImportError:
    pass
def ask_for_tracker():
    _l_(384974)

    _c_(384922, _n_(384921, "print", lambda: print), "Welcome! What Tracker API would you like to use?")
    _l_(384923)
    _c_(384925, _n_(384924, "print", lambda: print), "Enter 0 for BOOSTING: ")
    _l_(384926)
    _c_(384928, _n_(384927, "print", lambda: print), "Enter 1 for MIL: ")
    _l_(384929)
    _c_(384931, _n_(384930, "print", lambda: print), "Enter 2 for KCF: ")
    _l_(384932)
    _c_(384934, _n_(384933, "print", lambda: print), "Enter 3 for TLD: ")
    _l_(384935)
    _c_(384937, _n_(384936, "print", lambda: print), "Enter 4 for MEDIANFLOW: ")
    _l_(384938)
    choice = _c_(384940, _n_(384939, "input", lambda: input), "Please select your tracker: ")
    _l_(384941)
    
    if _n_(384942, "choice", lambda: choice) == '0':
        _l_(384947)

        tracker = _c_(384945, _a_(384944, _n_(384943, "cv2", lambda: cv2), "TrackerBoosting_create"))
        _l_(384946)
    if _n_(384948, "choice", lambda: choice) == '1':
        _l_(384953)

        tracker = _c_(384951, _a_(384950, _n_(384949, "cv2", lambda: cv2), "TrackerMIL_create"))
        _l_(384952)
    if _n_(384954, "choice", lambda: choice) == '2':
        _l_(384959)

        tracker = _c_(384957, _a_(384956, _n_(384955, "cv2", lambda: cv2), "TrackerKCF_create"))
        _l_(384958)
    if _n_(384960, "choice", lambda: choice) == '3':
        _l_(384965)

        tracker = _c_(384963, _a_(384962, _n_(384961, "cv2", lambda: cv2), "TrackerTLD_create"))
        _l_(384964)
    if _n_(384966, "choice", lambda: choice) == '4':
        _l_(384971)

        tracker = _c_(384969, _a_(384968, _n_(384967, "cv2", lambda: cv2), "TrackerMedianFlow_create"))
        _l_(384970)
    aux = _n_(384972, "tracker", lambda: tracker)
    _l_(384973)
    return aux

tracker = _c_(384976, _n_(384975, "ask_for_tracker", lambda: ask_for_tracker)) 
_l_(384977) 