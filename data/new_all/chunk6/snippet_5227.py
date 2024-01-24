# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53995606/typeerror-tuple-object-does-not-support-item-assignment-on-non-tuple-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
myresults=[('Raven', '18'), ('Cobra', '8'), ('Lion', '6'), ('Otter', '2')]
_l_(354462)


FirstScore=_n_(354463, "myresults", lambda: myresults)[0][1]
_l_(354464)
SecondHighestScore=0
_l_(354465)
ThirdHighestScore=0
_l_(354466)
for i in _n_(354467, "myresults", lambda: myresults):
    _l_(354476)

    if _n_(354468, "i", lambda: i)[1]==_n_(354469, "FirstScore", lambda: FirstScore):
        _l_(354475)

        _c_(354473, _a_(354471, _n_(354470, "FirstPlacePatrols", lambda: FirstPlacePatrols), "append"), _n_(354472, "i", lambda: i)[0])
        _l_(354474)
for i in _n_(354477, "myresults", lambda: myresults):
    _l_(354512)

    _c_(354480, _n_(354478, "print", lambda: print), _n_(354479, "i", lambda: i)[1])
    _l_(354481)
    _c_(354486, _n_(354482, "print", lambda: print), _c_(354485, _n_(354483, "repr", lambda: repr), _n_(354484, "i", lambda: i)[1]))
    _l_(354487)
    if _c_(354490, _n_(354488, "int", lambda: int), _n_(354489, "i", lambda: i)[1])<_c_(354493, _n_(354491, "int", lambda: int), _n_(354492, "FirstScore", lambda: FirstScore)):
        _l_(354511)

        if _c_(354496, _n_(354494, "int", lambda: int), _n_(354495, "i", lambda: i)[1])>=_n_(354497, "SecondHighestScore", lambda: SecondHighestScore):
            _l_(354510)

            _c_(354500, _n_(354498, "print", lambda: print), _n_(354499, "i", lambda: i)[1])
            _l_(354501)
            _n_(354502, "i", lambda: i)[1]=_n_(354503, "SecondHighestScore", lambda: SecondHighestScore)
            _l_(354504)
            _c_(354508, _a_(354506, _n_(354505, "SecondPlacePatrols", lambda: SecondPlacePatrols), "append"), _n_(354507, "i", lambda: i)[0])
            _l_(354509)
for i in _n_(354513, "myresults", lambda: myresults):
    _l_(354532)

    if _c_(354516, _n_(354514, "int", lambda: int), _n_(354515, "i", lambda: i)[1])<_n_(354517, "SecondHighestScore", lambda: SecondHighestScore):
        _l_(354531)

        if _c_(354520, _n_(354518, "int", lambda: int), _n_(354519, "i", lambda: i)[1])>=_n_(354521, "ThirdHighestScore", lambda: ThirdHighestScore):
            _l_(354530)

            _n_(354522, "i", lambda: i)[0]=_n_(354523, "ThirdHighestScore", lambda: ThirdHighestScore)
            _l_(354524)
            _c_(354528, _a_(354526, _n_(354525, "ThirdPlacePatrols", lambda: ThirdPlacePatrols), "append"), _n_(354527, "i", lambda: i)[0])
            _l_(354529)
_c_(354535, _n_(354533, "print", lambda: print), _n_(354534, "FirstPlacePatrols", lambda: FirstPlacePatrols))
_l_(354536)
_c_(354539, _n_(354537, "print", lambda: print), _n_(354538, "FirstScore", lambda: FirstScore))
_l_(354540)
_c_(354543, _n_(354541, "print", lambda: print), _n_(354542, "SecondPlacePatrols", lambda: SecondPlacePatrols))
_l_(354544)
_c_(354547, _n_(354545, "print", lambda: print), _n_(354546, "SecondHighestScore", lambda: SecondHighestScore))
_l_(354548)
_c_(354551, _n_(354549, "print", lambda: print), _n_(354550, "ThirdPlacePatrols", lambda: ThirdPlacePatrols))
_l_(354552)
_c_(354555, _n_(354553, "print", lambda: print), _n_(354554, "ThirdHighestScore", lambda: ThirdHighestScore))
_l_(354556)