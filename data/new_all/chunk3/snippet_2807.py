# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62538951/nameerror-name-jam-is-not-defined
# Initialize variables
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cnt_row = -1
_l_(542246)
cnt_col = 0
_l_(542247)
cnt_zero = 0
_l_(542248)

# Grab all relevant MIDI data (available in MIDI_dat)
for i in _c_(542253, _n_(542249, "range", lambda: range), 0, _c_(542252, _n_(542250, "len", lambda: len), _n_(542251, "jam", lambda: jam)['annotations'])):
    _l_(542369)

    if _n_(542254, "jam", lambda: jam)['annotations'][_c_(542257, _n_(542255, "int", lambda: int), _n_(542256, "i", lambda: i))]['namespace'] == 'note_midi':
        _l_(542368)

        for j in _c_(542267, _n_(542258, "range", lambda: range), 0, _c_(542266, _n_(542259, "len", lambda: len), _c_(542265, _n_(542260, "sorted", lambda: sorted), _n_(542261, "jam", lambda: jam)['annotations'][_c_(542264, _n_(542262, "int", lambda: int), _n_(542263, "i", lambda: i))]['data']))):
            _l_(542367)

            cnt_row = _n_(542268, "cnt_row", lambda: cnt_row) + 1
            _l_(542269)
            for k in _c_(542282, _n_(542270, "range", lambda: range), 0, _c_(542281, _n_(542271, "len", lambda: len), _c_(542277, _n_(542272, "sorted", lambda: sorted), _n_(542273, "jam", lambda: jam)['annotations'][_c_(542276, _n_(542274, "int", lambda: int), _n_(542275, "i", lambda: i))]['data'])[_c_(542280, _n_(542278, "int", lambda: int), _n_(542279, "j", lambda: j))]) - 1):
                _l_(542366)

                if _n_(542283, "cnt_zero", lambda: cnt_zero) == 0:
                    _l_(542311)

                    MIDI_arr = _c_(542307, _a_(542285, _n_(542284, "np", lambda: np), "zeros"), (_c_(542293, _n_(542286, "len", lambda: len), _c_(542292, _n_(542287, "sorted", lambda: sorted), _n_(542288, "jam", lambda: jam)['annotations'][_c_(542291, _n_(542289, "int", lambda: int), _n_(542290, "i", lambda: i))]['data'])), _c_(542304, _n_(542294, "len", lambda: len), _c_(542300, _n_(542295, "sorted", lambda: sorted), _n_(542296, "jam", lambda: jam)['annotations'][_c_(542299, _n_(542297, "int", lambda: int), _n_(542298, "i", lambda: i))]['data'])[_c_(542303, _n_(542301, "int", lambda: int), _n_(542302, "j", lambda: j))]) - 1), dtype = _a_(542306, _n_(542305, "np", lambda: np), "float32"))
                    _l_(542308)
                    cnt_zero = _n_(542309, "cnt_zero", lambda: cnt_zero) + 1
                    _l_(542310)
                if _n_(542312, "cnt_zero", lambda: cnt_zero) > 0:
                    _l_(542344)

                    MIDI_arr = _c_(542340, _a_(542314, _n_(542313, "np", lambda: np), "vstack"), (_n_(542315, "MIDI_arr", lambda: MIDI_arr), _c_(542339, _a_(542317, _n_(542316, "np", lambda: np), "zeros"), (_c_(542325, _n_(542318, "len", lambda: len), _c_(542324, _n_(542319, "sorted", lambda: sorted), _n_(542320, "jam", lambda: jam)['annotations'][_c_(542323, _n_(542321, "int", lambda: int), _n_(542322, "i", lambda: i))]['data'])), _c_(542336, _n_(542326, "len", lambda: len), _c_(542332, _n_(542327, "sorted", lambda: sorted), _n_(542328, "jam", lambda: jam)['annotations'][_c_(542331, _n_(542329, "int", lambda: int), _n_(542330, "i", lambda: i))]['data'])[_c_(542335, _n_(542333, "int", lambda: int), _n_(542334, "j", lambda: j))]) - 1), dtype = _a_(542338, _n_(542337, "np", lambda: np), "float32"))))
                    _l_(542341)
                    cnt_zero = _n_(542342, "cnt_zero", lambda: cnt_zero) + 1  # Keep
                    _l_(542343)  # Keep
                if _n_(542345, "cnt_col", lambda: cnt_col) > 2:
                    _l_(542347)

                    cnt_col = 0
                    _l_(542346)
                _n_(542348, "MIDI_arr", lambda: MIDI_arr)[_n_(542349, "cnt_row", lambda: cnt_row), _n_(542350, "cnt_col", lambda: cnt_col)] = _c_(542356, _n_(542351, "sorted", lambda: sorted), _n_(542352, "jam", lambda: jam)['annotations'][_c_(542355, _n_(542353, "int", lambda: int), _n_(542354, "i", lambda: i))]['data'])[_c_(542359, _n_(542357, "int", lambda: int), _n_(542358, "j", lambda: j))][_c_(542362, _n_(542360, "int", lambda: int), _n_(542361, "k", lambda: k))]
                _l_(542363)
                cnt_col = _n_(542364, "cnt_col", lambda: cnt_col) + 1
                _l_(542365)
MIDI_dat = _c_(542376, _a_(542371, _n_(542370, "np", lambda: np), "zeros"), (_n_(542372, "cnt_row", lambda: cnt_row) + 1, _n_(542373, "cnt_col", lambda: cnt_col)), dtype = _a_(542375, _n_(542374, "np", lambda: np), "float32"))
_l_(542377)
cnt_col2 = 0
_l_(542378)
for n in _c_(542381, _n_(542379, "range", lambda: range), 0, _n_(542380, "cnt_row", lambda: cnt_row) + 1):
    _l_(542398)

    for m in _c_(542384, _n_(542382, "range", lambda: range), 0, _n_(542383, "cnt_col", lambda: cnt_col)):
        _l_(542397)

        if _n_(542385, "cnt_col2", lambda: cnt_col2) > 2:
            _l_(542387)

            cnt_col2 = 0
            _l_(542386)
        _n_(542388, "MIDI_dat", lambda: MIDI_dat)[_n_(542389, "n", lambda: n), _n_(542390, "cnt_col2", lambda: cnt_col2)] = _n_(542391, "MIDI_arr", lambda: MIDI_arr)[_n_(542392, "n", lambda: n), _n_(542393, "cnt_col2", lambda: cnt_col2)]
        _l_(542394)
        cnt_col2 = _n_(542395, "cnt_col2", lambda: cnt_col2) + 1
        _l_(542396)
 # Return the unique MIDI notes played (available in MIDI_val)
MIDI_dat_dur = _c_(542402, _a_(542400, _n_(542399, "np", lambda: np), "copy"), _n_(542401, "MIDI_dat", lambda: MIDI_dat))
_l_(542403)
for r in _c_(542408, _n_(542404, "range", lambda: range), 0, _c_(542407, _n_(542405, "len", lambda: len), _n_(542406, "MIDI_dat", lambda: MIDI_dat)[:, 0])):
    _l_(542416)

    _n_(542409, "MIDI_dat_dur", lambda: MIDI_dat_dur)[_n_(542410, "r", lambda: r), 0] = _n_(542411, "MIDI_dat", lambda: MIDI_dat)[_n_(542412, "r", lambda: r), 0] + _n_(542413, "MIDI_dat", lambda: MIDI_dat)[_n_(542414, "r", lambda: r), 1]
    _l_(542415)
tab_1, = _c_(542426, _a_(542418, _n_(542417, "np", lambda: np), "where"), _c_(542425, _a_(542420, _n_(542419, "np", lambda: np), "logical_and"), _n_(542421, "MIDI_dat", lambda: MIDI_dat)[:, 0] >= _n_(542422, "start", lambda: start), _n_(542423, "MIDI_dat", lambda: MIDI_dat)[:, 0] <= _n_(542424, "stop", lambda: stop)))
_l_(542427)
tab_2, = _c_(542437, _a_(542429, _n_(542428, "np", lambda: np), "where"), _c_(542436, _a_(542431, _n_(542430, "np", lambda: np), "logical_and"), _n_(542432, "MIDI_dat_dur", lambda: MIDI_dat_dur)[:, 0] >= _n_(542433, "start", lambda: start), _n_(542434, "MIDI_dat_dur", lambda: MIDI_dat_dur)[:, 0] <= _n_(542435, "stop", lambda: stop)))
_l_(542438)
tab_3, = _c_(542456, _a_(542440, _n_(542439, "np", lambda: np), "where"), _c_(542455, _a_(542442, _n_(542441, "np", lambda: np), "logical_and"), _c_(542449, _a_(542444, _n_(542443, "np", lambda: np), "logical_and"), _n_(542445, "MIDI_dat", lambda: MIDI_dat)[:, 0] < _n_(542446, "start", lambda: start), _n_(542447, "MIDI_dat_dur", lambda: MIDI_dat_dur)[:, 0] > _n_(542448, "stop", lambda: stop)), _n_(542450, "MIDI_dat", lambda: MIDI_dat)[:, 1] > _c_(542454, _n_(542451, "int", lambda: int), _n_(542452, "stop", lambda: stop)-_n_(542453, "start", lambda: start))))
_l_(542457)
if _a_(542459, _n_(542458, "tab_1", lambda: tab_1), "size") != 0 and _a_(542461, _n_(542460, "tab_2", lambda: tab_2), "size") == 0 and _a_(542463, _n_(542462, "tab_3", lambda: tab_3), "size") == 0:
    _l_(542466)

    tab_ind = _n_(542464, "tab_1", lambda: tab_1)
    _l_(542465)
if _a_(542468, _n_(542467, "tab_1", lambda: tab_1), "size") == 0 and _a_(542470, _n_(542469, "tab_2", lambda: tab_2), "size") != 0 and _a_(542472, _n_(542471, "tab_3", lambda: tab_3), "size") == 0:
    _l_(542475)

    tab_ind = _n_(542473, "tab_2", lambda: tab_2)
    _l_(542474)
if _a_(542477, _n_(542476, "tab_1", lambda: tab_1), "size") == 0 and _a_(542479, _n_(542478, "tab_2", lambda: tab_2), "size") == 0 and _a_(542481, _n_(542480, "tab_3", lambda: tab_3), "size") != 0:
    _l_(542484)

    tab_ind = _n_(542482, "tab_3", lambda: tab_3)
    _l_(542483)
if _a_(542486, _n_(542485, "tab_1", lambda: tab_1), "size") != 0 and _a_(542488, _n_(542487, "tab_2", lambda: tab_2), "size") != 0 and _a_(542490, _n_(542489, "tab_3", lambda: tab_3), "size") == 0:
    _l_(542497)

    tab_ind = _c_(542495, _a_(542492, _n_(542491, "np", lambda: np), "concatenate"), [_n_(542493, "tab_1", lambda: tab_1), _n_(542494, "tab_2", lambda: tab_2)])
    _l_(542496)
if _a_(542499, _n_(542498, "tab_1", lambda: tab_1), "size") != 0 and _a_(542501, _n_(542500, "tab_2", lambda: tab_2), "size") == 0 and _a_(542503, _n_(542502, "tab_3", lambda: tab_3), "size") != 0:
    _l_(542510)

    tab_ind = _c_(542508, _a_(542505, _n_(542504, "np", lambda: np), "concatenate"), [_n_(542506, "tab_1", lambda: tab_1), _n_(542507, "tab_3", lambda: tab_3)])
    _l_(542509)
if _a_(542512, _n_(542511, "tab_1", lambda: tab_1), "size") == 0 and _a_(542514, _n_(542513, "tab_2", lambda: tab_2), "size") != 0 and _a_(542516, _n_(542515, "tab_3", lambda: tab_3), "size") != 0:
    _l_(542523)

    tab_ind = _c_(542521, _a_(542518, _n_(542517, "np", lambda: np), "concatenate"), [_n_(542519, "tab_2", lambda: tab_2), _n_(542520, "tab_3", lambda: tab_3)])
    _l_(542522)
if _a_(542525, _n_(542524, "tab_1", lambda: tab_1), "size") != 0 and _a_(542527, _n_(542526, "tab_2", lambda: tab_2), "size") != 0 and _a_(542529, _n_(542528, "tab_3", lambda: tab_3), "size") != 0:
    _l_(542537)

    tab_ind = _c_(542535, _a_(542531, _n_(542530, "np", lambda: np), "concatenate"), [_n_(542532, "tab_1", lambda: tab_1), _n_(542533, "tab_2", lambda: tab_2), _n_(542534, "tab_3", lambda: tab_3)])
    _l_(542536)
if _a_(542539, _n_(542538, "tab_1", lambda: tab_1), "size") == 0 and _a_(542541, _n_(542540, "tab_2", lambda: tab_2), "size") == 0 and _a_(542543, _n_(542542, "tab_3", lambda: tab_3), "size") == 0:
    _l_(542545)

    tab_ind = []
    _l_(542544)
if _c_(542548, _n_(542546, "len", lambda: len), _n_(542547, "tab_ind", lambda: tab_ind)) != 0:
    _l_(542579)

    MIDI_val = _c_(542556, _a_(542550, _n_(542549, "np", lambda: np), "zeros"), (_c_(542553, _n_(542551, "len", lambda: len), _n_(542552, "tab_ind", lambda: tab_ind)), 1), dtype = _a_(542555, _n_(542554, "np", lambda: np), "float32"))
    _l_(542557)
    for z in _c_(542562, _n_(542558, "range", lambda: range), 0, _c_(542561, _n_(542559, "len", lambda: len), _n_(542560, "tab_ind", lambda: tab_ind))):
        _l_(542573)

        _n_(542563, "MIDI_val", lambda: MIDI_val)[_n_(542564, "z", lambda: z), 0] = _c_(542571, _n_(542565, "int", lambda: int), _c_(542570, _n_(542566, "round", lambda: round), _n_(542567, "MIDI_dat", lambda: MIDI_dat)[_n_(542568, "tab_ind", lambda: tab_ind)[_n_(542569, "z", lambda: z)], 2]))
        _l_(542572)
elif _c_(542576, _n_(542574, "len", lambda: len), _n_(542575, "tab_ind", lambda: tab_ind)) == 0:
    _l_(542578)

    MIDI_val = []
    _l_(542577)
MIDI_val = _c_(542583, _a_(542581, _n_(542580, "np", lambda: np), "unique"), _n_(542582, "MIDI_val", lambda: MIDI_val))
_l_(542584)
if _a_(542586, _n_(542585, "MIDI_val", lambda: MIDI_val), "size") >= 6:
    _l_(542594)

    MIDI_val = _c_(542592, _a_(542588, _n_(542587, "np", lambda: np), "delete"), _n_(542589, "MIDI_val", lambda: MIDI_val), _a_(542591, _n_(542590, "np", lambda: np), "s_")[6::])
    _l_(542593)