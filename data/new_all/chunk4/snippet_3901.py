# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65580274/why-does-chatterbot-raise-typeerror-for-my-custom-corpus
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from chatterbot import ChatBot
    _l_(642760)

except ImportError:
    pass
try:
    from chatterbot.trainers import ChatterBotCorpusTrainer
    _l_(642762)

except ImportError:
    pass
chatterbot = _c_(642764, _n_(642763, "ChatBot", lambda: ChatBot), 'test')
_l_(642765)
trainer = _c_(642768, _n_(642766, "ChatterBotCorpusTrainer", lambda: ChatterBotCorpusTrainer), _n_(642767, "chatterbot", lambda: chatterbot))
_l_(642769)
_c_(642772, _a_(642771, _n_(642770, "trainer", lambda: trainer), "train"), 'chatterbot.corpus.custom.random')
_l_(642773)