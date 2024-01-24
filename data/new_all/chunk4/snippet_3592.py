# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71631276/attributeerror-module-tkinter-scrolledtext-has-no-attribute-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from operator import truediv
    _l_(626901)

except ImportError:
    pass
try:
    import socket
    _l_(626903)

except ImportError:
    pass
try:
    import threading
    _l_(626905)

except ImportError:
    pass
try:
    import tkinter
    _l_(626907)

except ImportError:
    pass
try:
    import tkinter.scrolledtext
    _l_(626909)

except ImportError:
    pass
try:
    from tkinter import simpledialog
    _l_(626911)

except ImportError:
    pass

class client:
    _l_(627155)


    def __init__(self):
        _l_(626964)

        _n_(626912, "self", lambda: self).server = _c_(626919, _a_(626914, _n_(626913, "socket", lambda: socket), "socket"), _a_(626916, _n_(626915, "socket", lambda: socket), "AF_INET"), _a_(626918, _n_(626917, "socket", lambda: socket), "SOCK_STREAM"))
        _l_(626920)
        _c_(626924, _a_(626923, _a_(626922, _n_(626921, "self", lambda: self), "server"), "connect"), ('localhost', 1234))
        _l_(626925)

        msg = _c_(626928, _a_(626927, _n_(626926, "tkinter", lambda: tkinter), "Tk"))
        _l_(626929)
        _c_(626932, _a_(626931, _n_(626930, "msg", lambda: msg), "withdraw"))
        _l_(626933)

        _n_(626934, "self", lambda: self).nickname = _c_(626938, _a_(626936, _n_(626935, "simpledialog", lambda: simpledialog), "askstring"), "Nickname", "Please choose a nickname", parent=_n_(626937, "msg", lambda: msg))
        _l_(626939)

        _n_(626940, "self", lambda: self).gui_done = False 
        _l_(626941) 
        _n_(626942, "self", lambda: self).running = True
        _l_(626943)

        gui_thread = _c_(626948, _a_(626945, _n_(626944, "threading", lambda: threading), "Thread"), target=_a_(626947, _n_(626946, "self", lambda: self), "gui_loop"))
        _l_(626949)
        receive_thread = _c_(626954, _a_(626951, _n_(626950, "threading", lambda: threading), "Thread"), target=_a_(626953, _n_(626952, "self", lambda: self), "receive"))
        _l_(626955)

        _c_(626958, _a_(626957, _n_(626956, "gui_thread", lambda: gui_thread), "start"))
        _l_(626959)
        _c_(626962, _a_(626961, _n_(626960, "receive_thread", lambda: receive_thread), "start"))
        _l_(626963)

    def gui_loop(self):
        _l_(627070)

        _n_(626965, "self", lambda: self).win = _c_(626968, _a_(626967, _n_(626966, "tkinter", lambda: tkinter), "Tk"))
        _l_(626969)
        _c_(626973, _a_(626972, _a_(626971, _n_(626970, "self", lambda: self), "win"), "configure"), bg="lightgray")
        _l_(626974)
        
        _n_(626975, "self", lambda: self).chat_label = _c_(626980, _a_(626977, _n_(626976, "tkinter", lambda: tkinter), "Label"), _a_(626979, _n_(626978, "self", lambda: self), "win"), text="Chat:", bg="lightgray")
        _l_(626981)
        _c_(626985, _a_(626984, _a_(626983, _n_(626982, "self", lambda: self), "chat_label"), "config"), font=("Arial", 12))
        _l_(626986)
        _c_(626990, _a_(626989, _a_(626988, _n_(626987, "self", lambda: self), "chat_label"), "pack"), padx=20, pady=5)
        _l_(626991)

        _n_(626992, "self", lambda: self).text_area = _a_(626996, _a_(626995, _a_(626994, _a_(626993, tkinter, "scrolledtext"), "tkinter"), "scrolledtext"), "ScrolledText")
        _l_(626997)
        _c_(627001, _a_(627000, _a_(626999, _n_(626998, "self", lambda: self), "text_area"), "pack"), padx=20, pady=5)
        _l_(627002)
        _c_(627006, _a_(627005, _a_(627004, _n_(627003, "self", lambda: self), "text_area"), "config"), state='disabled')
        _l_(627007)

        _n_(627008, "self", lambda: self).msg_label = _c_(627013, _a_(627010, _n_(627009, "tkinter", lambda: tkinter), "Label"), _a_(627012, _n_(627011, "self", lambda: self), "win"), text="Message:", bg="Lightgray")
        _l_(627014)
        _c_(627018, _a_(627017, _a_(627016, _n_(627015, "self", lambda: self), "msg_label"), "config"), font=("Arial", 12))
        _l_(627019)
        _c_(627023, _a_(627022, _a_(627021, _n_(627020, "self", lambda: self), "msg_label"), "pack"), padx=20, pady=5)
        _l_(627024)

        _n_(627025, "self", lambda: self).input_area = _c_(627030, _a_(627027, _n_(627026, "tkinter", lambda: tkinter), "Text"), _a_(627029, _n_(627028, "self", lambda: self), "win"), height=3)
        _l_(627031)
        _c_(627035, _a_(627034, _a_(627033, _n_(627032, "self", lambda: self), "input_area"), "pack"), padx=20, pady=5)
        _l_(627036)

        _n_(627037, "self", lambda: self).send_button = _c_(627044, _a_(627039, _n_(627038, "tkinter", lambda: tkinter), "Button"), _a_(627041, _n_(627040, "self", lambda: self), "win"), text="Send", command=_a_(627043, _n_(627042, "self", lambda: self), "write"))
        _l_(627045)
        _c_(627049, _a_(627048, _a_(627047, _n_(627046, "self", lambda: self), "send_button"), "config"), font=("Arial", 12))
        _l_(627050)
        _c_(627054, _a_(627053, _a_(627052, _n_(627051, "self", lambda: self), "end_button"), "pack"), padx=20, pady=5)
        _l_(627055)

        _n_(627056, "self", lambda: self).gui_done = True
        _l_(627057)

        _c_(627063, _a_(627060, _a_(627059, _n_(627058, "self", lambda: self), "win"), "protocol"), "WM_DELETE_WINDOW", _a_(627062, _n_(627061, "self", lambda: self), "stop"))
        _l_(627064)

        _c_(627068, _a_(627067, _a_(627066, _n_(627065, "self", lambda: self), "win"), "mainloop"))
        _l_(627069)

    def write(self):
        _l_(627078)

        message =f"{_a_(627072, _n_(627071, 'self', lambda: self), 'nickname')}: {_c_(627076, _a_(627075, _a_(627074, _n_(627073, 'self', lambda: self), 'input_area'), 'get'), '1.0', 'end')}"
        _l_(627077)


    def stop(self):
        _l_(627094)

        _n_(627079, "self", lambda: self).running = False
        _l_(627080)
        _c_(627084, _a_(627083, _a_(627082, _n_(627081, "self", lambda: self), "win"), "destroy"))
        _l_(627085)
        _c_(627089, _a_(627088, _a_(627087, _n_(627086, "self", lambda: self), "server"), "close"))
        _l_(627090)
        aux = 0
        _l_(627093)
        exit(aux)

    def receive(self):
        _l_(627154)

        while _a_(627096, _n_(627095, "self", lambda: self), "running"):
            _l_(627153)

            try:
                _l_(627152)

                message = _c_(627102, _a_(627101, _c_(627100, _a_(627099, _a_(627098, _n_(627097, "self", lambda: self), "sock"), "recv"), 1024), "decode"), 'utf-8')
                _l_(627103)
                if _n_(627104, "message", lambda: message) == 'NICKNAME':
                    _l_(627138)

                    _c_(627112, _a_(627107, _a_(627106, _n_(627105, "self", lambda: self), "server"), "send"), _c_(627111, _a_(627110, _a_(627109, _n_(627108, "self", lambda: self), "nickname"), "encode"), 'utd-8'))
                    _l_(627113)
                else:
                    if _a_(627115, _n_(627114, "self", lambda: self), "gui_done"):
                        _l_(627137)

                        _c_(627119, _a_(627118, _a_(627117, _n_(627116, "self", lambda: self), "text_area"), "config"), state='normal')
                        _l_(627120)
                        _c_(627125, _a_(627123, _a_(627122, _n_(627121, "self", lambda: self), "text_area"), "insert"), 'end', _n_(627124, "message", lambda: message))
                        _l_(627126)
                        _c_(627130, _a_(627129, _a_(627128, _n_(627127, "self", lambda: self), "text_area"), "yview"), 'end')
                        _l_(627131)
                        _c_(627135, _a_(627134, _a_(627133, _n_(627132, "self", lambda: self), "text_area"), "config"), state='disabled')
                        _l_(627136)
            except _n_(627139, "ConnectionAbortedError", lambda: ConnectionAbortedError):
                _l_(627141)

                break
                _l_(627140)
            except:
                _l_(627151)

                _c_(627143, _n_(627142, "print", lambda: print), "Error")
                _l_(627144)
                _c_(627148, _a_(627147, _a_(627146, _n_(627145, "self", lambda: self), "server"), "close"))
                _l_(627149)
                break
                _l_(627150)
Client = _c_(627157, _n_(627156, "client", lambda: client))
_l_(627158)
_c_(627160, _n_(627159, "Client", lambda: Client))
_l_(627161)