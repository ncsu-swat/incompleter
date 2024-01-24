# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56961816/attributeerror-list-object-has-no-attribute-iter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xml.etree.ElementTree as et
    _l_(571503)

except ImportError:
    pass
class SerializerFactory:
    _l_(571554)


    def serialize_all(self, format, member_list):
        _l_(571531)

        if _n_(571504, "format", lambda: format) == 'JSON':
            _l_(571530)

            serialize = _c_(571507, _n_(571505, "JsonSerializer", lambda: JsonSerializer), _n_(571506, "member_list", lambda: member_list))
            _l_(571508)
            _c_(571511, _a_(571510, _n_(571509, "serialize", lambda: serialize), "start_all_objects"))
            _l_(571512)
            aux = _n_(571513, "serialize", lambda: serialize)
            _l_(571514)
            return aux
        elif _n_(571515, "format", lambda: format) == 'XML':
            _l_(571529)

            serialize = _c_(571518, _n_(571516, "XmlSerializer", lambda: XmlSerializer), _n_(571517, "member_list", lambda: member_list))
            _l_(571519)
            _c_(571522, _a_(571521, _n_(571520, "serialize", lambda: serialize), "start_all_objects"))
            _l_(571523)
            aux = _n_(571524, "serialize", lambda: serialize)
            _l_(571525)
            return aux
        else:
            raise _c_(571527, _n_(571526, "ValueError", lambda: ValueError), "Format must be 'JSON' or 'XML'.")
            _l_(571528)

    def serialize_one(self, format, index, member_list):
        _l_(571553)

        if _n_(571532, "format", lambda: format) == 'JSON':
            _l_(571552)

            aux = _c_(571538, _a_(571536, _c_(571535, _n_(571533, "JsonSerializer", lambda: JsonSerializer), _n_(571534, "member_list", lambda: member_list)), "start_one_object"), _n_(571537, "index", lambda: index))
            _l_(571539)
            return aux
        elif _n_(571540, "format", lambda: format) == 'XML':
            _l_(571551)

            aux = _c_(571546, _a_(571544, _c_(571543, _n_(571541, "XmlSerializer", lambda: XmlSerializer), _n_(571542, "member_list", lambda: member_list)), "start_one_object"), _n_(571545, "index", lambda: index))
            _l_(571547)
            return aux
        else:
            raise _c_(571549, _n_(571548, "ValueError", lambda: ValueError), "Format must be 'JSON' or 'XML'.")
            _l_(571550)


class XmlSerializer:
    _l_(571638)

    def __init__(self, member_list):
        _l_(571562)

        _n_(571555, "self", lambda: self).member_list = _n_(571556, "member_list", lambda: member_list)
        _l_(571557)
        _n_(571558, "self", lambda: self).serialize_list = [] * _a_(571560, _n_(571559, "member_list", lambda: member_list), "size")
        _l_(571561)

    def start_all_objects(self):
        _l_(571599)

        for i in _c_(571567, _n_(571563, "range", lambda: range), _a_(571566, _a_(571565, _n_(571564, "self", lambda: self), "member_list"), "size")):
            _l_(571598)

            member = _a_(571569, _n_(571568, "self", lambda: self), "member_list")[_n_(571570, "i", lambda: i)]
            _l_(571571)
            number = _a_(571573, _n_(571572, "member", lambda: member), "mem_num")
            _l_(571574)
            l_name = _a_(571576, _n_(571575, "member", lambda: member), "l_name")
            _l_(571577)
            f_name = _a_(571579, _n_(571578, "member", lambda: member), "f_name")
            _l_(571580)
            mem_type = _a_(571582, _n_(571581, "member", lambda: member), "mem_type")
            _l_(571583)
            mem_list = _c_(571590, _a_(571585, _n_(571584, "et", lambda: et), "Element"), {'Number': _n_(571586, "number", lambda: number), 'Last Name': _n_(571587, "l_name", lambda: l_name),
                                   'First Name': _n_(571588, "f_name", lambda: f_name), 'Membership Type': _n_(571589, "mem_type", lambda: mem_type)})
            _l_(571591)

            _c_(571596, _a_(571594, _a_(571593, _n_(571592, "self", lambda: self), "serialize_list"), "append"), _n_(571595, "mem_list", lambda: mem_list))
            _l_(571597)

    def start_one_object(self, index):
        _l_(571630)

        member = _a_(571601, _n_(571600, "self", lambda: self), "member_list")[_n_(571602, "index", lambda: index)]
        _l_(571603)
        number = _a_(571605, _n_(571604, "member", lambda: member), "mem_num")
        _l_(571606)
        l_name = _a_(571608, _n_(571607, "member", lambda: member), "l_name")
        _l_(571609)
        f_name = _a_(571611, _n_(571610, "member", lambda: member), "f_name")
        _l_(571612)
        mem_type = _a_(571614, _n_(571613, "member", lambda: member), "mem_type")
        _l_(571615)
        mem_list = _c_(571622, _a_(571617, _n_(571616, "et", lambda: et), "Element"), {'Number': _n_(571618, "number", lambda: number), 'Last Name': _n_(571619, "l_name", lambda: l_name),
                               'First Name': _n_(571620, "f_name", lambda: f_name), 'Membership Type': _n_(571621, "mem_type", lambda: mem_type)})
        _l_(571623)
        _c_(571628, _a_(571626, _a_(571625, _n_(571624, "self", lambda: self), "serialize_list"), "append"), _n_(571627, "mem_list", lambda: mem_list))
        _l_(571629)

    def to_str(self):
        _l_(571637)

        aux = _c_(571635, _a_(571632, _n_(571631, "et", lambda: et), "tostring"), _a_(571634, _n_(571633, "self", lambda: self), "serialize_list"), encoding='unicode')
        _l_(571636)
        return aux


factory = _c_(571641, _a_(571640, _n_(571639, "MemberSerializer", lambda: MemberSerializer), "SerializerFactory"))
_l_(571642)
xml = _c_(571646, _a_(571644, _n_(571643, "factory", lambda: factory), "serialize_all"), 'XML', _n_(571645, "mem_list", lambda: mem_list))
_l_(571647)
_c_(571652, _n_(571648, "print", lambda: print), _c_(571651, _a_(571650, _n_(571649, "xml", lambda: xml), "to_str")))
_l_(571653)