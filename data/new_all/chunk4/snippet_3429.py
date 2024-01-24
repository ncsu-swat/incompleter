# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74468089/attributeerror-client-object-has-no-attribute-author-discord-bot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(600855)

except ImportError:
    pass
try:
    from amazon import search
    _l_(600857)

except ImportError:
    pass

TOKEN = 'hidden'
_l_(600858)
CHANNEL_ID = 'hidden'
_l_(600859)

client = _c_(600862, _a_(600861, _n_(600860, "discord", lambda: discord), "Client"))
_l_(600863)

@_a_(600865, _n_(600864, "client", lambda: client), "event")
async def on_message(message):
    _l_(600933)

    if _a_(600867, _n_(600866, "message", lambda: message), "author") == _a_(600869, _n_(600868, "client", lambda: client), "user"):
        _l_(600871)

        aux = "" 
        _l_(600870) 
        return aux 
#line 13
    if _a_(600874, _a_(600873, _n_(600872, "message", lambda: message), "channel"), "id") != _n_(600875, "CHANNEL_ID", lambda: CHANNEL_ID):
        _l_(600877)

        aux = ""
        _l_(600876)
        return aux

    if _c_(600881, _a_(600880, _a_(600879, _n_(600878, "message", lambda: message), "content"), "split"), ' ')[0] == '!amazon':
        _l_(600932)

        try:
            _l_(600931)

            query = _c_(600885, _a_(600884, _a_(600883, _n_(600882, "message", lambda: message), "content"), "replace"), '!amazon ', '')
            _l_(600886)

            item = _c_(600889, _n_(600887, "search", lambda: search), _n_(600888, "query", lambda: query))
            _l_(600890)

            embed = _c_(600895, _a_(600892, _n_(600891, "discord", lambda: discord), "Embed"), title=_n_(600893, "item", lambda: item)['title'],
                url='https://www.amazon.co.uk/' + _n_(600894, "item", lambda: item)['url']
            )
            _l_(600896)
            _c_(600900, _a_(600898, _n_(600897, "embed", lambda: embed), "set_thumbnail"), url=_n_(600899, "item", lambda: item)['img']
            )
            _l_(600901)
            _c_(600905, _a_(600903, _n_(600902, "embed", lambda: embed), "add_field"), name='Price',
                value=_n_(600904, "item", lambda: item)['price']
            )
            _l_(600906)
            _c_(600910, _a_(600908, _n_(600907, "embed", lambda: embed), "add_field"), name='Rating',
                value=_n_(600909, "item", lambda: item)['rating']
            )
            _l_(600911)
            _c_(600915, _a_(600913, _n_(600912, "embed", lambda: embed), "add_field"), name='Number of Ratings',
                value=_n_(600914, "item", lambda: item)['number_of_ratings']
            )
            _l_(600916)
            await _c_(600921, _a_(600919, _a_(600918, _n_(600917, "message", lambda: message), "channel"), "send"), embed=_n_(600920, "embed", lambda: embed))
            _l_(600922)
        except:
            _l_(600930)

            response = 'An error occurred with your request.'
            _l_(600923)
            await _c_(600928, _a_(600926, _a_(600925, _n_(600924, "message", lambda: message), "channel"), "send"), _n_(600927, "response", lambda: response))
            _l_(600929)

_c_(600937, _a_(600935, _n_(600934, "client", lambda: client), "run"), _n_(600936, "TOKEN", lambda: TOKEN))
_l_(600938)