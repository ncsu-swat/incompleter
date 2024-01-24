# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74966994/attributeerror-chatforbidden-object-has-no-attribute-access-hash
# Log in into the telegram account
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
client = _c_(668103, _n_(668100, "TelegramClient", lambda: TelegramClient), 'Tg_scraper', _n_(668101, "api_id", lambda: api_id), _n_(668102, "api_hash", lambda: api_hash))
_l_(668104)

chats = []
_l_(668105)
last_date = None
_l_(668106)
chunk_size = 200
_l_(668107)
groups = []
_l_(668108)
hash_list = []
_l_(668109)

# Get all the groups/channel of the account
result = _c_(668117, _n_(668110, "client", lambda: client), _c_(668116, _n_(668111, "GetDialogsRequest", lambda: GetDialogsRequest), offset_date=_n_(668112, "last_date", lambda: last_date),
    offset_id=0,
    offset_peer=_c_(668114, _n_(668113, "InputPeerEmpty", lambda: InputPeerEmpty)),
    limit=_n_(668115, "chunk_size", lambda: chunk_size),
    hash=0
))
_l_(668118)
_c_(668123, _a_(668120, _n_(668119, "chats", lambda: chats), "extend"), _a_(668122, _n_(668121, "result", lambda: result), "chats"))
_l_(668124)

# Puts all the group/channel into a list
i = 0
_l_(668125)
_c_(668127, _n_(668126, "print", lambda: print), 'Enter a NUMBER to choose a group where the members will be invited into:')
_l_(668128)
for chat in _n_(668129, "chats", lambda: chats):
    _l_(668151)

    try:
        _l_(668150)

        _c_(668133, _a_(668131, _n_(668130, "groups", lambda: groups), "append"), _n_(668132, "chat", lambda: chat))
        _l_(668134)
        _c_(668139, _a_(668136, _n_(668135, "hash_list", lambda: hash_list), "append"), _a_(668138, _n_(668137, "chat", lambda: chat), "access_hash"))
        _l_(668140)
        _c_(668145, _n_(668141, "print", lambda: print), f"({_n_(668142, 'i', lambda: i)})" + ' - ' + _a_(668144, _n_(668143, "chat", lambda: chat), "title"))
        _l_(668146)
        i += 1
        _l_(668147)
    except:
        _l_(668149)

        continue
        _l_(668148)

g_index = _c_(668153, _n_(668152, "input", lambda: input), "Enter a Number: ")
_l_(668154)
target_group = _n_(668155, "groups", lambda: groups)[_c_(668158, _n_(668156, "int", lambda: int), _n_(668157, "g_index", lambda: g_index))]
_l_(668159)

target_group_entity = _c_(668165, _n_(668160, "InputPeerChannel", lambda: InputPeerChannel), _a_(668162, _n_(668161, "target_group", lambda: target_group), "id"), _a_(668164, _n_(668163, "target_group", lambda: target_group), "access_hash"))
_l_(668166)