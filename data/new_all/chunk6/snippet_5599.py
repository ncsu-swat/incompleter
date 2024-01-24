# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68582138/typeerror-on-voice-state-update-takes-3-positional-arguments-but-4-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(360150)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(360152)

except ImportError:
    pass
try:
    from pymongo import MongoClient
    _l_(360154)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(360156)

except ImportError:
    pass
try:
    import time
    _l_(360158)

except ImportError:
    pass
try:
    import os
    _l_(360160)

except ImportError:
    pass


client = _c_(360163, _a_(360162, _n_(360161, "commands", lambda: commands), "Bot"), command_prefix = "!")
_l_(360164)
cluster = _c_(360166, _n_(360165, "MongoClient", lambda: MongoClient), "mongodb://127.0.0.1:27017")
_l_(360167)
colluser = _a_(360170, _a_(360169, _n_(360168, "cluster", lambda: cluster), "chill"), "user")
_l_(360171)
collclan = _a_(360174, _a_(360173, _n_(360172, "cluster", lambda: cluster), "chill"), "clans")
_l_(360175)
collshop = _a_(360178, _a_(360177, _n_(360176, "cluster", lambda: cluster), "chill"), "shop")
_l_(360179)


@_a_(360181, _n_(360180, "client", lambda: client), "event")
async def on_ready():
    _l_(360213)

    # DiscordComponents(client)
    _c_(360183, _n_(360182, "print", lambda: print), "Bot connected to the server")
    _l_(360184)
    # post2 = {

    # }

    for guild in _a_(360186, _n_(360185, "client", lambda: client), "guilds"):
        _l_(360212)

        for member in _a_(360188, _n_(360187, "guild", lambda: guild), "members"):
            _l_(360211)

            post = {
                "_id": _a_(360190, _n_(360189, "member", lambda: member), "id"),
                "name": _a_(360192, _n_(360191, "member", lambda: member), "mention"),
                "user": _a_(360194, _n_(360193, "member", lambda: member), "name"),
                "inventory": [],
                "warms": 0,
                "mute": 0,
                "voice_activ": 0,
                "localban": 0,
                "register": _a_(360196, _n_(360195, "member", lambda: member), "created_at"),
                "onservfrom": _a_(360198, _n_(360197, "member", lambda: member), "joined_at"),
                "clan": 0,
                "marry": 0,
                "love": 0,
                "childs": [],
                "balance": 0,
                "bank": 0,
                "rep": 0,
                "cdxp": 0,
                "cnxp": 0,
                "dxp": 0,
                "nxp": 0,
                "cdbal": 0,
                "cdlvl": 1,
                "cnlvl": 1,
                "dlvl": 1,
                "nlvl": 1
            }
            _l_(360199)

            if _c_(360204, _a_(360201, _n_(360200, "colluser", lambda: colluser), "count_documents"), {"_id": _a_(360203, _n_(360202, "member", lambda: member), "id")}) == 0:
                _l_(360210)

                _c_(360208, _a_(360206, _n_(360205, "colluser", lambda: colluser), "insert_one"), _n_(360207, "post", lambda: post))
                _l_(360209)

@_a_(360215, _n_(360214, "client", lambda: client), "event")
async def on_guild_role_create(role):
    _l_(360233)

    _c_(360217, _n_(360216, "print", lambda: print), "new role created")
    _l_(360218)
    # print(f"{role.id}")
    # print(f"{role.name}")
    post = {
        "_id": _a_(360220, _n_(360219, "role", lambda: role), "id"),
        "titel": "none",
        "cp": [],
        "exp": 0,
        "lvl": 0,
        "maxcp": 7,
        "bank": 0
    }
    _l_(360221)

    if _c_(360226, _a_(360223, _n_(360222, "collclan", lambda: collclan), "count_documents"), {"role_id": _a_(360225, _n_(360224, "role", lambda: role), "id")}) == 0:
        _l_(360232)

        _c_(360230, _a_(360228, _n_(360227, "collclan", lambda: collclan), "insert_one"), _n_(360229, "post", lambda: post))
        _l_(360231)

@_a_(360235, _n_(360234, "client", lambda: client), "event")
async def on_voice_state_update(member, before, after):
    _l_(360388)

    data = _c_(360240, _a_(360237, _n_(360236, "colluser", lambda: colluser), "find_one"), {"_id": _a_(360239, _n_(360238, "member", lambda: member), "id")})
    _l_(360241)
    day = _n_(360242, "data", lambda: data)["dxp"]
    _l_(360243)
    dark = _n_(360244, "data", lambda: data)["nxp"]
    _l_(360245)
    dl = _n_(360246, "data", lambda: data)["dlvl"]
    _l_(360247)
    nl = _n_(360248, "data", lambda: data)["nlvl"]
    _l_(360249)
    dexp = 500 + 100 * _n_(360250, "dl", lambda: dl)
    _l_(360251)
    nexp = 500 + 100 * _n_(360252, "nl", lambda: nl)
    _l_(360253)
    if _a_(360255, _n_(360254, "before", lambda: before), "channel") is None and _a_(360257, _n_(360256, "after", lambda: after), "channel") is not None:
        _l_(360387)

        _c_(360259, _n_(360258, "print", lambda: print), "1")
        _l_(360260)
        t1 = _c_(360263, _a_(360262, _n_(360261, "time", lambda: time), "time"))
        _l_(360264)
        _c_(360270, _a_(360266, _n_(360265, "colluser", lambda: colluser), "update_one"), {"_id": _a_(360268, _n_(360267, "member", lambda: member), "id")},
            {"$set": {"voice_tim1": _n_(360269, "t1", lambda: t1)}})
        _l_(360271)
    elif _a_(360273, _n_(360272, "before", lambda: before), "channel") is not None and _a_(360275, _n_(360274, "after", lambda: after), "channel") is None:
        _l_(360386)

        dtn = _c_(360280, _a_(360279, _c_(360278, _a_(360277, _n_(360276, "datetime", lambda: datetime), "today")), "strftime"), "%I:%M %p")
        _l_(360281)
        t1 = _n_(360282, "data", lambda: data)["voice_tim1"]
        _l_(360283)
        voice_activ1 = _n_(360284, "data", lambda: data)["voice_activ"]
        _l_(360285)
        balance = _n_(360286, "data", lambda: data)["balance"]
        _l_(360287)
        t2 = _c_(360290, _a_(360289, _n_(360288, "time", lambda: time), "time"))
        _l_(360291)
        tim = _n_(360292, "t2", lambda: t2)-_n_(360293, "t1", lambda: t1)
        _l_(360294)
        _c_(360296, _n_(360295, "print", lambda: print), "0")
        _l_(360297)
        _c_(360300, _n_(360298, "print", lambda: print), _n_(360299, "dtn", lambda: dtn))
        _l_(360301)
        _c_(360308, _a_(360303, _n_(360302, "colluser", lambda: colluser), "update_one"), {"_id": _a_(360305, _n_(360304, "member", lambda: member), "id")},
            {"$set": {"voice_activ": _n_(360306, "voice_activ1", lambda: voice_activ1) + _n_(360307, "tim", lambda: tim)}})
        _l_(360309)
        _c_(360316, _a_(360311, _n_(360310, "colluser", lambda: colluser), "update_one"), {"_id": _a_(360313, _n_(360312, "member", lambda: member), "id")},
            {"$set": {"balance": _n_(360314, "balance", lambda: balance) + _n_(360315, "tim", lambda: tim) / 30}})
        _l_(360317)
        if _c_(360321, _n_(360318, "any", lambda: any), (("AM" in _n_(360319, "dtn", lambda: dtn)) for AM in _n_(360320, "dtn", lambda: dtn))):
            _l_(360333)

            _c_(360323, _n_(360322, "print", lambda: print), "time is AM")
            _l_(360324)
            _c_(360331, _a_(360326, _n_(360325, "colluser", lambda: colluser), "update_one"), {"_id": _a_(360328, _n_(360327, "member", lambda: member), "id")},
                {"$set": {"dxp": _n_(360329, "day", lambda: day) + _n_(360330, "tim", lambda: tim) / 4}})
            _l_(360332)
        if _c_(360337, _n_(360334, "any", lambda: any), (("PM" in _n_(360335, "dtn", lambda: dtn)) for PM in _n_(360336, "dtn", lambda: dtn))):
            _l_(360349)

            _c_(360339, _n_(360338, "print", lambda: print), "time is PM")
            _l_(360340)
            _c_(360347, _a_(360342, _n_(360341, "colluser", lambda: colluser), "update_one"), {"_id": _a_(360344, _n_(360343, "member", lambda: member), "id")},
                {"$set": {"nxp": _n_(360345, "dark", lambda: dark) + _n_(360346, "tim", lambda: tim) / 4}})
            _l_(360348)
        if _n_(360350, "data", lambda: data)["dxp"] >= 500 + 100 * _n_(360351, "dl", lambda: dl):
            _l_(360367)

            _c_(360357, _a_(360353, _n_(360352, "colluser", lambda: colluser), "update_one"), {"_id": _a_(360355, _n_(360354, "member", lambda: member), "id")},
                {"$set": {"dlvl": _n_(360356, "dl", lambda: dl) + 1}})
            _l_(360358)
            _c_(360365, _a_(360360, _n_(360359, "colluser", lambda: colluser), "update_one"), {"_id": _a_(360362, _n_(360361, "member", lambda: member), "id")},
                {"$set": {"dxp": _n_(360363, "day", lambda: day) - _n_(360364, "dexp", lambda: dexp)}})
            _l_(360366)
        if _n_(360368, "data", lambda: data)["nxp"] >= 500 + 100 * _n_(360369, "nl", lambda: nl):
            _l_(360385)

            _c_(360375, _a_(360371, _n_(360370, "colluser", lambda: colluser), "update_one"), {"_id": _a_(360373, _n_(360372, "member", lambda: member), "id")},
                {"$set": {"nlvl": _n_(360374, "nl", lambda: nl) + 1}})
            _l_(360376)
            _c_(360383, _a_(360378, _n_(360377, "colluser", lambda: colluser), "update_one"), {"_id": _a_(360380, _n_(360379, "member", lambda: member), "id")},
                {"$set": {"nxp": _n_(360381, "dark", lambda: dark) - _n_(360382, "nexp", lambda: nexp)}})
            _l_(360384)


@_a_(360390, _n_(360389, "client", lambda: client), "event")
async def on_member_join(member):
    _l_(360413)

    post = {
        "_id": _a_(360392, _n_(360391, "member", lambda: member), "id"),
        "name": _a_(360394, _n_(360393, "member", lambda: member), "mention"),
        "user": _a_(360396, _n_(360395, "member", lambda: member), "name"),
        "inventory": [],
        "warms": 0,
        "mute": 0,
        "voice_activ": 0,
        "localban": 0,
        "register": _a_(360398, _n_(360397, "member", lambda: member), "created_at"),
        "onservfrom": _a_(360400, _n_(360399, "member", lambda: member), "joined_at"),
        "clan": 0,
        "marry": 0,
        "love": 0,
        "childs": [],
        "balance": 0,
        "bank": 0,
        "xp": 0,
        "dxp": 0,
        "nxp": 0,
        "cdbal": 0,
        "lvl": 1,
        "dlvl": 1,
        "nlvl": 1
    }
    _l_(360401)

    if _c_(360406, _a_(360403, _n_(360402, "colluser", lambda: colluser), "count_documents"), {"_id": _a_(360405, _n_(360404, "member", lambda: member), "id")}) == 0:
        _l_(360412)

        _c_(360410, _a_(360408, _n_(360407, "colluser", lambda: colluser), "insert_one"), _n_(360409, "post", lambda: post))
        _l_(360411)


@_a_(360415, _n_(360414, "client", lambda: client), "event")
async def on_command_error(ctx, error):
    _l_(360446)

    _c_(360418, _n_(360416, "print", lambda: print), _n_(360417, "error", lambda: error))
    _l_(360419)

    if _c_(360424, _n_(360420, "isinstance", lambda: isinstance), _n_(360421, "error", lambda: error), _a_(360423, _n_(360422, "commands", lambda: commands), "UserInputError")):
        _l_(360445)

        await _c_(360443, _a_(360426, _n_(360425, "ctx", lambda: ctx), "send"), embed = _c_(360442, _a_(360428, _n_(360427, "discord", lambda: discord), "Embed"), description = f"Правильное использование команды: `{_a_(360430, _n_(360429, 'ctx', lambda: ctx), 'prefix')}{_a_(360433, _a_(360432, _n_(360431, 'ctx', lambda: ctx), 'command'), 'name')}` ({_a_(360436, _a_(360435, _n_(360434, 'ctx', lambda: ctx), 'command'), 'brief')}): `{_a_(360438, _n_(360437, 'ctx', lambda: ctx), 'prefix')}{_a_(360441, _a_(360440, _n_(360439, 'ctx', lambda: ctx), 'command'), 'usage')}`"
        ))
        _l_(360444)


@_c_(360449, _a_(360448, _n_(360447, "client", lambda: client), "command"))
@_c_(360452, _a_(360451, _n_(360450, "commands", lambda: commands), "is_owner"))
async def load(ctx, extension):
    _l_(360458)

    _c_(360456, _a_(360454, _n_(360453, "client", lambda: client), "load_extension"), f"cogs.{_n_(360455, 'extension', lambda: extension)}")
    _l_(360457)


@_c_(360461, _a_(360460, _n_(360459, "client", lambda: client), "command"))
@_c_(360464, _a_(360463, _n_(360462, "commands", lambda: commands), "is_owner"))
async def unload(ctx, extension):
    _l_(360470)

    _c_(360468, _a_(360466, _n_(360465, "client", lambda: client), "unload_extension"), f"cogs.{_n_(360467, 'extension', lambda: extension)}")
    _l_(360469)


@_c_(360473, _a_(360472, _n_(360471, "client", lambda: client), "command"))
@_c_(360476, _a_(360475, _n_(360474, "commands", lambda: commands), "is_owner"))
async def reload(ctx, extension):
    _l_(360487)

    _c_(360480, _a_(360478, _n_(360477, "client", lambda: client), "unload_extension"), f"cogs.{_n_(360479, 'extension', lambda: extension)}")
    _l_(360481)
    _c_(360485, _a_(360483, _n_(360482, "client", lambda: client), "load_extension"), f"cogs.{_n_(360484, 'extension', lambda: extension)}")
    _l_(360486)


for filename in _c_(360490, _a_(360489, _n_(360488, "os", lambda: os), "listdir"), "./cogs"):
    _l_(360500)

    if _c_(360493, _a_(360492, _n_(360491, "filename", lambda: filename), "endswith"), ".py"):
        _l_(360499)

        _c_(360497, _a_(360495, _n_(360494, "client", lambda: client), "load_extension"), f"cogs.{_n_(360496, 'filename', lambda: filename)[:-3]}")
        _l_(360498)


_c_(360503, _a_(360502, _n_(360501, "client", lambda: client), "run"), "TOKEN")
_l_(360504)