# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53549356/trying-to-write-file-to-my-working-directory-error-typeerror-expected-str-by
# Read both text files and join them together
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _c_(525789, _a_(525788, _a_(525787, _n_(525786, "os", lambda: os), "path"), "exists"), 'list1.txt'):
    _l_(525803)

    with _c_(525791, _n_(525790, "open", lambda: open), 'list1.txt') as f:
        _l_(525802)

        list1 = _c_(525796, _a_(525795, _c_(525794, _a_(525793, _n_(525792, "f", lambda: f), "read")), "splitlines"))
        _l_(525797)
        _c_(525800, _a_(525799, _n_(525798, "f", lambda: f), "close"))
        _l_(525801)

if _c_(525807, _a_(525806, _a_(525805, _n_(525804, "os", lambda: os), "path"), "exists"), 'list2.txt'):
    _l_(525821)

    with _c_(525809, _n_(525808, "open", lambda: open), 'list2.txt') as f:
        _l_(525820)

        list2 = _c_(525814, _a_(525813, _c_(525812, _a_(525811, _n_(525810, "f", lambda: f), "read")), "splitlines"))
        _l_(525815)
        _c_(525818, _a_(525817, _n_(525816, "f", lambda: f), "close"))
        _l_(525819)

# Combine these into a MASTERLIST
MASTERLIST = _n_(525822, "list1", lambda: list1) + _n_(525823, "list2", lambda: list2)
_l_(525824)

# Remove duplicates
MASTERLIST = _c_(525829, _n_(525825, "list", lambda: list), _c_(525828, _n_(525826, "set", lambda: set), _n_(525827, "MASTERLIST", lambda: MASTERLIST)))
_l_(525830)
_c_(525832, _n_(525831, "print", lambda: print), '\n\n[+] MASTERLIST created!\n')
_l_(525833)
with _c_(525836, _n_(525834, "open", lambda: open), _n_(525835, "MASTERLIST", lambda: MASTERLIST), "w") as f:
    _l_(525841)

    _c_(525839, _a_(525838, _n_(525837, "f", lambda: f), "write"), '../conf/ignore.txt')
    _l_(525840)