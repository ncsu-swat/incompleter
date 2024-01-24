# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67100743/dbus-error-unable-to-append-with-type-error-saying-list-indices-must-be-integer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(565137, ('g-io-error-quark: GDBus.Error:org.freedesktop.DBus.Python.TypeError: '
 'Traceback (most recent call last):\n'
 '  File "/usr/lib/python3/dist-packages/dbus/service.py", line 751, in '
 '_message_cb\n'
 '    _method_reply_return(connection, message, method_name, signature, '
 '*retval)\n'
 '  File "/usr/lib/python3/dist-packages/dbus/service.py", line 254, in '
 '_method_reply_return\n'
 '    reply.append(signature=signature, *retval)\n'
 'TypeError: list indices must be integers or slices, not list\n'
 ' (36)'), 'g-io-error-quark: GDBus.Error:org.freedesktop.DBus.Python.TypeError: '
 'Traceback (most recent call last):\n'
 '  File "/usr/lib/python3/dist-packages/dbus/service.py", line 751, in '
 '_message_cb\n'
 '    _method_reply_return(connection, message, method_name, signature, '
 '*retval)\n'
 '  File "/usr/lib/python3/dist-packages/dbus/service.py", line 254, in '
 '_method_reply_return\n'
 '    reply.append(signature=signature, *retval)\n'
 'TypeError: list indices must be integers or slices, not dict\n'
 ' (36)')
_l_(565138)