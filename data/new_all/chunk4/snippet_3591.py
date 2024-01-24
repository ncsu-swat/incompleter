# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71631276/attributeerror-module-tkinter-scrolledtext-has-no-attribute-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from operator import truediv
    _l_(590097)

except ImportError:
    pass
try:
    import socket
    _l_(590099)

except ImportError:
    pass
try:
    import threading
    _l_(590101)

except ImportError:
    pass
try:
    import tkinter
    _l_(590103)

except ImportError:
    pass
try:
    import tkinter.scrolledtext
    _l_(590105)

except ImportError:
    pass
try:
    from tkinter import simpledialog
    _l_(590107)

except ImportError:
    pass

class client:
    _l_(590351)


    def __init__(self):
        _l_(590160)

        _n_(590108, "self", lambda: self).server = _c_(590115, _a_(590110, _n_(590109, "socket", lambda: socket), "socket"), _a_(590112, _n_(590111, "socket", lambda: socket), "AF_INET"), _a_(590114, _n_(590113, "socket", lambda: socket), "SOCK_STREAM"))
        _l_(590116)
        _c_(590120, _a_(590119, _a_(590118, _n_(590117, "self", lambda: self), "server"), "connect"), ('localhost', 1234))
        _l_(590121)

        msg = _c_(590124, _a_(590123, _n_(590122, "tkinter", lambda: tkinter), "Tk"))
        _l_(590125)
        _c_(590128, _a_(590127, _n_(590126, "msg", lambda: msg), "withdraw"))
        _l_(590129)

        _n_(590130, "self", lambda: self).nickname = _c_(590134, _a_(590132, _n_(590131, "simpledialog", lambda: simpledialog), "askstring"), "Nickname", "Please choose a nickname", parent=_n_(590133, "msg", lambda: msg))
        _l_(590135)

        _n_(590136, "self", lambda: self).gui_done = False 
        _l_(590137) 
        _n_(590138, "self", lambda: self).running = True
        _l_(590139)

        gui_thread = _c_(590144, _a_(590141, _n_(590140, "threading", lambda: threading), "Thread"), target=_a_(590143, _n_(590142, "self", lambda: self), "gui_loop"))
        _l_(590145)
        receive_thread = _c_(590150, _a_(590147, _n_(590146, "threading", lambda: threading), "Thread"), target=_a_(590149, _n_(590148, "self", lambda: self), "receive"))
        _l_(590151)

        _c_(590154, _a_(590153, _n_(590152, "gui_thread", lambda: gui_thread), "start"))
        _l_(590155)
        _c_(590158, _a_(590157, _n_(590156, "receive_thread", lambda: receive_thread), "start"))
        _l_(590159)

    def gui_loop(self):
        _l_(590266)

        _n_(590161, "self", lambda: self).win = _c_(590164, _a_(590163, _n_(590162, "tkinter", lambda: tkinter), "Tk"))
        _l_(590165)
        _c_(590169, _a_(590168, _a_(590167, _n_(590166, "self", lambda: self), "win"), "configure"), bg="lightgray")
        _l_(590170)
        
        _n_(590171, "self", lambda: self).chat_label = _c_(590176, _a_(590173, _n_(590172, "tkinter", lambda: tkinter), "Label"), _a_(590175, _n_(590174, "self", lambda: self), "win"), text="Chat:", bg="lightgray")
        _l_(590177)
        _c_(590181, _a_(590180, _a_(590179, _n_(590178, "self", lambda: self), "chat_label"), "config"), font=("Arial", 12))
        _l_(590182)
        _c_(590186, _a_(590185, _a_(590184, _n_(590183, "self", lambda: self), "chat_label"), "pack"), padx=20, pady=5)
        _l_(590187)

        _n_(590188, "self", lambda: self).text_area = _a_(590192, _a_(590191, _a_(590190, _a_(590189, tkinter, "scrolledtext"), "tkinter"), "scrolledtext"), "ScrolledText")
        _l_(590193)
        _c_(590197, _a_(590196, _a_(590195, _n_(590194, "self", lambda: self), "text_area"), "pack"), padx=20, pady=5)
        _l_(590198)
        _c_(590202, _a_(590201, _a_(590200, _n_(590199, "self", lambda: self), "text_area"), "config"), state='disabled')
        _l_(590203)

        _n_(590204, "self", lambda: self).msg_label = _c_(590209, _a_(590206, _n_(590205, "tkinter", lambda: tkinter), "Label"), _a_(590208, _n_(590207, "self", lambda: self), "win"), text="Message:", bg="Lightgray")
        _l_(590210)
        _c_(590214, _a_(590213, _a_(590212, _n_(590211, "self", lambda: self), "msg_label"), "config"), font=("Arial", 12))
        _l_(590215)
        _c_(590219, _a_(590218, _a_(590217, _n_(590216, "self", lambda: self), "msg_label"), "pack"), padx=20, pady=5)
        _l_(590220)

        _n_(590221, "self", lambda: self).input_area = _c_(590226, _a_(590223, _n_(590222, "tkinter", lambda: tkinter), "Text"), _a_(590225, _n_(590224, "self", lambda: self), "win"), height=3)
        _l_(590227)
        _c_(590231, _a_(590230, _a_(590229, _n_(590228, "self", lambda: self), "input_area"), "pack"), padx=20, pady=5)
        _l_(590232)

        _n_(590233, "self", lambda: self).send_button = _c_(590240, _a_(590235, _n_(590234, "tkinter", lambda: tkinter), "Button"), _a_(590237, _n_(590236, "self", lambda: self), "win"), text="Send", command=_a_(590239, _n_(590238, "self", lambda: self), "write"))
        _l_(590241)
        _c_(590245, _a_(590244, _a_(590243, _n_(590242, "self", lambda: self), "send_button"), "config"), font=("Arial", 12))
        _l_(590246)
        _c_(590250, _a_(590249, _a_(590248, _n_(590247, "self", lambda: self), "end_button"), "pack"), padx=20, pady=5)
        _l_(590251)

        _n_(590252, "self", lambda: self).gui_done = True
        _l_(590253)

        _c_(590259, _a_(590256, _a_(590255, _n_(590254, "self", lambda: self), "win"), "protocol"), "WM_DELETE_WINDOW", _a_(590258, _n_(590257, "self", lambda: self), "stop"))
        _l_(590260)

        _c_(590264, _a_(590263, _a_(590262, _n_(590261, "self", lambda: self), "win"), "mainloop"))
        _l_(590265)

    def write(self):
        _l_(590274)

        message =f"{_a_(590268, _n_(590267, 'self', lambda: self), 'nickname')}: {_c_(590272, _a_(590271, _a_(590270, _n_(590269, 'self', lambda: self), 'input_area'), 'get'), '1.0', 'end')}"
        _l_(590273)


    def stop(self):
        _l_(590290)

        _n_(590275, "self", lambda: self).running = False
        _l_(590276)
        _c_(590280, _a_(590279, _a_(590278, _n_(590277, "self", lambda: self), "win"), "destroy"))
        _l_(590281)
        _c_(590285, _a_(590284, _a_(590283, _n_(590282, "self", lambda: self), "server"), "close"))
        _l_(590286)
        aux = 0
        _l_(590289)
        exit(aux)

    def receive(self):
        _l_(590350)

        while _a_(590292, _n_(590291, "self", lambda: self), "running"):
            _l_(590349)

            try:
                _l_(590348)

                message = _c_(590298, _a_(590297, _c_(590296, _a_(590295, _a_(590294, _n_(590293, "self", lambda: self), "sock"), "recv"), 1024), "decode"), 'utf-8')
                _l_(590299)
                if _n_(590300, "message", lambda: message) == 'NICKNAME':
                    _l_(590334)

                    _c_(590308, _a_(590303, _a_(590302, _n_(590301, "self", lambda: self), "server"), "send"), _c_(590307, _a_(590306, _a_(590305, _n_(590304, "self", lambda: self), "nickname"), "encode"), 'utd-8'))
                    _l_(590309)
                else:
                    if _a_(590311, _n_(590310, "self", lambda: self), "gui_done"):
                        _l_(590333)

                        _c_(590315, _a_(590314, _a_(590313, _n_(590312, "self", lambda: self), "text_area"), "config"), state='normal')
                        _l_(590316)
                        _c_(590321, _a_(590319, _a_(590318, _n_(590317, "self", lambda: self), "text_area"), "insert"), 'end', _n_(590320, "message", lambda: message))
                        _l_(590322)
                        _c_(590326, _a_(590325, _a_(590324, _n_(590323, "self", lambda: self), "text_area"), "yview"), 'end')
                        _l_(590327)
                        _c_(590331, _a_(590330, _a_(590329, _n_(590328, "self", lambda: self), "text_area"), "config"), state='disabled')
                        _l_(590332)
            except _n_(590335, "ConnectionAbortedError", lambda: ConnectionAbortedError):
                _l_(590337)

                break
                _l_(590336)
            except:
                _l_(590347)

                _c_(590339, _n_(590338, "print", lambda: print), "Error")
                _l_(590340)
                _c_(590344, _a_(590343, _a_(590342, _n_(590341, "self", lambda: self), "server"), "close"))
                _l_(590345)
                break
                _l_(590346)
Client = _c_(590353, _n_(590352, "client", lambda: client))
_l_(590354)
_c_(590356, _n_(590355, "Client", lambda: Client))
_l_(590357)