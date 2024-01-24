# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56277732/native-messaging-firefox-extension-example-ping-pong-not-working-because-of-ty
#!/usr/bin/python -u

# Note that running python with the `-u` flag is required on Windows,
# in order to ensure that stdin and stdout are opened in binary, rather
# than text, mode.

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(558554)

except ImportError:
    pass
try:
    import sys
    _l_(558556)

except ImportError:
    pass
try:
    import struct
    _l_(558558)

except ImportError:
    pass


# Read a message from stdin and decode it.
def get_message():
    _l_(558586)

    raw_length = _c_(558562, _a_(558561, _a_(558560, _n_(558559, "sys", lambda: sys), "stdin"), "read"), 4)
    _l_(558563)
    if not _n_(558564, "raw_length", lambda: raw_length):
        _l_(558569)

        _c_(558567, _a_(558566, _n_(558565, "sys", lambda: sys), "exit"), 0)
        _l_(558568)
    message_length = _c_(558573, _a_(558571, _n_(558570, "struct", lambda: struct), "unpack"), '=I', _n_(558572, "raw_length", lambda: raw_length))[0]
    _l_(558574)
    message = _c_(558579, _a_(558577, _a_(558576, _n_(558575, "sys", lambda: sys), "stdin"), "read"), _n_(558578, "message_length", lambda: message_length))
    _l_(558580)
    aux = _c_(558584, _a_(558582, _n_(558581, "json", lambda: json), "loads"), _n_(558583, "message", lambda: message))
    _l_(558585)
    return aux


# Encode a message for transmission, given its content.
def encode_message(message_content):
    _l_(558602)

    encoded_content = _c_(558590, _a_(558588, _n_(558587, "json", lambda: json), "dumps"), _n_(558589, "message_content", lambda: message_content))
    _l_(558591)
    encoded_length = _c_(558597, _a_(558593, _n_(558592, "struct", lambda: struct), "pack"), '=I', _c_(558596, _n_(558594, "len", lambda: len), _n_(558595, "encoded_content", lambda: encoded_content)))
    _l_(558598)
    aux = {'length': _n_(558599, "encoded_length", lambda: encoded_length), 'content': _n_(558600, "encoded_content", lambda: encoded_content)}
    _l_(558601)
    return aux


# Send an encoded message to stdout.
def send_message(encoded_message):
    _l_(558620)

    _c_(558607, _a_(558605, _a_(558604, _n_(558603, "sys", lambda: sys), "stdout"), "write"), _n_(558606, "encoded_message", lambda: encoded_message)['length'])
    _l_(558608)
    _c_(558613, _a_(558611, _a_(558610, _n_(558609, "sys", lambda: sys), "stdout"), "write"), _n_(558612, "encoded_message", lambda: encoded_message)['content'])
    _l_(558614)
    _c_(558618, _a_(558617, _a_(558616, _n_(558615, "sys", lambda: sys), "stdout"), "flush"))
    _l_(558619)


while True:
    _l_(558631)

    message = _c_(558622, _n_(558621, "get_message", lambda: get_message))
    _l_(558623)
    if _n_(558624, "message", lambda: message) == "ping":
        _l_(558630)

        _c_(558628, _n_(558625, "send_message", lambda: send_message), _c_(558627, _n_(558626, "encode_message", lambda: encode_message), "pong"))
        _l_(558629)