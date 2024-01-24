# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77414673/how-do-i-fix-a-type-error-missing-annotation-for-my-discord-bot-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(604812, _a_(604811, _n_(604810, "app_commands", lambda: app_commands), "command"), name='kick', description='Kicks the member of your choice if you have kick permissions.')
@_c_(604814, _n_(604813, "has_permissions", lambda: has_permissions), kick_members=True)
async def kick(s, interaction:_a_(604816, _n_(604815, "discord", lambda: discord), "Interaction"), member:_a_(604818, _n_(604817, "discord", lambda: discord), "Member"), *, reason='None'):
    _l_(604830)

    await _c_(604823, _a_(604821, _a_(604820, _n_(604819, "interaction", lambda: interaction), "response"), "send_message"), f'User {_n_(604822, "member", lambda: member)} has been kicked.')
    _l_(604824)
    await _c_(604828, _a_(604826, _n_(604825, 'member', lambda: member), 'kick'), reason=_n_(604827, 'reason', lambda: reason))
    _l_(604829)
@_a_(604832, _n_(604831, 'kick', lambda: kick), 'error')
async def kick_error(s, interaction:_a_(604834, _n_(604833, 'discord', lambda: discord), 'Interaction'), error):
    _l_(604846)

    if _c_(604839, _n_(604835, 'isinstance', lambda: isinstance), _n_(604836, 'error', lambda: error), _a_(604838, _n_(604837, 'commands', lambda: commands), 'MissingPermissions')):
        _l_(604845)

        await _c_(604843, _a_(604842, _a_(604841, _n_(604840, 'interaction', lambda: interaction), 'response'), 'send_message'), 'You don\'t have permission to kick people!')
        _l_(604844)