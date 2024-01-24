# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67486095/nameerror-name-status-code-is-not-defined-while-parsing-access-log
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
     import argparse
     _l_(372898)

except ImportError:
     pass
try:
     import json
     _l_(372900)

except ImportError:
     pass
try:
     import re
     _l_(372902)

except ImportError:
     pass
try:
     from collections import defaultdict
     _l_(372904)

except ImportError:
     pass

parser = _c_(372907, _a_(372906, _n_(372905, "argparse", lambda: argparse), "ArgumentParser"), description='log parser')
_l_(372908)
_c_(372911, _a_(372910, _n_(372909, "parser", lambda: parser), "add_argument"), '-f', dest='logfile', action='store', default='access.log')
_l_(372912)
args = _c_(372915, _a_(372914, _n_(372913, "parser", lambda: parser), "parse_args"))
_l_(372916)

regul_ip = (r"^(?P<ips>.*?)")
_l_(372917)
regul_statuscode = (r"\s(?P<status_code>400)\s")
_l_(372918)


dict_ip = _c_(372920, _n_(372919, "defaultdict", lambda: defaultdict), lambda: {"400": 0})
_l_(372921)

with _c_(372925, _n_(372922, "open", lambda: open), _a_(372924, _n_(372923, "args", lambda: args), "logfile")) as file:
     _l_(372956)

     for index, line in _c_(372930, _n_(372926, "enumerate", lambda: enumerate), _c_(372929, _a_(372928, _n_(372927, "file", lambda: file), "readlines"))):
          _l_(372955)

          try:
               _l_(372950)

               ip = _c_(372937, _a_(372936, _c_(372935, _a_(372932, _n_(372931, "re", lambda: re), "search"), _n_(372933, "regul_ip", lambda: regul_ip), _n_(372934, "line", lambda: line)), "group"))
               _l_(372938)
               status_code = _c_(372945, _a_(372944, _c_(372943, _a_(372940, _n_(372939, "re", lambda: re), "search"), _n_(372941, "regul_statuscode", lambda: regul_statuscode), _n_(372942, "line", lambda: line)), "groups"))[0]
               _l_(372946)
          except _n_(372947, "AttributeError", lambda: AttributeError):
               _l_(372949)

               pass
               _l_(372948)
          _n_(372951, "dict_ip", lambda: dict_ip)[_n_(372952, "ip", lambda: ip)][_n_(372953, "status_code", lambda: status_code)] += 1
          _l_(372954)

_c_(372962, _n_(372957, "print", lambda: print), _c_(372961, _a_(372959, _n_(372958, "json", lambda: json), "dumps"), _n_(372960, "dict_ip", lambda: dict_ip), indent=4))
_l_(372963)
with _c_(372965, _n_(372964, "open", lambda: open), "final_log.json", "w") as jsonfile:
     _l_(372972)

     _c_(372970, _a_(372967, _n_(372966, "json", lambda: json), "dump"), _n_(372968, "dict_ip", lambda: dict_ip), _n_(372969, "jsonfile", lambda: jsonfile), indent=5)
     _l_(372971)