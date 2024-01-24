# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36809972/socket-attributeerror-str-object-has-no-attribute-send
#---Import statments---#
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket, os, multiprocessing
    _l_(670193)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(670195)

except ImportError:
    pass

#---global variables---#
setup = ''
_l_(670196)
cleintsocket = ''
_l_(670197)

#---Defs---#
def setup():
    _l_(670211)

    global host, port, user
    _l_(670198)
    host = _c_(670201, _a_(670200, _n_(670199, "setup_host_box", lambda: setup_host_box), "get"))
    _l_(670202)
    port = _c_(670205, _a_(670204, _n_(670203, "setup_port_box", lambda: setup_port_box), "get"))
    _l_(670206)
    user = _c_(670209, _a_(670208, _n_(670207, "setup_user_box", lambda: setup_user_box), "get"))
    _l_(670210)

def connect(self, hostname, connectingport):
    _l_(670231)

    _c_(670218, _a_(670213, _n_(670212, "self", lambda: self), "connect"), (_n_(670214, "hostname", lambda: hostname), _c_(670217, _n_(670215, "int", lambda: int), _n_(670216, "connectingport", lambda: connectingport))))
    _l_(670219)
    _c_(670221, _n_(670220, "print", lambda: print), 'connected')
    _l_(670222)
    _c_(670229, _a_(670228, _c_(670227, _a_(670224, _n_(670223, "multiprocessing", lambda: multiprocessing), "Process"), target = _c_(670226, _n_(670225, "resv", lambda: resv))), "start"))
    _l_(670230)

def create_sock(nhost, nport):
    _l_(670247)

    global cleintsocket
    _l_(670232)
    cleintsocket = _c_(670239, _a_(670234, _n_(670233, "socket", lambda: socket), "socket"), _a_(670236, _n_(670235, "socket", lambda: socket), "AF_INET"), _a_(670238, _n_(670237, "socket", lambda: socket), "SOCK_STREAM"))
    _l_(670240)
    _c_(670245, _n_(670241, "connect", lambda: connect), _n_(670242, "cleintsocket", lambda: cleintsocket), _n_(670243, "nhost", lambda: nhost), _n_(670244, "nport", lambda: nport))
    _l_(670246)

def send(username, cleintsock):
    _l_(670261)

    '''to send a message'''
    _l_(670248)
    usrmsg = _c_(670254, _a_(670253, (_n_(670249, "username", lambda: username) + ' - ' + _c_(670252, _a_(670251, _n_(670250, "chat_msg_box", lambda: chat_msg_box), "get"))), "encode"))
    _l_(670255)
    _c_(670259, _a_(670257, _n_(670256, "cleintsock", lambda: cleintsock), "send"), _n_(670258, "usrmsg", lambda: usrmsg))
    _l_(670260)

def resv(sock):
    _l_(670275)

    '''resive subscript, run through mutiprosses module'''
    _l_(670262)
    while True:
        _l_(670274)

        rmsg = _c_(670267, _a_(670266, _c_(670265, _a_(670264, _n_(670263, "sock", lambda: sock), "recv"), 1024), "decode"))
        _l_(670268)
        _c_(670272, _a_(670270, _n_(670269, "chat_msg_display_text", lambda: chat_msg_display_text), "insert"), 'end.0.', _n_(670271, "rmsg", lambda: rmsg))
        _l_(670273)

def chat():
    _l_(670317)

    '''loads chat page'''
    _l_(670276)
    _c_(670279, _a_(670278, _n_(670277, "setup_host_text", lambda: setup_host_text), "pack_forget"))
    _l_(670280)
    _c_(670283, _a_(670282, _n_(670281, "setup_host_box", lambda: setup_host_box), "pack_forget"))
    _l_(670284)
    _c_(670287, _a_(670286, _n_(670285, "setup_port_text", lambda: setup_port_text), "pack_forget"))
    _l_(670288)
    _c_(670291, _a_(670290, _n_(670289, "setup_port_box", lambda: setup_port_box), "pack_forget"))
    _l_(670292)
    _c_(670295, _a_(670294, _n_(670293, "setup_user_text", lambda: setup_user_text), "pack_forget"))
    _l_(670296)
    _c_(670299, _a_(670298, _n_(670297, "setup_user_box", lambda: setup_user_box), "pack_forget"))
    _l_(670300)
    _c_(670303, _a_(670302, _n_(670301, "setup_confirm_button", lambda: setup_confirm_button), "pack_forget"))
    _l_(670304)
    _c_(670307, _a_(670306, _n_(670305, "chat_msg_desplay_text", lambda: chat_msg_desplay_text), "pack"))
    _l_(670308)
    _c_(670311, _a_(670310, _n_(670309, "chat_msg_box", lambda: chat_msg_box), "pack"))
    _l_(670312)
    _c_(670315, _a_(670314, _n_(670313, "chat_msg_send_button", lambda: chat_msg_send_button), "pack"))
    _l_(670316)

def start():
    _l_(670347)

    '''starts the setup page'''
    _l_(670318)
    _c_(670321, _a_(670320, _n_(670319, "setup_host_text", lambda: setup_host_text), "pack"))
    _l_(670322)
    _c_(670325, _a_(670324, _n_(670323, "setup_host_box", lambda: setup_host_box), "pack"))
    _l_(670326)
    _c_(670329, _a_(670328, _n_(670327, "setup_port_text", lambda: setup_port_text), "pack"))
    _l_(670330)
    _c_(670333, _a_(670332, _n_(670331, "setup_port_box", lambda: setup_port_box), "pack"))
    _l_(670334)
    _c_(670337, _a_(670336, _n_(670335, "setup_user_text", lambda: setup_user_text), "pack"))
    _l_(670338)
    _c_(670341, _a_(670340, _n_(670339, "setup_user_box", lambda: setup_user_box), "pack"))
    _l_(670342)
    _c_(670345, _a_(670344, _n_(670343, "setup_confirm_button", lambda: setup_confirm_button), "pack"))
    _l_(670346)

#---TK Setup---#
#--window setup--#
window = _c_(670350, _a_(670349, _n_(670348, "tk", lambda: tk), "Tk"))
_l_(670351)
_c_(670354, _a_(670353, _n_(670352, "window", lambda: window), "title"), 'Chat')
_l_(670355)
_c_(670358, _a_(670357, _n_(670356, "window", lambda: window), "geometry"), '600x600')
_l_(670359)
_c_(670362, _a_(670361, _n_(670360, "window", lambda: window), "configure"), background='#ffffff')
_l_(670363)
#--connection setup page--#
setup_host_text = _c_(670367, _a_(670365, _n_(670364, "tk", lambda: tk), "Label"), _n_(670366, "window", lambda: window), text = 'Host')
_l_(670368)
setup_host_box = _c_(670372, _a_(670370, _n_(670369, "tk", lambda: tk), "Entry"), _n_(670371, "window", lambda: window), bg = '#ffffff')
_l_(670373)
setup_port_text = _c_(670377, _a_(670375, _n_(670374, "tk", lambda: tk), "Label"), _n_(670376, "window", lambda: window), text = 'Port')
_l_(670378)
setup_port_box = _c_(670382, _a_(670380, _n_(670379, "tk", lambda: tk), "Entry"), _n_(670381, "window", lambda: window), bg = '#ffffff')
_l_(670383)
setup_user_text = _c_(670387, _a_(670385, _n_(670384, "tk", lambda: tk), "Label"), _n_(670386, "window", lambda: window), text = 'Username')
_l_(670388)
setup_user_box = _c_(670392, _a_(670390, _n_(670389, "tk", lambda: tk), "Entry"), _n_(670391, "window", lambda: window), bg = '#ffffff')
_l_(670393)
setup_confirm_button = _c_(670399, _a_(670395, _n_(670394, "tk", lambda: tk), "Button"), _n_(670396, "window", lambda: window),text = 'Connect', command = _c_(670398, _n_(670397, "setup", lambda: setup)))
_l_(670400)
#--chat page--#
chat_msg_box = _c_(670404, _a_(670402, _n_(670401, "tk", lambda: tk), "Entry"), _n_(670403, "window", lambda: window), bg='#ffffff')
_l_(670405)
chat_msg_send_button = _c_(670413, _a_(670407, _n_(670406, "tk", lambda: tk), "Button"), _n_(670408, "window", lambda: window), text = 'send', command = _c_(670412, _n_(670409, "send", lambda: send), _n_(670410, "user", lambda: user), _n_(670411, "cleintsocket", lambda: cleintsocket)))
_l_(670414)
chat_msg_display_text = _c_(670418, _a_(670416, _n_(670415, "tk", lambda: tk), "Text"), _n_(670417, "window", lambda: window), width=600, height=500, wrap = 'word')
_l_(670419)
#--------------#

_c_(670421, _n_(670420, "start", lambda: start))
_l_(670422)