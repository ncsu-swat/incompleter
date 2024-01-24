# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72251386/typeerror-object-of-type-coroutine-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import configparser
    _l_(585362)

except ImportError:
    pass
try:
    import json
    _l_(585364)

except ImportError:
    pass
try:
    import datetime
    _l_(585366)

except ImportError:
    pass
try:
    from telethon.sync import TelegramClient , events
    _l_(585368)

except ImportError:
    pass
try:
    from telethon import connection
    _l_(585370)

except ImportError:
    pass
try:
    from datetime import date, datetime
    _l_(585372)

except ImportError:
    pass
try:
    from telethon.tl.functions.channels import GetParticipantsRequest
    _l_(585374)

except ImportError:
    pass
try:
    from telethon.tl.types import ChannelParticipantsSearch
    _l_(585376)

except ImportError:
    pass
try:
    from telethon.tl.functions.messages import GetHistoryRequest
    _l_(585378)

except ImportError:
    pass


config = _c_(585381, _a_(585380, _n_(585379, "configparser", lambda: configparser), "ConfigParser"))
_l_(585382)
_c_(585385, _a_(585384, _n_(585383, "config", lambda: config), "read"), "config.ini")
_l_(585386)


api_id   = _n_(585387, "config", lambda: config)['Telegram']['api_id']
_l_(585388)
api_hash = _n_(585389, "config", lambda: config)['Telegram']['api_hash']
_l_(585390)
username = _n_(585391, "config", lambda: config)['Telegram']['username']
_l_(585392)
bot__token = _n_(585393, "config", lambda: config)['Telegram']['bot_token']
_l_(585394)

client = _c_(585399, _n_(585395, "TelegramClient", lambda: TelegramClient), _n_(585396, "username", lambda: username), _n_(585397, "api_id", lambda: api_id), _n_(585398, "api_hash", lambda: api_hash) )
_l_(585400)
bot = _c_(585407, _a_(585405, _c_(585404, _n_(585401, "TelegramClient", lambda: TelegramClient), 'bot' , _n_(585402, "api_id", lambda: api_id) , _n_(585403, "api_hash", lambda: api_hash) ), "start"), bot_token = _n_(585406, "bot__token", lambda: bot__token) )
_l_(585408)


current_action = ''
_l_(585409)

async def dump_all_messages(channel):
    _l_(585494)

    offset_msg = 0 
    _l_(585410) 
    limit_msg = 100
    _l_(585411)
    
    all_messages = []
    _l_(585412)
    total_messages = 0
    _l_(585413)
    total_count_limit = 2
    _l_(585414)
    
    class DateTimeEncoder(_a_(585416, _n_(585415, "json", lambda: json), "JSONEncoder")):
        _l_(585443)

        
        def default(self, o):
            _l_(585442)

            if _c_(585420, _n_(585417, "isinstance", lambda: isinstance), _n_(585418, "o", lambda: o), _n_(585419, "datetime", lambda: datetime)):
                _l_(585425)

                aux = _c_(585423, _a_(585422, _n_(585421, "o", lambda: o), "isoformat"))
                _l_(585424)
                return aux
            if _c_(585429, _n_(585426, "isinstance", lambda: isinstance), _n_(585427, "o", lambda: o), _n_(585428, "bytes", lambda: bytes)):
                _l_(585434)

                aux = _c_(585432, _n_(585430, "list", lambda: list), _n_(585431, "o", lambda: o))
                _l_(585433)
                return aux
            aux = _c_(585440, _a_(585437, _a_(585436, _n_(585435, "json", lambda: json), "JSONEncoder"), "default"), _n_(585438, "self", lambda: self), _n_(585439, "o", lambda: o))
            _l_(585441)
            return aux
    while True:
        _l_(585483)

        history = await _c_(585450, _n_(585444, "client", lambda: client), _c_(585449, _n_(585445, "GetHistoryRequest", lambda: GetHistoryRequest), peer=_n_(585446, "channel", lambda: channel),
                offset_id=_n_(585447, "offset_msg", lambda: offset_msg),
                offset_date=None,
                add_offset=0,
                limit=_n_(585448, "limit_msg", lambda: limit_msg), 
                max_id=0, 
                min_id=0,
                hash=0
            )
        )
        _l_(585451)
        if not _a_(585453, _n_(585452, "history", lambda: history), "messages"):
            _l_(585455)

            break
            _l_(585454)
        messages = _a_(585457, _n_(585456, "history", lambda: history), "messages")
        _l_(585458)
        for message in _n_(585459, "messages", lambda: messages):
            _l_(585467)

            _c_(585465, _a_(585461, _n_(585460, "all_messages", lambda: all_messages), "append"), _c_(585464, _a_(585463, _n_(585462, "message", lambda: message), "to_dict")))
            _l_(585466)
        offset_msg = _a_(585472, _n_(585468, "messages", lambda: messages)[_c_(585471, _n_(585469, "len", lambda: len), _n_(585470, "messages", lambda: messages)) - 1], "id")
        _l_(585473)
        total_messages = _c_(585476, _n_(585474, "len", lambda: len), _n_(585475, "all_messages", lambda: all_messages))
        _l_(585477)
        if _n_(585478, "total_count_limit", lambda: total_count_limit) != 0 and _n_(585479, "total_messages", lambda: total_messages) >= _n_(585480, "total_count_limit", lambda: total_count_limit):
            _l_(585482)

            break
            _l_(585481)
    with _c_(585485, _n_(585484, "open", lambda: open), 'channel_messages.json', 'w', encoding='utf8') as outfile:
        _l_(585493)

        _c_(585491, _a_(585487, _n_(585486, "json", lambda: json), "dump"), _n_(585488, "all_messages", lambda: all_messages), _n_(585489, "outfile", lambda: outfile), ensure_ascii=False, cls=_n_(585490, "DateTimeEncoder", lambda: DateTimeEncoder))
        _l_(585492)



@_c_(585499, _a_(585496, _n_(585495, "bot", lambda: bot), "on"), _a_(585498, _n_(585497, "events", lambda: events), "NewMessage") )
async def list( event ):
    _l_(585515)

    match _n_(585500, "current_action", lambda: current_action):
        case '/tracking':
            channel = await _c_(585506, _a_(585502, _n_(585501, "client", lambda: client), "get_entity"), _a_(585505, _a_(585504, _n_(585503, "event", lambda: event), "message"), "message") )
            _l_(585507)
            await _c_(585510, _n_(585508, "dump_all_messages", lambda: dump_all_messages), _n_(585509, "channel", lambda: channel) )
            _l_(585511)
            raise _a_(585513, _n_(585512, "events", lambda: events), "StopPropagation")
            _l_(585514)


@_c_(585521, _a_(585517, _n_(585516, "bot", lambda: bot), "on"), _c_(585520, _a_(585519, _n_(585518, "events", lambda: events), "NewMessage"), pattern = '/tracking' ) )
async def link(event):
    _l_(585531)

    global current_action
    _l_(585522)
    current_action = '/tracking'
    _l_(585523)
    await _c_(585526, _a_(585525, _n_(585524, "event", lambda: event), "respond"), 'I\'m expecting a link')
    _l_(585527)
    raise _a_(585529, _n_(585528, "events", lambda: events), "StopPropagation")
    _l_(585530)

_c_(585534, _a_(585533, _n_(585532, "client", lambda: client), "start"))
_l_(585535)
_c_(585538, _a_(585537, _n_(585536, "bot", lambda: bot), "run_until_disconnected"))
_l_(585539)