# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28182582/typeerror-does-not-support-the-buffer-interface-twitch-irc-chat-bot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(387904)

except ImportError:
    pass
try:
    import threading
    _l_(387906)

except ImportError:
    pass

bot_owner = 'BetterFollowerBot'
_l_(387907)
nick = 'BetterFollowerBot'
_l_(387908)
channel = '#BetterFollowerBot'
_l_(387909)
server = 'irc.twitch.tv'
_l_(387910)
password = '~Took This Out~'
_l_(387911)

queue = 0 #sets variable for anti-spam queue functionality
_l_(387912) #sets variable for anti-spam queue functionality

irc = _c_(387915, _a_(387914, _n_(387913, "socket", lambda: socket), "socket"))
_l_(387916)
_c_(387920, _a_(387918, _n_(387917, "irc", lambda: irc), "connect"), (_n_(387919, "server", lambda: server), 6667)) #connects to the server
_l_(387921) #connects to the server

#sends variables for connection to twitch chat
_c_(387925, _a_(387923, _n_(387922, "irc", lambda: irc), "send"), 'PASS ' + _n_(387924, "password", lambda: password) + '\r\n')
_l_(387926)
_c_(387931, _a_(387928, _n_(387927, "irc", lambda: irc), "send"), 'USER ' + _n_(387929, "nick", lambda: nick) + ' 0 * :' + _n_(387930, "bot_owner", lambda: bot_owner) + '\r\n')
_l_(387932)
_c_(387936, _a_(387934, _n_(387933, "irc", lambda: irc), "send"), 'NICK ' + _n_(387935, "nick", lambda: nick) + '\r\n')
_l_(387937)
_c_(387941, _a_(387939, _n_(387938, "irc", lambda: irc), "send"), 'JOIN ' + _n_(387940, "channel", lambda: channel) + '\r\n') 
_l_(387942) 

def message(msg):
    _l_(387961)

    global queue
    _l_(387943)
    queue = _n_(387944, "queue", lambda: queue) + 1
    _l_(387945)
    _c_(387948, _n_(387946, "print", lambda: print), _n_(387947, "queue", lambda: queue))
    _l_(387949)
    if _n_(387950, "queue", lambda: queue) < 20:
        _l_(387960)

        _c_(387955, _a_(387952, _n_(387951, "irc", lambda: irc), "send"), 'PRIVMSG ' + _n_(387953, "channel", lambda: channel) + ' :' + _n_(387954, "msg", lambda: msg) + '\r\n')
        _l_(387956)
    else:
        _c_(387958, _n_(387957, "print", lambda: print), 'Message deleted')
        _l_(387959)

def queuetimer():
    _l_(387974)

    global queue
    _l_(387962)
    _c_(387964, _n_(387963, "print", lambda: print), 'queue reset')
    _l_(387965)
    queue = 0
    _l_(387966)
    _c_(387972, _a_(387971, _c_(387970, _a_(387968, _n_(387967, "threading", lambda: threading), "Timer"), 30,_n_(387969, "queuetimer", lambda: queuetimer)), "start"))
    _l_(387973)
_c_(387976, _n_(387975, "queuetimer", lambda: queuetimer))
_l_(387977)

while True:
    _l_(388012)

    data = _c_(387980, _a_(387979, _n_(387978, "irc", lambda: irc), "recv"), 1204) #gets output from IRC server
    _l_(387981) #gets output from IRC server
    user = _c_(387984, _a_(387983, _n_(387982, "data", lambda: data), "split"), ':')[1]
    _l_(387985)
    user = _c_(387988, _a_(387987, _n_(387986, "user", lambda: user), "split"), '!')[0] #determines the sender of the messages
    _l_(387989) #determines the sender of the messages
    _c_(387992, _n_(387990, "print", lambda: print), _n_(387991, "data", lambda: data))
    _l_(387993)

    if _c_(387996, _a_(387995, _n_(387994, "data", lambda: data), "find"), 'PING') != -1:
        _l_(388004)

        _c_(388002, _a_(387998, _n_(387997, "irc", lambda: irc), "send"), _c_(388001, _a_(388000, _n_(387999, "data", lambda: data), "replace"), 'PING', 'PONG')) #responds to PINGS from the server
        _l_(388003) #responds to PINGS from the server
    if _c_(388007, _a_(388006, _n_(388005, "data", lambda: data), "find"), '!test') != -1:
        _l_(388011)

        _c_(388009, _n_(388008, "message", lambda: message), 'Hi')
        _l_(388010)