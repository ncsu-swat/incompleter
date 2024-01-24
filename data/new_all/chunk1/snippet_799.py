# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75137674/how-can-i-solve-the-attributeerror-nonetype-object-has-no-attribute-author
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(411886)

except ImportError:
    pass
try:
    import discord.ext
    _l_(411888)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(411890)

except ImportError:
    pass
try:
    import asyncio
    _l_(411892)

except ImportError:
    pass
try:
    import json
    _l_(411894)

except ImportError:
    pass
try:
    from apscheduler.schedulers.background import BackgroundScheduler
    _l_(411896)

except ImportError:
    pass
try:
    import time
    _l_(411898)

except ImportError:
    pass

intents = _c_(411902, _a_(411901, _a_(411900, _n_(411899, "discord", lambda: discord), "Intents"), "all"))
_l_(411903)
bot = _c_(411910, _a_(411905, _n_(411904, "commands", lambda: commands), "Bot"), command_prefix='/', intents=_c_(411909, _a_(411908, _a_(411907, _n_(411906, "discord", lambda: discord), "Intents"), "all")))
_l_(411911)


@_a_(411913, _n_(411912, "bot", lambda: bot), "event")
async def on_ready():
    _l_(411925)

    synced = await _c_(411917, _a_(411916, _a_(411915, _n_(411914, "bot", lambda: bot), "tree"), "sync"))
    _l_(411918)
    _c_(411923, _n_(411919, "print", lambda: print), f'Synced {_c_(411922, _n_(411920, "len", lambda: len), _n_(411921, "synced", lambda: synced))} command(s)')
    _l_(411924)


@_c_(411929, _a_(411928, _a_(411927, _n_(411926, 'bot', lambda: bot), 'tree'), 'command'), name='help', description='Displays a list of all available commands.')
async def help(interaction: _a_(411931, _n_(411930, 'discord', lambda: discord), 'Interaction')):
    _l_(411942)

    help_embed = _c_(411934, _a_(411933, _n_(411932, 'discord', lambda: discord), 'Embed'), title='Commands',
                               description='``!help``\n**Displays this help message.**\n\n``!taskdone``\n **Adds +1 to your amount of completed tasks.**\n\n``!viewtasks``\n**Displays a list of every developer and their number of completed tasks.**',
                               color=0x2f3136)
    _l_(411935)
    await _c_(411940, _a_(411938, _a_(411937, _n_(411936, 'interaction', lambda: interaction), 'response'), 'send_message'), embed=_n_(411939, 'help_embed', lambda: help_embed))
    _l_(411941)


@_c_(411946, _a_(411945, _a_(411944, _n_(411943, 'bot', lambda: bot), 'tree'), 'command'), name='ping', description= 'Shows latency.')
async def ping(interaction: _a_(411948, _n_(411947, 'discord', lambda: discord), 'Interaction')):
    _l_(411956)

    await _c_(411954, _a_(411951, _a_(411950, _n_(411949, 'interaction', lambda: interaction), 'response'), 'send_message'), f'**Latency:** {_a_(411953, _n_(411952, "bot", lambda: bot), "latency")} Milliseconds')
    _l_(411955)


@_c_(411960, _a_(411959, _a_(411958, _n_(411957, 'bot', lambda: bot), 'tree'), 'command'), name='taskdone', description ='Adds +1 to your amount of completed tasks.')
async def taskdone(interaction: _a_(411962, _n_(411961, 'discord', lambda: discord), 'Interaction')):
    _l_(412095)

    authorID = _c_(411968, _n_(411963, 'str', lambda: str), _a_(411967, _a_(411966, _a_(411965, _n_(411964, 'interaction', lambda: interaction), 'message'), 'author'), 'id'))
    _l_(411969)
    for guild in _a_(411971, _n_(411970, 'bot', lambda: bot), 'guilds'):
        _l_(412094)

        juniorDevs = _c_(411977, _a_(411974, _a_(411973, _n_(411972, 'discord', lambda: discord), 'utils'), 'get'), _a_(411976, _n_(411975, 'guild', lambda: guild), 'roles'), name='Junior Developers')
        _l_(411978)
        seniorDevs = _c_(411984, _a_(411981, _a_(411980, _n_(411979, 'discord', lambda: discord), 'utils'), 'get'), _a_(411983, _n_(411982, 'guild', lambda: guild), 'roles'), name='Senior Developers')
        _l_(411985)
        leadDevs = _c_(411991, _a_(411988, _a_(411987, _n_(411986, 'discord', lambda: discord), 'utils'), 'get'), _a_(411990, _n_(411989, 'guild', lambda: guild), 'roles'), name='Lead Developers')
        _l_(411992)
        projectManagers = _c_(411998, _a_(411995, _a_(411994, _n_(411993, 'discord', lambda: discord), 'utils'), 'get'), _a_(411997, _n_(411996, 'guild', lambda: guild), 'roles'), name="Project Managers")
        _l_(411999)

        if _n_(412000, 'juniorDevs', lambda: juniorDevs) in _a_(412004, _a_(412003, _a_(412002, _n_(412001, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(412005, 'seniorDevs', lambda: seniorDevs) in _a_(412009, _a_(412008, _a_(412007, _n_(412006, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(412010, 'leadDevs', lambda: leadDevs) in _a_(412014, _a_(412013, _a_(412012, _n_(412011, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(412015, 'projectManagers', lambda: projectManagers) in _a_(412019, _a_(412018, _a_(412017, _n_(412016, 'interaction', lambda: interaction), 'message'), 'author'), 'roles'):
            _l_(412093)

            with _c_(412021, _n_(412020, 'open', lambda: open), 'database.json', 'r') as f:
                _l_(412027)

                data = _c_(412025, _a_(412023, _n_(412022, 'json', lambda: json), 'load'), _n_(412024, 'f', lambda: f))
                _l_(412026)

            if _n_(412028, 'authorID', lambda: authorID) in _c_(412031, _a_(412030, _n_(412029, 'data', lambda: data), 'keys')):
                _l_(412061)

                _n_(412032, 'data', lambda: data)[_n_(412033, 'authorID', lambda: authorID)] += 1
                _l_(412034)

                with _c_(412036, _n_(412035, 'open', lambda: open), 'database.json', 'w') as f:
                    _l_(412043)

                    _c_(412041, _a_(412038, _n_(412037, 'json', lambda: json), 'dump'), _n_(412039, 'data', lambda: data), _n_(412040, 'f', lambda: f), indent=2)
                    _l_(412042)

            elif _n_(412044, 'authorID', lambda: authorID) not in _c_(412047, _a_(412046, _n_(412045, 'data', lambda: data), 'keys')):
                _l_(412060)

                _n_(412048, 'data', lambda: data)[_n_(412049, 'authorID', lambda: authorID)] = 1
                _l_(412050)

                with _c_(412052, _n_(412051, 'open', lambda: open), 'database.json', 'w') as f:
                    _l_(412059)

                    _c_(412057, _a_(412054, _n_(412053, 'json', lambda: json), 'dump'), _n_(412055, 'data', lambda: data), _n_(412056, 'f', lambda: f), indent=2)
                    _l_(412058)

            await _c_(412065, _a_(412064, _a_(412063, _n_(412062, 'interaction', lambda: interaction), 'response'), 'send_message'), '**Task amount updated!** :white_check_mark:')
            _l_(412066)
        elif _n_(412067, 'juniorDevs', lambda: juniorDevs) not in _a_(412071, _a_(412070, _a_(412069, _n_(412068, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(412072, 'seniorDevs', lambda: seniorDevs) not in _a_(412076, _a_(412075, _a_(412074, _n_(412073, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(412077, 'leadDevs', lambda: leadDevs) not in _a_(412081, _a_(412080, _a_(412079, _n_(412078, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(412082, 'projectManagers', lambda: projectManagers) not in _a_(412086, _a_(412085, _a_(412084, _n_(412083, 'interaction', lambda: interaction), 'message'), 'author'), 'roles'):
            _l_(412092)

            await _c_(412090, _a_(412089, _a_(412088, _n_(412087, 'interaction', lambda: interaction), 'response'), 'send_message'), '**You do not have permission to run this command!** :x:')
            _l_(412091)

@_c_(412099, _a_(412098, _a_(412097, _n_(412096, 'bot', lambda: bot), 'tree'), 'command'), name='viewtasks', description = 'Displays a list of every developer and their number of completed tasks.')
async def viewtasks(interaction: _a_(412101, _n_(412100, 'discord', lambda: discord), 'Interaction')):
    _l_(412210)

    for guild in _a_(412103, _n_(412102, 'bot', lambda: bot), 'guilds'):
        _l_(412209)

        juniorDevs = _c_(412109, _a_(412106, _a_(412105, _n_(412104, 'discord', lambda: discord), 'utils'), 'get'), _a_(412108, _n_(412107, 'guild', lambda: guild), 'roles'), name='Junior Developers')
        _l_(412110)
        seniorDevs = _c_(412116, _a_(412113, _a_(412112, _n_(412111, 'discord', lambda: discord), 'utils'), 'get'), _a_(412115, _n_(412114, 'guild', lambda: guild), 'roles'), name='Senior Developers')
        _l_(412117)
        leadDevs = _c_(412123, _a_(412120, _a_(412119, _n_(412118, 'discord', lambda: discord), 'utils'), 'get'), _a_(412122, _n_(412121, 'guild', lambda: guild), 'roles'), name='Lead Developers')
        _l_(412124)
        projectManagers = _c_(412130, _a_(412127, _a_(412126, _n_(412125, 'discord', lambda: discord), 'utils'), 'get'), _a_(412129, _n_(412128, 'guild', lambda: guild), 'roles'), name="Project Managers")
        _l_(412131)

        # Open the database file in read mode
        with _c_(412133, _n_(412132, 'open', lambda: open), 'database.json', 'r') as database:
            _l_(412139)

            # Load the contents of the file into a dictionary
            data = _c_(412137, _a_(412135, _n_(412134, 'json', lambda: json), 'load'), _n_(412136, 'database', lambda: database))
            _l_(412138)

        if _n_(412140, 'juniorDevs', lambda: juniorDevs) in _a_(412144, _a_(412143, _a_(412142, _n_(412141, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(412145, 'seniorDevs', lambda: seniorDevs) in _a_(412149, _a_(412148, _a_(412147, _n_(412146, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(412150, 'leadDevs', lambda: leadDevs) in _a_(412154, _a_(412153, _a_(412152, _n_(412151, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(412155, 'projectManagers', lambda: projectManagers) in _a_(412159, _a_(412158, _a_(412157, _n_(412156, 'interaction', lambda: interaction), 'message'), 'author'), 'roles'):
            _l_(412208)

            # Initialize the message
            message_text = ""
            _l_(412160)
            # Build the message using string formatting
            for user_id, value in _c_(412166, _n_(412161, 'sorted', lambda: sorted), _c_(412164, _a_(412163, _n_(412162, 'data', lambda: data), 'items')), key=lambda x: _n_(412165, 'x', lambda: x)[1], reverse=True):
                _l_(412170)

                message_text += f"<@{_n_(412167, 'user_id', lambda: user_id)}>**: {_n_(412168, 'value', lambda: value)}**\n"
                _l_(412169)

            # Create the embed
            task_embed = _c_(412174, _a_(412172, _n_(412171, "discord", lambda: discord), "Embed"), title='Tasks Completed This Week', description=_n_(412173, "message_text", lambda: message_text), color=0x2f3136)
            _l_(412175)

            # Send the embed
            await _c_(412180, _a_(412178, _a_(412177, _n_(412176, "interaction", lambda: interaction), "response"), "send_message"), embed=_n_(412179, "task_embed", lambda: task_embed))
            _l_(412181)

        elif _n_(412182, "juniorDevs", lambda: juniorDevs) not in _a_(412186, _a_(412185, _a_(412184, _n_(412183, "interaction", lambda: interaction), "message"), "author"), "roles") or _n_(412187, "seniorDevs", lambda: seniorDevs) not in _a_(412191, _a_(412190, _a_(412189, _n_(412188, "interaction", lambda: interaction), "message"), "author"), "roles") or _n_(412192, "leadDevs", lambda: leadDevs) not in _a_(412196, _a_(412195, _a_(412194, _n_(412193, "interaction", lambda: interaction), "message"), "author"), "roles") or _n_(412197, "projectManagers", lambda: projectManagers) not in _a_(412201, _a_(412200, _a_(412199, _n_(412198, "interaction", lambda: interaction), "message"), "author"), "roles"):
            _l_(412207)

            # The message author does not have one of the roles
            #Don't perform the code actions
            await _c_(412205, _a_(412204, _a_(412203, _n_(412202, "interaction", lambda: interaction), "response"), "send_message"), '**You do not have permission to run this command!** :x:')
            _l_(412206)


def reset_values():
    _l_(412235)

    # Open the database file in read mode
    with _c_(412212, _n_(412211, "open", lambda: open), 'database.json', 'r') as f:
        _l_(412218)

        # Load the contents of the file into a dictionary
        data = _c_(412216, _a_(412214, _n_(412213, "json", lambda: json), "load"), _n_(412215, "f", lambda: f))
        _l_(412217)

    # Iterate through the keys in the dictionary
    for key in _c_(412221, _a_(412220, _n_(412219, "data", lambda: data), "keys")):
        _l_(412225)

        # Set the value of each key to 0
        _n_(412222, "data", lambda: data)[_n_(412223, "key", lambda: key)] = 0
        _l_(412224)

    # Open the file in write mode
    with _c_(412227, _n_(412226, "open", lambda: open), 'database.json', 'w') as f:
        _l_(412234)

        # Write the updated dictionary to the file
        _c_(412232, _a_(412229, _n_(412228, "json", lambda: json), "dump"), _n_(412230, "data", lambda: data), _n_(412231, "f", lambda: f), indent=2)
        _l_(412233)


scheduler = _c_(412237, _n_(412236, "BackgroundScheduler", lambda: BackgroundScheduler))
_l_(412238)

# Schedule the reset_values function to run every Monday at 00:00
_c_(412242, _a_(412240, _n_(412239, "scheduler", lambda: scheduler), "add_job"), _n_(412241, "reset_values", lambda: reset_values), 'cron', day_of_week='1', hour=0, minute=0)
_l_(412243)

_c_(412246, _a_(412245, _n_(412244, "scheduler", lambda: scheduler), "start"))
_l_(412247)
# non-slash command part of code
@_a_(412249, _n_(412248, "bot", lambda: bot), "event")
async def on_message(message):
    _l_(412286)

    args = _c_(412257, _a_(412256, _c_(412255, _a_(412254, _c_(412253, _n_(412250, "str", lambda: str), _a_(412252, _n_(412251, "message", lambda: message), "content")), "lower")), "split"), ' ')
    _l_(412258)
    if _n_(412259, "args", lambda: args)[0] == 'bruh':
        _l_(412285)

        await _c_(412263, _a_(412262, _a_(412261, _n_(412260, "message", lambda: message), "channel"), "send"), '<:bruh_stone:1059119664543825950>')
        _l_(412264)

    elif _n_(412265, "args", lambda: args)[0] == "i'm" and _c_(412268, _a_(412266, " ", "join"), _n_(412267, "args", lambda: args)[1:]) == "horny":
        _l_(412284)

        await _c_(412272, _a_(412271, _a_(412270, _n_(412269, "message", lambda: message), "channel"), "send"), 'https://tenor.com/view/vorzek-vorzneck-oglg-og-lol-gang-gif-24901093')
        _l_(412273)

    elif _n_(412274, "args", lambda: args)[0] == "im" and _c_(412277, _a_(412275, " ", "join"), _n_(412276, "args", lambda: args)[1:]) == "horny":
        _l_(412283)

        await _c_(412281, _a_(412280, _a_(412279, _n_(412278, "message", lambda: message), "channel"), "send"), 'https://tenor.com/view/vorzek-vorzneck-oglg-og-lol-gang-gif-24901093')
        _l_(412282)


_c_(412289, _a_(412288, _n_(412287, "bot", lambda: bot), "run"), 'token')
_l_(412290)