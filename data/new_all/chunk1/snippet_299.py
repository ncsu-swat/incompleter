# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42751642/py2neo-v3-attributeerror-object-has-no-attribute-db-exists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Content(_n_(393439, "GraphObject", lambda: GraphObject)):
    _l_(393441)

    pass
    _l_(393440)

class Person(_n_(393442, "Content", lambda: Content)):
    _l_(393474)

    __primarykey__ = 'name'
    _l_(393443)

    name = _c_(393444, Property)
    _l_(393445)
    in_scholar_names = _c_(393446, Property)
    _l_(393447)
#   
    mentored = _c_(393448, RelatedTo, 'Person')
    _l_(393449)
    mentored_by = _c_(393450, RelatedFrom, 'Person', 'MENTORED')
    _l_(393451)
    worked_alongside = _c_(393452, Related, 'Person', 'WORKED_ALONGSIDE')
    _l_(393453)
    studied_at = _c_(393454, RelatedTo, 'Institution')
    _l_(393455)
    worked_at = _c_(393456, RelatedTo, 'Institution')
    _l_(393457)
    tagged = _c_(393458, RelatedTo, 'Tag')
    _l_(393459)
    member_of = _c_(393460, RelatedTo, 'Institution')
    _l_(393461)

    last_update = _c_(393462, RelatedTo, 'UpdateLog')
    _l_(393463)

    def __lt__(self, other):
        _l_(393473)

        aux = _c_(393467, _a_(393466, _a_(393465, _n_(393464, "self", lambda: self), "name"), "split"))[-1] < _c_(393471, _a_(393470, _a_(393469, _n_(393468, "other", lambda: other), "name"), "split"))[-1]
        _l_(393472)
        return aux

class Institution(_n_(393475, "Content", lambda: Content)):
    _l_(393499)

    __primarykey__ = 'name'
    _l_(393476)
#   
    name = _c_(393477, Property)
    _l_(393478)
    location = _c_(393479, Property)
    _l_(393480)
    type = _c_(393481, Property)
    _l_(393482)
    carnegie_class = _c_(393483, Property)
    _l_(393484)
#   
    students = _c_(393485, RelatedFrom, 'Person', 'STUDIED_AT')
    _l_(393486)
    employees = _c_(393487, RelatedFrom, 'Person', 'WORKED_AT')
    _l_(393488)
    members = _c_(393489, RelatedFrom, 'Person', 'MEMBER_OF')
    _l_(393490)

    last_update = _c_(393491, RelatedTo, 'UpdateLog')
    _l_(393492)

    def __lt__(self, other):
        _l_(393498)

        aux = _a_(393494, _n_(393493, "self", lambda: self), "name") < _a_(393496, _n_(393495, "other", lambda: other), "name")
        _l_(393497)
        return aux


class User(_n_(393500, "GraphObject", lambda: GraphObject)):
    _l_(393512)

    __primarykey__ = 'username'
    _l_(393501)

    username = _c_(393502, Property)
    _l_(393503)
    joined = _c_(393504, Property)
    _l_(393505)
    last_access = _c_(393506, Property)
    _l_(393507)
    active = _c_(393508, Property)
    _l_(393509)

    contributed = _c_(393510, RelatedTo, 'UpdateLog')
    _l_(393511)


class Provenance(_n_(393513, "GraphObject", lambda: GraphObject)):
    _l_(393515)

    pass    
    _l_(393514)    
# 
class UpdateLog(_n_(393516, "Provenance", lambda: Provenance)):
    _l_(393534)

    __primarykey__ = 'id'
    _l_(393517)

    id = _c_(393518, Property)
    _l_(393519)
    timestamp = _c_(393520, Property)
    _l_(393521)
    query = _c_(393522, Property)
    _l_(393523)

    previous = _c_(393524, RelatedTo, 'UpdateLog', 'LAST_UPDATE')
    _l_(393525)
    next = _c_(393526, RelatedFrom, 'UpdateLog', 'LAST_UPDATE')
    _l_(393527)
    based_on = _c_(393528, RelatedTo, 'Provenance', 'BASED_ON')
    _l_(393529)

    affected_nodes = _c_(393530, RelatedFrom, 'Content', 'LAST_UPDATE')
    _l_(393531)
    contributed_by = _c_(393532, RelatedFrom, 'User', 'CONTRIBUTED')
    _l_(393533)

class DataSource(_n_(393535, "Provenance", lambda: Provenance)):
    _l_(393545)

    __primarykey__ = 'uri'
    _l_(393536)

    id = _c_(393537, Property)
    _l_(393538)
    description = _c_(393539, Property)
    _l_(393540)
    uri = _c_(393541, Property)
    _l_(393542)

    source_for = _c_(393543, RelatedFrom, 'UpdateLog', 'BASED_ON')
    _l_(393544)


class Tag(_n_(393546, "GraphObject", lambda: GraphObject)):
    _l_(393556)

    __primarykey__ = 'name'
    _l_(393547)

    name = _c_(393548, Property)
    _l_(393549)
    description = _c_(393550, Property)
    _l_(393551)

    see_also = _c_(393552, Related, 'Tag')
    _l_(393553)
    tagged = _c_(393554, RelatedFrom, 'Content')
    _l_(393555)