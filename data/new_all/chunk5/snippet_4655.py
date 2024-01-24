# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53336322/python-buf-findidentified-0-typeerror-a-bytes-like-object-is-requ
#!/usr/bin/env python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
'''
Created on Apr 4, 2012

@author: lanquarden
'''
_l_(659704)
try:
    import sys
    _l_(659706)

except ImportError:
    pass
try:
    import argparse
    _l_(659708)

except ImportError:
    pass
try:
    import socket
    _l_(659710)

except ImportError:
    pass
try:
    import driver
    _l_(659712)

except ImportError:
    pass

if _n_(659713, "__name__", lambda: __name__) == '__main__':
    _l_(659715)

    pass
    _l_(659714)

# Configure the argument parser
parser = _c_(659718, _a_(659717, _n_(659716, "argparse", lambda: argparse), "ArgumentParser"), description = 'Python client to connect to the TORCS SCRC server.')
_l_(659719)

_c_(659722, _a_(659721, _n_(659720, "parser", lambda: parser), "add_argument"), '--host', action='store', dest='host_ip', default='localhost',
                    help='Host IP address (default: localhost)')
_l_(659723)
_c_(659727, _a_(659725, _n_(659724, "parser", lambda: parser), "add_argument"), '--port', action='store', type=_n_(659726, "int", lambda: int), dest='host_port', default=3001,
                    help='Host port number (default: 3001)')
_l_(659728)
_c_(659731, _a_(659730, _n_(659729, "parser", lambda: parser), "add_argument"), '--id', action='store', dest='id', default='SCR',
                    help='Bot ID (default: SCR)')
_l_(659732)
_c_(659736, _a_(659734, _n_(659733, "parser", lambda: parser), "add_argument"), '--maxEpisodes', action='store', dest='max_episodes', type=_n_(659735, "int", lambda: int), default=1,
                    help='Maximum number of learning episodes (default: 1)')
_l_(659737)
_c_(659741, _a_(659739, _n_(659738, "parser", lambda: parser), "add_argument"), '--maxSteps', action='store', dest='max_steps', type=_n_(659740, "int", lambda: int), default=0,
                    help='Maximum number of steps (default: 0)')
_l_(659742)
_c_(659745, _a_(659744, _n_(659743, "parser", lambda: parser), "add_argument"), '--track', action='store', dest='track', default=None,
                    help='Name of the track')
_l_(659746)
_c_(659750, _a_(659748, _n_(659747, "parser", lambda: parser), "add_argument"), '--stage', action='store', dest='stage', type=_n_(659749, "int", lambda: int), default=3,
                    help='Stage (0 - Warm-Up, 1 - Qualifying, 2 - Race, 3 - Unknown)')
_l_(659751)

arguments = _c_(659754, _a_(659753, _n_(659752, "parser", lambda: parser), "parse_args"))
_l_(659755)

# Print summary
_c_(659761, _n_(659756, "print", lambda: print), 'Connecting to server host ip:', _a_(659758, _n_(659757, "arguments", lambda: arguments), "host_ip"), '@ port:', _a_(659760, _n_(659759, "arguments", lambda: arguments), "host_port"))
_l_(659762)
_c_(659766, _n_(659763, "print", lambda: print), 'Bot ID:', _a_(659765, _n_(659764, "arguments", lambda: arguments), "id"))
_l_(659767)
_c_(659771, _n_(659768, "print", lambda: print), 'Maximum episodes:', _a_(659770, _n_(659769, "arguments", lambda: arguments), "max_episodes"))
_l_(659772)
_c_(659776, _n_(659773, "print", lambda: print), 'Maximum steps:', _a_(659775, _n_(659774, "arguments", lambda: arguments), "max_steps"))
_l_(659777)
_c_(659781, _n_(659778, "print", lambda: print), 'Track:', _a_(659780, _n_(659779, "arguments", lambda: arguments), "track"))
_l_(659782)
_c_(659786, _n_(659783, "print", lambda: print), 'Stage:', _a_(659785, _n_(659784, "arguments", lambda: arguments), "stage"))
_l_(659787)
_c_(659789, _n_(659788, "print", lambda: print), '*********************************************')
_l_(659790)

try:
    _l_(659809)

    sock = _c_(659797, _a_(659792, _n_(659791, "socket", lambda: socket), "socket"), _a_(659794, _n_(659793, "socket", lambda: socket), "AF_INET"), _a_(659796, _n_(659795, "socket", lambda: socket), "SOCK_DGRAM"))
    _l_(659798)
except _a_(659800, _n_(659799, "socket", lambda: socket), "error") as msg:
    _l_(659808)

    _c_(659802, _n_(659801, "print", lambda: print), 'Could not make a socket.')
    _l_(659803)
    _c_(659806, _a_(659805, _n_(659804, "sys", lambda: sys), "exit"), -1)
    _l_(659807)

# one second timeout
_c_(659812, _a_(659811, _n_(659810, "sock", lambda: sock), "settimeout"), 1.0)
_l_(659813)

shutdownClient = False
_l_(659814)
curEpisode = 0
_l_(659815)

verbose = False
_l_(659816)

d = _c_(659821, _a_(659818, _n_(659817, "driver", lambda: driver), "Driver"), _a_(659820, _n_(659819, "arguments", lambda: arguments), "stage"))
_l_(659822)

while not _n_(659823, "shutdownClient", lambda: shutdownClient):
    _l_(659978)

    while True:
        _l_(659881)

        _c_(659827, _n_(659824, "print", lambda: print), 'Sending id to server: ', _a_(659826, _n_(659825, "arguments", lambda: arguments), "id"))
        _l_(659828)
        buf = _a_(659830, _n_(659829, "arguments", lambda: arguments), "id") + _c_(659833, _a_(659832, _n_(659831, "d", lambda: d), "init"))
        _l_(659834)
        _c_(659837, _n_(659835, "print", lambda: print), 'Sending init string to server:', _n_(659836, "buf", lambda: buf))
        _l_(659838)

        try:
            _l_(659860)

            _c_(659848, _a_(659840, _n_(659839, "sock", lambda: sock), "sendto"), _c_(659843, _a_(659842, _n_(659841, "buf", lambda: buf), "encode")), (_a_(659845, _n_(659844, "arguments", lambda: arguments), "host_ip"), _a_(659847, _n_(659846, "arguments", lambda: arguments), "host_port")))
            _l_(659849)
        except _a_(659851, _n_(659850, "socket", lambda: socket), "error") as msg:
            _l_(659859)

            _c_(659853, _n_(659852, "print", lambda: print), 'Failed to send data...Exiting...')
            _l_(659854)
            _c_(659857, _a_(659856, _n_(659855, "sys", lambda: sys), "exit"), -1)
            _l_(659858)

        try:
            _l_(659871)

            buf, addr = _c_(659863, _a_(659862, _n_(659861, "sock", lambda: sock), "recvfrom"), 1000)
            _l_(659864)
        except _a_(659866, _n_(659865, "socket", lambda: socket), "error") as msg:
            _l_(659870)

            _c_(659868, _n_(659867, "print", lambda: print), 'didn\'t get response from server...')
            _l_(659869)

        if _c_(659874, _a_(659873, _n_(659872, "buf", lambda: buf), "find"), '***identified***') >= 0:
            _l_(659880)

            _c_(659877, _n_(659875, "print", lambda: print), 'Received: ', _n_(659876, "buf", lambda: buf))
            _l_(659878)
            break
            _l_(659879)

    currentStep = 0
    _l_(659882)

    while True:
        _l_(659971)

        # wait for an answer from server
        buf = None
        _l_(659883)
        try:
            _l_(659894)

            buf, addr = _c_(659886, _a_(659885, _n_(659884, "sock", lambda: sock), "recvfrom"), 1000)
            _l_(659887)
        except _a_(659889, _n_(659888, "socket", lambda: socket), "error") as msg:
            _l_(659893)

            _c_(659891, _n_(659890, "print", lambda: print), 'didn\'t get response from server...')
            _l_(659892)

        if _n_(659895, "verbose", lambda: verbose):
            _l_(659900)

            _c_(659898, _n_(659896, "print", lambda: print), 'Received: ', _n_(659897, "buf", lambda: buf))
            _l_(659899)

        if _n_(659901, "buf", lambda: buf) != None and _c_(659904, _a_(659903, _n_(659902, "buf", lambda: buf), "find"), '***shutdown***') >= 0:
            _l_(659914)

            _c_(659907, _a_(659906, _n_(659905, "d", lambda: d), "onShutDown"))
            _l_(659908)
            shutdownClient = True
            _l_(659909)
            _c_(659911, _n_(659910, "print", lambda: print), 'Client Shutdown')
            _l_(659912)
            break
            _l_(659913)

        if _n_(659915, "buf", lambda: buf) != None and _c_(659918, _a_(659917, _n_(659916, "buf", lambda: buf), "find"), '***restart***') >= 0:
            _l_(659927)

            _c_(659921, _a_(659920, _n_(659919, "d", lambda: d), "onRestart"))
            _l_(659922)
            _c_(659924, _n_(659923, "print", lambda: print), 'Client Restart')
            _l_(659925)
            break
            _l_(659926)

        currentStep += 1
        _l_(659928)
        if _n_(659929, "currentStep", lambda: currentStep) != _a_(659931, _n_(659930, "arguments", lambda: arguments), "max_steps"):
            _l_(659940)

            if _n_(659932, "buf", lambda: buf) != None:
                _l_(659938)

                buf = _c_(659936, _a_(659934, _n_(659933, "d", lambda: d), "drive"), _n_(659935, "buf", lambda: buf))
                _l_(659937)
        else:
            buf = '(meta 1)'
            _l_(659939)

        if _n_(659941, "verbose", lambda: verbose):
            _l_(659946)

            _c_(659944, _n_(659942, "print", lambda: print), 'Sending: ', _n_(659943, "buf", lambda: buf))
            _l_(659945)

        if _n_(659947, "buf", lambda: buf) != None:
            _l_(659970)

            try:
                _l_(659969)

                _c_(659957, _a_(659949, _n_(659948, "sock", lambda: sock), "sendto"), _c_(659952, _a_(659951, _n_(659950, "buf", lambda: buf), "encode")), (_a_(659954, _n_(659953, "arguments", lambda: arguments), "host_ip"), _a_(659956, _n_(659955, "arguments", lambda: arguments), "host_port")))
                _l_(659958)
            except _a_(659960, _n_(659959, "socket", lambda: socket), "error") as msg:
                _l_(659968)

                _c_(659962, _n_(659961, "print", lambda: print), 'Failed to send data...Exiting...')
                _l_(659963)
                _c_(659966, _a_(659965, _n_(659964, "sys", lambda: sys), "exit"), -1)
                _l_(659967)

    curEpisode += 1
    _l_(659972)

    if _n_(659973, "curEpisode", lambda: curEpisode) == _a_(659975, _n_(659974, "arguments", lambda: arguments), "max_episodes"):
        _l_(659977)

        shutdownClient = True
        _l_(659976)


_c_(659981, _a_(659980, _n_(659979, "sock", lambda: sock), "close"))
_l_(659982)