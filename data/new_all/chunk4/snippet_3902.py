# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65580274/why-does-chatterbot-raise-typeerror-for-my-custom-corpus
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from chatterbot import ChatBot
    _l_(585240)

except ImportError:
    pass
try:
    from chatterbot.trainers import ChatterBotCorpusTrainer
    _l_(585242)

except ImportError:
    pass
chatterbot = _c_(585244, _n_(585243, "ChatBot", lambda: ChatBot), 'test')
_l_(585245)
trainer = _c_(585248, _n_(585246, "ChatterBotCorpusTrainer", lambda: ChatterBotCorpusTrainer), _n_(585247, "chatterbot", lambda: chatterbot))
_l_(585249)
_c_(585252, _a_(585251, _n_(585250, "trainer", lambda: trainer), "train"), 'chatterbot.corpus.custom.random')
_l_(585253)