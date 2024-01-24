# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74322469/python3-multiprocessing-pool-in-pyqt5-qthread-raises-typeerror-cannot-pickle-ta
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(530953)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
    _l_(530955)

except ImportError:
    pass
try:
    from PyQt5.QtCore import QThread, pyqtSignal , pyqtSlot
    _l_(530957)

except ImportError:
    pass
try:
    import time
    _l_(530959)

except ImportError:
    pass
try:
    import os
    _l_(530961)

except ImportError:
    pass
try:
    import multiprocessing as mp
    _l_(530963)

except ImportError:
    pass


def work(x):
    _l_(530974)

    # print('os.getpid() : {}'.format(os.getpid()), time.time(),'\n')
    _c_(530966, _a_(530965, _n_(530964, "time", lambda: time), "sleep"), 1)
    _l_(530967)
    _c_(530970, _n_(530968, "print", lambda: print), _n_(530969, "x", lambda: x))
    _l_(530971)
    aux = _n_(530972, "x", lambda: x)
    _l_(530973)
    
    return aux

class TaskThread(_n_(530975, "QThread", lambda: QThread)):
    _l_(531062)

    
    results = _c_(530978, _n_(530976, "pyqtSignal", lambda: pyqtSignal), _n_(530977, "object", lambda: object))
    _l_(530979)
    
    def __init__(self, parent=None, **kwargs):
        _l_(530995)

        _c_(530983, _a_(530981, _n_(530980, "super", lambda: super)(), "__init__"), _n_(530982, "parent", lambda: parent))
        _l_(530984)
        
        _c_(530993, _n_(530985, "print", lambda: print), "Thread app:", _c_(530992, _n_(530986, "int", lambda: int), _c_(530991, _a_(530990, _c_(530989, _a_(530988, _n_(530987, "QThread", lambda: QThread), "currentThread")), "currentThreadId"))))
        _l_(530994)
    
    
    @_c_(530997, _n_(530996, "pyqtSlot", lambda: pyqtSlot))
    def run(self):
        _l_(531054)

        
        _c_(530999, _n_(530998, "print", lambda: print), 'run..................')
        _l_(531000)
        
        _c_(531009, _n_(531001, "print", lambda: print), "Thread app run :", _c_(531008, _n_(531002, "int", lambda: int), _c_(531007, _a_(531006, _c_(531005, _a_(531004, _n_(531003, "QThread", lambda: QThread), "currentThread")), "currentThreadId")))) ## i.e. 140079831918336
        _l_(531010) ## i.e. 140079831918336
        
        _c_(531015, _n_(531011, "print", lambda: print), "Thread app run :", _c_(531014, _a_(531013, _n_(531012, "QThread", lambda: QThread), "currentThread"))) ## i.e. <__main__.TaskThread object at 0x7f66ed6f9280>
        _l_(531016) ## i.e. <__main__.TaskThread object at 0x7f66ed6f9280>
        
        _c_(531023, _n_(531017, "print", lambda: print), "Thread app run :", _c_(531022, _a_(531021, _c_(531020, _a_(531019, _n_(531018, "QThread", lambda: QThread), "currentThread")), "currentThreadId"))) ## i.e. <sip.voidptr object at 0x7f66eceb94b0>
        _l_(531024) ## i.e. <sip.voidptr object at 0x7f66eceb94b0>
        
        testFL = [1, 2, 3, 4, 5, 6]
        _l_(531025)
        pool = _c_(531028, _a_(531027, _n_(531026, "mp", lambda: mp), "Pool"), 6)
        _l_(531029)
       
        
       
        result = _c_(531035, _a_(531031, _n_(531030, "pool", lambda: pool), "map"), _a_(531033, _n_(531032, "self", lambda: self), "work"), _n_(531034, "testFL", lambda: testFL))  # TypeError: cannot pickle 'TaskThread' object
        _l_(531036)  # TypeError: cannot pickle 'TaskThread' object
        
        # result = pool.map(work, testFL)  ## this works using work at top level 
        
        _c_(531039, _a_(531038, _n_(531037, "pool", lambda: pool), "close"))
        _l_(531040)
        _c_(531043, _a_(531042, _n_(531041, "pool", lambda: pool), "join"))
        _l_(531044)
        
        
        # result = []
        # for i in testFL:
            
        #     result.append(self.work(i))
            
            
        
        
        # print(result)
        # print(type(result))
        
        _c_(531049, _a_(531047, _a_(531046, _n_(531045, "self", lambda: self), "results"), "emit"), _n_(531048, "result", lambda: result))
        _l_(531050)
        
        _c_(531052, _n_(531051, "print", lambda: print), 'QThread run finished')
        _l_(531053)
    def work(self, x):
        _l_(531061)

        # print('os.getpid() : {}'.format(os.getpid()), time.time())
        # time.sleep(1)
        _c_(531057, _n_(531055, "print", lambda: print), _n_(531056, "x", lambda: x))
        _l_(531058)
        aux = _n_(531059, "x", lambda: x)
        _l_(531060)
        return aux
class MainWindow(_n_(531063, "QMainWindow", lambda: QMainWindow)):
    _l_(531171)

    
    def __init__(self, *args, **kwargs):
        _l_(531119)

        _c_(531068, _a_(531065, _n_(531064, "super", lambda: super)(), "__init__"), *_n_(531066, "args", lambda: args), **_n_(531067, "kwargs", lambda: kwargs))
        _l_(531069)

        _c_(531072, _a_(531071, _n_(531070, "self", lambda: self), "setGeometry"), 100, 100, 300, 50)
        _l_(531073)
        _c_(531076, _a_(531075, _n_(531074, "self", lambda: self), "setWindowTitle"), 'QThread Demo')
        _l_(531077)
        
        # setup widget
        _n_(531078, "self", lambda: self).widget = _c_(531080, _n_(531079, "QWidget", lambda: QWidget))
        _l_(531081)
        layout = _c_(531083, _n_(531082, "QVBoxLayout", lambda: QVBoxLayout))
        _l_(531084)
        _c_(531089, _a_(531087, _a_(531086, _n_(531085, "self", lambda: self), "widget"), "setLayout"), _n_(531088, "layout", lambda: layout))
        _l_(531090)
        _c_(531095, _a_(531092, _n_(531091, "self", lambda: self), "setCentralWidget"), _a_(531094, _n_(531093, "self", lambda: self), "widget"))       
        _l_(531096)       

        _n_(531097, "self", lambda: self).btn_start = _c_(531101, _n_(531098, "QPushButton", lambda: QPushButton), 'Start', clicked=_a_(531100, _n_(531099, "self", lambda: self), "start"))
        _l_(531102)

        _c_(531107, _a_(531104, _n_(531103, "layout", lambda: layout), "addWidget"), _a_(531106, _n_(531105, "self", lambda: self), "btn_start"))
        _l_(531108)
        
        _c_(531117, _n_(531109, "print", lambda: print), "QMainWindow:", _c_(531116, _n_(531110, "int", lambda: int), _c_(531115, _a_(531114, _c_(531113, _a_(531112, _n_(531111, "QThread", lambda: QThread), "currentThread")), "currentThreadId"))))
        _l_(531118)
    def start(self):
        _l_(531124)

        
        _c_(531122, _a_(531121, _n_(531120, "self", lambda: self), "use_thread"))
        _l_(531123)


    def use_thread(self):
        _l_(531151)

        _n_(531125, "self", lambda: self).thread = _c_(531128, _n_(531126, "TaskThread", lambda: TaskThread), _n_(531127, "self", lambda: self))
        _l_(531129)
        _c_(531136, _a_(531133, _a_(531132, _a_(531131, _n_(531130, "self", lambda: self), "thread"), "finished"), "connect"), _a_(531135, _n_(531134, "self", lambda: self), "task_finished"))
        _l_(531137)
        
        
        _c_(531144, _a_(531141, _a_(531140, _a_(531139, _n_(531138, "self", lambda: self), "thread"), "results"), "connect"), _a_(531143, _n_(531142, "self", lambda: self), "print_qthread_res"))
        _l_(531145)
        
        _c_(531149, _a_(531148, _a_(531147, _n_(531146, "self", lambda: self), "thread"), "start"))
        _l_(531150)
    
    @_c_(531154, _n_(531152, "pyqtSlot", lambda: pyqtSlot), _n_(531153, "object", lambda: object))
    def print_qthread_res(self, objectz):
        _l_(531165)

        
        _c_(531157, _n_(531155, "print", lambda: print), 'passssed .......... : ', _n_(531156, "objectz", lambda: objectz))
        _l_(531158)
        _c_(531163, _n_(531159, "print", lambda: print), 'type : ', _c_(531162, _n_(531160, "type", lambda: type), _n_(531161, "objectz", lambda: objectz)))
        _l_(531164)
    
    def task_finished(self):
        _l_(531170)

        
        _c_(531167, _n_(531166, "print", lambda: print), 'QThread FINISHED !!!!!!!!!')
        _l_(531168)
        pass
        _l_(531169)
if _n_(531172, "__name__", lambda: __name__) == '__main__':
    _l_(531192)

    app = _c_(531176, _n_(531173, "QApplication", lambda: QApplication), _a_(531175, _n_(531174, "sys", lambda: sys), "argv"))
    _l_(531177)
    window = _c_(531179, _n_(531178, "MainWindow", lambda: MainWindow))
    _l_(531180)
    _c_(531183, _a_(531182, _n_(531181, "window", lambda: window), "show"))
    _l_(531184)
    _c_(531190, _a_(531186, _n_(531185, "sys", lambda: sys), "exit"), _c_(531189, _a_(531188, _n_(531187, "app", lambda: app), "exec")))
    _l_(531191)