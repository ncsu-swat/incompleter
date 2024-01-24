# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63427602/attributeerror-chatbot-object-has-no-attribute-set-trainer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, render_template, request
    _l_(632294)

except ImportError:
    pass
try:
    from chatterbot import ChatBot
    _l_(632296)

except ImportError:
    pass
try:
    from chatterbot.trainers import ChatterBotCorpusTrainer
    _l_(632298)

except ImportError:
    pass
try:
    from chatterbot.trainers import ListTrainer
    _l_(632300)

except ImportError:
    pass

app = _c_(632303, _n_(632301, "Flask", lambda: Flask), _n_(632302, "__name__", lambda: __name__))
_l_(632304)
bot = _c_(632306, _n_(632305, "ChatBot", lambda: ChatBot), "Candice")
_l_(632307)
_c_(632311, _a_(632309, _n_(632308, "bot", lambda: bot), "set_trainer"), _n_(632310, "ListTrainer", lambda: ListTrainer))
_l_(632312)
_c_(632316, _a_(632314, _n_(632313, "bot", lambda: bot), "set_trainer"), _n_(632315, "ChatterBotCorpusTrainer", lambda: ChatterBotCorpusTrainer))
_l_(632317)
_c_(632320, _a_(632319, _n_(632318, "bot", lambda: bot), "train"), "chatterbot.corpus.english")
_l_(632321)

@_c_(632324, _a_(632323, _n_(632322, "app", lambda: app), "route"), "/")
def home():
    _l_(632328)

    aux = _c_(632326, _n_(632325, "render_template", lambda: render_template), "home.html") 
    _l_(632327) 
    return aux 
@_c_(632331, _a_(632330, _n_(632329, "app", lambda: app), "route"), "/get")
def get_bot_response():
    _l_(632344)

    userText = _c_(632335, _a_(632334, _a_(632333, _n_(632332, "request", lambda: request), "args"), "get"), 'msg')    
    _l_(632336)    
    aux = _c_(632342, _n_(632337, "str", lambda: str), _c_(632341, _a_(632339, _n_(632338, "bot", lambda: bot), "get_response"), _n_(632340, "userText", lambda: userText))) 
    _l_(632343) 
    return aux 
if _n_(632345, "__name__", lambda: __name__) == "__main__":
    _l_(632350)

    _c_(632348, _a_(632347, _n_(632346, "app", lambda: app), "run"))
    _l_(632349)