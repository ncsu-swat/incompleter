# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65383456/command-raised-an-exception-nameerror-name-convert-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Giveaway(_a_(547367, _n_(547366, "commands", lambda: commands), "Cog")):
    _l_(547555)

    def __init__(self, client):
        _l_(547371)

        _n_(547368, "self", lambda: self).client = _n_(547369, "client", lambda: client)
        _l_(547370)

    def convert(time):
        _l_(547391)

        pos = ["s", "m", "h", "d"]
        _l_(547372)
        time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}
        _l_(547373)
        unit = _n_(547374, "time", lambda: time)[-1]
        _l_(547375)

        if _n_(547376, "unit", lambda: unit) not in _n_(547377, "pos", lambda: pos):
            _l_(547379)

            aux = -1
            _l_(547378)
            return aux
        try:
            _l_(547386)

            val = _c_(547382, _n_(547380, "int", lambda: int), _n_(547381, "time", lambda: time)[:-1])
            _l_(547383)
        except:
            _l_(547385)

            aux = -2
            _l_(547384)
            return aux
        aux = _n_(547387, "val", lambda: val) * _n_(547388, "time_dict", lambda: time_dict)[_n_(547389, "unit", lambda: unit)]
        _l_(547390)

        return aux

    @_c_(547393, _a_(547392, commands, "command"))
    async def giveaway(self, ctx):
        _l_(547554)

        await _c_(547396, _a_(547395, _n_(547394, "ctx", lambda: ctx), "send"), "Answer The Following Questions For Giveaway:")
        _l_(547397)

        questions = ["Channel For Giveaway?",
                     "Duration Of Giveaway? (s , m , h , d)",
                     "Prize Of Giveaway?"]
        _l_(547398)

        answers = []
        _l_(547399)

        def check(m):
            _l_(547409)

            aux = _a_(547401, _n_(547400, "m", lambda: m), "author") == _a_(547403, _n_(547402, "ctx", lambda: ctx), "author") and _a_(547405, _n_(547404, "m", lambda: m), "channel") == _a_(547407, _n_(547406, "ctx", lambda: ctx), "channel")
            _l_(547408)
            return aux

        for i in _n_(547410, "questions", lambda: questions):
            _l_(547437)

            await _c_(547414, _a_(547412, _n_(547411, "ctx", lambda: ctx), "send"), _n_(547413, "i", lambda: i))
            _l_(547415)

            try:
                _l_(547436)

                msg = await _c_(547420, _a_(547418, _a_(547417, _n_(547416, "self", lambda: self), "client"), "wait_for"), 'message', timeout=20.0, check=_n_(547419, "check", lambda: check))
                _l_(547421)
            except _a_(547423, _n_(547422, "asyncio", lambda: asyncio), "TimeoutError"):
                _l_(547429)

                await _c_(547426, _a_(547425, _n_(547424, "ctx", lambda: ctx), "send"), 'You Did Not Answer In Time!')
                _l_(547427)
                aux = ""
                _l_(547428)
                return aux
            else:
                _c_(547434, _a_(547431, _n_(547430, "answers", lambda: answers), "append"), _a_(547433, _n_(547432, "msg", lambda: msg), "content"))
                _l_(547435)

        try:
            _l_(547451)

            c_id = _c_(547440, _n_(547438, "int", lambda: int), _n_(547439, "answers", lambda: answers)[0][2:-1])
            _l_(547441)
        except:
            _l_(547450)

            await _c_(547447, _a_(547443, _n_(547442, "ctx", lambda: ctx), "send"), f'Mention Channel Properly! Example: {_a_(547446, _a_(547445, _n_(547444, "ctx", lambda: ctx), "channel"), "mention")}')
            _l_(547448)
            aux = ""
            _l_(547449)
            return aux

        channel = _c_(547456, _a_(547454, _a_(547453, _n_(547452, 'self', lambda: self), 'client'), 'get_channel'), _n_(547455, 'c_id', lambda: c_id))
        _l_(547457)

        time = _c_(547460, _n_(547458, 'convert', lambda: convert), _n_(547459, 'answers', lambda: answers)[1])
        _l_(547461)
        if _n_(547462, 'time', lambda: time) == -1:
            _l_(547475)

            await _c_(547465, _a_(547464, _n_(547463, 'ctx', lambda: ctx), 'send'), f'Answer Time With A Proper Unit (s, m, h, d)')
            _l_(547466)
            aux = ""
            _l_(547467)
            return aux
        elif _n_(547468, 'time', lambda: time) == -2:
            _l_(547474)

            await _c_(547471, _a_(547470, _n_(547469, 'ctx', lambda: ctx), 'send'), f'Time Must Be A Integer!')
            _l_(547472)
            aux = ""
            _l_(547473)
            return aux

        prize = _n_(547476, 'answers', lambda: answers)[2]
        _l_(547477)

        await _c_(547483, _a_(547479, _n_(547478, 'ctx', lambda: ctx), 'send'), f'Giveaway Will Be In Channel {_a_(547481, _n_(547480, "channel", lambda: channel), "mention")} And Will Last {_n_(547482, "time", lambda: time)}.')
        _l_(547484)

        embed = _c_(547491, _a_(547486, _n_(547485, 'discord', lambda: discord), 'Embed'), title="🎉Giveaway🎉", description=f"{_n_(547487, 'prize', lambda: prize)}", color=_a_(547490, _a_(547489, _n_(547488, "ctx", lambda: ctx), "author"), "color"))
        _l_(547492)
        _c_(547498, _a_(547494, _n_(547493, "embed", lambda: embed), "add_field"), name="Hosted by:", value= _a_(547497, _a_(547496, _n_(547495, "ctx", lambda: ctx), "author"), "mention"))
        _l_(547499)
        _c_(547503, _a_(547501, _n_(547500, "embed", lambda: embed), "set_footer"), text=f"Ends after {_n_(547502, 'answers', lambda: answers)[1]} from now. ")
        _l_(547504)

        g_msg = await _c_(547508, _a_(547506, _n_(547505, "channel", lambda: channel), "send"), embed=_n_(547507, "embed", lambda: embed))
        _l_(547509)

        await _c_(547512, _a_(547511, _n_(547510, "g_msg", lambda: g_msg), "add_reaction"), "🎉")
        _l_(547513)

        await _c_(547517, _a_(547515, _n_(547514, "asyncio", lambda: asyncio), "sleep"), _n_(547516, "time", lambda: time))
        _l_(547518)

        new_msg = await _c_(547523, _a_(547520, _n_(547519, "channel", lambda: channel), "fetch_message"), _a_(547522, _n_(547521, "g_msg", lambda: g_msg), "id"))
        _l_(547524)

        users = await _c_(547530, _a_(547529, _c_(547528, _a_(547527, _a_(547526, _n_(547525, "g_msg", lambda: g_msg), "reactions")[0], "users")), "flatten"))
        _l_(547531)
        _c_(547540, _a_(547533, _n_(547532, "users", lambda: users), "pop"), _c_(547539, _a_(547535, _n_(547534, "users", lambda: users), "index"), _a_(547538, _a_(547537, _n_(547536, "self", lambda: self), "client"), "user")))
        _l_(547541)

        winner = _c_(547545, _a_(547543, _n_(547542, "random", lambda: random), "choice"), _n_(547544, "users", lambda: users))
        _l_(547546)

        await _c_(547552, _a_(547548, _n_(547547, "channel", lambda: channel), "send"), f'Congrats! {_a_(547550, _n_(547549, "winner", lambda: winner), "mention")} won {_n_(547551, "prize", lambda: prize)}!')
        _l_(547553)