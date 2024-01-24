# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51988684/discord-py-when-creating-group-gives-attributeerror
# reddit group commands
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(471365, "function_debug", lambda: function_debug)
@_c_(471368, _a_(471367, _n_(471366, "bot", lambda: bot), "group"), pass_context = True)
async def reddit(context):
    _l_(471405)

    message = _a_(471370, _n_(471369, "context", lambda: context), "message")
    _l_(471371)
    _c_(471376, _a_(471373, _n_(471372, "logger", lambda: logger), "debug"), _a_(471375, _n_(471374, "message", lambda: message), "content"))
    _l_(471377)
    try:
        _l_(471404)

        if _a_(471380, _a_(471379, _n_(471378, "message", lambda: message), "server"), "name") == 'PeaceCrafters' and _a_(471383, _a_(471382, _n_(471381, "message", lambda: message), "channel"), "name") == 'utilbots':
            _l_(471391)

            cont = True
            _l_(471384)
        elif _a_(471387, _a_(471386, _n_(471385, "message", lambda: message), "server"), "name") != 'PeaceCrafters':
            _l_(471390)

            cont = True
            _l_(471388)
        else:
            cont = False
            _l_(471389)
    except _n_(471392, "AttributeError", lambda: AttributeError):
        _l_(471394)

        cont = True
        _l_(471393)
    finally:
        _l_(471403)

        if _n_(471395, "cont", lambda: cont):
            _l_(471402)

            if _a_(471397, _n_(471396, "context", lambda: context), "invoked_subcommand") is None:
                _l_(471401)

                await _c_(471399, _n_(471398, "reddit_help", lambda: reddit_help))
                _l_(471400)


@_n_(471406, "function_debug", lambda: function_debug)
@_c_(471409, _a_(471408, _n_(471407, "reddit", lambda: reddit), "command"), name = 'help', description = 'Provides help with reddit', pass_context = True)
async def reddit_help(context):
    _l_(471447)

    message = _a_(471411, _n_(471410, "context", lambda: context), "message")
    _l_(471412)
    _c_(471417, _a_(471414, _n_(471413, "logger", lambda: logger), "debug"), _a_(471416, _n_(471415, "message", lambda: message), "content"))
    _l_(471418)
    try:
        _l_(471446)

        if _a_(471421, _a_(471420, _n_(471419, "message", lambda: message), "server"), "name") == 'PeaceCrafters' and _a_(471424, _a_(471423, _n_(471422, "message", lambda: message), "channel"), "name") == 'utilbots':
            _l_(471432)

            cont = True
            _l_(471425)
        elif _a_(471428, _a_(471427, _n_(471426, "message", lambda: message), "server"), "name") != 'PeaceCrafters':
            _l_(471431)

            cont = True
            _l_(471429)
        else:
            cont = False
            _l_(471430)
    except _n_(471433, "AttributeError", lambda: AttributeError):
        _l_(471435)

        cont = True
        _l_(471434)
    finally:
        _l_(471445)

        if _n_(471436, "cont", lambda: cont):
            _l_(471444)

            message = _n_(471437, "reddit_message", lambda: reddit_message)
            _l_(471438)
            await _c_(471442, _a_(471440, _n_(471439, "bot", lambda: bot), "say"), _n_(471441, "message", lambda: message))
            _l_(471443)


@_n_(471448, "function_debug", lambda: function_debug)
@_c_(471451, _a_(471450, _n_(471449, "reddit", lambda: reddit), "group"), pass_context = True)
async def subreddit(context):
    _l_(471489)

    message = _a_(471453, _n_(471452, "context", lambda: context), "message")
    _l_(471454)
    _c_(471459, _a_(471456, _n_(471455, "logger", lambda: logger), "debug"), _a_(471458, _n_(471457, "message", lambda: message), "content"))
    _l_(471460)
    try:
        _l_(471488)

        if _a_(471463, _a_(471462, _n_(471461, "message", lambda: message), "server"), "name") == 'PeaceCrafters' and _a_(471466, _a_(471465, _n_(471464, "message", lambda: message), "channel"), "name") == 'utilbots':
            _l_(471474)

            cont = True
            _l_(471467)
        elif _a_(471470, _a_(471469, _n_(471468, "message", lambda: message), "server"), "name") != 'PeaceCrafters':
            _l_(471473)

            cont = True
            _l_(471471)
        else:
            cont = False
            _l_(471472)
    except _n_(471475, "AttributeError", lambda: AttributeError):
        _l_(471477)

        cont = True
        _l_(471476)
    finally:
        _l_(471487)

        if _n_(471478, "cont", lambda: cont):
            _l_(471486)

            info = _c_(471482, _a_(471481, _a_(471480, _n_(471479, "message", lambda: message), "content"), "split"), ' ')[1:]
            _l_(471483)
            subreddit = _n_(471484, "info", lambda: info)[0]
            _l_(471485)

@_n_(471490, "function_debug", lambda: function_debug)
@_c_(471493, _a_(471492, _n_(471491, "subreddit", lambda: subreddit), "command"), name = 'hot', description = 'Lists the hot commands in the subreddit', pass_context = True)
async def subreddit_hot(context):
    _l_(471525)

    message = _a_(471495, _n_(471494, "context", lambda: context), "message")
    _l_(471496)
    _c_(471501, _a_(471498, _n_(471497, "logger", lambda: logger), "debug"), _a_(471500, _n_(471499, "message", lambda: message), "content"))
    _l_(471502)
    try:
        _l_(471524)

        if _a_(471505, _a_(471504, _n_(471503, "message", lambda: message), "server"), "name") == 'PeaceCrafters' and _a_(471508, _a_(471507, _n_(471506, "message", lambda: message), "channel"), "name") == 'utilbots':
            _l_(471516)

            cont = True
            _l_(471509)
        elif _a_(471512, _a_(471511, _n_(471510, "message", lambda: message), "server"), "name") != 'PeaceCrafters':
            _l_(471515)

            cont = True
            _l_(471513)
        else:
            cont = False
            _l_(471514)
    except _n_(471517, "AttributeError", lambda: AttributeError):
        _l_(471519)

        cont = True
        _l_(471518)
    finally:
        _l_(471523)

        if _n_(471520, "cont", lambda: cont):
            _l_(471522)

            pass #i will add more once i figure out how message.content is handled
            _l_(471521) #i will add more once i figure out how message.content is handled