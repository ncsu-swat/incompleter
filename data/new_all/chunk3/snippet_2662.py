# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67511899/attributeerror-nonetype-object-has-no-attribute-send-when-i-try-to-send-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time, random, discord
    _l_(550255)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(550257)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(550259)

except ImportError:
    pass

bot = _c_(550262, _a_(550261, _n_(550260, "commands", lambda: commands), "Bot"), command_prefix='.')
_l_(550263)

@_c_(550266, _a_(550265, _n_(550264, "bot", lambda: bot), "command"))
async def time_messege(args):
    _l_(550336)

    
    alarmtime = "20:54"
    _l_(550267)
    

    #greeting_channel = bot.get_channel("814238156396298310")


    client = _c_(550270, _a_(550269, _n_(550268, "discord", lambda: discord), "Client"))
    _l_(550271)


    while True:
        _l_(550335)

      
        lcltime = _c_(550276, _a_(550275, _c_(550274, _a_(550273, _n_(550272, "datetime", lambda: datetime), "now")), "strftime"), '%H:%M')
        _l_(550277)

        if _n_(550278, "lcltime", lambda: lcltime) == _n_(550279, "alarmtime", lambda: alarmtime):
            _l_(550334)


            #aca pondria el code de detectar canal y enviar
            _c_(550281, _n_(550280, "print", lambda: print), "is time!")
            _l_(550282)

            random_num = _c_(550285, _a_(550284, _n_(550283, "random", lambda: random), "randint"), 1, 4)
            _l_(550286)

            if _n_(550287, "random_num", lambda: random_num) == 1:
                _l_(550322)

                #await greeting_channel.send("Holi!, como estan chic@s?")
                await _c_(550293, _a_(550289, _n_(550288, "client", lambda: client), "send_message"), _c_(550292, _a_(550291, _n_(550290, "discord", lambda: discord), "Object"), id='814238156396298310'), "Holi!, como estan chic@s?")
                _l_(550294)
            elif _n_(550295, "random_num", lambda: random_num) == 2:
                _l_(550321)

                #await greeting_channel.send("Holi!, oCmo va su dia? que me cuentan?")
                await _c_(550301, _a_(550297, _n_(550296, "client", lambda: client), "send_message"), _c_(550300, _a_(550299, _n_(550298, "discord", lambda: discord), "Object"), id='814238156396298310'), "Holi!, oCmo va su dia? que me cuentan?")
                _l_(550302)
            elif _n_(550303, "random_num", lambda: random_num) == 3:
                _l_(550320)

                #await greeting_channel.send("Holi!, Como va su dia? que andan haciendo?")
                await _c_(550309, _a_(550305, _n_(550304, "client", lambda: client), "send_message"), _c_(550308, _a_(550307, _n_(550306, "discord", lambda: discord), "Object"), id='814238156396298310'), "Holi!, Como va su dia? que andan haciendo?")
                _l_(550310)
            elif _n_(550311, "random_num", lambda: random_num) == 4:
                _l_(550319)

                #await greeting_channel.send("Holi!, como se encuentran?")
                await _c_(550317, _a_(550313, _n_(550312, "client", lambda: client), "send_message"), _c_(550316, _a_(550315, _n_(550314, "discord", lambda: discord), "Object"), id='814238156396298310'), "Holi!, como se encuentran?")
                _l_(550318)

            _c_(550325, _a_(550324, _n_(550323, "time", lambda: time), "sleep"), 90)
            _l_(550326)

        else:
            _c_(550328, _n_(550327, "print", lambda: print), "not yet")
            _l_(550329)
            _c_(550332, _a_(550331, _n_(550330, "time", lambda: time), "sleep"), 10)
            _l_(550333)