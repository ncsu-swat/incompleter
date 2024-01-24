# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61902310/typeerror-init-got-an-unexpected-keyword-argument-num-workers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from nornir import InitNornir
    _l_(663686)

except ImportError:
    pass
nr = _c_(663688, _n_(663687, "InitNornir", lambda: InitNornir), core={"num_workers": 100},
    inventory={
        "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
        "options": {
            "host_file": "inventory/hosts.yaml",
            "group_file": "inventory/groups.yaml"
        }
    }
)
_l_(663689)