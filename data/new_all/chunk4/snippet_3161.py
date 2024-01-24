# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35423739/lpthw-ex49-get-attributeerror-in-unit-test
#!/usr/bin/env python
# encoding: utf-8
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from nose.tools import *
    _l_(603339)

except ImportError:
    pass
try:
    import lexicon
    _l_(603341)

except ImportError:
    pass
try:
    import parser
    _l_(603343)

except ImportError:
    pass

def test_sentence_obj():
    _l_(603374)

    s = _c_(603346, _a_(603345, _n_(603344, "parser", lambda: parser), "Sentence"), ('noun', 'bear'), ('verb', 'eat'), ('number', 1), ('noun', 'door'))
    _l_(603347)
    _c_(603351, _n_(603348, "assert_equal", lambda: assert_equal), _a_(603350, _n_(603349, "s", lambda: s), "subject"), 'bear')
    _l_(603352)
    _c_(603356, _n_(603353, "assert_equal", lambda: assert_equal), _a_(603355, _n_(603354, "s", lambda: s), "verb"), 'eat')
    _l_(603357)
    _c_(603361, _n_(603358, "assert_equal", lambda: assert_equal), _a_(603360, _n_(603359, "s", lambda: s), "number"), 1)
    _l_(603362)
    _c_(603366, _n_(603363, "assert_equal", lambda: assert_equal), _a_(603365, _n_(603364, "s", lambda: s), "object"), 'door')
    _l_(603367)
    _c_(603372, _n_(603368, "assert_equal", lambda: assert_equal), _c_(603371, _a_(603370, _n_(603369, "s", lambda: s), "to_tuple")), ('bear', 'eat', 1, 'door'))
    _l_(603373)

def test_peek():
    _l_(603392)

    word_list = _c_(603377, _a_(603376, _n_(603375, "lexicon", lambda: lexicon), "scan"), 'princess')
    _l_(603378)
    _c_(603384, _n_(603379, "assert_equal", lambda: assert_equal), _c_(603383, _a_(603381, _n_(603380, "parser", lambda: parser), "peek"), _n_(603382, "word_list", lambda: word_list)), 'noun')
    _l_(603385)
    _c_(603390, _n_(603386, "assert_equal", lambda: assert_equal), _c_(603389, _a_(603388, _n_(603387, "parser", lambda: parser), "peek"), None), None)
    _l_(603391)

def test_match():
    _l_(603417)

    word_list = _c_(603395, _a_(603394, _n_(603393, "lexicon", lambda: lexicon), "scan"), 'princess')
    _l_(603396)
    _c_(603402, _n_(603397, "assert_equal", lambda: assert_equal), _c_(603401, _a_(603399, _n_(603398, "parser", lambda: parser), "match"), _n_(603400, "word_list", lambda: word_list), 'noun'), ('noun', 'princess'))
    _l_(603403)
    _c_(603409, _n_(603404, "assert_equal", lambda: assert_equal), _c_(603408, _a_(603406, _n_(603405, "parser", lambda: parser), "match"), _n_(603407, "word_list", lambda: word_list), 'stop'), None)
    _l_(603410)
    _c_(603415, _n_(603411, "assert_equal", lambda: assert_equal), _c_(603414, _a_(603413, _n_(603412, "parser", lambda: parser), "match"), None, 'noun'), None)
    _l_(603416)

def test_skip():
    _l_(603435)

    word_list = _c_(603420, _a_(603419, _n_(603418, "lexicon", lambda: lexicon), "scan"), 'bear eat door')
    _l_(603421)
    _c_(603424, _n_(603422, "assert_equal", lambda: assert_equal), _n_(603423, "word_list", lambda: word_list), [('noun', 'bear'), ('verb', 'eat'), ('noun', 'door')])
    _l_(603425)
    _c_(603429, _a_(603427, _n_(603426, "parser", lambda: parser), "skip"), _n_(603428, "word_list", lambda: word_list), 'noun')
    _l_(603430)
    _c_(603433, _n_(603431, "assert_equal", lambda: assert_equal), _n_(603432, "word_list", lambda: word_list), [('verb', 'eat'), ('noun', 'door')])
    _l_(603434)

def test_parse_verb():
    _l_(603459)

    word_list = _c_(603438, _a_(603437, _n_(603436, "lexicon", lambda: lexicon), "scan"), 'it eat door')
    _l_(603439)
    _c_(603445, _n_(603440, "assert_equal", lambda: assert_equal), _c_(603444, _a_(603442, _n_(603441, "parser", lambda: parser), "parse_verb"), _n_(603443, "word_list", lambda: word_list)), ('verb', 'eat'))
    _l_(603446)
    word_list = _c_(603449, _a_(603448, _n_(603447, "lexicon", lambda: lexicon), "scan"), 'bear eat door')
    _l_(603450)
    _c_(603457, _n_(603451, "assert_raise", lambda: assert_raise), _a_(603453, _n_(603452, "parser", lambda: parser), "ParserError"), _a_(603455, _n_(603454, "parser", lambda: parser), "parse_verb"), _n_(603456, "word_list", lambda: word_list))
    _l_(603458)

def test_parse_object():
    _l_(603494)

    word_list = _c_(603462, _a_(603461, _n_(603460, "lexicon", lambda: lexicon), "scan"), 'the door')
    _l_(603463)
    _c_(603469, _n_(603464, "assert_equal", lambda: assert_equal), _c_(603468, _a_(603466, _n_(603465, "parser", lambda: parser), "parse_object"), _n_(603467, "word_list", lambda: word_list)), ('noun', 'door'))
    _l_(603470)
    word_list = _c_(603473, _a_(603472, _n_(603471, "lexicon", lambda: lexicon), "scan"), 'the east')
    _l_(603474)
    _c_(603480, _n_(603475, "assert_equal", lambda: assert_equal), _c_(603479, _a_(603477, _n_(603476, "parser", lambda: parser), "parse_object"), _n_(603478, "word_list", lambda: word_list)), ('direction', 'east'))
    _l_(603481)
    word_list = _c_(603484, _a_(603483, _n_(603482, "lexicon", lambda: lexicon), "scan"), 'the it')
    _l_(603485)
    _c_(603492, _n_(603486, "assert_raise", lambda: assert_raise), _a_(603488, _n_(603487, "parser", lambda: parser), "ParserError"), _a_(603490, _n_(603489, "parser", lambda: parser), "parse_object"), _n_(603491, "word_list", lambda: word_list))
    _l_(603493)

def test_parse_subject():
    _l_(603512)

    word_list = _c_(603497, _a_(603496, _n_(603495, "lexicon", lambda: lexicon), "scan"), 'eat door')
    _l_(603498)
    subj = ('noun', 'bear')
    _l_(603499)
    s = _c_(603504, _a_(603501, _n_(603500, "parser", lambda: parser), "parse_subject"), _n_(603502, "word_list", lambda: word_list), _n_(603503, "subj", lambda: subj))
    _l_(603505)
    _c_(603510, _n_(603506, "assert_raise", lambda: assert_raise), _c_(603509, _a_(603508, _n_(603507, "s", lambda: s), "to_tuple")), ('bear', 'eat', 1, 'door'))
    _l_(603511)

def test_parse_sentence():
    _l_(603555)

    word_list = _c_(603515, _a_(603514, _n_(603513, "lexicon", lambda: lexicon), "scan"), 'the bear eat door')
    _l_(603516)
    s = _c_(603520, _a_(603518, _n_(603517, "parser", lambda: parser), "parse_sentence"), _n_(603519, "word_list", lambda: word_list))
    _l_(603521)
    _c_(603526, _n_(603522, "assert_equal", lambda: assert_equal), _c_(603525, _a_(603524, _n_(603523, "s", lambda: s), "to_tuple")), ('bear', 'eat', 1, 'door'))
    _l_(603527)
    word_list = _c_(603530, _a_(603529, _n_(603528, "lexicon", lambda: lexicon), "scan"), 'in the door')
    _l_(603531)
    s = _c_(603535, _a_(603533, _n_(603532, "parser", lambda: parser), "parse_sentence"), _n_(603534, "word_list", lambda: word_list))
    _l_(603536)
    _c_(603541, _n_(603537, "assert_equal", lambda: assert_equal), _c_(603540, _a_(603539, _n_(603538, "s", lambda: s), "to_tuple")), ('player', 'eat', 1, 'door'))
    _l_(603542)
    word_list = _c_(603545, _a_(603544, _n_(603543, "lexicon", lambda: lexicon), "scan"), 'north eat door')
    _l_(603546)
    _c_(603553, _n_(603547, "assert_equal", lambda: assert_equal), _a_(603549, _n_(603548, "parser", lambda: parser), "ParserError"), _a_(603551, _n_(603550, "parser", lambda: parser), "parse_sentence"), _n_(603552, "word_list", lambda: word_list))
    _l_(603554)

def test_unknown_words():
    _l_(603571)

    word_list = _c_(603558, _a_(603557, _n_(603556, "lexicon", lambda: lexicon), "scan"), 'xxx the xxx bear xxx eat xxx 5 xxx door xxx')
    _l_(603559)
    s = _c_(603563, _a_(603561, _n_(603560, "parser", lambda: parser), "parse_sentence"), _n_(603562, "word_list", lambda: word_list))
    _l_(603564)
    _c_(603569, _n_(603565, "assert_equal", lambda: assert_equal), _c_(603568, _a_(603567, _n_(603566, "s", lambda: s), "to_tuple")), ('bear', 'eat', 1, 'door'))
    _l_(603570)

def test_number():
    _l_(603587)

    word_list = _c_(603574, _a_(603573, _n_(603572, "lexicon", lambda: lexicon), "scan"), 'xxx the xxx bear xxx eat xxx 5 xxx door xxx')
    _l_(603575)
    s = _c_(603579, _a_(603577, _n_(603576, "parser", lambda: parser), "parse_sentence"), _n_(603578, "word_list", lambda: word_list))
    _l_(603580)
    _c_(603585, _n_(603581, "assert_equal", lambda: assert_equal), _c_(603584, _a_(603583, _n_(603582, "s", lambda: s), "to_tuple")), ('bear', 'eat', 5, 'door'))
    _l_(603586)