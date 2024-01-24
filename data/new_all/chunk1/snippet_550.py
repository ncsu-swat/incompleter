# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64441507/attributeerror-callbackcontext-update-object-has-no-attribute-message
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def start(bot, update):
    _l_(388306)

    if _a_(388289, _a_(388288, _a_(388287, _n_(388286, "update", lambda: update), "message"), "from_user"), "username") == _n_(388290, "AAA", lambda: AAA):
        _l_(388305)

        _c_(388296, _a_(388292, _n_(388291, "bot", lambda: bot), "sendMessage"), chat_id=_a_(388295, _a_(388294, _n_(388293, "update", lambda: update), "message"), "chat_id"), text="Text_one")
        _l_(388297)
    else:
        _c_(388303, _a_(388299, _n_(388298, "bot", lambda: bot), "sendMessage"), chat_id=_a_(388302, _a_(388301, _n_(388300, "update", lambda: update), "message"), "chat_id"), text="Text_two")
        _l_(388304)
...
_l_(388307)
updater = _c_(388310, _n_(388308, "Updater", lambda: Updater), token=_n_(388309, "bot_token", lambda: bot_token))
_l_(388311)

start_handler = _c_(388314, _n_(388312, "CommandHandler", lambda: CommandHandler), 'start', _n_(388313, "start", lambda: start))
_l_(388315)
_c_(388320, _a_(388318, _a_(388317, _n_(388316, "updater", lambda: updater), "dispatcher"), "add_handler"), _n_(388319, "start_handler", lambda: start_handler))
_l_(388321)