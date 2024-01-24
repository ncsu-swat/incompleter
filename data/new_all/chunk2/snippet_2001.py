# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71173098/filenotfounderror-errno-2-no-such-file-or-directory-discrepancy-between-prog
# Datengenerierung für Logname, Kundennummer, Zeit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
num_dt = _c_(425716, _a_(425715, _n_(425714, "datetime", lambda: datetime), "now"))
_l_(425717)
num_dt_l = _c_(425720, _a_(425719, _n_(425718, "num_dt", lambda: num_dt), "strftime"), "%d_%m_%Y %HH_%MM_%SS")
_l_(425721)
rndnr = _c_(425726, _n_(425722, "str", lambda: str), _c_(425725, _a_(425724, _n_(425723, "random", lambda: random), "randint"), 1, 9999))
_l_(425727)
log_n = r"Logs/" + _c_(425730, _n_(425728, "str", lambda: str), _n_(425729, "num_dt_l", lambda: num_dt_l)) + "__" + _n_(425731, "rndnr", lambda: rndnr) + r".txt"
_l_(425732)


# Print-Funktion
def logp(lv1, lv2):
    _l_(425755)

    with _c_(425737, _n_(425733, "redirect_stdout", lambda: redirect_stdout), _c_(425736, _n_(425734, "open", lambda: open), _n_(425735, "log_n", lambda: log_n), 'a')):
        _l_(425754)

        _c_(425752, _n_(425738, "print", lambda: print), "-----------\n" + _c_(425745, _n_(425739, "str", lambda: str), _c_(425744, _a_(425743, _c_(425742, _a_(425741, _n_(425740, "datetime", lambda: datetime), "now")), "strftime"), "%HH:%MM:%SS")) + " " + _c_(425748, _n_(425746, "str", lambda: str), _n_(425747, "lv1", lambda: lv1)) + " " + _c_(425751, _n_(425749, "str", lambda: str), _n_(425750, "lv2", lambda: lv2)) + ".")
        _l_(425753)


with _c_(425760, _n_(425756, "redirect_stdout", lambda: redirect_stdout), _c_(425759, _n_(425757, "open", lambda: open), _n_(425758, "log_n", lambda: log_n), 'a')):
    _l_(425764)

    _c_(425762, _n_(425761, "print", lambda: print), "****************************\nTest", "started\n****************************")
    _l_(425763)

_c_(425769, _n_(425765, "logp", lambda: logp), "Global Number: " + _c_(425768, _n_(425766, "str", lambda: str), _n_(425767, "rndnr", lambda: rndnr)), "")
_l_(425770)
_c_(425773, _n_(425771, "logp", lambda: logp), "Datum ist:", _n_(425772, "num_dt_l", lambda: num_dt_l))
_l_(425774)