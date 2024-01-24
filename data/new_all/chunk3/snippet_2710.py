# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65903474/nameerror-name-class-name-is-not-defined-issue
# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(535856)

except ImportError:
    pass
try:
    import os
    _l_(535858)

except ImportError:
    pass
try:
    import random
    _l_(535860)

except ImportError:
    pass
try:
    import time
    _l_(535862)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(535864)

except ImportError:
    pass

BMW330i = 'https://automanager.blob.core.windows.net/wmphotos/037685/1844fa46dd334f7dae94afc9ca49aa8a/eaa2cae362_800.jpg'
_l_(535865)
HONDAs2000 = 'https://cimg3.ibsrv.net/cimg/www.s2ki.com/1600x900_85-1/343/1-Make-Improvements-408343.jpg'
_l_(535866)
NISSANsilvia ='https://static.carthrottle.com/workspace/uploads/posts/2015/12/9a8cd0a4a74fb73c29f564f6e33aa20f.jpg'
_l_(535867)

users = 0
_l_(535868)

class user:
    _l_(535903)

    def __init__(self, name, car, car1,hp, hp1, carc, car1c, cari, car1i, money, daily):
        _l_(535902)

        _n_(535869, "self", lambda: self).name = _n_(535870, "name", lambda: name)
        _l_(535871)
        _n_(535872, "self", lambda: self).car = _n_(535873, "car", lambda: car)
        _l_(535874)
        _n_(535875, "self", lambda: self).car1 = _n_(535876, "car1", lambda: car1)
        _l_(535877)
        _n_(535878, "self", lambda: self).carc = _n_(535879, "carc", lambda: carc)
        _l_(535880)
        _n_(535881, "self", lambda: self).car1c = _n_(535882, "car1c", lambda: car1c)
        _l_(535883)
        _n_(535884, "self", lambda: self).hp = _n_(535885, "hp", lambda: hp)
        _l_(535886)
        _n_(535887, "self", lambda: self).hp1 = _n_(535888, "hp1", lambda: hp1)
        _l_(535889)
        _n_(535890, "self", lambda: self).money = _n_(535891, "money", lambda: money)
        _l_(535892)
        _n_(535893, "self", lambda: self).daily = _n_(535894, "daily", lambda: daily)
        _l_(535895)
        _n_(535896, "self", lambda: self).cari = _n_(535897, "cari", lambda: cari)
        _l_(535898)
        _n_(535899, "self", lambda: self).car1i = _n_(535900, "car1i", lambda: car1i)
        _l_(535901)

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = _c_(535906, _a_(535905, _n_(535904, "commands", lambda: commands), "Bot"), command_prefix=";")
_l_(535907)

@_c_(535910, _a_(535909, _n_(535908, "bot", lambda: bot), "command"))
async def test(message):
    _l_(535921)

    p1 = _c_(535912, _n_(535911, "user", lambda: user), 'imaad', 'd', 'd', 5, 5, 2, 2, 2, 2,2 ,2)
    _l_(535913)
    await _c_(535919, _a_(535916, _a_(535915, _n_(535914, "message", lambda: message), "channel"), "send"), _a_(535918, _n_(535917, "p1", lambda: p1), "name"))
    _l_(535920)
@_c_(535924, _a_(535923, _n_(535922, "bot", lambda: bot), "command"))
async def test1(message):
    _l_(535933)

    global p1
    _l_(535925)
    await _c_(535931, _a_(535928, _a_(535927, _n_(535926, "message", lambda: message), "channel"), "send"), _a_(535930, _n_(535929, "p1", lambda: p1), "name"))
    _l_(535932)

@_c_(535936, _a_(535935, _n_(535934, "bot", lambda: bot), "command"))
async def reg(cxt):
    _l_(536016)

    global users
    _l_(535937)
    carstart = _c_(535940, _a_(535939, _n_(535938, "random", lambda: random), "randint"), 1,3)
    _l_(535941)
    if _n_(535942, "users", lambda: users) == 0:
        _l_(536015)

        await _c_(535949, _a_(535945, _a_(535944, _n_(535943, "cxt", lambda: cxt), "channel"), "send"), 'Hey, ' + _a_(535948, _a_(535947, _n_(535946, "cxt", lambda: cxt), "author"), "name"))
        _l_(535950)
        if _n_(535951, "carstart", lambda: carstart) == 1:
            _l_(535960)

            p0 = _c_(535958, _n_(535952, "user", lambda: user), _c_(535956, _n_(535953, "str", lambda: str), _a_(535955, _n_(535954, "cxt", lambda: cxt), "author")), '2003 BMW 330i', 'Empty', (235), 'Empty', (9), 'Empty',  _n_(535957, "BMW330i", lambda: BMW330i), 'Empty', (1000), (0))
            _l_(535959)
        if _n_(535961, "carstart", lambda: carstart) == 2:
            _l_(535970)

            p0 = _c_(535968, _n_(535962, "user", lambda: user), _c_(535966, _n_(535963, "str", lambda: str), _a_(535965, _n_(535964, "cxt", lambda: cxt), "author")), '2000 Honda S2000', 'Empty', (240), 'Empty', (9), 'Empty',  _n_(535967, "HONDAs2000", lambda: HONDAs2000), 'Empty', (1000), (0))
            _l_(535969)
        if _n_(535971, "carstart", lambda: carstart) == 3:
            _l_(535980)

            p0 = _c_(535978, _n_(535972, "user", lambda: user), _c_(535976, _n_(535973, "str", lambda: str), _a_(535975, _n_(535974, "cxt", lambda: cxt), "author")),  '2000 Nissan Silvia', 'Empty', (243), 'Empty', (9), 'Empty',  _n_(535977, "NISSANsilvia", lambda: NISSANsilvia), 'Empty', (1000), (0))
            _l_(535979)
        await _c_(535992, _a_(535983, _a_(535982, _n_(535981, "cxt", lambda: cxt), "channel"), "send"), 'Welcome to Brooklyn, ' + _a_(535985, _n_(535984, "p0", lambda: p0), "name") + ' lucky for you I managed to fetch a ' + _a_(535987, _n_(535986, "p0", lambda: p0), "car") + ' with ' + _c_(535991, _n_(535988, "str", lambda: str), _a_(535990, _n_(535989, "p0", lambda: p0), "hp")) + 'HP')
        _l_(535993)
        await _c_(535999, _a_(535996, _a_(535995, _n_(535994, "cxt", lambda: cxt), "channel"), "send"), _a_(535998, _n_(535997, "p0", lambda: p0), "cari"))
        _l_(536000)
        await _c_(536006, _a_(536003, _a_(536002, _n_(536001, "cxt", lambda: cxt), "channel"), "send"), _a_(536005, _n_(536004, "p0", lambda: p0), "name"))
        _l_(536007)
        users = _n_(536008, "users", lambda: users) + 1
        _l_(536009)
    else:
        await _c_(536013, _a_(536012, _a_(536011, _n_(536010, "cxt", lambda: cxt), "channel"), "send"), 'k')
        _l_(536014)
        




# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
_c_(536019, _a_(536018, _n_(536017, "bot", lambda: bot), "run"), 'ODAxODA0NjY0ODM2MDYzMjQy.YAmAyA.snnqa9lOqYheREA0_PqH3GxK94E')
_l_(536020)