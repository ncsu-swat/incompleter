# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60043979/how-to-resolve-typeerror-when-migrating-code-to-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(566476, _n_(566475, "keep_alive", lambda: keep_alive), 1,1)
_l_(566477)
process = _c_(566483, _a_(566479, _n_(566478, "subprocess", lambda: subprocess), "Popen"), 'grep -E -o ".Source QR CODE :.{0,65}" ' + _n_(566480, "latest_file", lambda: latest_file) + ' | tail -1', shell=True, stdout=_a_(566482, _n_(566481, "subprocess", lambda: subprocess), "PIPE"),)
_l_(566484)
stdout_list = _c_(566487, _a_(566486, _n_(566485, "process", lambda: process), "communicate"))
_l_(566488)
qr_code = _c_(566491, _a_(566490, _n_(566489, "stdout_list", lambda: stdout_list)[0], "replace"), 'Source QR CODE : ','')
_l_(566492)
qr_code = _c_(566495, _a_(566494, _n_(566493, "qr_code", lambda: qr_code), "replace"), ' ','')
_l_(566496)
qr_code = _c_(566499, _a_(566498, _n_(566497, "qr_code", lambda: qr_code), "replace"), '\n', '')
_l_(566500)
qr_code = _c_(566503, _n_(566501, "str", lambda: str), _n_(566502, "qr_code", lambda: qr_code))
_l_(566504)