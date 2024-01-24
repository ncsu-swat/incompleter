# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64441507/attributeerror-callbackcontext-update-object-has-no-attribute-message
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def rating(bot, update):
    _l_(392011)

    _c_(392009, _a_(392007, _n_(392006, "bot", lambda: bot), "send_sticker"), _n_(392008, "chat_id", lambda: chat_id),'some_sticker_id')
    _l_(392010)
...
_l_(392012)
rating_handler = _c_(392015, _n_(392013, "CommandHandler", lambda: CommandHandler), 'rating', _n_(392014, "rating", lambda: rating))
_l_(392016)
_c_(392021, _a_(392019, _a_(392018, _n_(392017, "updater", lambda: updater), "dispatcher"), "add_handler"), _n_(392020, "rating_handler", lambda: rating_handler))
_l_(392022)