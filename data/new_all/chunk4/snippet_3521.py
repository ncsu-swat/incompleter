# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72912852/python3-typeerror-a-bytes-like-object-is-required-not-str
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random, json, subprocess, psutil
    _l_(645710)

except ImportError:
    pass

json_key={}
_l_(645711)

def cpu_usage():
    _l_(645721)

    cpu_usage = _c_(645714, _a_(645713, _n_(645712, "psutil", lambda: psutil), "cpu_percent"), interval=2)
    _l_(645715)
    _n_(645716, "json_key", lambda: json_key)['cpu_usage'] = _c_(645719, _n_(645717, "float", lambda: float), _n_(645718, "cpu_usage", lambda: cpu_usage))
    _l_(645720)

def cpu_temp():
    _l_(645735)

    cpu_comm = "sensors |grep 'Core 0' |awk '{print $3}'|sed 's/\+//g;s/°C//g'"
    _l_(645722)
    cpu_value = _c_(645726, _a_(645724, _n_(645723, "subprocess", lambda: subprocess), "check_output"), _n_(645725, "cpu_comm", lambda: cpu_comm), shell=True)
    _l_(645727)
    _n_(645728, "json_key", lambda: json_key)['cpu_temp'] = _c_(645733, _n_(645729, "float", lambda: float), _c_(645732, _a_(645731, _n_(645730, "cpu_value", lambda: cpu_value), "rstrip"), '\n'))
    _l_(645734)

def disk_percent():
    _l_(645749)

    cmd_uptime = "df -h |grep sda1| awk '{print $5}'| sed 's/%//g'"
    _l_(645736)
    hdd_data = _c_(645740, _a_(645738, _n_(645737, "subprocess", lambda: subprocess), "check_output"), _n_(645739, "cmd_uptime", lambda: cmd_uptime), shell=True)
    _l_(645741)
    _n_(645742, "json_key", lambda: json_key)['hdd_percent'] = _c_(645747, _n_(645743, "float", lambda: float), _c_(645746, _a_(645745, _n_(645744, "hdd_data", lambda: hdd_data), "rstrip"), '\n'))
    _l_(645748)

def used_mem():
    _l_(645759)

    mem_cmd = "free -m |egrep 'cache|Mem' |grep -v used|awk '{print $3}'"
    _l_(645750)
    mem_used = _c_(645753, _a_(645752, _n_(645751, "psutil", lambda: psutil), "virtual_memory"))
    _l_(645754)
    _n_(645755, "json_key", lambda: json_key)['used_mem'] = _a_(645757, _n_(645756, "mem_used", lambda: mem_used), "total") >> 20
    _l_(645758)

def percent_mem():
    _l_(645768)

    mem_percent = _a_(645763, _c_(645762, _a_(645761, _n_(645760, "psutil", lambda: psutil), "virtual_memory")), "percent")
    _l_(645764)
    _n_(645765, "json_key", lambda: json_key)['percent_mem'] = _n_(645766, "mem_percent", lambda: mem_percent)
    _l_(645767)

'''This function is used to retrive values used by td-agent'''
_l_(645769)
def print_json():
    _l_(645777)

    _c_(645775, _n_(645770, "print", lambda: print), _c_(645774, _a_(645772, _n_(645771, "json", lambda: json), "dumps"), _n_(645773, "json_key", lambda: json_key)))
    _l_(645776)

if _n_(645778, "__name__", lambda: __name__) == "__main__":
    _l_(645797)

    _c_(645780, _n_(645779, "cpu_usage", lambda: cpu_usage))
    _l_(645781)
    _c_(645783, _n_(645782, "cpu_temp", lambda: cpu_temp))
    _l_(645784)
    _c_(645786, _n_(645785, "disk_percent", lambda: disk_percent))
    _l_(645787)
    _c_(645789, _n_(645788, "used_mem", lambda: used_mem))
    _l_(645790)
    _c_(645792, _n_(645791, "percent_mem", lambda: percent_mem))
    _l_(645793)
    _c_(645795, _n_(645794, "print_json", lambda: print_json))
    _l_(645796)