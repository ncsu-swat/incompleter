# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52556478/pyvbox-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
vm = _c_(689010, _a_(689008, _n_(689007, "vbox", lambda: vbox), "find_machine"), _n_(689009, "vm_name", lambda: vm_name))
_l_(689011)
session = _c_(689014, _a_(689013, _n_(689012, "vm", lambda: vm), "create_session"))
_l_(689015)
guest_session = _c_(689022, _a_(689019, _a_(689018, _a_(689017, _n_(689016, "session", lambda: session), "console"), "guest"), "create_session"), _n_(689020, "vm_username", lambda: vm_username), _n_(689021, "vm_password", lambda: vm_password))
_l_(689023)
_c_(689027, _a_(689025, _n_(689024, "guest_session", lambda: guest_session), "execute"), 'C:\\Program Files\\Internet Explorer\\iexplore.exe', [_n_(689026, "url", lambda: url)])
_l_(689028)