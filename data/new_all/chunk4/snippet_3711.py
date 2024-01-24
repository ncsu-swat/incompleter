# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69509069/getting-typeerror-when-trying-to-log-messages-in-discord
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(589470, _a_(589469, _n_(589468, "bot", lambda: bot), "command"))
@_c_(589473, _a_(589472, _n_(589471, "commands", lambda: commands), "has_permissions"), administrator = True)
async def logsave(ctx, amount = None, logName = None):
    _l_(589644)

    #Checks if user input an amount, either a number or "all".
    if _n_(589474, "amount", lambda: amount) == None:
        _l_(589491)

        desc = f'**Specify an amount**'
        _l_(589475)
        errorEmbed = _c_(589483, _a_(589477, _n_(589476, 'discord', lambda: discord), 'Embed'), title = f'**Log**', description = _n_(589478, 'desc', lambda: desc), colour = _c_(589482, _a_(589481, _a_(589480, _n_(589479, 'discord', lambda: discord), 'Color'), 'from_rgb'), 36, 227, 170))
        _l_(589484)
        await _c_(589488, _a_(589486, _n_(589485, 'ctx', lambda: ctx), 'send'), embed = _n_(589487, 'errorEmbed', lambda: errorEmbed))
        _l_(589489)
        aux = ""
        _l_(589490)
        return aux

    #Checks if user input a name for the log.
    if _n_(589492, 'logName', lambda: logName) == None:
        _l_(589509)

        desc = f'**Specify a name.**'
        _l_(589493)
        errorEmbed = _c_(589501, _a_(589495, _n_(589494, 'discord', lambda: discord), 'Embed'), title = f'**Log**', description = _n_(589496, 'desc', lambda: desc), colour = _c_(589500, _a_(589499, _a_(589498, _n_(589497, 'discord', lambda: discord), 'Color'), 'from_rgb'), 36, 227, 170))
        _l_(589502)
        logMsg = await _c_(589506, _a_(589504, _n_(589503, 'ctx', lambda: ctx), 'send'), embed = _n_(589505, 'errorEmbed', lambda: errorEmbed))
        _l_(589507)
        aux = ""
        _l_(589508)
        return aux

    #Checks if user input "all"
    if _c_(589512, _a_(589511, _n_(589510, 'amount', lambda: amount), 'lower')) == 'all':
        _l_(589515)

        isAll = True
        _l_(589513)
    else:
        isAll = False
        _l_(589514)

    #Gets message history
    channel = _a_(589517, _n_(589516, 'ctx', lambda: ctx), 'channel')
    _l_(589518)
    if _n_(589519, 'isAll', lambda: isAll):
        _l_(589550)

        desc = f'**Started Logging**'
        _l_(589520)
        startEmbed = _c_(589528, _a_(589522, _n_(589521, 'discord', lambda: discord), 'Embed'), title = f'**Log**', description = _n_(589523, 'desc', lambda: desc), colour = _c_(589527, _a_(589526, _a_(589525, _n_(589524, 'discord', lambda: discord), 'Color'), 'from_rgb'), 36, 227, 170))
        _l_(589529)
        logMsg = await _c_(589533, _a_(589531, _n_(589530, 'ctx', lambda: ctx), 'send'), embed = _n_(589532, 'startEmbed', lambda: startEmbed))
        _l_(589534)
        messages = await _c_(589539, _a_(589538, _c_(589537, _a_(589536, _n_(589535, 'channel', lambda: channel), 'history'), limit = None, oldest_first = True), 'flatten'))
        _l_(589540)
    else:
        messages = await _c_(589548, _a_(589547, _c_(589546, _a_(589542, _n_(589541, 'channel', lambda: channel), 'history'), limit = _c_(589545, _n_(589543, 'int', lambda: int), _n_(589544, 'amount', lambda: amount)), oldest_first = True), 'flatten'))
        _l_(589549)

    #Loads previous logs for editing
    logsFile = _c_(589553, _n_(589551, 'open', lambda: open), f'{_n_(589552, "currentDirectory", lambda: currentDirectory)}\Saved\logs.json', 'r+')
    _l_(589554)
    logsJson = _c_(589558, _a_(589556, _n_(589555, 'json', lambda: json), 'load'), _n_(589557, 'logsFile', lambda: logsFile))
    _l_(589559)

    #Creates new message log in JSON
    logCount = _n_(589560, 'logsJson', lambda: logsJson)[_n_(589561, 'messages', lambda: messages)][-1]["count"] + 1
    _l_(589562)
    newLog = {
        "name": _n_(589563, 'logName', lambda: logName),
        "creator": _a_(589565, _n_(589564, 'ctx', lambda: ctx), 'author'),
        "msgs": [],
        "count": _n_(589566, 'logCount', lambda: logCount)
    }
    _l_(589567)
    _c_(589571, _a_(589569, _n_(589568, 'logsJson', lambda: logsJson)["messageLogs"], 'append'), _n_(589570, 'newLog', lambda: newLog))
    _l_(589572)

    #Stars logging the messages, I'm pretty sure this is where my error is coming from.
    for msg in _n_(589573, 'messages', lambda: messages):
        _l_(589614)

        msgAuthor = _a_(589575, _n_(589574, 'msg', lambda: msg), 'author')
        _l_(589576)
        if _a_(589578, _n_(589577, 'msgAuthor', lambda: msgAuthor), 'bot'):
            _l_(589580)

            aux = ""
            _l_(589579)
            return aux
        _c_(589582, _n_(589581, 'print', lambda: print), "done")
        _l_(589583)
        msgContent = _a_(589585, _n_(589584, 'msg', lambda: msg), 'content')
        _l_(589586)
        msgAttachments = _a_(589588, _n_(589587, 'msg', lambda: msg), 'attachments')
        _l_(589589)
        msgCreated = _a_(589591, _n_(589590, 'msg', lambda: msg), 'created_at')
        _l_(589592)
        msgWrite = f'\n{_n_(589593, "msgAuthor", lambda: msgAuthor)} [{_n_(589594, "msgCreated", lambda: msgCreated)}]\n{_n_(589595, "msgContent", lambda: msgContent)}'
        _l_(589596)
        newMessage = {
            "id": _a_(589598, _n_(589597, 'msg', lambda: msg), 'id'),
            "authorname": _c_(589601, _n_(589599, 'str', lambda: str), _n_(589600, 'msgAuthor', lambda: msgAuthor)),
            "authorid": _a_(589603, _n_(589602, 'msgAuthor', lambda: msgAuthor), 'id'),
            "content": _n_(589604, 'msgWrite', lambda: msgWrite),
            "published": _n_(589605, 'msgCreated', lambda: msgCreated),
            "attachments": _n_(589606, 'msgAttachments', lambda: msgAttachments)
        }
        _l_(589607)
        _c_(589612, _a_(589610, _n_(589608, 'logsJson', lambda: logsJson)["messageLogs"][_n_(589609, 'logCount', lambda: logCount)]["msgs"], 'append'), _n_(589611, 'newMessage', lambda: newMessage))
        _l_(589613)

    #Edits previous log.
    _c_(589619, _a_(589616, _n_(589615, 'json', lambda: json), 'dump'), _n_(589617, 'logsJson', lambda: logsJson), _n_(589618, 'logsFile', lambda: logsFile))
    _l_(589620)
    _c_(589623, _a_(589622, _n_(589621, 'logsFile', lambda: logsFile), 'close'))
    _l_(589624)

    #Ends
    _c_(589627, _a_(589626, _n_(589625, 'logMsg', lambda: logMsg), 'delete'))
    _l_(589628)
    desc = f'**Finished Logging**'
    _l_(589629)
    endEmbed = _c_(589637, _a_(589631, _n_(589630, 'discord', lambda: discord), 'Embed'), title = f'**Log**', description = _n_(589632, 'desc', lambda: desc), colour = _c_(589636, _a_(589635, _a_(589634, _n_(589633, 'discord', lambda: discord), 'Color'), 'from_rgb'), 36, 227, 170))
    _l_(589638)
    await _c_(589642, _a_(589640, _n_(589639, 'ctx', lambda: ctx), 'send'), embed = _n_(589641, 'endEmbed', lambda: endEmbed))
    _l_(589643)