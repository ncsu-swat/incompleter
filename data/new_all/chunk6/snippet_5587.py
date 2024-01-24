# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71635051/typeerror-init-missing-3-required-positional-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from operator import truediv
    _l_(368672)

except ImportError:
    pass
try:
    import socket
    _l_(368674)

except ImportError:
    pass
try:
    import threading
    _l_(368676)

except ImportError:
    pass
try:
    import tkinter
    _l_(368678)

except ImportError:
    pass
try:
    import tkinter.scrolledtext
    _l_(368680)

except ImportError:
    pass
try:
    from tkinter import simpledialog
    _l_(368682)

except ImportError:
    pass


class Client:
    _l_(368937)


    def __init__(self, msg, gui_thread, receive_thread):
        _l_(368735)

        _n_(368683, "self", lambda: self).sock = _c_(368690, _a_(368685, _n_(368684, "socket", lambda: socket), "socket"), _a_(368687, _n_(368686, "socket", lambda: socket), "AF_INET"), _a_(368689, _n_(368688, "socket", lambda: socket), "SOCK_STREAM"))
        _l_(368691)
        _c_(368695, _a_(368694, _a_(368693, _n_(368692, "self", lambda: self), "sock"), "connect"), ('localhost', 1234))
        _l_(368696)

        msg = _c_(368699, _a_(368698, _n_(368697, "tkinter", lambda: tkinter), "Tk"))
        _l_(368700)
        _c_(368703, _a_(368702, _n_(368701, "msg", lambda: msg), "withdraw"))
        _l_(368704)

        _n_(368705, "self", lambda: self).nickname = _c_(368709, _a_(368707, _n_(368706, "simpledialog", lambda: simpledialog), "askstring"), "Nickname", "Please choose a nickname", parent=_n_(368708, "msg", lambda: msg))
        _l_(368710)

        _n_(368711, "self", lambda: self).gui_done = False 
        _l_(368712) 
        _n_(368713, "self", lambda: self).running = True
        _l_(368714)

        gui_thread = _c_(368719, _a_(368716, _n_(368715, "threading", lambda: threading), "Thread"), target=_a_(368718, _n_(368717, "self", lambda: self), "gui_loop"))
        _l_(368720)
        receive_thread = _c_(368725, _a_(368722, _n_(368721, "threading", lambda: threading), "Thread"), target=_a_(368724, _n_(368723, "self", lambda: self), "receive"))
        _l_(368726)

        _c_(368729, _a_(368728, _n_(368727, "gui_thread", lambda: gui_thread), "start"))
        _l_(368730)
        _c_(368733, _a_(368732, _n_(368731, "receive_thread", lambda: receive_thread), "start"))
        _l_(368734)

    def gui_loop(self):
        _l_(368839)

        _n_(368736, "self", lambda: self).win = _c_(368739, _a_(368738, _n_(368737, "tkinter", lambda: tkinter), "Tk"))
        _l_(368740)
        _c_(368744, _a_(368743, _a_(368742, _n_(368741, "self", lambda: self), "win"), "configure"), bg="lightgray")
        _l_(368745)
        
        _n_(368746, "self", lambda: self).chat_label = _c_(368751, _a_(368748, _n_(368747, "tkinter", lambda: tkinter), "Label"), _a_(368750, _n_(368749, "self", lambda: self), "win"), text="Chat:", bg="lightgray")
        _l_(368752)
        _c_(368756, _a_(368755, _a_(368754, _n_(368753, "self", lambda: self), "chat_label"), "config"), font=("Arial", 12))
        _l_(368757)
        _c_(368761, _a_(368760, _a_(368759, _n_(368758, "self", lambda: self), "chat_label"), "pack"), padx=20, pady=5)
        _l_(368762)

        _n_(368763, "self", lambda: self).text_area = _a_(368765, _a_(368764, tkinter, "scrolledtext"), "ScrolledText")
        _l_(368766)
        _c_(368770, _a_(368769, _a_(368768, _n_(368767, "self", lambda: self), "text_area"), "pack"), padx=20, pady=5)
        _l_(368771)
        _c_(368775, _a_(368774, _a_(368773, _n_(368772, "self", lambda: self), "text_area"), "config"), state='disabled')
        _l_(368776)

        _n_(368777, "self", lambda: self).msg_label = _c_(368782, _a_(368779, _n_(368778, "tkinter", lambda: tkinter), "Label"), _a_(368781, _n_(368780, "self", lambda: self), "win"), text="Message:", bg="Lightgray")
        _l_(368783)
        _c_(368787, _a_(368786, _a_(368785, _n_(368784, "self", lambda: self), "msg_label"), "config"), font=("Arial", 12))
        _l_(368788)
        _c_(368792, _a_(368791, _a_(368790, _n_(368789, "self", lambda: self), "msg_label"), "pack"), padx=20, pady=5)
        _l_(368793)

        _n_(368794, "self", lambda: self).input_area = _c_(368799, _a_(368796, _n_(368795, "tkinter", lambda: tkinter), "Text"), _a_(368798, _n_(368797, "self", lambda: self), "win"), height=3)
        _l_(368800)
        _c_(368804, _a_(368803, _a_(368802, _n_(368801, "self", lambda: self), "input_area"), "pack"), padx=20, pady=5)
        _l_(368805)

        _n_(368806, "self", lambda: self).send_button = _c_(368813, _a_(368808, _n_(368807, "tkinter", lambda: tkinter), "Button"), _a_(368810, _n_(368809, "self", lambda: self), "win"), text="Send", command=_a_(368812, _n_(368811, "self", lambda: self), "write"))
        _l_(368814)
        _c_(368818, _a_(368817, _a_(368816, _n_(368815, "self", lambda: self), "send_button"), "config"), font=("Arial", 12))
        _l_(368819)
        _c_(368823, _a_(368822, _a_(368821, _n_(368820, "self", lambda: self), "end_button"), "pack"), padx=20, pady=5)
        _l_(368824)

        _n_(368825, "self", lambda: self).gui_done = True
        _l_(368826)

        _c_(368832, _a_(368829, _a_(368828, _n_(368827, "self", lambda: self), "win"), "protocol"), "WM_DELETE_WINDOW", _a_(368831, _n_(368830, "self", lambda: self), "stop"))
        _l_(368833)

        _c_(368837, _a_(368836, _a_(368835, _n_(368834, "self", lambda: self), "win"), "mainloop"))
        _l_(368838)

    def write(self):
        _l_(368860)

        message =f"{_a_(368841, _n_(368840, 'self', lambda: self), 'nickname')}: {_c_(368845, _a_(368844, _a_(368843, _n_(368842, 'self', lambda: self), 'input_area'), 'get'), '1.0', 'end')}"
        _l_(368846)
        _c_(368853, _a_(368849, _a_(368848, _n_(368847, "self", lambda: self), "sock"), "send"), _c_(368852, _a_(368851, _n_(368850, "message", lambda: message), "encode"), 'utf-8'))
        _l_(368854)
        _c_(368858, _a_(368857, _a_(368856, _n_(368855, "self", lambda: self), "input_area"), "delete"), '1.0', 'end')
        _l_(368859)


    def stop(self):
        _l_(368876)

        _n_(368861, "self", lambda: self).running = False
        _l_(368862)
        _c_(368866, _a_(368865, _a_(368864, _n_(368863, "self", lambda: self), "win"), "destroy"))
        _l_(368867)
        _c_(368871, _a_(368870, _a_(368869, _n_(368868, "self", lambda: self), "sock"), "close"))
        _l_(368872)
        aux = 0
        _l_(368875)
        exit(aux)

    def receive(self):
        _l_(368936)

        while _a_(368878, _n_(368877, "self", lambda: self), "running"):
            _l_(368935)

            try:
                _l_(368934)

                message = _c_(368884, _a_(368883, _c_(368882, _a_(368881, _a_(368880, _n_(368879, "self", lambda: self), "sock"), "recv"), 1024), "decode"), 'utf-8')
                _l_(368885)
                if _n_(368886, "message", lambda: message) == 'NICK':
                    _l_(368920)

                    _c_(368894, _a_(368889, _a_(368888, _n_(368887, "self", lambda: self), "server"), "send"), _c_(368893, _a_(368892, _a_(368891, _n_(368890, "self", lambda: self), "nickname"), "encode"), 'utf-8'))
                    _l_(368895)
                else:
                    if _a_(368897, _n_(368896, "self", lambda: self), "gui_done"):
                        _l_(368919)

                        _c_(368901, _a_(368900, _a_(368899, _n_(368898, "self", lambda: self), "text_area"), "config"), state='normal')
                        _l_(368902)
                        _c_(368907, _a_(368905, _a_(368904, _n_(368903, "self", lambda: self), "text_area"), "insert"), 'end', _n_(368906, "message", lambda: message))
                        _l_(368908)
                        _c_(368912, _a_(368911, _a_(368910, _n_(368909, "self", lambda: self), "text_area"), "yview"), 'end')
                        _l_(368913)
                        _c_(368917, _a_(368916, _a_(368915, _n_(368914, "self", lambda: self), "text_area"), "config"), state='disabled')
                        _l_(368918)
            except _n_(368921, "ConnectionAbortedError", lambda: ConnectionAbortedError):
                _l_(368923)

                break
                _l_(368922)
            except:
                _l_(368933)

                _c_(368925, _n_(368924, "print", lambda: print), "Error")
                _l_(368926)
                _c_(368930, _a_(368929, _a_(368928, _n_(368927, "self", lambda: self), "sock"), "close"))
                _l_(368931)
                break
                _l_(368932)

_c_(368939, _n_(368938, "Client", lambda: Client))
_l_(368940)