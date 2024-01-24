# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71629374/typeerror-init-missing-1-required-positional-argument-server
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from operator import truediv
    _l_(561174)

except ImportError:
    pass
try:
    import socket
    _l_(561176)

except ImportError:
    pass
try:
    import threading
    _l_(561178)

except ImportError:
    pass
try:
    import tkinter
    _l_(561180)

except ImportError:
    pass
try:
    import tkinter.scrolledtext
    _l_(561182)

except ImportError:
    pass
try:
    from tkinter import simpledialog
    _l_(561184)

except ImportError:
    pass

class Client:
    _l_(561427)


    def __init__(self, server):
        _l_(561236)

        server = _c_(561191, _a_(561186, _n_(561185, "socket", lambda: socket), "socket"), _a_(561188, _n_(561187, "socket", lambda: socket), "AF_INET"), _a_(561190, _n_(561189, "socket", lambda: socket), "SOCK_STREAM"))
        _l_(561192)
        _c_(561196, _a_(561195, _a_(561194, _n_(561193, "self", lambda: self), "server"), "connect"), ('localhost', 1234))
        _l_(561197)

        msg = _c_(561200, _a_(561199, _n_(561198, "tkinter", lambda: tkinter), "Tk"))
        _l_(561201)
        _c_(561204, _a_(561203, _n_(561202, "msg", lambda: msg), "withdraw"))
        _l_(561205)

        _n_(561206, "self", lambda: self).nickname = _c_(561210, _a_(561208, _n_(561207, "simpledialog", lambda: simpledialog), "askstring"), "Nickname", "Please choose a nickname", parent=_n_(561209, "msg", lambda: msg))
        _l_(561211)

        _n_(561212, "self", lambda: self).gui_done = False 
        _l_(561213) 
        _n_(561214, "self", lambda: self).running = True
        _l_(561215)

        gui_thread = _c_(561220, _a_(561217, _n_(561216, "threading", lambda: threading), "Thread"), targer=_a_(561219, _n_(561218, "self", lambda: self), "gui_loop"))
        _l_(561221)
        receive_thread = _c_(561226, _a_(561223, _n_(561222, "threading", lambda: threading), "Thread"), targer=_a_(561225, _n_(561224, "self", lambda: self), "receive"))
        _l_(561227)

        _c_(561230, _a_(561229, _n_(561228, "gui_thread", lambda: gui_thread), "start"))
        _l_(561231)
        _c_(561234, _a_(561233, _n_(561232, "receive_thread", lambda: receive_thread), "start"))
        _l_(561235)

    def gui_loop(self):
        _l_(561342)

        _n_(561237, "self", lambda: self).win = _c_(561240, _a_(561239, _n_(561238, "tkinter", lambda: tkinter), "Tk"))
        _l_(561241)
        _c_(561245, _a_(561244, _a_(561243, _n_(561242, "self", lambda: self), "win"), "configure"), bg="lightgray")
        _l_(561246)
        
        _n_(561247, "self", lambda: self).chat_label = _c_(561252, _a_(561249, _n_(561248, "tkinter", lambda: tkinter), "Label"), _a_(561251, _n_(561250, "self", lambda: self), "win"), text="Chat:", bg="lightgray")
        _l_(561253)
        _c_(561257, _a_(561256, _a_(561255, _n_(561254, "self", lambda: self), "chat_label"), "config"), font=("Arial", 12))
        _l_(561258)
        _c_(561262, _a_(561261, _a_(561260, _n_(561259, "self", lambda: self), "chat_label"), "pack"), padx=20, pady=5)
        _l_(561263)

        _n_(561264, "self", lambda: self).text_area = _a_(561268, _a_(561267, _a_(561266, _a_(561265, tkinter, "scrolledtext"), "tkinter"), "scrolledtext"), "ScrolledText")
        _l_(561269)
        _c_(561273, _a_(561272, _a_(561271, _n_(561270, "self", lambda: self), "text_area"), "pack"), padx=20, pady=5)
        _l_(561274)
        _c_(561278, _a_(561277, _a_(561276, _n_(561275, "self", lambda: self), "text_area"), "config"), state='disabled')
        _l_(561279)

        _n_(561280, "self", lambda: self).msg_label = _c_(561285, _a_(561282, _n_(561281, "tkinter", lambda: tkinter), "Label"), _a_(561284, _n_(561283, "self", lambda: self), "win"), text="Message:", bg="Lightgray")
        _l_(561286)
        _c_(561290, _a_(561289, _a_(561288, _n_(561287, "self", lambda: self), "msg_label"), "config"), font=("Arial", 12))
        _l_(561291)
        _c_(561295, _a_(561294, _a_(561293, _n_(561292, "self", lambda: self), "msg_label"), "pack"), padx=20, pady=5)
        _l_(561296)

        _n_(561297, "self", lambda: self).input_area = _c_(561302, _a_(561299, _n_(561298, "tkinter", lambda: tkinter), "Text"), _a_(561301, _n_(561300, "self", lambda: self), "win"), height=3)
        _l_(561303)
        _c_(561307, _a_(561306, _a_(561305, _n_(561304, "self", lambda: self), "input_area"), "pack"), padx=20, pady=5)
        _l_(561308)

        _n_(561309, "self", lambda: self).send_button = _c_(561316, _a_(561311, _n_(561310, "tkinter", lambda: tkinter), "Button"), _a_(561313, _n_(561312, "self", lambda: self), "win"), text="Send", command=_a_(561315, _n_(561314, "self", lambda: self), "write"))
        _l_(561317)
        _c_(561321, _a_(561320, _a_(561319, _n_(561318, "self", lambda: self), "send_button"), "config"), font=("Arial", 12))
        _l_(561322)
        _c_(561326, _a_(561325, _a_(561324, _n_(561323, "self", lambda: self), "end_button"), "pack"), padx=20, pady=5)
        _l_(561327)

        _n_(561328, "self", lambda: self).gui_done = True
        _l_(561329)

        _c_(561335, _a_(561332, _a_(561331, _n_(561330, "self", lambda: self), "win"), "protocol"), "WM_DELETE_WINDOW", _a_(561334, _n_(561333, "self", lambda: self), "stop"))
        _l_(561336)

        _c_(561340, _a_(561339, _a_(561338, _n_(561337, "self", lambda: self), "win"), "mainloop"))
        _l_(561341)

    def write(self):
        _l_(561350)

        message =f"{_a_(561344, _n_(561343, 'self', lambda: self), 'nickname')}: {_c_(561348, _a_(561347, _a_(561346, _n_(561345, 'self', lambda: self), 'input_area'), 'get'), '1.0', 'end')}"
        _l_(561349)


    def stop(self):
        _l_(561366)

        _n_(561351, "self", lambda: self).running = False
        _l_(561352)
        _c_(561356, _a_(561355, _a_(561354, _n_(561353, "self", lambda: self), "win"), "destroy"))
        _l_(561357)
        _c_(561361, _a_(561360, _a_(561359, _n_(561358, "self", lambda: self), "server"), "close"))
        _l_(561362)
        aux = 0
        _l_(561365)
        exit(aux)

    def receive(self):
        _l_(561426)

        while _a_(561368, _n_(561367, "self", lambda: self), "running"):
            _l_(561425)

            try:
                _l_(561424)

                message = _c_(561374, _a_(561373, _c_(561372, _a_(561371, _a_(561370, _n_(561369, "self", lambda: self), "sock"), "recv"), 1024), "decode"), 'utf-8')
                _l_(561375)
                if _n_(561376, "message", lambda: message) == 'NICKNAME':
                    _l_(561410)

                    _c_(561384, _a_(561379, _a_(561378, _n_(561377, "self", lambda: self), "server"), "send"), _c_(561383, _a_(561382, _a_(561381, _n_(561380, "self", lambda: self), "nickname"), "encode"), 'utd-8'))
                    _l_(561385)
                else:
                    if _a_(561387, _n_(561386, "self", lambda: self), "gui_done"):
                        _l_(561409)

                        _c_(561391, _a_(561390, _a_(561389, _n_(561388, "self", lambda: self), "text_area"), "config"), state='normal')
                        _l_(561392)
                        _c_(561397, _a_(561395, _a_(561394, _n_(561393, "self", lambda: self), "text_area"), "insert"), 'end', _n_(561396, "message", lambda: message))
                        _l_(561398)
                        _c_(561402, _a_(561401, _a_(561400, _n_(561399, "self", lambda: self), "text_area"), "yview"), 'end')
                        _l_(561403)
                        _c_(561407, _a_(561406, _a_(561405, _n_(561404, "self", lambda: self), "text_area"), "config"), state='disabled')
                        _l_(561408)
            except _n_(561411, "ConnectionAbortedError", lambda: ConnectionAbortedError):
                _l_(561413)

                break
                _l_(561412)
            except:
                _l_(561423)

                _c_(561415, _n_(561414, "print", lambda: print), "Error")
                _l_(561416)
                _c_(561420, _a_(561419, _a_(561418, _n_(561417, "self", lambda: self), "server"), "close"))
                _l_(561421)
                break
                _l_(561422)
client = _c_(561429, _n_(561428, "Client", lambda: Client))
_l_(561430)