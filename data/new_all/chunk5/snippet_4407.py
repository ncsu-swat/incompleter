# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58227430/how-to-fix-attribute-error-in-a-page-summarizer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def text():
      _l_(671157)

      for i in _c_(671148, _n_(671144, "range", lambda: range), 0,_c_(671147, _n_(671145, "len", lambda: len), _n_(671146, "text_p", lambda: text_p))):
            _l_(671156)

            text += _n_(671149, "text_p", lambda: text_p)[_n_(671150, "i", lambda: i)].text
            _l_(671151)
            text = _c_(671154, _a_(671153, _n_(671152, "text", lambda: text), "lower"))
            _l_(671155)


# tokenize the text
tokens =[_n_(671158, "t", lambda: t) for t in _c_(671161, _a_(671160, _n_(671159, "text", lambda: text), "split"))]
_l_(671162)
_c_(671165, _n_(671163, "print", lambda: print), _n_(671164, "tokens", lambda: tokens))
_l_(671166)