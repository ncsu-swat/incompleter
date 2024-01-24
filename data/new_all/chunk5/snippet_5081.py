# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74966994/attributeerror-chatforbidden-object-has-no-attribute-access-hash
# Log in into the telegram account
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
client = _c_(692092, _n_(692089, "TelegramClient", lambda: TelegramClient), 'Tg_scraper', _n_(692090, "api_id", lambda: api_id), _n_(692091, "api_hash", lambda: api_hash))
_l_(692093)

chats = []
_l_(692094)
last_date = None
_l_(692095)
chunk_size = 200
_l_(692096)
groups = []
_l_(692097)
hash_list = []
_l_(692098)

# Get all the groups/channel of the account
result = _c_(692106, _n_(692099, "client", lambda: client), _c_(692105, _n_(692100, "GetDialogsRequest", lambda: GetDialogsRequest), offset_date=_n_(692101, "last_date", lambda: last_date),
    offset_id=0,
    offset_peer=_c_(692103, _n_(692102, "InputPeerEmpty", lambda: InputPeerEmpty)),
    limit=_n_(692104, "chunk_size", lambda: chunk_size),
    hash=0
))
_l_(692107)
_c_(692112, _a_(692109, _n_(692108, "chats", lambda: chats), "extend"), _a_(692111, _n_(692110, "result", lambda: result), "chats"))
_l_(692113)

# Puts all the group/channel into a list
i = 0
_l_(692114)
_c_(692116, _n_(692115, "print", lambda: print), 'Enter a NUMBER to choose a group where the members will be invited into:')
_l_(692117)
for chat in _n_(692118, "chats", lambda: chats):
    _l_(692140)

    try:
        _l_(692139)

        _c_(692122, _a_(692120, _n_(692119, "groups", lambda: groups), "append"), _n_(692121, "chat", lambda: chat))
        _l_(692123)
        _c_(692128, _a_(692125, _n_(692124, "hash_list", lambda: hash_list), "append"), _a_(692127, _n_(692126, "chat", lambda: chat), "access_hash"))
        _l_(692129)
        _c_(692134, _n_(692130, "print", lambda: print), f"({_n_(692131, 'i', lambda: i)})" + ' - ' + _a_(692133, _n_(692132, "chat", lambda: chat), "title"))
        _l_(692135)
        i += 1
        _l_(692136)
    except:
        _l_(692138)

        continue
        _l_(692137)

g_index = _c_(692142, _n_(692141, "input", lambda: input), "Enter a Number: ")
_l_(692143)
target_group = _n_(692144, "groups", lambda: groups)[_c_(692147, _n_(692145, "int", lambda: int), _n_(692146, "g_index", lambda: g_index))]
_l_(692148)

target_group_entity = _c_(692154, _n_(692149, "InputPeerChannel", lambda: InputPeerChannel), _a_(692151, _n_(692150, "target_group", lambda: target_group), "id"), _a_(692153, _n_(692152, "target_group", lambda: target_group), "access_hash"))
_l_(692155)