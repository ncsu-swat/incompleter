# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69669751/typeerror-bool-object-is-not-subscriptable-with-while-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ITI1=3
_l_(592452)
ITI2=5
_l_(592453)
ITI3=7
_l_(592454)
ItiDurations = _c_(592460, _n_(592455, "list", lambda: list), _c_(592459, _a_(592457, _n_(592456, "itertools", lambda: itertools), "repeat"), _n_(592458, "ITI1", lambda: ITI1), 6))+_c_(592466, _n_(592461, "list", lambda: list), _c_(592465, _a_(592463, _n_(592462, "itertools", lambda: itertools), "repeat"), _n_(592464, "ITI2", lambda: ITI2),4))+_c_(592472, _n_(592467, "list", lambda: list), _c_(592471, _a_(592469, _n_(592468, "itertools", lambda: itertools), "repeat"), _n_(592470, "ITI3", lambda: ITI3),2))
_l_(592473)
def duplicate(testlist, n):
    _l_(592477)

    aux = _n_(592474, "testlist", lambda: testlist)*_n_(592475, "n", lambda: n)
    _l_(592476)
    return aux
ValCong=['pos', 'neg']
_l_(592478)
StimValCong = _c_(592481, _n_(592479, "duplicate", lambda: duplicate), _n_(592480, "ValCong", lambda: ValCong),6)
_l_(592482)
ActCong=['go', 'nogo']
_l_(592483)
ActionCong = _c_(592486, _n_(592484, "duplicate", lambda: duplicate), _n_(592485, "ActCong", lambda: ActCong),6)
_l_(592487)
# Congruency list (cong=0, incong=1)
Cong = _c_(592489, _n_(592488, "duplicate", lambda: duplicate), [0],12)
_l_(592490)
Conblock_1 = _c_(592501, _a_(592492, _n_(592491, "pd", lambda: pd), "DataFrame"), _c_(592500, _n_(592493, "list", lambda: list), _c_(592499, _n_(592494, "zip", lambda: zip), _n_(592495, "ItiDurations", lambda: ItiDurations),_n_(592496, "StimValCong", lambda: StimValCong),_n_(592497, "ActionCong", lambda: ActionCong),_n_(592498, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(592502)
Conblock_2 = _c_(592513, _a_(592504, _n_(592503, "pd", lambda: pd), "DataFrame"), _c_(592512, _n_(592505, "list", lambda: list), _c_(592511, _n_(592506, "zip", lambda: zip), _n_(592507, "ItiDurations", lambda: ItiDurations),_n_(592508, "StimValCong", lambda: StimValCong),_n_(592509, "ActionCong", lambda: ActionCong),_n_(592510, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(592514)
Conblock_3 = _c_(592525, _a_(592516, _n_(592515, "pd", lambda: pd), "DataFrame"), _c_(592524, _n_(592517, "list", lambda: list), _c_(592523, _n_(592518, "zip", lambda: zip), _n_(592519, "ItiDurations", lambda: ItiDurations),_n_(592520, "StimValCong", lambda: StimValCong),_n_(592521, "ActionCong", lambda: ActionCong),_n_(592522, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(592526)
Conblock_4 = _c_(592537, _a_(592528, _n_(592527, "pd", lambda: pd), "DataFrame"), _c_(592536, _n_(592529, "list", lambda: list), _c_(592535, _n_(592530, "zip", lambda: zip), _n_(592531, "ItiDurations", lambda: ItiDurations),_n_(592532, "StimValCong", lambda: StimValCong),_n_(592533, "ActionCong", lambda: ActionCong),_n_(592534, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(592538)
Conblock_5 = _c_(592549, _a_(592540, _n_(592539, "pd", lambda: pd), "DataFrame"), _c_(592548, _n_(592541, "list", lambda: list), _c_(592547, _n_(592542, "zip", lambda: zip), _n_(592543, "ItiDurations", lambda: ItiDurations),_n_(592544, "StimValCong", lambda: StimValCong),_n_(592545, "ActionCong", lambda: ActionCong),_n_(592546, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(592550)
Conblock_6 = _c_(592561, _a_(592552, _n_(592551, "pd", lambda: pd), "DataFrame"), _c_(592560, _n_(592553, "list", lambda: list), _c_(592559, _n_(592554, "zip", lambda: zip), _n_(592555, "ItiDurations", lambda: ItiDurations),_n_(592556, "StimValCong", lambda: StimValCong),_n_(592557, "ActionCong", lambda: ActionCong),_n_(592558, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(592562)
Conblock_7 = _c_(592573, _a_(592564, _n_(592563, "pd", lambda: pd), "DataFrame"), _c_(592572, _n_(592565, "list", lambda: list), _c_(592571, _n_(592566, "zip", lambda: zip), _n_(592567, "ItiDurations", lambda: ItiDurations),_n_(592568, "StimValCong", lambda: StimValCong),_n_(592569, "ActionCong", lambda: ActionCong),_n_(592570, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(592574)
Conblock_8 = _c_(592585, _a_(592576, _n_(592575, "pd", lambda: pd), "DataFrame"), _c_(592584, _n_(592577, "list", lambda: list), _c_(592583, _n_(592578, "zip", lambda: zip), _n_(592579, "ItiDurations", lambda: ItiDurations),_n_(592580, "StimValCong", lambda: StimValCong),_n_(592581, "ActionCong", lambda: ActionCong),_n_(592582, "Cong", lambda: Cong))),columns=['ITI','StimVal', 'Action', 'Congruency'])
_l_(592586)
dictCon={1:_n_(592587, "Conblock_1", lambda: Conblock_1), 2:_n_(592588, "Conblock_2", lambda: Conblock_2), 3:_n_(592589, "Conblock_3", lambda: Conblock_3), 4:_n_(592590, "Conblock_4", lambda: Conblock_4), 5:_n_(592591, "Conblock_5", lambda: Conblock_5), 6:_n_(592592, "Conblock_6", lambda: Conblock_6), 7:_n_(592593, "Conblock_7", lambda: Conblock_7), 8:_n_(592594, "Conblock_8", lambda: Conblock_8)}
_l_(592595)