# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63427602/attributeerror-chatbot-object-has-no-attribute-set-trainer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, render_template, request
    _l_(643684)

except ImportError:
    pass
try:
    from chatterbot import ChatBot
    _l_(643686)

except ImportError:
    pass
try:
    from chatterbot.trainers import ChatterBotCorpusTrainer
    _l_(643688)

except ImportError:
    pass
try:
    from chatterbot.trainers import ListTrainer
    _l_(643690)

except ImportError:
    pass

app = _c_(643693, _n_(643691, "Flask", lambda: Flask), _n_(643692, "__name__", lambda: __name__))
_l_(643694)
bot = _c_(643696, _n_(643695, "ChatBot", lambda: ChatBot), "Candice")
_l_(643697)
_c_(643701, _a_(643699, _n_(643698, "bot", lambda: bot), "set_trainer"), _n_(643700, "ListTrainer", lambda: ListTrainer))
_l_(643702)
_c_(643706, _a_(643704, _n_(643703, "bot", lambda: bot), "set_trainer"), _n_(643705, "ChatterBotCorpusTrainer", lambda: ChatterBotCorpusTrainer))
_l_(643707)
_c_(643710, _a_(643709, _n_(643708, "bot", lambda: bot), "train"), "chatterbot.corpus.english")
_l_(643711)

@_c_(643714, _a_(643713, _n_(643712, "app", lambda: app), "route"), "/")
def home():
    _l_(643718)

    aux = _c_(643716, _n_(643715, "render_template", lambda: render_template), "home.html") 
    _l_(643717) 
    return aux 
@_c_(643721, _a_(643720, _n_(643719, "app", lambda: app), "route"), "/get")
def get_bot_response():
    _l_(643734)

    userText = _c_(643725, _a_(643724, _a_(643723, _n_(643722, "request", lambda: request), "args"), "get"), 'msg')    
    _l_(643726)    
    aux = _c_(643732, _n_(643727, "str", lambda: str), _c_(643731, _a_(643729, _n_(643728, "bot", lambda: bot), "get_response"), _n_(643730, "userText", lambda: userText))) 
    _l_(643733) 
    return aux 
if _n_(643735, "__name__", lambda: __name__) == "__main__":
    _l_(643740)

    _c_(643738, _a_(643737, _n_(643736, "app", lambda: app), "run"))
    _l_(643739)