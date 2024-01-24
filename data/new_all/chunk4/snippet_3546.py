# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72422206/typeerror-object-type-class-str-cannot-be-passed-to-c-code-valueerror-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import sys
   _l_(591274)

except ImportError:
   pass
try:
   import base64
   _l_(591276)

except ImportError:
   pass
try:
   from Crypto.Cipher import AES
   _l_(591278)

except ImportError:
   pass

if _c_(591282, _n_(591279, "len", lambda: len), _a_(591281, _n_(591280, "sys", lambda: sys), "argv")) != 2:
   _l_(591300)

   _c_(591284, _n_(591283, "print", lambda: print), "Incorrect amount of arguments.")
   _l_(591285)
   _c_(591287, _n_(591286, "print", lambda: print), "Example of use:")
   _l_(591288)
   _c_(591294, _n_(591289, "print", lambda: print), _c_(591293, _a_(591290, "$ python {} LjFWQMzS3GWDeav7+0Q0oSoOM43VwD30YZDVaItj8e0", "format"), _a_(591292, _n_(591291, "sys", lambda: sys), "argv")[0]))
   _l_(591295)
   _c_(591298, _a_(591297, _n_(591296, "sys", lambda: sys), "exit"))
   _l_(591299)

cpassword = _a_(591302, _n_(591301, "sys", lambda: sys), "argv")[1]
_l_(591303)

while _c_(591306, _n_(591304, "len", lambda: len), _n_(591305, "cpassword", lambda: cpassword)) % 4 > 0:
   _l_(591308)

   cpassword += "="
   _l_(591307)

decoded_password = _c_(591312, _a_(591310, _n_(591309, "base64", lambda: base64), "b64decode"), _n_(591311, "cpassword", lambda: cpassword))
_l_(591313)

# This is a Microsoft hardcoded key used to decrypt GPO hash.
key = '\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'
_l_(591314)

decryption_suite = _c_(591320, _a_(591316, _n_(591315, "AES", lambda: AES), "new"), _n_(591317, "key", lambda: key), _a_(591319, _n_(591318, "AES", lambda: AES), "MODE_CBC"), '\00'*16)
_l_(591321)
plain_text = _c_(591325, _a_(591323, _n_(591322, "decryption_suite", lambda: decryption_suite), "decrypt"), _n_(591324, "decoded_password", lambda: decoded_password))
_l_(591326)

_c_(591333, _n_(591327, "print", lambda: print), _c_(591332, _a_(591328, "Password is: {}", "format"), _c_(591331, _a_(591330, _n_(591329, "plain_text", lambda: plain_text), "strip"))))
_l_(591334)