# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
word_list = _c_(116916, _a_(116915, _n_(116914, "string_words", lambda: string_words), "split"))
_l_(116917)
word_freq = [_c_(116921, _a_(116919, _n_(116918, "word_list", lambda: word_list), "count"), _n_(116920, "n", lambda: n)) for n in _n_(116922, "word_list", lambda: word_list)]
_l_(116923)
_c_(116928, _n_(116924, "print", lambda: print), _c_(116927, _a_(116925, 'String:\n {} \n', "format"), _n_(116926, "string_words", lambda: string_words)))
_l_(116929)
_c_(116936, _n_(116930, "print", lambda: print), _c_(116935, _a_(116931, 'List:\n {} \n', "format"), _c_(116934, _n_(116932, "str", lambda: str), _n_(116933, "word_list", lambda: word_list))))
_l_(116937)
_c_(116949, _n_(116938, "print", lambda: print), _c_(116948, _a_(116939, 'Pairs (Words and Frequencies:\n {}', "format"), _c_(116947, _n_(116940, "str", lambda: str), _c_(116946, _n_(116941, "list", lambda: list), _c_(116945, _n_(116942, "zip", lambda: zip), _n_(116943, "word_list", lambda: word_list), _n_(116944, "word_freq", lambda: word_freq))))))
_l_(116950)