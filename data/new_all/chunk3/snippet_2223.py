# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57117240/super-attributeerror-when-trying-to-access-ids
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(524589)

except ImportError:
    pass
try:
    import random
    _l_(524591)

except ImportError:
    pass
try:
    import kivy
    _l_(524593)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(524595)

except ImportError:
    pass
try:
    from kivy.uix.button import Label
    _l_(524597)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(524599)

except ImportError:
    pass
try:
    from kivy.uix.gridlayout import GridLayout
    _l_(524601)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(524603)

except ImportError:
    pass

class Cell(_n_(524604, "Button", lambda: Button)):
    _l_(524770)

    def __init__(self, text, loc, board, **kwargs):
        _l_(524638)

        _c_(524610, _a_(524608, _n_(524605, "super", lambda: super)(_n_(524606, "Cell", lambda: Cell), _n_(524607, "self", lambda: self)), "__init__"), **_n_(524609, "kwargs", lambda: kwargs))
        _l_(524611)
        _n_(524612, "self", lambda: self).size = (25,25)
        _l_(524613)
        _n_(524614, "self", lambda: self).board = _n_(524615, "board", lambda: board)
        _l_(524616)
        _n_(524617, "self", lambda: self).loc = _n_(524618, "loc", lambda: loc)
        _l_(524619)
        _n_(524620, "self", lambda: self).text = _n_(524621, "text", lambda: text)
        _l_(524622)
        _n_(524623, "self", lambda: self).val = 0
        _l_(524624)
        _c_(524629, _a_(524626, _n_(524625, "self", lambda: self), "bind"), on_touch_up = _a_(524628, _n_(524627, "self", lambda: self), "onPress"))
        _l_(524630)
        _n_(524631, "self", lambda: self).visible = False
        _l_(524632)
        _n_(524633, "self", lambda: self).app = _c_(524636, _a_(524635, _n_(524634, "App", lambda: App), "get_running_app"))
        _l_(524637)

    def onPress(self, instance, touch):
        _l_(524683)

        if _c_(524643, _a_(524640, _n_(524639, "self", lambda: self), "collide_point"), *_a_(524642, _n_(524641, "touch", lambda: touch), "pos")):
            _l_(524682)

            if _a_(524645, _n_(524644, "self", lambda: self), "visible") == False:
                _l_(524681)

                _n_(524646, "self", lambda: self).visible = True
                _l_(524647)
                if _a_(524649, _n_(524648, "touch", lambda: touch), "button") == 'right':
                    _l_(524680)

                    if _a_(524651, _n_(524650, "self", lambda: self), "text") == '!':
                        _l_(524656)

                        _n_(524652, "self", lambda: self).text = '?'
                        _l_(524653)
                    else:
                        _n_(524654, "self", lambda: self).text = '!'
                        _l_(524655)
                elif _a_(524658, _n_(524657, "touch", lambda: touch), "button") == 'left':
                    _l_(524679)

                    _n_(524659, "self", lambda: self).text = _a_(524661, _n_(524660, "self", lambda: self), "val")
                    _l_(524662)
                    if _a_(524664, _n_(524663, "self", lambda: self), "val") == 'X':
                        _l_(524678)

                        None
                        _l_(524665)
                    elif _a_(524667, _n_(524666, "self", lambda: self), "val") == '0':
                        _l_(524677)

                        _c_(524674, _a_(524669, _n_(524668, "self", lambda: self), "revealNeighbors"), _a_(524671, _n_(524670, "self", lambda: self), "loc")[0],_a_(524673, _n_(524672, "self", lambda: self), "loc")[1])
                        _l_(524675)
                    else:
                        None
                        _l_(524676)

    def revealNeighbors(self,y,x):
        _l_(524769)

        for i in _c_(524685, _n_(524684, "range", lambda: range), -1,2):
            _l_(524767)

            for j in _c_(524687, _n_(524686, "range", lambda: range), -1,2):
                _l_(524766)

                if (0 <= (_a_(524689, _n_(524688, "self", lambda: self), "loc")[0] + _n_(524690, "i", lambda: i)) < _a_(524692, _n_(524691, "self", lambda: self), "board")[0]) and (0 <= (_a_(524694, _n_(524693, "self", lambda: self), "loc")[1] + _n_(524695, "j", lambda: j)) < _a_(524697, _n_(524696, "self", lambda: self), "board")[1]):
                    _l_(524765)

                    _c_(524700, _n_(524698, "print", lambda: print), _n_(524699, "self", lambda: self))
                    _l_(524701)
                    if _a_(524710, _a_(524707, _a_(524706, _a_(524705, _a_(524704, _a_(524703, _n_(524702, "self", lambda: self), "app"), "root"), "ids"), "myboard"), "cells")[_n_(524708, "i", lambda: i)][_n_(524709, "j", lambda: j)], "visible") != True:
                        _l_(524764)

                        _a_(524715, _a_(524714, _a_(524713, _a_(524712, _n_(524711, "self", lambda: self), "app"), "ids"), "myboard"), "cells")[_n_(524716, "i", lambda: i)][_n_(524717, "j", lambda: j)].visible = True
                        _l_(524718)
                        _a_(524723, _a_(524722, _a_(524721, _a_(524720, _n_(524719, "self", lambda: self), "app"), "ids"), "myboard"), "cells")[_n_(524724, "i", lambda: i)][_n_(524725, "j", lambda: j)].text = _a_(524733, _a_(524730, _a_(524729, _a_(524728, _a_(524727, _n_(524726, "self", lambda: self), "app"), "ids"), "myboard"), "cells")[_n_(524731, "i", lambda: i)][_n_(524732, "j", lambda: j)], "val")
                        _l_(524734)
                        if _a_(524742, _a_(524739, _a_(524738, _a_(524737, _a_(524736, _n_(524735, "self", lambda: self), "app"), "ids"), "myboard"), "cells")[_n_(524740, "i", lambda: i)][_n_(524741, "j", lambda: j)], "val") == '0':
                            _l_(524763)

                            _c_(524761, _a_(524751, _a_(524748, _a_(524747, _a_(524746, _a_(524745, _a_(524744, _n_(524743, "self", lambda: self), "app"), "root"), "ids"), "myboard"), "cells")[_n_(524749, "i", lambda: i)][_n_(524750, "j", lambda: j)], "revealNeighbors"), _a_(524756, _a_(524755, _a_(524754, _a_(524753, _n_(524752, "self", lambda: self), "app"), "ids"), "myboard"), "cells")[_n_(524757, "i", lambda: i)][_n_(524758, "j", lambda: j)],_n_(524759, "i", lambda: i),_n_(524760, "j", lambda: j))
                            _l_(524762)


        None
        _l_(524768)


class GameBoard(_n_(524771, "GridLayout", lambda: GridLayout)):
    _l_(525558)

    def __init__(self, **kwargs):
        _l_(525557)

        id: _n_(524772, "myboard", lambda: myboard)
        _l_(524773)
        name: "Board"
        _l_(524774)
        _c_(524780, _a_(524778, _n_(524775, "super", lambda: super)(_n_(524776, "GameBoard", lambda: GameBoard), _n_(524777, "self", lambda: self)), "__init__"), **_n_(524779, "kwargs", lambda: kwargs))
        _l_(524781)

        _n_(524782, "self", lambda: self).row_force_default = True
        _l_(524783)
        _n_(524784, "self", lambda: self).row_default_height = 30
        _l_(524785)
        _n_(524786, "self", lambda: self).col_force_default = True
        _l_(524787)
        _n_(524788, "self", lambda: self).col_default_width = 30
        _l_(524789)

        _n_(524790, "self", lambda: self).cols = 30
        _l_(524791)
        _n_(524792, "self", lambda: self).rows = 16
        _l_(524793)
        _n_(524794, "Window", lambda: Window).size = (_a_(524796, _n_(524795, "self", lambda: self), "cols") * _a_(524798, _n_(524797, "self", lambda: self), "col_default_width"), _a_(524800, _n_(524799, "self", lambda: self), "rows") * _a_(524802, _n_(524801, "self", lambda: self), "row_default_height"))
        _l_(524803)
        _n_(524804, "self", lambda: self).cells = _c_(524806, _n_(524805, "list", lambda: list))
        _l_(524807)
        mines = 0
        _l_(524808)
        minelst = _c_(524810, _n_(524809, "list", lambda: list))
        _l_(524811)

        _n_(524812, "self", lambda: self).score = 0
        _l_(524813)

        for i in _c_(524817, _n_(524814, "range", lambda: range), _a_(524816, _n_(524815, "self", lambda: self), "rows")):
            _l_(524851)

            temp = _c_(524819, _n_(524818, "list", lambda: list))
            _l_(524820)
            for j in _c_(524824, _n_(524821, "range", lambda: range), _a_(524823, _n_(524822, "self", lambda: self), "cols")):
                _l_(524844)

                newCell = _c_(524832, _n_(524825, "Cell", lambda: Cell), text = '0',loc = [_n_(524826, "i", lambda: i),_n_(524827, "j", lambda: j)], board = [_a_(524829, _n_(524828, "self", lambda: self), "rows"),_a_(524831, _n_(524830, "self", lambda: self), "cols")])
                _l_(524833)
                _c_(524837, _a_(524835, _n_(524834, "temp", lambda: temp), "append"), _n_(524836, "newCell", lambda: newCell))
                _l_(524838)
                _c_(524842, _a_(524840, _n_(524839, "self", lambda: self), "add_widget"), _n_(524841, "temp", lambda: temp)[-1])
                _l_(524843)
            _c_(524849, _a_(524847, _a_(524846, _n_(524845, "self", lambda: self), "cells"), "append"), _n_(524848, "temp", lambda: temp))
            _l_(524850)

        for k in _c_(524854, _n_(524852, "range", lambda: range), _n_(524853, "mines", lambda: mines)):
            _l_(524908)

            randX = _c_(524859, _a_(524856, _n_(524855, "random", lambda: random), "randint"), 0,_a_(524858, _n_(524857, "self", lambda: self), "cols") - 1)
            _l_(524860)
            randY = _c_(524865, _a_(524862, _n_(524861, "random", lambda: random), "randint"), 0,_a_(524864, _n_(524863, "self", lambda: self), "rows") - 1)
            _l_(524866)
            while _a_(524871, _a_(524868, _n_(524867, "self", lambda: self), "cells")[_n_(524869, "randY", lambda: randY)][_n_(524870, "randX", lambda: randX)], "text") == 'X':
                _l_(524884)

                randX = _c_(524876, _a_(524873, _n_(524872, "random", lambda: random), "randint"), 0,_a_(524875, _n_(524874, "self", lambda: self), "cols") - 1)
                _l_(524877)
                randY = _c_(524882, _a_(524879, _n_(524878, "random", lambda: random), "randint"), 0,_a_(524881, _n_(524880, "self", lambda: self), "rows") - 1)
                _l_(524883)
            _a_(524886, _n_(524885, "self", lambda: self), "cells")[_n_(524887, "randY", lambda: randY)][_n_(524888, "randX", lambda: randX)].text = 'X'
            _l_(524889)
            temp = _c_(524891, _n_(524890, "list", lambda: list))
            _l_(524892)
            _c_(524896, _a_(524894, _n_(524893, "temp", lambda: temp), "append"), _n_(524895, "randY", lambda: randY))
            _l_(524897)
            _c_(524901, _a_(524899, _n_(524898, "temp", lambda: temp), "append"), _n_(524900, "randX", lambda: randX))
            _l_(524902)
            _c_(524906, _a_(524904, _n_(524903, "minelst", lambda: minelst), "append"), _n_(524905, "temp", lambda: temp))
            _l_(524907)
        _c_(524911, _a_(524910, _n_(524909, "minelst", lambda: minelst), "sort"))
        _l_(524912)

        for mine in _n_(524913, "minelst", lambda: minelst):
            _l_(525531)

            if _n_(524914, "mine", lambda: mine)[0] == 0:
                _l_(525530)

                if _n_(524915, "mine", lambda: mine)[1] == 0:
                    _l_(525079)

                    if _a_(524918, _a_(524917, _n_(524916, "self", lambda: self), "cells")[0][1], "text") != 'X':
                        _l_(524929)

                        _a_(524920, _n_(524919, "self", lambda: self), "cells")[0][1].text = _c_(524927, _n_(524921, "str", lambda: str), _c_(524926, _n_(524922, "int", lambda: int), _a_(524925, _a_(524924, _n_(524923, "self", lambda: self), "cells")[0][1], "text")) + 1)
                        _l_(524928)
                    if _a_(524932, _a_(524931, _n_(524930, "self", lambda: self), "cells")[1][0], "text") != 'X':
                        _l_(524943)

                        _a_(524934, _n_(524933, "self", lambda: self), "cells")[1][0].text = _c_(524941, _n_(524935, "str", lambda: str), _c_(524940, _n_(524936, "int", lambda: int), _a_(524939, _a_(524938, _n_(524937, "self", lambda: self), "cells")[1][0], "text")) + 1)
                        _l_(524942)
                    if _a_(524946, _a_(524945, _n_(524944, "self", lambda: self), "cells")[1][1], "text") != 'X':
                        _l_(524957)

                        _a_(524948, _n_(524947, "self", lambda: self), "cells")[1][1].text = _c_(524955, _n_(524949, "str", lambda: str), _c_(524954, _n_(524950, "int", lambda: int), _a_(524953, _a_(524952, _n_(524951, "self", lambda: self), "cells")[1][1], "text")) + 1)
                        _l_(524956)
                elif _n_(524958, "mine", lambda: mine)[1] == (_a_(524960, _n_(524959, "self", lambda: self), "cols") -1):
                    _l_(525078)

                    if _a_(524965, _a_(524962, _n_(524961, "self", lambda: self), "cells")[0][_a_(524964, _n_(524963, "self", lambda: self), "cols") -2], "text") != 'X':
                        _l_(524980)

                        _a_(524967, _n_(524966, "self", lambda: self), "cells")[0][_a_(524969, _n_(524968, "self", lambda: self), "cols") -2].text = _c_(524978, _n_(524970, "str", lambda: str), _c_(524977, _n_(524971, "int", lambda: int), _a_(524976, _a_(524973, _n_(524972, "self", lambda: self), "cells")[0][_a_(524975, _n_(524974, "self", lambda: self), "cols") -2], "text")) + 1)
                        _l_(524979)
                    if _a_(524985, _a_(524982, _n_(524981, "self", lambda: self), "cells")[1][_a_(524984, _n_(524983, "self", lambda: self), "cols") -1], "text") != 'X':
                        _l_(525000)

                        _a_(524987, _n_(524986, "self", lambda: self), "cells")[1][_a_(524989, _n_(524988, "self", lambda: self), "cols") -1].text = _c_(524998, _n_(524990, "str", lambda: str), _c_(524997, _n_(524991, "int", lambda: int), _a_(524996, _a_(524993, _n_(524992, "self", lambda: self), "cells")[1][_a_(524995, _n_(524994, "self", lambda: self), "cols") -1], "text")) + 1)
                        _l_(524999)
                    if _a_(525005, _a_(525002, _n_(525001, "self", lambda: self), "cells")[1][_a_(525004, _n_(525003, "self", lambda: self), "cols") -2], "text") != 'X':
                        _l_(525020)

                        _a_(525007, _n_(525006, "self", lambda: self), "cells")[1][_a_(525009, _n_(525008, "self", lambda: self), "cols") -2].text = _c_(525018, _n_(525010, "str", lambda: str), _c_(525017, _n_(525011, "int", lambda: int), _a_(525016, _a_(525013, _n_(525012, "self", lambda: self), "cells")[1][_a_(525015, _n_(525014, "self", lambda: self), "cols") -2], "text")) + 1)
                        _l_(525019)
                else:
                    if _a_(525024, _a_(525022, _n_(525021, "self", lambda: self), "cells")[0][_n_(525023, "mine", lambda: mine)[1]-1], "text") != 'X':
                        _l_(525037)

                        _a_(525026, _n_(525025, "self", lambda: self), "cells")[0][_n_(525027, "mine", lambda: mine)[1]-1].text = _c_(525035, _n_(525028, "str", lambda: str), _c_(525034, _n_(525029, "int", lambda: int), _a_(525033, _a_(525031, _n_(525030, "self", lambda: self), "cells")[0][_n_(525032, "mine", lambda: mine)[1]-1], "text")) + 1)
                        _l_(525036)
                    if _a_(525041, _a_(525039, _n_(525038, "self", lambda: self), "cells")[0][_n_(525040, "mine", lambda: mine)[1]+1], "text") != 'X':
                        _l_(525054)

                        _a_(525043, _n_(525042, "self", lambda: self), "cells")[0][_n_(525044, "mine", lambda: mine)[1]+1].text = _c_(525052, _n_(525045, "str", lambda: str), _c_(525051, _n_(525046, "int", lambda: int), _a_(525050, _a_(525048, _n_(525047, "self", lambda: self), "cells")[0][_n_(525049, "mine", lambda: mine)[1]+1], "text")) + 1)
                        _l_(525053)
                    for i in _c_(525056, _n_(525055, "range", lambda: range), 3):
                        _l_(525077)

                        if _a_(525061, _a_(525058, _n_(525057, "self", lambda: self), "cells")[1][(_n_(525059, "mine", lambda: mine)[1]-1)+_n_(525060, "i", lambda: i)], "text") != 'X':
                            _l_(525076)

                            _a_(525063, _n_(525062, "self", lambda: self), "cells")[1][(_n_(525064, "mine", lambda: mine)[1]-1)+_n_(525065, "i", lambda: i)].text = _c_(525074, _n_(525066, "str", lambda: str), _c_(525073, _n_(525067, "int", lambda: int), _a_(525072, _a_(525069, _n_(525068, "self", lambda: self), "cells")[1][(_n_(525070, "mine", lambda: mine)[1]-1)+_n_(525071, "i", lambda: i)], "text")) + 1)
                            _l_(525075)
            elif _n_(525080, "mine", lambda: mine)[0] == (_a_(525082, _n_(525081, "self", lambda: self), "rows") -1):
                _l_(525529)

                if _n_(525083, "mine", lambda: mine)[1] == 0:
                    _l_(525301)

                    if _a_(525088, _a_(525085, _n_(525084, "self", lambda: self), "cells")[_a_(525087, _n_(525086, "self", lambda: self), "rows") -1][1], "text") != 'X':
                        _l_(525103)

                        _a_(525090, _n_(525089, "self", lambda: self), "cells")[_a_(525092, _n_(525091, "self", lambda: self), "rows") -1][1].text = _c_(525101, _n_(525093, "str", lambda: str), _c_(525100, _n_(525094, "int", lambda: int), _a_(525099, _a_(525096, _n_(525095, "self", lambda: self), "cells")[_a_(525098, _n_(525097, "self", lambda: self), "rows") -1][1], "text")) + 1)
                        _l_(525102)
                    if _a_(525108, _a_(525105, _n_(525104, "self", lambda: self), "cells")[_a_(525107, _n_(525106, "self", lambda: self), "rows") -2][0], "text") != 'X':
                        _l_(525123)

                        _a_(525110, _n_(525109, "self", lambda: self), "cells")[_a_(525112, _n_(525111, "self", lambda: self), "rows") -2][0].text = _c_(525121, _n_(525113, "str", lambda: str), _c_(525120, _n_(525114, "int", lambda: int), _a_(525119, _a_(525116, _n_(525115, "self", lambda: self), "cells")[_a_(525118, _n_(525117, "self", lambda: self), "rows") -2][0], "text")) + 1)
                        _l_(525122)
                    if _a_(525128, _a_(525125, _n_(525124, "self", lambda: self), "cells")[_a_(525127, _n_(525126, "self", lambda: self), "rows") -2][1], "text") != 'X':
                        _l_(525143)

                        _a_(525130, _n_(525129, "self", lambda: self), "cells")[_a_(525132, _n_(525131, "self", lambda: self), "rows") -2][1].text = _c_(525141, _n_(525133, "str", lambda: str), _c_(525140, _n_(525134, "int", lambda: int), _a_(525139, _a_(525136, _n_(525135, "self", lambda: self), "cells")[_a_(525138, _n_(525137, "self", lambda: self), "rows") -2][1], "text")) + 1)
                        _l_(525142)
                elif _n_(525144, "mine", lambda: mine)[1] == (_a_(525146, _n_(525145, "self", lambda: self), "cols") -1):
                    _l_(525300)

                    if _a_(525153, _a_(525148, _n_(525147, "self", lambda: self), "cells")[_a_(525150, _n_(525149, "self", lambda: self), "rows") -1][_a_(525152, _n_(525151, "self", lambda: self), "cols") -2], "text") != 'X':
                        _l_(525172)

                        _a_(525155, _n_(525154, "self", lambda: self), "cells")[_a_(525157, _n_(525156, "self", lambda: self), "rows") -1][_a_(525159, _n_(525158, "self", lambda: self), "cols") -2].text = _c_(525170, _n_(525160, "str", lambda: str), _c_(525169, _n_(525161, "int", lambda: int), _a_(525168, _a_(525163, _n_(525162, "self", lambda: self), "cells")[_a_(525165, _n_(525164, "self", lambda: self), "rows") -1][_a_(525167, _n_(525166, "self", lambda: self), "cols") -2], "text")) + 1)
                        _l_(525171)
                    if _a_(525179, _a_(525174, _n_(525173, "self", lambda: self), "cells")[_a_(525176, _n_(525175, "self", lambda: self), "rows") -2][_a_(525178, _n_(525177, "self", lambda: self), "cols") -1], "text") != 'X':
                        _l_(525198)

                        _a_(525181, _n_(525180, "self", lambda: self), "cells")[_a_(525183, _n_(525182, "self", lambda: self), "rows") -2][_a_(525185, _n_(525184, "self", lambda: self), "cols") -1].text = _c_(525196, _n_(525186, "str", lambda: str), _c_(525195, _n_(525187, "int", lambda: int), _a_(525194, _a_(525189, _n_(525188, "self", lambda: self), "cells")[_a_(525191, _n_(525190, "self", lambda: self), "rows") -2][_a_(525193, _n_(525192, "self", lambda: self), "cols") -1], "text")) + 1)
                        _l_(525197)
                    if _a_(525205, _a_(525200, _n_(525199, "self", lambda: self), "cells")[_a_(525202, _n_(525201, "self", lambda: self), "rows") -2][_a_(525204, _n_(525203, "self", lambda: self), "cols") -2], "text") != 'X':
                        _l_(525224)

                        _a_(525207, _n_(525206, "self", lambda: self), "cells")[_a_(525209, _n_(525208, "self", lambda: self), "rows") -2][_a_(525211, _n_(525210, "self", lambda: self), "cols") -2].text = _c_(525222, _n_(525212, "str", lambda: str), _c_(525221, _n_(525213, "int", lambda: int), _a_(525220, _a_(525215, _n_(525214, "self", lambda: self), "cells")[_a_(525217, _n_(525216, "self", lambda: self), "rows") -2][_a_(525219, _n_(525218, "self", lambda: self), "cols") -2], "text")) + 1)
                        _l_(525223)
                else:
                    if _a_(525230, _a_(525226, _n_(525225, "self", lambda: self), "cells")[_a_(525228, _n_(525227, "self", lambda: self), "rows") -1][_n_(525229, "mine", lambda: mine)[1]-1], "text") != 'X':
                        _l_(525247)

                        _a_(525232, _n_(525231, "self", lambda: self), "cells")[_a_(525234, _n_(525233, "self", lambda: self), "rows") -1][_n_(525235, "mine", lambda: mine)[1]-1].text = _c_(525245, _n_(525236, "str", lambda: str), _c_(525244, _n_(525237, "int", lambda: int), _a_(525243, _a_(525239, _n_(525238, "self", lambda: self), "cells")[_a_(525241, _n_(525240, "self", lambda: self), "rows") -1][_n_(525242, "mine", lambda: mine)[1]-1], "text")) + 1)
                        _l_(525246)
                    if _a_(525253, _a_(525249, _n_(525248, "self", lambda: self), "cells")[_a_(525251, _n_(525250, "self", lambda: self), "rows") -1][_n_(525252, "mine", lambda: mine)[1]+1], "text") != 'X':
                        _l_(525270)

                        _a_(525255, _n_(525254, "self", lambda: self), "cells")[_a_(525257, _n_(525256, "self", lambda: self), "rows") -1][_n_(525258, "mine", lambda: mine)[1]+1].text = _c_(525268, _n_(525259, "str", lambda: str), _c_(525267, _n_(525260, "int", lambda: int), _a_(525266, _a_(525262, _n_(525261, "self", lambda: self), "cells")[_a_(525264, _n_(525263, "self", lambda: self), "rows") -1][_n_(525265, "mine", lambda: mine)[1]+1], "text")) + 1)
                        _l_(525269)
                    for i in _c_(525272, _n_(525271, "range", lambda: range), 3):
                        _l_(525299)

                        if _a_(525279, _a_(525274, _n_(525273, "self", lambda: self), "cells")[_a_(525276, _n_(525275, "self", lambda: self), "rows") -2][(_n_(525277, "mine", lambda: mine)[1]-1)+_n_(525278, "i", lambda: i)], "text") != 'X':
                            _l_(525298)

                            _a_(525281, _n_(525280, "self", lambda: self), "cells")[_a_(525283, _n_(525282, "self", lambda: self), "rows") -2][(_n_(525284, "mine", lambda: mine)[1]-1)+_n_(525285, "i", lambda: i)].text = _c_(525296, _n_(525286, "str", lambda: str), _c_(525295, _n_(525287, "int", lambda: int), _a_(525294, _a_(525289, _n_(525288, "self", lambda: self), "cells")[_a_(525291, _n_(525290, "self", lambda: self), "rows") -2][(_n_(525292, "mine", lambda: mine)[1]-1)+_n_(525293, "i", lambda: i)], "text")) + 1)
                            _l_(525297)
            elif _n_(525302, "mine", lambda: mine)[1] == 0:
                _l_(525528)

                if _a_(525306, _a_(525304, _n_(525303, "self", lambda: self), "cells")[_n_(525305, "mine", lambda: mine)[0]-1][0], "text") != 'X':
                    _l_(525319)

                    _a_(525308, _n_(525307, "self", lambda: self), "cells")[_n_(525309, "mine", lambda: mine)[0]-1][0].text = _c_(525317, _n_(525310, "str", lambda: str), _c_(525316, _n_(525311, "int", lambda: int), _a_(525315, _a_(525313, _n_(525312, "self", lambda: self), "cells")[_n_(525314, "mine", lambda: mine)[0]-1][0], "text")) + 1)
                    _l_(525318)
                if _a_(525323, _a_(525321, _n_(525320, "self", lambda: self), "cells")[_n_(525322, "mine", lambda: mine)[0]+1][0], "text") != 'X':
                    _l_(525336)

                    _a_(525325, _n_(525324, "self", lambda: self), "cells")[_n_(525326, "mine", lambda: mine)[0]+1][0].text = _c_(525334, _n_(525327, "str", lambda: str), _c_(525333, _n_(525328, "int", lambda: int), _a_(525332, _a_(525330, _n_(525329, "self", lambda: self), "cells")[_n_(525331, "mine", lambda: mine)[0]+1][0], "text")) + 1)
                    _l_(525335)
                for i in _c_(525338, _n_(525337, "range", lambda: range), 3):
                    _l_(525359)

                    if _a_(525343, _a_(525340, _n_(525339, "self", lambda: self), "cells")[(_n_(525341, "mine", lambda: mine)[0]-1)+_n_(525342, "i", lambda: i)][1], "text") != 'X':
                        _l_(525358)

                        _a_(525345, _n_(525344, "self", lambda: self), "cells")[(_n_(525346, "mine", lambda: mine)[0]-1)+_n_(525347, "i", lambda: i)][1].text = _c_(525356, _n_(525348, "str", lambda: str), _c_(525355, _n_(525349, "int", lambda: int), _a_(525354, _a_(525351, _n_(525350, "self", lambda: self), "cells")[(_n_(525352, "mine", lambda: mine)[0]-1)+_n_(525353, "i", lambda: i)][1], "text"))+1)
                        _l_(525357)
            elif _n_(525360, "mine", lambda: mine)[1] == (_a_(525362, _n_(525361, "self", lambda: self), "cols") -1):
                _l_(525527)

                if _a_(525368, _a_(525364, _n_(525363, "self", lambda: self), "cells")[_n_(525365, "mine", lambda: mine)[0]-1][_a_(525367, _n_(525366, "self", lambda: self), "cols") -1], "text") != 'X':
                    _l_(525385)

                    _a_(525370, _n_(525369, "self", lambda: self), "cells")[_n_(525371, "mine", lambda: mine)[0]-1][_a_(525373, _n_(525372, "self", lambda: self), "cols") -1].text = _c_(525383, _n_(525374, "str", lambda: str), _c_(525382, _n_(525375, "int", lambda: int), _a_(525381, _a_(525377, _n_(525376, "self", lambda: self), "cells")[_n_(525378, "mine", lambda: mine)[0]-1][_a_(525380, _n_(525379, "self", lambda: self), "cols") -1], "text")) + 1)
                    _l_(525384)
                if _a_(525391, _a_(525387, _n_(525386, "self", lambda: self), "cells")[_n_(525388, "mine", lambda: mine)[0]+1][_a_(525390, _n_(525389, "self", lambda: self), "cols") -1], "text") != 'X':
                    _l_(525408)

                    _a_(525393, _n_(525392, "self", lambda: self), "cells")[_n_(525394, "mine", lambda: mine)[0]+1][_a_(525396, _n_(525395, "self", lambda: self), "cols") -1].text = _c_(525406, _n_(525397, "str", lambda: str), _c_(525405, _n_(525398, "int", lambda: int), _a_(525404, _a_(525400, _n_(525399, "self", lambda: self), "cells")[_n_(525401, "mine", lambda: mine)[0]+1][_a_(525403, _n_(525402, "self", lambda: self), "cols") -1], "text")) + 1)
                    _l_(525407)
                for i in _c_(525410, _n_(525409, "range", lambda: range), 3):
                    _l_(525437)

                    if _a_(525417, _a_(525412, _n_(525411, "self", lambda: self), "cells")[(_n_(525413, "mine", lambda: mine)[0]-1)+_n_(525414, "i", lambda: i)][_a_(525416, _n_(525415, "self", lambda: self), "cols") -2], "text") != 'X':
                        _l_(525436)

                        _a_(525419, _n_(525418, "self", lambda: self), "cells")[(_n_(525420, "mine", lambda: mine)[0]-1)+_n_(525421, "i", lambda: i)][_a_(525423, _n_(525422, "self", lambda: self), "cols") -2].text = _c_(525434, _n_(525424, "str", lambda: str), _c_(525433, _n_(525425, "int", lambda: int), _a_(525432, _a_(525427, _n_(525426, "self", lambda: self), "cells")[(_n_(525428, "mine", lambda: mine)[0]-1)+_n_(525429, "i", lambda: i)][_a_(525431, _n_(525430, "self", lambda: self), "cols") -2], "text"))+1)
                        _l_(525435)
            else: # interior mines
                for i in _c_(525439, _n_(525438, "range", lambda: range), 3):
                    _l_(525486)

                    if _a_(525445, _a_(525441, _n_(525440, "self", lambda: self), "cells")[_n_(525442, "mine", lambda: mine)[0]-1][(_n_(525443, "mine", lambda: mine)[1]-1)+_n_(525444, "i", lambda: i)], "text") != 'X':
                        _l_(525462)

                        _a_(525447, _n_(525446, "self", lambda: self), "cells")[_n_(525448, "mine", lambda: mine)[0]-1][(_n_(525449, "mine", lambda: mine)[1]-1)+_n_(525450, "i", lambda: i)].text = _c_(525460, _n_(525451, "str", lambda: str), _c_(525459, _n_(525452, "int", lambda: int), _a_(525458, _a_(525454, _n_(525453, "self", lambda: self), "cells")[_n_(525455, "mine", lambda: mine)[0]-1][(_n_(525456, "mine", lambda: mine)[1]-1)+_n_(525457, "i", lambda: i)], "text"))+1)
                        _l_(525461)
                    if _a_(525468, _a_(525464, _n_(525463, "self", lambda: self), "cells")[_n_(525465, "mine", lambda: mine)[0]+1][(_n_(525466, "mine", lambda: mine)[1]-1)+_n_(525467, "i", lambda: i)], "text") != 'X':
                        _l_(525485)

                        _a_(525470, _n_(525469, "self", lambda: self), "cells")[_n_(525471, "mine", lambda: mine)[0]+1][(_n_(525472, "mine", lambda: mine)[1]-1)+_n_(525473, "i", lambda: i)].text = _c_(525483, _n_(525474, "str", lambda: str), _c_(525482, _n_(525475, "int", lambda: int), _a_(525481, _a_(525477, _n_(525476, "self", lambda: self), "cells")[_n_(525478, "mine", lambda: mine)[0]+1][(_n_(525479, "mine", lambda: mine)[1]-1)+_n_(525480, "i", lambda: i)], "text"))+1)
                        _l_(525484)
                if _a_(525491, _a_(525488, _n_(525487, "self", lambda: self), "cells")[_n_(525489, "mine", lambda: mine)[0]][_n_(525490, "mine", lambda: mine)[1]-1], "text") != 'X':
                    _l_(525506)

                    _a_(525493, _n_(525492, "self", lambda: self), "cells")[_n_(525494, "mine", lambda: mine)[0]][_n_(525495, "mine", lambda: mine)[1]-1].text = _c_(525504, _n_(525496, "str", lambda: str), _c_(525503, _n_(525497, "int", lambda: int), _a_(525502, _a_(525499, _n_(525498, "self", lambda: self), "cells")[_n_(525500, "mine", lambda: mine)[0]][_n_(525501, "mine", lambda: mine)[1]-1], "text"))+1)
                    _l_(525505)
                if _a_(525511, _a_(525508, _n_(525507, "self", lambda: self), "cells")[_n_(525509, "mine", lambda: mine)[0]][_n_(525510, "mine", lambda: mine)[1]+1], "text") != 'X':
                    _l_(525526)

                    _a_(525513, _n_(525512, "self", lambda: self), "cells")[_n_(525514, "mine", lambda: mine)[0]][_n_(525515, "mine", lambda: mine)[1]+1].text = _c_(525524, _n_(525516, "str", lambda: str), _c_(525523, _n_(525517, "int", lambda: int), _a_(525522, _a_(525519, _n_(525518, "self", lambda: self), "cells")[_n_(525520, "mine", lambda: mine)[0]][_n_(525521, "mine", lambda: mine)[1]+1], "text"))+1)
                    _l_(525525)

        for i in _c_(525535, _n_(525532, "range", lambda: range), _a_(525534, _n_(525533, "self", lambda: self), "rows")):
            _l_(525556)

            for j in _c_(525539, _n_(525536, "range", lambda: range), _a_(525538, _n_(525537, "self", lambda: self), "cols")):
                _l_(525555)

                _a_(525541, _n_(525540, "self", lambda: self), "cells")[_n_(525542, "i", lambda: i)][_n_(525543, "j", lambda: j)].val = _a_(525548, _a_(525545, _n_(525544, "self", lambda: self), "cells")[_n_(525546, "i", lambda: i)][_n_(525547, "j", lambda: j)], "text")
                _l_(525549)
                _a_(525551, _n_(525550, "self", lambda: self), "cells")[_n_(525552, "i", lambda: i)][_n_(525553, "j", lambda: j)].text = '?'
                _l_(525554)

class MineSweeper(_n_(525559, "App", lambda: App)):
    _l_(525568)

    def build(self):
        _l_(525567)

        _n_(525560, "self", lambda: self).root = _c_(525562, _n_(525561, "GameBoard", lambda: GameBoard))
        _l_(525563)
        aux = _a_(525565, _n_(525564, "self", lambda: self), "root")
        _l_(525566)
        return aux

mineSweeper = _c_(525570, _n_(525569, "MineSweeper", lambda: MineSweeper))
_l_(525571)

_c_(525574, _a_(525573, _n_(525572, "mineSweeper", lambda: mineSweeper), "run"))
_l_(525575)