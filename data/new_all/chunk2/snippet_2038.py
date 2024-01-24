# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67687865/typeerror-can-only-concatenate-str-not-list-to-str-when-using-a-txt-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(454103)

except ImportError:
    pass
try:
    import json
    _l_(454105)

except ImportError:
    pass
try:
    from discord_webhook import DiscordWebhook, DiscordEmbed
    _l_(454107)

except ImportError:
    pass
try:
    import pyfiglet
    _l_(454109)

except ImportError:
    pass
try:
    from pyfiglet import figlet_format
    _l_(454111)

except ImportError:
    pass
try:
    import colorama
    _l_(454113)

except ImportError:
    pass
try:
    from colorama import Fore, Style
    _l_(454115)

except ImportError:
    pass

_c_(454118, _a_(454117, _n_(454116, "colorama", lambda: colorama), "init"))
_l_(454119)

def title():
    _l_(454132)

    _c_(454123, _n_(454120, "print", lambda: print), _c_(454122, _n_(454121, "figlet_format", lambda: figlet_format), "Gxzs's Checker!"))
    _l_(454124)
    _c_(454130, _n_(454125, "print", lambda: print), _a_(454127, _n_(454126, "Fore", lambda: Fore), "CYAN") + 'Contact me on Discord Gxzs#3448 for Inquiries' + _a_(454129, _n_(454128, "Fore", lambda: Fore), "CYAN"))
    _l_(454131)

_c_(454134, _n_(454133, "title", lambda: title))
_l_(454135)


def check():
    _l_(454217)

    _c_(454138, _a_(454137, _n_(454136, "colorama", lambda: colorama), "init"))
    _l_(454139)
    token = _c_(454141, _n_(454140, "input", lambda: input), "Enter token > ")
    _l_(454142)
    
    username = [_c_(454145, _a_(454144, _n_(454143, "line", lambda: line), "strip")) for line in _c_(454147, _n_(454146, "open", lambda: open), "usernames.txt")]
    _l_(454148)
    
    r = _c_(454153, _a_(454150, _n_(454149, "requests", lambda: requests), "get"), "https://public-ubiservices.ubi.com/v2/profiles?nameOnPlatform=" + _n_(454151, "username", lambda: username) + "&platformType=uplay", headers = {
                'Method':'GET',
                'Authority':'public-ubiservices.ubi.com',
                'Ubi-AppId':'880650b9-35a5-4480-8f32-6a328eaa3aad',
                'Authorization': _n_(454152, "token", lambda: token),
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                'Ubi-RequestedPlatformType':'uplay',
                })   
    _l_(454154)   
      
    userWasFound = _c_(454159, _n_(454155, "len", lambda: len), _c_(454158, _a_(454157, _n_(454156, "r", lambda: r), "json"))['profiles']) != 0
    _l_(454160)
    for i in _c_(454162, _n_(454161, "range", lambda: range), 5):
        _l_(454166)

        _c_(454164, _n_(454163, "print", lambda: print), " ")
        _l_(454165)
    if _n_(454167, "userWasFound", lambda: userWasFound) == False:
        _l_(454206)

        _c_(454174, _n_(454168, "print", lambda: print), _n_(454169, "username", lambda: username) + _a_(454171, _n_(454170, "Fore", lambda: Fore), "WHITE") + ' is available! :)' + _a_(454173, _n_(454172, "Fore", lambda: Fore), "WHITE"))
        _l_(454175)
        with _c_(454177, _n_(454176, "open", lambda: open), "available.txt", 'a') as f:
            _l_(454183)

            _c_(454181, _a_(454179, _n_(454178, "f", lambda: f), "write"), f"{_n_(454180, 'username', lambda: username)}\n")
            _l_(454182)
        webhook = _c_(454185, _n_(454184, "DiscordWebhook", lambda: DiscordWebhook), url='https://discord.com/api/webhooks/845031037838688297/N8cjHEwfhoYV-kWgSCA8L5vpMP8C32RsuPz29rTawAx7qtXqzlTV5DNuD7cKYPSSkWbw')
        _l_(454186)
        embed = _c_(454189, _n_(454187, "DiscordEmbed", lambda: DiscordEmbed), title="Gxzs' Ubisoft Service", description= _n_(454188, "username", lambda: username) + " is available or restricted", color='03b2f8')
        _l_(454190)
        _c_(454194, _a_(454192, _n_(454191, "webhook", lambda: webhook), "add_embed"), _n_(454193, "embed", lambda: embed))
        _l_(454195)
        _c_(454198, _a_(454197, _n_(454196, "embed", lambda: embed), "set_image"), url='https://media2.giphy.com/media/y8fXirTJjj6E0/giphy.gif?cid=ecf05e47foeqh9oalc5del7633idlrw3jg0jp7jo3fs7o8j3&rid=giphy.gif&ct=g')
        _l_(454199)
        response = _c_(454202, _a_(454201, _n_(454200, "webhook", lambda: webhook), "execute"))
        _l_(454203)
        username="Gxzs' uPlay Bot",
        _l_(454204)
        avatar_url="https://i.4cdn.org/soc/1620674149395.png"
        _l_(454205)

    if _n_(454207, "userWasFound", lambda: userWasFound) == True:
        _l_(454216)

        _c_(454214, _n_(454208, "print", lambda: print), _n_(454209, "username", lambda: username) + _a_(454211, _n_(454210, "Fore", lambda: Fore), "WHITE") + ' is taken :( ' + _a_(454213, _n_(454212, "Fore", lambda: Fore), "WHITE"))
        _l_(454215)

_c_(454223, _n_(454218, "print", lambda: print), _a_(454220, _n_(454219, "Fore", lambda: Fore), "CYAN") + "Press ENTER to start the process..." + _a_(454222, _n_(454221, "Fore", lambda: Fore), "CYAN"))
_l_(454224)
_c_(454226, _n_(454225, "input", lambda: input), "")
_l_(454227)
_c_(454229, _n_(454228, "check", lambda: check))
_l_(454230)