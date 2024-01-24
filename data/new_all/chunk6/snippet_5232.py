# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53995606/typeerror-tuple-object-does-not-support-item-assignment-on-non-tuple-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
myresults=[('Raven', '18'), ('Cobra', '8'), ('Lion', '6'), ('Otter', '2')]
_l_(350732)


FirstScore=_n_(350733, "myresults", lambda: myresults)[0][1]
_l_(350734)
SecondHighestScore=0
_l_(350735)
ThirdHighestScore=0
_l_(350736)
for i in _n_(350737, "myresults", lambda: myresults):
    _l_(350746)

    if _n_(350738, "i", lambda: i)[1]==_n_(350739, "FirstScore", lambda: FirstScore):
        _l_(350745)

        _c_(350743, _a_(350741, _n_(350740, "FirstPlacePatrols", lambda: FirstPlacePatrols), "append"), _n_(350742, "i", lambda: i)[0])
        _l_(350744)
for i in _n_(350747, "myresults", lambda: myresults):
    _l_(350782)

    _c_(350750, _n_(350748, "print", lambda: print), _n_(350749, "i", lambda: i)[1])
    _l_(350751)
    _c_(350756, _n_(350752, "print", lambda: print), _c_(350755, _n_(350753, "repr", lambda: repr), _n_(350754, "i", lambda: i)[1]))
    _l_(350757)
    if _c_(350760, _n_(350758, "int", lambda: int), _n_(350759, "i", lambda: i)[1])<_c_(350763, _n_(350761, "int", lambda: int), _n_(350762, "FirstScore", lambda: FirstScore)):
        _l_(350781)

        if _c_(350766, _n_(350764, "int", lambda: int), _n_(350765, "i", lambda: i)[1])>=_n_(350767, "SecondHighestScore", lambda: SecondHighestScore):
            _l_(350780)

            _c_(350770, _n_(350768, "print", lambda: print), _n_(350769, "i", lambda: i)[1])
            _l_(350771)
            _n_(350772, "i", lambda: i)[1]=_n_(350773, "SecondHighestScore", lambda: SecondHighestScore)
            _l_(350774)
            _c_(350778, _a_(350776, _n_(350775, "SecondPlacePatrols", lambda: SecondPlacePatrols), "append"), _n_(350777, "i", lambda: i)[0])
            _l_(350779)
for i in _n_(350783, "myresults", lambda: myresults):
    _l_(350802)

    if _c_(350786, _n_(350784, "int", lambda: int), _n_(350785, "i", lambda: i)[1])<_n_(350787, "SecondHighestScore", lambda: SecondHighestScore):
        _l_(350801)

        if _c_(350790, _n_(350788, "int", lambda: int), _n_(350789, "i", lambda: i)[1])>=_n_(350791, "ThirdHighestScore", lambda: ThirdHighestScore):
            _l_(350800)

            _n_(350792, "i", lambda: i)[0]=_n_(350793, "ThirdHighestScore", lambda: ThirdHighestScore)
            _l_(350794)
            _c_(350798, _a_(350796, _n_(350795, "ThirdPlacePatrols", lambda: ThirdPlacePatrols), "append"), _n_(350797, "i", lambda: i)[0])
            _l_(350799)
_c_(350805, _n_(350803, "print", lambda: print), _n_(350804, "FirstPlacePatrols", lambda: FirstPlacePatrols))
_l_(350806)
_c_(350809, _n_(350807, "print", lambda: print), _n_(350808, "FirstScore", lambda: FirstScore))
_l_(350810)
_c_(350813, _n_(350811, "print", lambda: print), _n_(350812, "SecondPlacePatrols", lambda: SecondPlacePatrols))
_l_(350814)
_c_(350817, _n_(350815, "print", lambda: print), _n_(350816, "SecondHighestScore", lambda: SecondHighestScore))
_l_(350818)
_c_(350821, _n_(350819, "print", lambda: print), _n_(350820, "ThirdPlacePatrols", lambda: ThirdPlacePatrols))
_l_(350822)
_c_(350825, _n_(350823, "print", lambda: print), _n_(350824, "ThirdHighestScore", lambda: ThirdHighestScore))
_l_(350826)