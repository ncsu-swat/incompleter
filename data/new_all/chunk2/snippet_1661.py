# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66005708/discord-custom-activity-attribute-error-emoji-object-doesnt-have-attribute-ge
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(430685, _a_(430684, _n_(430683, "tasks", lambda: tasks), "loop"), seconds=10)
async def change_presence():
    _l_(430710)

    await _c_(430688, _a_(430687, _n_(430686, "client", lambda: client), "wait_until_ready"))
    _l_(430689)
    emoji = _c_(430692, _a_(430691, _n_(430690, "client", lambda: client), "get_emoji"), 773100346749878293)
    _l_(430693)
    activity = _c_(430700, _a_(430695, _n_(430694, "discord", lambda: discord), "CustomActivity"), name="DMs", type=_a_(430698, _a_(430697, _n_(430696, "discord", lambda: discord), "ActivityType"), "watching"), emoji=_n_(430699, "emoji", lambda: emoji))
    _l_(430701)
    await _c_(430708, _a_(430703, _n_(430702, "bot", lambda: bot), "change_presence"), status=_a_(430706, _a_(430705, _n_(430704, "discord", lambda: discord), "Status"), "online"), activity=_n_(430707, "activity", lambda: activity))
    _l_(430709)