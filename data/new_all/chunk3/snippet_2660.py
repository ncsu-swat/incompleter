# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67511899/attributeerror-nonetype-object-has-no-attribute-send-when-i-try-to-send-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time, random, discord
    _l_(540077)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(540079)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(540081)

except ImportError:
    pass


async def time_messege(args):
    _l_(540155)

    bot = _c_(540084, _a_(540083, _n_(540082, "commands", lambda: commands), "Bot"), command_prefix='.')
    _l_(540085)
    alarmtime = "19:23"
    _l_(540086)
    #greeting_channel = bot.get_channel("814238156396298310")
    #channel = bot.get_channel = xxx

    client = _c_(540089, _a_(540088, _n_(540087, "discord", lambda: discord), "Client"))
    _l_(540090)

    while True:
        _l_(540154)

      
        lcltime = _c_(540095, _a_(540094, _c_(540093, _a_(540092, _n_(540091, "datetime", lambda: datetime), "now")), "strftime"), '%H:%M')
        _l_(540096)

        if _n_(540097, "lcltime", lambda: lcltime) == _n_(540098, "alarmtime", lambda: alarmtime):
            _l_(540153)


            #aca pondria el code de detectar canal y enviar
            _c_(540100, _n_(540099, "print", lambda: print), "is time!")
            _l_(540101)

            random_num = _c_(540104, _a_(540103, _n_(540102, "random", lambda: random), "randint"), 1, 4)
            _l_(540105)

            if _n_(540106, "random_num", lambda: random_num) == 1:
                _l_(540141)

                #await greeting_channel.send("Holi!, como estan chic@s?")
                await _c_(540112, _a_(540108, _n_(540107, "client", lambda: client), "send_message"), _c_(540111, _a_(540110, _n_(540109, "discord", lambda: discord), "Object"), id='814238156396298310'), "Holi!, como estan chic@s?")
                _l_(540113)
            elif _n_(540114, "random_num", lambda: random_num) == 2:
                _l_(540140)

                #await greeting_channel.send("Holi!, oCmo va su dia? que me cuentan?")
                await _c_(540120, _a_(540116, _n_(540115, "client", lambda: client), "send_message"), _c_(540119, _a_(540118, _n_(540117, "discord", lambda: discord), "Object"), id='814238156396298310'), "Holi!, oCmo va su dia? que me cuentan?")
                _l_(540121)
            elif _n_(540122, "random_num", lambda: random_num) == 3:
                _l_(540139)

                #await greeting_channel.send("Holi!, Como va su dia? que andan haciendo?")
                await _c_(540128, _a_(540124, _n_(540123, "client", lambda: client), "send_message"), _c_(540127, _a_(540126, _n_(540125, "discord", lambda: discord), "Object"), id='814238156396298310'), "Holi!, Como va su dia? que andan haciendo?")
                _l_(540129)
            elif _n_(540130, "random_num", lambda: random_num) == 4:
                _l_(540138)

                #await greeting_channel.send("Holi!, como se encuentran?")
                await _c_(540136, _a_(540132, _n_(540131, "client", lambda: client), "send_message"), _c_(540135, _a_(540134, _n_(540133, "discord", lambda: discord), "Object"), id='814238156396298310'), "Holi!, como se encuentran?")
                _l_(540137)

            _c_(540144, _a_(540143, _n_(540142, "time", lambda: time), "sleep"), 90)
            _l_(540145)

        else:
            _c_(540147, _n_(540146, "print", lambda: print), "not yet")
            _l_(540148)
            _c_(540151, _a_(540150, _n_(540149, "time", lambda: time), "sleep"), 10)
            _l_(540152)