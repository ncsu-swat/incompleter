# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75825362/attributeerror-encode-when-returning-streamingresponse-in-fastapi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import openai
    _l_(415408)

except ImportError:
    pass

def chat_stream(question: _n_(415409, "str", lambda: str), key: _n_(415410, "str", lambda: str)):
    _l_(415422)

    _n_(415411, "openai", lambda: openai).api_key = _n_(415412, "key", lambda: key)
    _l_(415413)
    # create a completion
    completion = _c_(415418, _a_(415416, _a_(415415, _n_(415414, "openai", lambda: openai), "Completion"), "create"), model="text-davinci-003",
                                          prompt=_n_(415417, "question", lambda: question),
                                          stream=True)
    _l_(415419)
    aux = _n_(415420, "completion", lambda: completion)
    _l_(415421)
    return aux