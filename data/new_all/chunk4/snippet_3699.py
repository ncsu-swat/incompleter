# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69669751/typeerror-bool-object-is-not-subscriptable-with-while-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ITI1=3
_l_(597738)
ITI2=5
_l_(597739)
ITI3=7
_l_(597740)
ItiDurations = _c_(597746, _n_(597741, "list", lambda: list), _c_(597745, _a_(597743, _n_(597742, "itertools", lambda: itertools), "repeat"), _n_(597744, "ITI1", lambda: ITI1), 6))+_c_(597752, _n_(597747, "list", lambda: list), _c_(597751, _a_(597749, _n_(597748, "itertools", lambda: itertools), "repeat"), _n_(597750, "ITI2", lambda: ITI2),4))+_c_(597758, _n_(597753, "list", lambda: list), _c_(597757, _a_(597755, _n_(597754, "itertools", lambda: itertools), "repeat"), _n_(597756, "ITI3", lambda: ITI3),2))
_l_(597759)
def duplicate(testlist, n):
    _l_(597763)

    aux = _n_(597760, "testlist", lambda: testlist)*_n_(597761, "n", lambda: n)
    _l_(597762)
    return aux
ValCong=['pos', 'neg']
_l_(597764)
StimValCong = _c_(597767, _n_(597765, "duplicate", lambda: duplicate), _n_(597766, "ValCong", lambda: ValCong),6)
_l_(597768)
ActCong=['go', 'nogo']
_l_(597769)
ActionCong = _c_(597772, _n_(597770, "duplicate", lambda: duplicate), _n_(597771, "ActCong", lambda: ActCong),6)
_l_(597773)
# Congruency list (cong=0, incong=1)
Cong = _c_(597775, _n_(597774, "duplicate", lambda: duplicate), [0],12)
_l_(597776)
Conblock_1 = _c_(597787, _a_(597778, _n_(597777, "pd", lambda: pd), "DataFrame"), _c_(597786, _n_(597779, "list", lambda: list), _c_(597785, _n_(597780, "zip", lambda: zip), _n_(597781, "ItiDurations", lambda: ItiDurations),_n_(597782, "StimValCong", lambda: StimValCong),_n_(597783, "ActionCong", lambda: ActionCong),_n_(597784, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(597788)
Conblock_2 = _c_(597799, _a_(597790, _n_(597789, "pd", lambda: pd), "DataFrame"), _c_(597798, _n_(597791, "list", lambda: list), _c_(597797, _n_(597792, "zip", lambda: zip), _n_(597793, "ItiDurations", lambda: ItiDurations),_n_(597794, "StimValCong", lambda: StimValCong),_n_(597795, "ActionCong", lambda: ActionCong),_n_(597796, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(597800)
Conblock_3 = _c_(597811, _a_(597802, _n_(597801, "pd", lambda: pd), "DataFrame"), _c_(597810, _n_(597803, "list", lambda: list), _c_(597809, _n_(597804, "zip", lambda: zip), _n_(597805, "ItiDurations", lambda: ItiDurations),_n_(597806, "StimValCong", lambda: StimValCong),_n_(597807, "ActionCong", lambda: ActionCong),_n_(597808, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(597812)
Conblock_4 = _c_(597823, _a_(597814, _n_(597813, "pd", lambda: pd), "DataFrame"), _c_(597822, _n_(597815, "list", lambda: list), _c_(597821, _n_(597816, "zip", lambda: zip), _n_(597817, "ItiDurations", lambda: ItiDurations),_n_(597818, "StimValCong", lambda: StimValCong),_n_(597819, "ActionCong", lambda: ActionCong),_n_(597820, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(597824)
Conblock_5 = _c_(597835, _a_(597826, _n_(597825, "pd", lambda: pd), "DataFrame"), _c_(597834, _n_(597827, "list", lambda: list), _c_(597833, _n_(597828, "zip", lambda: zip), _n_(597829, "ItiDurations", lambda: ItiDurations),_n_(597830, "StimValCong", lambda: StimValCong),_n_(597831, "ActionCong", lambda: ActionCong),_n_(597832, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(597836)
Conblock_6 = _c_(597847, _a_(597838, _n_(597837, "pd", lambda: pd), "DataFrame"), _c_(597846, _n_(597839, "list", lambda: list), _c_(597845, _n_(597840, "zip", lambda: zip), _n_(597841, "ItiDurations", lambda: ItiDurations),_n_(597842, "StimValCong", lambda: StimValCong),_n_(597843, "ActionCong", lambda: ActionCong),_n_(597844, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(597848)
Conblock_7 = _c_(597859, _a_(597850, _n_(597849, "pd", lambda: pd), "DataFrame"), _c_(597858, _n_(597851, "list", lambda: list), _c_(597857, _n_(597852, "zip", lambda: zip), _n_(597853, "ItiDurations", lambda: ItiDurations),_n_(597854, "StimValCong", lambda: StimValCong),_n_(597855, "ActionCong", lambda: ActionCong),_n_(597856, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(597860)
Conblock_8 = _c_(597871, _a_(597862, _n_(597861, "pd", lambda: pd), "DataFrame"), _c_(597870, _n_(597863, "list", lambda: list), _c_(597869, _n_(597864, "zip", lambda: zip), _n_(597865, "ItiDurations", lambda: ItiDurations),_n_(597866, "StimValCong", lambda: StimValCong),_n_(597867, "ActionCong", lambda: ActionCong),_n_(597868, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(597872)
dictCon={1:_n_(597873, "Conblock_1", lambda: Conblock_1), 2:_n_(597874, "Conblock_2", lambda: Conblock_2), 3:_n_(597875, "Conblock_3", lambda: Conblock_3), 4:_n_(597876, "Conblock_4", lambda: Conblock_4), 5:_n_(597877, "Conblock_5", lambda: Conblock_5), 6:_n_(597878, "Conblock_6", lambda: Conblock_6), 7:_n_(597879, "Conblock_7", lambda: Conblock_7), 8:_n_(597880, "Conblock_8", lambda: Conblock_8)}
_l_(597881)