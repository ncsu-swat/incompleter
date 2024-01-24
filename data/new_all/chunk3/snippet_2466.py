# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77660827/im-getting-typeerror-io-textiowrapper-object-is-not-subscriptable-on-my-chat
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def AXIS():
  _l_(542968)

  knowledge_base:_n_(542909, "dict", lambda: dict) = _c_(542911, _n_(542910, "open", lambda: open), 'knowledge_base.json','r',errors = 'ignore')
  _l_(542912)
  while True:
    _l_(542967)

    user_input:_n_(542913, "str", lambda: str) = _c_(542915, _n_(542914, "input", lambda: input), 'You:')
    _l_(542916)
    if _c_(542919, _a_(542918, _n_(542917, "user_input", lambda: user_input), "lower")) in ("q", "quit", "shut down", "shutdown", "cancel", "power off", "poweroff", "power down", "powerdown", "off", "turn off", "turnoff"):
      _l_(542924)

      _c_(542921, _n_(542920, "print", lambda: print), "AXIS: powering down")
      _l_(542922)
      break
      _l_(542923)

    best_match: _n_(542925, "str", lambda: str) | None = _c_(542929, _n_(542926, "find_best_match", lambda: find_best_match), _n_(542927, "user_input", lambda: user_input), _n_(542928, "list", lambda: list)['q("question") for q in knowledge_base.json("questions")'])
    _l_(542930)
    if _n_(542931, "best_match", lambda: best_match):
      _l_(542966)

      answer: _n_(542932, "str", lambda: str) = _c_(542936, _n_(542933, "get_answer_for_question", lambda: get_answer_for_question), _n_(542934, "best_match", lambda: best_match), _n_(542935, "knowledge_base", lambda: knowledge_base))
      _l_(542937)
      _c_(542940, _n_(542938, "print", lambda: print), f'AXIS: {_n_(542939, "answer", lambda: answer)}')
      _l_(542941)
    else:
      _c_(542943, _n_(542942, 'print', lambda: print), 'AXIS: I don\'t know the answer. please teach me?')
      _l_(542944)
      new_answer: _n_(542945, 'str', lambda: str) = _c_(542947, _n_(542946, 'input', lambda: input), 'Type the answer or "skip" to skip:  ')
      _l_(542948)
      if _c_(542951, _a_(542950, _n_(542949, 'new_answer', lambda: new_answer), 'lower')) != 'skip':
        _l_(542965)

        _c_(542956, _a_(542953, _n_(542952, 'knowledge_base', lambda: knowledge_base)["questions"], 'append'), {"question": _n_(542954, 'user_input', lambda: user_input), "answer": _n_(542955, 'new_answer', lambda: new_answer)})
        _l_(542957)
        _c_(542960, _n_(542958, 'save_knowledge_base', lambda: save_knowledge_base), 'knowledge_base.json', _n_(542959, 'knowledge_base', lambda: knowledge_base))
        _l_(542961)
        _c_(542963, _n_(542962, 'print', lambda: print), 'AXIS: I have learned a new response!')
        _l_(542964)

if _n_(542969, '__name__', lambda: __name__) =='__main__':
  _l_(542973)

  _c_(542971, _n_(542970, 'AXIS', lambda: AXIS))
  _l_(542972)