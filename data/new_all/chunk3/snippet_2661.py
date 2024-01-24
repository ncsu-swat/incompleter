# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67511899/attributeerror-nonetype-object-has-no-attribute-send-when-i-try-to-send-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time, random, discord
    _l_(544154)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(544156)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(544158)

except ImportError:
    pass


async def time_messege(args):
    _l_(544220)

    bot = _c_(544161, _a_(544160, _n_(544159, "commands", lambda: commands), "Bot"), command_prefix='.')
    _l_(544162)
    alarmtime = "19:36"
    _l_(544163)
    
    greeting_channel = _c_(544166, _a_(544165, _n_(544164, "bot", lambda: bot), "get_channel"), "814238156396298310")
    _l_(544167)
    #channel = bot.get_channel = xxx

    #client = discord.Client()


    while True:
        _l_(544219)

      
        lcltime = _c_(544172, _a_(544171, _c_(544170, _a_(544169, _n_(544168, "datetime", lambda: datetime), "now")), "strftime"), '%H:%M')
        _l_(544173)

        if _n_(544174, "lcltime", lambda: lcltime) == _n_(544175, "alarmtime", lambda: alarmtime):
            _l_(544218)


            #aca pondria el code de detectar canal y enviar
            _c_(544177, _n_(544176, "print", lambda: print), "is time!")
            _l_(544178)

            random_num = _c_(544181, _a_(544180, _n_(544179, "random", lambda: random), "randint"), 1, 4)
            _l_(544182)

            if _n_(544183, "random_num", lambda: random_num) == 1:
                _l_(544206)

                await _c_(544186, _a_(544185, _n_(544184, "greeting_channel", lambda: greeting_channel), "send"), "Holi!, como estan chic@s?")
                _l_(544187)
            elif _n_(544188, "random_num", lambda: random_num) == 2:
                _l_(544205)

                await _c_(544191, _a_(544190, _n_(544189, "greeting_channel", lambda: greeting_channel), "send"), "Holi!, oCmo va su dia? que me cuentan?")
                _l_(544192)
            elif _n_(544193, "random_num", lambda: random_num) == 3:
                _l_(544204)

                await _c_(544196, _a_(544195, _n_(544194, "greeting_channel", lambda: greeting_channel), "send"), "Holi!, Como va su dia? que andan haciendo?")
                _l_(544197)
            elif _n_(544198, "random_num", lambda: random_num) == 4:
                _l_(544203)

                await _c_(544201, _a_(544200, _n_(544199, "greeting_channel", lambda: greeting_channel), "send"), "Holi!, como se encuentran?")
                _l_(544202)

            _c_(544209, _a_(544208, _n_(544207, "time", lambda: time), "sleep"), 90)
            _l_(544210)

        else:
            _c_(544212, _n_(544211, "print", lambda: print), "not yet")
            _l_(544213)
            _c_(544216, _a_(544215, _n_(544214, "time", lambda: time), "sleep"), 10)
            _l_(544217)