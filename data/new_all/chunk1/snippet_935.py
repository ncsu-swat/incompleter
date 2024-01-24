# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69390842/parsing-namespace-xml-generates-attributeerror-str-object-has-no-attribute-t
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for ecu_container in _c_(384493, _a_(384492, _n_(384491, "root", lambda: root), "findall"), './/{http://autosar.org/schema/r4.0}ECUC-CONTAINER-VALUE'):
    _l_(384512)

    short_name = _a_(384497, _c_(384496, _a_(384495, _n_(384494, "ecu_container", lambda: ecu_container), "find"), './/{http://autosar.org/schema/r4.0}SHORT-NAME'), "text")
    _l_(384498)
    if(_n_(384499, "short_name", lambda: short_name) == _n_(384500, "component", lambda: component)):
        _l_(384511)

        value = _a_(384504, _c_(384503, _a_(384502, _n_(384501, "ecu_container", lambda: ecu_container), "find"), './/{http://autosar.org/schema/r4.0}VALUE'), "text")
        _l_(384505)
        _n_(384506, "value", lambda: value).text = _c_(384509, _n_(384507, "str", lambda: str), _n_(384508, "imageState", lambda: imageState))
        _l_(384510)