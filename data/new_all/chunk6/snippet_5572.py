# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/24950570/typeerror-cant-convert-int-object-to-str-implicitly-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cgi
    _l_(337460)

except ImportError:
    pass
form = _c_(337463, _a_(337462, _n_(337461, "cgi", lambda: cgi), "FieldStorage"))
_l_(337464)

name = _c_(337469, _n_(337465, "str", lambda: str), _c_(337468, _a_(337467, _n_(337466, "form", lambda: form), "getvalue"), "name"))
_l_(337470)
age = _c_(337475, _n_(337471, "int", lambda: int), _c_(337474, _a_(337473, _n_(337472, "form", lambda: form), "getvalue"), "age"))
_l_(337476)

_c_(337478, _n_(337477, "print", lambda: print), """Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html><head>
<title>Lab 9</title>
</head><body>
""")
_l_(337479)

_c_(337482, _n_(337480, "print", lambda: print), "<p>Hello," +_n_(337481, "name", lambda: name)+ ".</p>")
_l_(337483)
_c_(337488, _n_(337484, "print", lambda: print), "Next year you will be" + _c_(337487, _n_(337485, "str", lambda: str), _n_(337486, "age", lambda: age)+1) + "years old")
_l_(337489)
_c_(337491, _n_(337490, "print", lambda: print), "</body></html>") 
_l_(337492) 