# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50665581/attributeerror-textchunker-object-has-no-attribute-print-chunks
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(665748)

except ImportError:
    pass
try:
    from nltk.corpus import brown
    _l_(665750)

except ImportError:
    pass

# Split the input text into chunks, where
# each chunk contains N words
class textChunker:
    _l_(665817)


    def __init__(self, input_data='', chunk_size=0):
        _l_(665757)


        _n_(665751, "self", lambda: self).input_data = _n_(665752, "input_data", lambda: input_data)
        _l_(665753)
        _n_(665754, "self", lambda: self).chunk_size = _n_(665755, "chunk_size", lambda: chunk_size)
        _l_(665756)

    def chunker(self,input_data, N):
        _l_(665816)

        input_words = _c_(665760, _a_(665759, _n_(665758, "input_data", lambda: input_data), "split"), ' ')
        _l_(665761)
        output = []
        _l_(665762)

        cur_chunk = []
        _l_(665763)
        count = 0
        _l_(665764)
        for word in _n_(665765, "input_words", lambda: input_words):
            _l_(665783)

            _c_(665769, _a_(665767, _n_(665766, "cur_chunk", lambda: cur_chunk), "append"), _n_(665768, "word", lambda: word))
            _l_(665770)
            count += 1
            _l_(665771)
            if _n_(665772, "count", lambda: count) == _n_(665773, "N", lambda: N):
                _l_(665782)

                _c_(665779, _a_(665775, _n_(665774, "output", lambda: output), "append"), _c_(665778, _a_(665776, ' ', "join"), _n_(665777, "cur_chunk", lambda: cur_chunk)))
                _l_(665780)
                count, cur_chunk = 0, []
                _l_(665781)

        _c_(665789, _a_(665785, _n_(665784, "output", lambda: output), "append"), _c_(665788, _a_(665786, ' ', "join"), _n_(665787, "cur_chunk", lambda: cur_chunk)))
        _l_(665790)
        aux = _n_(665791, "output", lambda: output)
        _l_(665792)

        return aux

        def print_chunks(self,input_data,chunk_size):
            _l_(665815)

            try:
                import chunker
                _l_(665794)

            except ImportError:
                pass
            chunks = _c_(665798, _n_(665795, "chunker", lambda: chunker), _n_(665796, "input_data", lambda: input_data), _n_(665797, "chunk_size", lambda: chunk_size))
            _l_(665799)
            _c_(665804, _n_(665800, "print", lambda: print), '\nNumber of text chunks =', _c_(665803, _n_(665801, "len", lambda: len), _n_(665802, "chunks", lambda: chunks)), '\n')
            _l_(665805)
            for i, chunk in _c_(665808, _n_(665806, "enumerate", lambda: enumerate), _n_(665807, "chunks", lambda: chunks)):
                _l_(665814)

                _c_(665812, _n_(665809, "print", lambda: print), 'Chunk', _n_(665810, "i", lambda: i) + 1, '==>', _n_(665811, "chunk", lambda: chunk)[:50])
                _l_(665813)

if _n_(665818, "__name__", lambda: __name__)=='__main__':
    _l_(665835)


    input_data = _c_(665823, _a_(665819, ' ', "join"), _c_(665822, _a_(665821, _n_(665820, "brown", lambda: brown), "words"))[:12000])
    _l_(665824)
    chunk_size = 700
    _l_(665825)

    text_Chunker=_c_(665827, _n_(665826, "textChunker", lambda: textChunker))
    _l_(665828)
    printchunks =_c_(665833, _a_(665830, _n_(665829, "text_Chunker", lambda: text_Chunker), "print_chunks"), _n_(665831, "input_data", lambda: input_data),_n_(665832, "chunk_size", lambda: chunk_size))
    _l_(665834)