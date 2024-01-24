# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32288466/python-attributeerror-str-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
__author__ = 'Goldsmitd'
_l_(443653)

class Rook:
    _l_(443669)

    def __init__(self,x,y,sl,team):
        _l_(443668)

        _n_(443654, "self", lambda: self).name = 'Rook'
        _l_(443655)
        _n_(443656, "self", lambda: self).x = _n_(443657, "x", lambda: x)
        _l_(443658)
        _n_(443659, "self", lambda: self).y = _n_(443660, "y", lambda: y)
        _l_(443661)
        _n_(443662, "self", lambda: self).sl = _n_(443663, "sl", lambda: sl)
        _l_(443664)
        _n_(443665, "self", lambda: self).team = _n_(443666, "team", lambda: team)
        _l_(443667)


class Knight:
    _l_(443685)

    def __init__(self,x,y,sl,team):
        _l_(443684)

        _n_(443670, "self", lambda: self).name = 'Knight'
        _l_(443671)
        _n_(443672, "self", lambda: self).x = _n_(443673, "x", lambda: x)
        _l_(443674)
        _n_(443675, "self", lambda: self).y = _n_(443676, "y", lambda: y)
        _l_(443677)
        _n_(443678, "self", lambda: self).sl = _n_(443679, "sl", lambda: sl)
        _l_(443680)
        _n_(443681, "self", lambda: self).team = _n_(443682, "team", lambda: team)
        _l_(443683)


class Bishop:
    _l_(443701)

    def __init__(self,x,y,sl,team):
        _l_(443700)

        _n_(443686, "self", lambda: self).name = 'Bishop'
        _l_(443687)
        _n_(443688, "self", lambda: self).x = _n_(443689, "x", lambda: x)
        _l_(443690)
        _n_(443691, "self", lambda: self).y = _n_(443692, "y", lambda: y)
        _l_(443693)
        _n_(443694, "self", lambda: self).sl = _n_(443695, "sl", lambda: sl)
        _l_(443696)
        _n_(443697, "self", lambda: self).team = _n_(443698, "team", lambda: team)
        _l_(443699)


class Queen:
    _l_(443717)

    def __init__(self,x,y,sl,team):
        _l_(443716)

        _n_(443702, "self", lambda: self).name = 'Queen'
        _l_(443703)
        _n_(443704, "self", lambda: self).x = _n_(443705, "x", lambda: x)
        _l_(443706)
        _n_(443707, "self", lambda: self).y = _n_(443708, "y", lambda: y)
        _l_(443709)
        _n_(443710, "self", lambda: self).sl = _n_(443711, "sl", lambda: sl)
        _l_(443712)
        _n_(443713, "self", lambda: self).team = _n_(443714, "team", lambda: team)
        _l_(443715)


class King:
    _l_(443733)

    def __init__(self,x,y,sl,team):
        _l_(443732)

        _n_(443718, "self", lambda: self).name = 'King'
        _l_(443719)
        _n_(443720, "self", lambda: self).x = _n_(443721, "x", lambda: x)
        _l_(443722)
        _n_(443723, "self", lambda: self).y = _n_(443724, "y", lambda: y)
        _l_(443725)
        _n_(443726, "self", lambda: self).sl = _n_(443727, "sl", lambda: sl)
        _l_(443728)
        _n_(443729, "self", lambda: self).team = _n_(443730, "team", lambda: team)
        _l_(443731)


class Pawn:
    _l_(443749)

    def __init__(self,x,y,sl,team):
        _l_(443748)

        _n_(443734, "self", lambda: self).name = 'Pawn'
        _l_(443735)
        _n_(443736, "self", lambda: self).x = _n_(443737, "x", lambda: x)
        _l_(443738)
        _n_(443739, "self", lambda: self).y = _n_(443740, "y", lambda: y)
        _l_(443741)
        _n_(443742, "self", lambda: self).sl = _n_(443743, "sl", lambda: sl)
        _l_(443744)
        _n_(443745, "self", lambda: self).team = _n_(443746, "team", lambda: team)
        _l_(443747)


class Chess_Board:
    _l_(444020)

    def __init__(self):
        _l_(443834)

        _n_(443750, "self", lambda: self).board = [['.']*8 for _ in _c_(443752, _n_(443751, "range", lambda: range), 8)]
        _l_(443753)
        _a_(443755, _n_(443754, "self", lambda: self), "board")[7][0] = _c_(443757, _n_(443756, "Rook", lambda: Rook), x=7,y=0,sl='R',team='white')
        _l_(443758)
        _a_(443760, _n_(443759, "self", lambda: self), "board")[7][1] = _c_(443762, _n_(443761, "Knight", lambda: Knight), x=7,y=1,sl='N',team='white')
        _l_(443763)
        _a_(443765, _n_(443764, "self", lambda: self), "board")[7][2] = _c_(443767, _n_(443766, "Bishop", lambda: Bishop), x=7,y=2,sl='B',team='white')
        _l_(443768)
        _a_(443770, _n_(443769, "self", lambda: self), "board")[7][3] = _c_(443772, _n_(443771, "Queen", lambda: Queen), x=7,y=3,sl='Q',team='white')
        _l_(443773)
        _a_(443775, _n_(443774, "self", lambda: self), "board")[7][4] = _c_(443777, _n_(443776, "King", lambda: King), x=7,y=4,sl='K',team='white')
        _l_(443778)
        _a_(443780, _n_(443779, "self", lambda: self), "board")[7][5] = _c_(443782, _n_(443781, "Bishop", lambda: Bishop), x=7,y=5,sl='B',team='white')
        _l_(443783)
        _a_(443785, _n_(443784, "self", lambda: self), "board")[7][6] = _c_(443787, _n_(443786, "Knight", lambda: Knight), x=7,y=6,sl='N',team='white')
        _l_(443788)
        _a_(443790, _n_(443789, "self", lambda: self), "board")[7][7] = _c_(443792, _n_(443791, "Rook", lambda: Rook), x=7,y=7,sl='R',team='white')
        _l_(443793)
        _a_(443795, _n_(443794, "self", lambda: self), "board")[6][0] = _c_(443797, _n_(443796, "Pawn", lambda: Pawn), x=6,y=0,sl='P',team='white')
        _l_(443798)
        _a_(443800, _n_(443799, "self", lambda: self), "board")[6][0] = _c_(443802, _n_(443801, "Pawn", lambda: Pawn), x=6,y=1,sl='P',team='white')
        _l_(443803)
        _a_(443805, _n_(443804, "self", lambda: self), "board")[6][0] = _c_(443807, _n_(443806, "Pawn", lambda: Pawn), x=6,y=2,sl='P',team='white')
        _l_(443808)
        _a_(443810, _n_(443809, "self", lambda: self), "board")[6][0] = _c_(443812, _n_(443811, "Pawn", lambda: Pawn), x=6,y=3,sl='P',team='white')
        _l_(443813)
        _a_(443815, _n_(443814, "self", lambda: self), "board")[6][0] = _c_(443817, _n_(443816, "Pawn", lambda: Pawn), x=6,y=4,sl='P',team='white')
        _l_(443818)
        _a_(443820, _n_(443819, "self", lambda: self), "board")[6][0] = _c_(443822, _n_(443821, "Pawn", lambda: Pawn), x=6,y=5,sl='P',team='white')
        _l_(443823)
        _a_(443825, _n_(443824, "self", lambda: self), "board")[6][0] = _c_(443827, _n_(443826, "Pawn", lambda: Pawn), x=6,y=6,sl='P',team='white')
        _l_(443828)
        _a_(443830, _n_(443829, "self", lambda: self), "board")[6][0] = _c_(443832, _n_(443831, "Pawn", lambda: Pawn), x=6,y=7,sl='P',team='white')
        _l_(443833)

    def display(self):
        _l_(443905)

        for i in _c_(443836, _n_(443835, "range", lambda: range), 8):
            _l_(443904)

            for j in _c_(443838, _n_(443837, "range", lambda: range), 8):
                _l_(443900)

                if _a_(443843, _a_(443840, _n_(443839, "self", lambda: self), "board")[_n_(443841, "i", lambda: i)][_n_(443842, "j", lambda: j)], "sl")=='R':
                    _l_(443899)

                    _c_(443845, _n_(443844, "print", lambda: print), 'R',end=' ')
                    _l_(443846)
                elif _a_(443851, _a_(443848, _n_(443847, "self", lambda: self), "board")[_n_(443849, "i", lambda: i)][_n_(443850, "j", lambda: j)], "sl")=='N':
                    _l_(443898)

                    _c_(443853, _n_(443852, "print", lambda: print), 'N',end=' ')
                    _l_(443854)
                elif _a_(443859, _a_(443856, _n_(443855, "self", lambda: self), "board")[_n_(443857, "i", lambda: i)][_n_(443858, "j", lambda: j)], "sl")=='B':
                    _l_(443897)

                    _c_(443861, _n_(443860, "print", lambda: print), 'B',end=' ')
                    _l_(443862)
                elif _a_(443867, _a_(443864, _n_(443863, "self", lambda: self), "board")[_n_(443865, "i", lambda: i)][_n_(443866, "j", lambda: j)], "sl")=='Q':
                    _l_(443896)

                    _c_(443869, _n_(443868, "print", lambda: print), 'Q',end=' ')
                    _l_(443870)
                elif _a_(443875, _a_(443872, _n_(443871, "self", lambda: self), "board")[_n_(443873, "i", lambda: i)][_n_(443874, "j", lambda: j)], "sl")=='K':
                    _l_(443895)

                    _c_(443877, _n_(443876, "print", lambda: print), 'K',end=' ')
                    _l_(443878)
                elif _a_(443883, _a_(443880, _n_(443879, "self", lambda: self), "board")[_n_(443881, "i", lambda: i)][_n_(443882, "j", lambda: j)], "sl")=='P':
                    _l_(443894)

                    _c_(443885, _n_(443884, "print", lambda: print), 'P',end=' ')
                    _l_(443886)
                else:
                    _c_(443892, _n_(443887, "print", lambda: print), _a_(443889, _n_(443888, "self", lambda: self), "board")[_n_(443890, "i", lambda: i)][_n_(443891, "j", lambda: j)],end=' ')
                    _l_(443893)
            _c_(443902, _n_(443901, "print", lambda: print))
            _l_(443903)

    def figure_choice(self):
        _l_(443928)

        while True:
            _l_(443927)

            try:
                _l_(443926)

                _c_(443907, _n_(443906, "print", lambda: print), 'please give a position of figure which you chose')
                _l_(443908)
                sx=_c_(443912, _n_(443909, "int", lambda: int), _c_(443911, _n_(443910, "input", lambda: input)))
                _l_(443913)
                sy=_c_(443917, _n_(443914, "int", lambda: int), _c_(443916, _n_(443915, "input", lambda: input)))
                _l_(443918)
                aux = _n_(443919, "sx", lambda: sx),_n_(443920, "sy", lambda: sy)
                _l_(443921)
                return aux
            except:
                _l_(443925)

                _c_(443923, _n_(443922, "print", lambda: print), 'ERROR. Your choice is valid. Please choose only integers')
                _l_(443924)

    def move_king(self):
        _l_(444019)


        while True:
            _l_(444018)

            try:
                _l_(443949)

                _c_(443930, _n_(443929, "print", lambda: print), 'please give a position of figure which you chose')
                _l_(443931)
                sx=_c_(443935, _n_(443932, "int", lambda: int), _c_(443934, _n_(443933, "input", lambda: input)))
                _l_(443936)
                sy=_c_(443940, _n_(443937, "int", lambda: int), _c_(443939, _n_(443938, "input", lambda: input)))
                _l_(443941)
                aux = _n_(443942, "sx", lambda: sx),_n_(443943, "sy", lambda: sy)
                _l_(443944)
                return aux
            except:
                _l_(443948)

                _c_(443946, _n_(443945, "print", lambda: print), 'ERROR. Your choice is valid. Please choose only integers')
                _l_(443947)
            try:
                _l_(443967)

                _c_(443951, _n_(443950, "print", lambda: print), 'please give a position of king')
                _l_(443952)
                sx=_c_(443956, _n_(443953, "int", lambda: int), _c_(443955, _n_(443954, "input", lambda: input)))
                _l_(443957)
                sy=_c_(443961, _n_(443958, "int", lambda: int), _c_(443960, _n_(443959, "input", lambda: input)))
                _l_(443962)
            except:
                _l_(443966)

                _c_(443964, _n_(443963, "print", lambda: print), 'ERROR. Your choice is valid. Please choose only integers')
                _l_(443965)
            try:
                _l_(443985)

                _c_(443969, _n_(443968, "print", lambda: print), 'please choose a destination for king')
                _l_(443970)
                dx=_c_(443974, _n_(443971, "int", lambda: int), _c_(443973, _n_(443972, "input", lambda: input)))
                _l_(443975)
                dy=_c_(443979, _n_(443976, "int", lambda: int), _c_(443978, _n_(443977, "input", lambda: input)))
                _l_(443980)
            except:
                _l_(443984)

                _c_(443982, _n_(443981, "print", lambda: print), 'ERROR. Your choice is valid. Please choose only integers')
                _l_(443983)
            if _a_(443987, _n_(443986, "self", lambda: self), "board")[_n_(443988, "dx", lambda: dx)][_n_(443989, "dy", lambda: dy)] == '.' :
                _l_(444017)

                if ( _c_(443993, _n_(443990, "abs", lambda: abs), _n_(443991, "sx", lambda: sx)-_n_(443992, "dx", lambda: dx)) <2 and _c_(443997, _n_(443994, "abs", lambda: abs), _n_(443995, "sx", lambda: sx)-_n_(443996, "dy", lambda: dy)) < 2 ):
                    _l_(444016)

                    _a_(443999, _n_(443998, "self", lambda: self), "board")[_n_(444000, "dx", lambda: dx)][_n_(444001, "dy", lambda: dy)]=_c_(444005, _n_(444002, "King", lambda: King), x=_n_(444003, "dx", lambda: dx),y=_n_(444004, "dy", lambda: dy),sl='K',team='white')
                    _l_(444006)
                    _a_(444008, _n_(444007, "self", lambda: self), "board")[_n_(444009, "sx", lambda: sx)][_n_(444010, "sy", lambda: sy)] = '.'
                    _l_(444011)
                    aux = _a_(444013, _n_(444012, "self", lambda: self), "board")
                    _l_(444014)
                    return aux
                    break
                    _l_(444015)


a=_c_(444022, _n_(444021, "Chess_Board", lambda: Chess_Board))
_l_(444023)

_c_(444026, _a_(444025, _n_(444024, "a", lambda: a), "display"))
_l_(444027)
_c_(444032, _n_(444028, "print", lambda: print), _a_(444031, _a_(444030, _n_(444029, "a", lambda: a), "board")[7][0], "sl"))
_l_(444033)