# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74661159/building-tg-bot-with-python-giving-me-typeerror-module-object-is-not-callabl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import telegram.ext
    _l_(585541)

except ImportError:
    pass

Token = "API_KEY"
_l_(585542)

updater = _c_(585545, _a_(585544, _a_(585543, telegram, "ext"), "updater"), "API_KEY", use_context = True)
_l_(585546)
dispatcher = _a_(585548, _n_(585547, "updater", lambda: updater), "dispatcher")
_l_(585549)

def start(update, context):
    _l_(585555)

    _c_(585553, _a_(585552, _a_(585551, _n_(585550, "update", lambda: update), "message"), "reply_text"), "Hello! Thanks for messaging me!")
    _l_(585554)

def help(update, context):
    _l_(585561)

    _c_(585559, _a_(585558, _a_(585557, _n_(585556, "update", lambda: update), "message"), "reply_text"), """
        /aboutme -> More info about me.
        /jobs -> See all my open jobs!
        /myinfo -> My email information.
        /latamsalaries -> Current LATAM salaries for devs.
        """
    )
    _l_(585560)

def aboutme(update, context):
    _l_(585567)

    _c_(585565, _a_(585564, _a_(585563, _n_(585562, "update", lambda: update), "message"), "reply_text"), "My name is Robert Grootjen, and I'm a technical headhunter! My mission is to connect the best talent in Latin America with topnotch companies in the United States and Canada.")
    _l_(585566)

def jobs(update, context):
    _l_(585573)

    _c_(585571, _a_(585570, _a_(585569, _n_(585568, "update", lambda: update), "message"), "reply_text"), "")
    _l_(585572)

def myinfo(update, context):
    _l_(585579)

    _c_(585577, _a_(585576, _a_(585575, _n_(585574, "update", lambda: update), "message"), "reply_text"), "Linkedin: https://www.linkedin.com/in/robert-grootjen-08a10b15a/")
    _l_(585578)

def latamsalaries(update, context):
    _l_(585585)

    _c_(585583, _a_(585582, _a_(585581, _n_(585580, "update", lambda: update), "message"), "reply_text"), "Jr - $1500 - $3000 USD")
    _l_(585584)


_c_(585592, _a_(585587, _n_(585586, "dispatcher", lambda: dispatcher), "add_handler"), _c_(585591, _a_(585589, _a_(585588, telegram, "ext"), "CommandHandler"), 'start', _n_(585590, "start", lambda: start)))
_l_(585593)
_c_(585600, _a_(585595, _n_(585594, "dispatcher", lambda: dispatcher), "add_handler"), _c_(585599, _a_(585597, _a_(585596, telegram, "ext"), "CommandHandler"), 'aboutme', _n_(585598, "aboutme", lambda: aboutme)))
_l_(585601)
_c_(585608, _a_(585603, _n_(585602, "dispatcher", lambda: dispatcher), "add_handler"), _c_(585607, _a_(585605, _a_(585604, telegram, "ext"), "CommandHandler"), 'jobs', _n_(585606, "jobs", lambda: jobs)))
_l_(585609)
_c_(585616, _a_(585611, _n_(585610, "dispatcher", lambda: dispatcher), "add_handler"), _c_(585615, _a_(585613, _a_(585612, telegram, "ext"), "CommandHandler"), 'myinfo', _n_(585614, "myinfo", lambda: myinfo)))
_l_(585617)
_c_(585624, _a_(585619, _n_(585618, "dispatcher", lambda: dispatcher), "add_handler"), _c_(585623, _a_(585621, _a_(585620, telegram, "ext"), "CommandHandler"), 'latamsalaries', _n_(585622, "latamsalaries", lambda: latamsalaries)))
_l_(585625)

_c_(585628, _a_(585627, _n_(585626, "updater", lambda: updater), "start_polling"))
_l_(585629)
_c_(585632, _a_(585631, _n_(585630, "updater", lambda: updater), "idle"))
_l_(585633)