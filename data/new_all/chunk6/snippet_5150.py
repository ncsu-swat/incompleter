# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77441584/attributeerror-tuple-object-has-no-attribute-split-options-list-using-pick
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(350587, _n_(350583, "open", lambda: open), _c_(350586, _n_(350584, "str", lambda: str), _n_(350585, "option", lambda: option))[2:-2], 'r') as quiz:
    _l_(350684)

    quiz_info = [_c_(350590, _a_(350589, _n_(350588, "line", lambda: line), "strip")) for line in _n_(350591, "quiz", lambda: quiz)]
    _l_(350592)
    quiz_title = _c_(350595, _n_(350593, "str", lambda: str), _n_(350594, "option", lambda: option))
    _l_(350596)
    title = '-----------\n QUIZZABLE \n-----------\n   Quiz    \n-----------\n\nQuiz:', _n_(350597, "quiz_title", lambda: quiz_title)
    _l_(350598)
    quiz_question_total = _n_(350599, "quiz_info", lambda: quiz_info)[0]
    _l_(350600)
    quiz_score = 0
    _l_(350601)
    quiz_question_count = _c_(350603, _n_(350602, "int", lambda: int), 1)
    _l_(350604)
    quiz_current_line = _c_(350606, _n_(350605, "int", lambda: int), 1)
    _l_(350607)
    while _n_(350608, "quiz_question_count", lambda: quiz_question_count) <= _c_(350611, _n_(350609, "int", lambda: int), _n_(350610, "quiz_question_total", lambda: quiz_question_total)):
        _l_(350683)

        quiz_question = _n_(350612, "quiz_info", lambda: quiz_info)[_c_(350615, _n_(350613, "int", lambda: int), _n_(350614, "quiz_current_line", lambda: quiz_current_line))]
        _l_(350616)
        quiz_current_line = _c_(350619, _n_(350617, "int", lambda: int), _n_(350618, "quiz_current_line", lambda: quiz_current_line)) + _c_(350621, _n_(350620, "int", lambda: int), 1)
        _l_(350622)
        quiz_question_option_count = _n_(350623, "quiz_info", lambda: quiz_info)[_c_(350626, _n_(350624, "int", lambda: int), _n_(350625, "quiz_current_line", lambda: quiz_current_line))]
        _l_(350627)
        quiz_current_line = _c_(350630, _n_(350628, "int", lambda: int), _n_(350629, "quiz_current_line", lambda: quiz_current_line)) + _c_(350632, _n_(350631, "int", lambda: int), 1)
        _l_(350633)
        quiz_question_option = _c_(350635, _n_(350634, "int", lambda: int), 1)
        _l_(350636)
        options = []
        _l_(350637)
        while _n_(350638, "quiz_question_option", lambda: quiz_question_option) <= _c_(350641, _n_(350639, "int", lambda: int), _n_(350640, "quiz_question_option_count", lambda: quiz_question_option_count)):
            _l_(350659)

            options += [_n_(350642, "quiz_info", lambda: quiz_info)[_c_(350645, _n_(350643, "int", lambda: int), _n_(350644, "quiz_current_line", lambda: quiz_current_line))]]
            _l_(350646)
            quiz_current_line = _c_(350649, _n_(350647, "int", lambda: int), _n_(350648, "quiz_current_line", lambda: quiz_current_line)) + _c_(350651, _n_(350650, "int", lambda: int), 1)
            _l_(350652)
            quiz_question_option = _c_(350655, _n_(350653, "int", lambda: int), _n_(350654, "quiz_question_option", lambda: quiz_question_option)) + _c_(350657, _n_(350656, "int", lambda: int), 1)
            _l_(350658)
        quiz_question_answer = _n_(350660, "quiz_info", lambda: quiz_info)[_c_(350663, _n_(350661, "int", lambda: int), _n_(350662, "quiz_current_line", lambda: quiz_current_line))]
        _l_(350664)
        quiz_current_line = _c_(350667, _n_(350665, "int", lambda: int), _n_(350666, "quiz_current_line", lambda: quiz_current_line)) + _c_(350669, _n_(350668, "int", lambda: int), 1)
        _l_(350670)
        option, index = _c_(350674, _n_(350671, "pick", lambda: pick), _n_(350672, "options", lambda: options), _n_(350673, "title", lambda: title), indicator='[>]', default_index=0)    #problem
        _l_(350675)    #problem
        if _n_(350676, "option", lambda: option) == _n_(350677, "quiz_question_answer", lambda: quiz_question_answer):
            _l_(350682)

            quiz_score = _n_(350678, "quiz_score", lambda: quiz_score) + _c_(350680, _n_(350679, "int", lambda: int), 1)
            _l_(350681)