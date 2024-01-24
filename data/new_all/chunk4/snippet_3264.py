# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76497050/python-nornir-attributeerror-nonetype-object-has-no-attribute-get
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from nornir import InitNornir
    _l_(614650)

except ImportError:
    pass
try:
    from nornir_netmiko.tasks import netmiko_send_command
    _l_(614652)

except ImportError:
    pass
try:
    from nornir_utils.plugins.functions import print_result
    _l_(614654)

except ImportError:
    pass

NORNIR_CONFIG_FILE = "/home/aruba/config.yaml"
_l_(614655)

nr = _c_(614658, _n_(614656, "InitNornir", lambda: InitNornir), config_file=_n_(614657, "NORNIR_CONFIG_FILE", lambda: NORNIR_CONFIG_FILE))
_l_(614659)

nr = _c_(614662, _a_(614661, _n_(614660, "nr", lambda: nr), "filter"), role="access")
_l_(614663)

def show_ip(task):
    _l_(614669)

    _c_(614667, _a_(614665, _n_(614664, "task", lambda: task), "run"), task=_n_(614666, "netmiko_send_command", lambda: netmiko_send_command), command_string="show ip")
    _l_(614668)

result = _c_(614673, _a_(614671, _n_(614670, "nr", lambda: nr), "run"), task=_n_(614672, "show_ip", lambda: show_ip))
_l_(614674)

if _n_(614675, "__name__", lambda: __name__) == "__main__":
    _l_(614680)

    _c_(614678, _n_(614676, "print_result", lambda: print_result), _n_(614677, "result", lambda: result))
    _l_(614679)