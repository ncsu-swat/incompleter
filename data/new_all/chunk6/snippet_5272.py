# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75137674/how-can-i-solve-the-attributeerror-nonetype-object-has-no-attribute-author
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(352564)

except ImportError:
    pass
try:
    import discord.ext
    _l_(352566)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(352568)

except ImportError:
    pass
try:
    import asyncio
    _l_(352570)

except ImportError:
    pass
try:
    import json
    _l_(352572)

except ImportError:
    pass
try:
    from apscheduler.schedulers.background import BackgroundScheduler
    _l_(352574)

except ImportError:
    pass
try:
    import time
    _l_(352576)

except ImportError:
    pass

intents = _c_(352580, _a_(352579, _a_(352578, _n_(352577, "discord", lambda: discord), "Intents"), "all"))
_l_(352581)
bot = _c_(352588, _a_(352583, _n_(352582, "commands", lambda: commands), "Bot"), command_prefix='/', intents=_c_(352587, _a_(352586, _a_(352585, _n_(352584, "discord", lambda: discord), "Intents"), "all")))
_l_(352589)


@_a_(352591, _n_(352590, "bot", lambda: bot), "event")
async def on_ready():
    _l_(352603)

    synced = await _c_(352595, _a_(352594, _a_(352593, _n_(352592, "bot", lambda: bot), "tree"), "sync"))
    _l_(352596)
    _c_(352601, _n_(352597, "print", lambda: print), f'Synced {_c_(352600, _n_(352598, "len", lambda: len), _n_(352599, "synced", lambda: synced))} command(s)')
    _l_(352602)


@_c_(352607, _a_(352606, _a_(352605, _n_(352604, 'bot', lambda: bot), 'tree'), 'command'), name='help', description='Displays a list of all available commands.')
async def help(interaction: _a_(352609, _n_(352608, 'discord', lambda: discord), 'Interaction')):
    _l_(352620)

    help_embed = _c_(352612, _a_(352611, _n_(352610, 'discord', lambda: discord), 'Embed'), title='Commands',
                               description='``!help``\n**Displays this help message.**\n\n``!taskdone``\n **Adds +1 to your amount of completed tasks.**\n\n``!viewtasks``\n**Displays a list of every developer and their number of completed tasks.**',
                               color=0x2f3136)
    _l_(352613)
    await _c_(352618, _a_(352616, _a_(352615, _n_(352614, 'interaction', lambda: interaction), 'response'), 'send_message'), embed=_n_(352617, 'help_embed', lambda: help_embed))
    _l_(352619)


@_c_(352624, _a_(352623, _a_(352622, _n_(352621, 'bot', lambda: bot), 'tree'), 'command'), name='ping', description= 'Shows latency.')
async def ping(interaction: _a_(352626, _n_(352625, 'discord', lambda: discord), 'Interaction')):
    _l_(352634)

    await _c_(352632, _a_(352629, _a_(352628, _n_(352627, 'interaction', lambda: interaction), 'response'), 'send_message'), f'**Latency:** {_a_(352631, _n_(352630, "bot", lambda: bot), "latency")} Milliseconds')
    _l_(352633)


@_c_(352638, _a_(352637, _a_(352636, _n_(352635, 'bot', lambda: bot), 'tree'), 'command'), name='taskdone', description ='Adds +1 to your amount of completed tasks.')
async def taskdone(interaction: _a_(352640, _n_(352639, 'discord', lambda: discord), 'Interaction')):
    _l_(352773)

    authorID = _c_(352646, _n_(352641, 'str', lambda: str), _a_(352645, _a_(352644, _a_(352643, _n_(352642, 'interaction', lambda: interaction), 'message'), 'author'), 'id'))
    _l_(352647)
    for guild in _a_(352649, _n_(352648, 'bot', lambda: bot), 'guilds'):
        _l_(352772)

        juniorDevs = _c_(352655, _a_(352652, _a_(352651, _n_(352650, 'discord', lambda: discord), 'utils'), 'get'), _a_(352654, _n_(352653, 'guild', lambda: guild), 'roles'), name='Junior Developers')
        _l_(352656)
        seniorDevs = _c_(352662, _a_(352659, _a_(352658, _n_(352657, 'discord', lambda: discord), 'utils'), 'get'), _a_(352661, _n_(352660, 'guild', lambda: guild), 'roles'), name='Senior Developers')
        _l_(352663)
        leadDevs = _c_(352669, _a_(352666, _a_(352665, _n_(352664, 'discord', lambda: discord), 'utils'), 'get'), _a_(352668, _n_(352667, 'guild', lambda: guild), 'roles'), name='Lead Developers')
        _l_(352670)
        projectManagers = _c_(352676, _a_(352673, _a_(352672, _n_(352671, 'discord', lambda: discord), 'utils'), 'get'), _a_(352675, _n_(352674, 'guild', lambda: guild), 'roles'), name="Project Managers")
        _l_(352677)

        if _n_(352678, 'juniorDevs', lambda: juniorDevs) in _a_(352682, _a_(352681, _a_(352680, _n_(352679, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(352683, 'seniorDevs', lambda: seniorDevs) in _a_(352687, _a_(352686, _a_(352685, _n_(352684, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(352688, 'leadDevs', lambda: leadDevs) in _a_(352692, _a_(352691, _a_(352690, _n_(352689, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(352693, 'projectManagers', lambda: projectManagers) in _a_(352697, _a_(352696, _a_(352695, _n_(352694, 'interaction', lambda: interaction), 'message'), 'author'), 'roles'):
            _l_(352771)

            with _c_(352699, _n_(352698, 'open', lambda: open), 'database.json', 'r') as f:
                _l_(352705)

                data = _c_(352703, _a_(352701, _n_(352700, 'json', lambda: json), 'load'), _n_(352702, 'f', lambda: f))
                _l_(352704)

            if _n_(352706, 'authorID', lambda: authorID) in _c_(352709, _a_(352708, _n_(352707, 'data', lambda: data), 'keys')):
                _l_(352739)

                _n_(352710, 'data', lambda: data)[_n_(352711, 'authorID', lambda: authorID)] += 1
                _l_(352712)

                with _c_(352714, _n_(352713, 'open', lambda: open), 'database.json', 'w') as f:
                    _l_(352721)

                    _c_(352719, _a_(352716, _n_(352715, 'json', lambda: json), 'dump'), _n_(352717, 'data', lambda: data), _n_(352718, 'f', lambda: f), indent=2)
                    _l_(352720)

            elif _n_(352722, 'authorID', lambda: authorID) not in _c_(352725, _a_(352724, _n_(352723, 'data', lambda: data), 'keys')):
                _l_(352738)

                _n_(352726, 'data', lambda: data)[_n_(352727, 'authorID', lambda: authorID)] = 1
                _l_(352728)

                with _c_(352730, _n_(352729, 'open', lambda: open), 'database.json', 'w') as f:
                    _l_(352737)

                    _c_(352735, _a_(352732, _n_(352731, 'json', lambda: json), 'dump'), _n_(352733, 'data', lambda: data), _n_(352734, 'f', lambda: f), indent=2)
                    _l_(352736)

            await _c_(352743, _a_(352742, _a_(352741, _n_(352740, 'interaction', lambda: interaction), 'response'), 'send_message'), '**Task amount updated!** :white_check_mark:')
            _l_(352744)
        elif _n_(352745, 'juniorDevs', lambda: juniorDevs) not in _a_(352749, _a_(352748, _a_(352747, _n_(352746, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(352750, 'seniorDevs', lambda: seniorDevs) not in _a_(352754, _a_(352753, _a_(352752, _n_(352751, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(352755, 'leadDevs', lambda: leadDevs) not in _a_(352759, _a_(352758, _a_(352757, _n_(352756, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(352760, 'projectManagers', lambda: projectManagers) not in _a_(352764, _a_(352763, _a_(352762, _n_(352761, 'interaction', lambda: interaction), 'message'), 'author'), 'roles'):
            _l_(352770)

            await _c_(352768, _a_(352767, _a_(352766, _n_(352765, 'interaction', lambda: interaction), 'response'), 'send_message'), '**You do not have permission to run this command!** :x:')
            _l_(352769)

@_c_(352777, _a_(352776, _a_(352775, _n_(352774, 'bot', lambda: bot), 'tree'), 'command'), name='viewtasks', description = 'Displays a list of every developer and their number of completed tasks.')
async def viewtasks(interaction: _a_(352779, _n_(352778, 'discord', lambda: discord), 'Interaction')):
    _l_(352888)

    for guild in _a_(352781, _n_(352780, 'bot', lambda: bot), 'guilds'):
        _l_(352887)

        juniorDevs = _c_(352787, _a_(352784, _a_(352783, _n_(352782, 'discord', lambda: discord), 'utils'), 'get'), _a_(352786, _n_(352785, 'guild', lambda: guild), 'roles'), name='Junior Developers')
        _l_(352788)
        seniorDevs = _c_(352794, _a_(352791, _a_(352790, _n_(352789, 'discord', lambda: discord), 'utils'), 'get'), _a_(352793, _n_(352792, 'guild', lambda: guild), 'roles'), name='Senior Developers')
        _l_(352795)
        leadDevs = _c_(352801, _a_(352798, _a_(352797, _n_(352796, 'discord', lambda: discord), 'utils'), 'get'), _a_(352800, _n_(352799, 'guild', lambda: guild), 'roles'), name='Lead Developers')
        _l_(352802)
        projectManagers = _c_(352808, _a_(352805, _a_(352804, _n_(352803, 'discord', lambda: discord), 'utils'), 'get'), _a_(352807, _n_(352806, 'guild', lambda: guild), 'roles'), name="Project Managers")
        _l_(352809)

        # Open the database file in read mode
        with _c_(352811, _n_(352810, 'open', lambda: open), 'database.json', 'r') as database:
            _l_(352817)

            # Load the contents of the file into a dictionary
            data = _c_(352815, _a_(352813, _n_(352812, 'json', lambda: json), 'load'), _n_(352814, 'database', lambda: database))
            _l_(352816)

        if _n_(352818, 'juniorDevs', lambda: juniorDevs) in _a_(352822, _a_(352821, _a_(352820, _n_(352819, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(352823, 'seniorDevs', lambda: seniorDevs) in _a_(352827, _a_(352826, _a_(352825, _n_(352824, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(352828, 'leadDevs', lambda: leadDevs) in _a_(352832, _a_(352831, _a_(352830, _n_(352829, 'interaction', lambda: interaction), 'message'), 'author'), 'roles') or _n_(352833, 'projectManagers', lambda: projectManagers) in _a_(352837, _a_(352836, _a_(352835, _n_(352834, 'interaction', lambda: interaction), 'message'), 'author'), 'roles'):
            _l_(352886)

            # Initialize the message
            message_text = ""
            _l_(352838)
            # Build the message using string formatting
            for user_id, value in _c_(352844, _n_(352839, 'sorted', lambda: sorted), _c_(352842, _a_(352841, _n_(352840, 'data', lambda: data), 'items')), key=lambda x: _n_(352843, 'x', lambda: x)[1], reverse=True):
                _l_(352848)

                message_text += f"<@{_n_(352845, 'user_id', lambda: user_id)}>**: {_n_(352846, 'value', lambda: value)}**\n"
                _l_(352847)

            # Create the embed
            task_embed = _c_(352852, _a_(352850, _n_(352849, "discord", lambda: discord), "Embed"), title='Tasks Completed This Week', description=_n_(352851, "message_text", lambda: message_text), color=0x2f3136)
            _l_(352853)

            # Send the embed
            await _c_(352858, _a_(352856, _a_(352855, _n_(352854, "interaction", lambda: interaction), "response"), "send_message"), embed=_n_(352857, "task_embed", lambda: task_embed))
            _l_(352859)

        elif _n_(352860, "juniorDevs", lambda: juniorDevs) not in _a_(352864, _a_(352863, _a_(352862, _n_(352861, "interaction", lambda: interaction), "message"), "author"), "roles") or _n_(352865, "seniorDevs", lambda: seniorDevs) not in _a_(352869, _a_(352868, _a_(352867, _n_(352866, "interaction", lambda: interaction), "message"), "author"), "roles") or _n_(352870, "leadDevs", lambda: leadDevs) not in _a_(352874, _a_(352873, _a_(352872, _n_(352871, "interaction", lambda: interaction), "message"), "author"), "roles") or _n_(352875, "projectManagers", lambda: projectManagers) not in _a_(352879, _a_(352878, _a_(352877, _n_(352876, "interaction", lambda: interaction), "message"), "author"), "roles"):
            _l_(352885)

            # The message author does not have one of the roles
            #Don't perform the code actions
            await _c_(352883, _a_(352882, _a_(352881, _n_(352880, "interaction", lambda: interaction), "response"), "send_message"), '**You do not have permission to run this command!** :x:')
            _l_(352884)


def reset_values():
    _l_(352913)

    # Open the database file in read mode
    with _c_(352890, _n_(352889, "open", lambda: open), 'database.json', 'r') as f:
        _l_(352896)

        # Load the contents of the file into a dictionary
        data = _c_(352894, _a_(352892, _n_(352891, "json", lambda: json), "load"), _n_(352893, "f", lambda: f))
        _l_(352895)

    # Iterate through the keys in the dictionary
    for key in _c_(352899, _a_(352898, _n_(352897, "data", lambda: data), "keys")):
        _l_(352903)

        # Set the value of each key to 0
        _n_(352900, "data", lambda: data)[_n_(352901, "key", lambda: key)] = 0
        _l_(352902)

    # Open the file in write mode
    with _c_(352905, _n_(352904, "open", lambda: open), 'database.json', 'w') as f:
        _l_(352912)

        # Write the updated dictionary to the file
        _c_(352910, _a_(352907, _n_(352906, "json", lambda: json), "dump"), _n_(352908, "data", lambda: data), _n_(352909, "f", lambda: f), indent=2)
        _l_(352911)


scheduler = _c_(352915, _n_(352914, "BackgroundScheduler", lambda: BackgroundScheduler))
_l_(352916)

# Schedule the reset_values function to run every Monday at 00:00
_c_(352920, _a_(352918, _n_(352917, "scheduler", lambda: scheduler), "add_job"), _n_(352919, "reset_values", lambda: reset_values), 'cron', day_of_week='1', hour=0, minute=0)
_l_(352921)

_c_(352924, _a_(352923, _n_(352922, "scheduler", lambda: scheduler), "start"))
_l_(352925)
# non-slash command part of code
@_a_(352927, _n_(352926, "bot", lambda: bot), "event")
async def on_message(message):
    _l_(352964)

    args = _c_(352935, _a_(352934, _c_(352933, _a_(352932, _c_(352931, _n_(352928, "str", lambda: str), _a_(352930, _n_(352929, "message", lambda: message), "content")), "lower")), "split"), ' ')
    _l_(352936)
    if _n_(352937, "args", lambda: args)[0] == 'bruh':
        _l_(352963)

        await _c_(352941, _a_(352940, _a_(352939, _n_(352938, "message", lambda: message), "channel"), "send"), '<:bruh_stone:1059119664543825950>')
        _l_(352942)

    elif _n_(352943, "args", lambda: args)[0] == "i'm" and _c_(352946, _a_(352944, " ", "join"), _n_(352945, "args", lambda: args)[1:]) == "horny":
        _l_(352962)

        await _c_(352950, _a_(352949, _a_(352948, _n_(352947, "message", lambda: message), "channel"), "send"), 'https://tenor.com/view/vorzek-vorzneck-oglg-og-lol-gang-gif-24901093')
        _l_(352951)

    elif _n_(352952, "args", lambda: args)[0] == "im" and _c_(352955, _a_(352953, " ", "join"), _n_(352954, "args", lambda: args)[1:]) == "horny":
        _l_(352961)

        await _c_(352959, _a_(352958, _a_(352957, _n_(352956, "message", lambda: message), "channel"), "send"), 'https://tenor.com/view/vorzek-vorzneck-oglg-og-lol-gang-gif-24901093')
        _l_(352960)


_c_(352967, _a_(352966, _n_(352965, "bot", lambda: bot), "run"), 'token')
_l_(352968)