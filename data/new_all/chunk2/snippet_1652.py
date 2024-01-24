# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66721562/python-multiprocessing-typeerror-cannot-pickle-tkinter-tkapp-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class experimentPage(_a_(466285, _n_(466284, "tk", lambda: tk), "Frame")):
    _l_(466365)


    def __init__(self, parent, controller):
        _l_(466306)

        _c_(466291, _a_(466288, _a_(466287, _n_(466286, "tk", lambda: tk), "Frame"), "__init__"), _n_(466289, "self", lambda: self), _n_(466290, "parent", lambda: parent))
        _l_(466292)

        # start experiment on click
        _n_(466293, "self", lambda: self).button2 = _c_(466299, _a_(466295, _n_(466294, "tk", lambda: tk), "Button"), _n_(466296, "self", lambda: self), text="Ready",
                            command=_a_(466298, _n_(466297, "self", lambda: self), "logic"))
        _l_(466300)
        _c_(466304, _a_(466303, _a_(466302, _n_(466301, "self", lambda: self), "button2"), "pack"))
        _l_(466305)

    def proc1(self):
        _l_(466311)

        while True:
            _l_(466310)

            _c_(466308, _n_(466307, "print", lambda: print), "LOL1")
            _l_(466309)

    def proc2(self):
        _l_(466316)

        while True:
            _l_(466315)

            _c_(466313, _n_(466312, "print", lambda: print), "LOL2")
            _l_(466314)

    def proc3(self):
        _l_(466321)

        while True:
            _l_(466320)

            _c_(466318, _n_(466317, "print", lambda: print), "LOL3")
            _l_(466319)

    def logic(self):
        _l_(466364)

        t1 = _c_(466326, _a_(466323, _n_(466322, "multiprocessing", lambda: multiprocessing), "Process"), target=_a_(466325, _n_(466324, "self", lambda: self), "proc1"))
        _l_(466327)
        t2 = _c_(466332, _a_(466329, _n_(466328, "multiprocessing", lambda: multiprocessing), "Process"), target=_a_(466331, _n_(466330, "self", lambda: self), "proc2"))
        _l_(466333)
        t3 = _c_(466338, _a_(466335, _n_(466334, "multiprocessing", lambda: multiprocessing), "Process"), target=_a_(466337, _n_(466336, "self", lambda: self), "proc3"))
        _l_(466339)
        _c_(466342, _a_(466341, _n_(466340, "t1", lambda: t1), "start"))
        _l_(466343)
        _c_(466346, _a_(466345, _n_(466344, "t2", lambda: t2), "start"))
        _l_(466347)
        _c_(466350, _a_(466349, _n_(466348, "t3", lambda: t3), "start"))
        _l_(466351)
        _c_(466354, _a_(466353, _n_(466352, "t1", lambda: t1), "join"))
        _l_(466355)
        _c_(466358, _a_(466357, _n_(466356, "t2", lambda: t2), "join"))
        _l_(466359)
        _c_(466362, _a_(466361, _n_(466360, "t3", lambda: t3), "join"))
        _l_(466363)