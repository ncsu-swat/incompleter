# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/13832397/attributeerror-object-has-no-attribute-execute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def AddQuestion(self, Question, Answer1, Answer2, Answer3, Answer4):
    _l_(445712)

    _c_(445710, _a_(445703, _a_(445702, _n_(445701, "self", lambda: self), "cursor"), "execute"), """INSERT INTO questions
                        VALUES (?, ?, ?, ?, ?, ?)""", [None, _n_(445704, "Question", lambda: Question), _n_(445705, "Answer1", lambda: Answer1), _n_(445706, "Answer2", lambda: Answer2), _n_(445707, "Answer3", lambda: Answer3), _n_(445708, "Answer4", lambda: Answer4), _n_(445709, "CorrectAnswer", lambda: CorrectAnswer)])
    _l_(445711)
_c_(445716, _a_(445715, _a_(445714, _n_(445713, "self", lambda: self), "connection"), "commit"))
_l_(445717)