# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74245441/does-anyone-know-why-i-have-an-attribute-error-on-a-python-discord-bot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import os
  _l_(552252)

except ImportError:
  pass
try:
  import nextcord
  _l_(552254)

except ImportError:
  pass
try:
  import random
  _l_(552256)

except ImportError:
  pass
try:
  from nextcord.ext import commands
  _l_(552258)

except ImportError:
  pass

intents = _c_(552262, _a_(552261, _a_(552260, _n_(552259, "discord", lambda: discord), "Intents"), "default"))
_l_(552263)
_n_(552264, "intents", lambda: intents).message_content = True
_l_(552265)

bot = _c_(552269, _a_(552267, _n_(552266, "commands", lambda: commands), "Bot"), command_prefix='/', case_insensitive=True, intents=_n_(552268, "intents", lambda: intents))
_l_(552270)


#when bot joins server console prints
@_a_(552272, _n_(552271, "bot", lambda: bot), "event")
async def on_connect():
  _l_(552276)

  _c_(552274, _n_(552273, "print", lambda: print), "Your bot Greg is online!")
  _l_(552275)


#///////////////////////////////////////////////////////////


#commands for bot to follow
@_c_(552279, _a_(552278, _n_(552277, "bot", lambda: bot), "command"), name='ping')
async def ping(ctx):
  _l_(552288)

  await _c_(552282, _a_(552281, _n_(552280, "ctx", lambda: ctx), "send"), 'pong!')
  _l_(552283)
  await _c_(552286, _a_(552285, _n_(552284, "ctx", lambda: ctx), "send"), 'Hi new person!')
  _l_(552287)


#///////////////////////////////////////////////////////////


@_c_(552291, _a_(552290, _n_(552289, "bot", lambda: bot), "command"), name='helpc')
async def helpCommand(ctx, *, fromcommands=False):
  _l_(552311)

  if _c_(552293, _n_(552292, "fromcommands", lambda: fromcommands), False):
    _l_(552295)

    status = 'did not'
    _l_(552294)
  if _c_(552297, _n_(552296, "fromcommands", lambda: fromcommands), True):
    _l_(552299)

    status = 'did'
    _l_(552298)
  _c_(552305, _n_(552300, "print", lambda: print), f'{_a_(552303, _a_(552302, _n_(552301, "ctx", lambda: ctx), "message"), "author")} asked for help and {_n_(552304, "status", lambda: status)} come from the /commands command.'
  )
  _l_(552306)
  await _c_(552309, _a_(552308, _n_(552307, 'ctx', lambda: ctx), 'send'))
  _l_(552310)


#///////////////////////////////////////////////////////////


@_c_(552314, _a_(552313, _n_(552312, 'bot', lambda: bot), 'command'), name='crtchannel',
             description='This is a command for admins to create text channels'
             )
@_c_(552317, _a_(552316, _n_(552315, 'commands', lambda: commands), 'has_any_role'), 'That_common_coder', 'The creator')
async def create_text(ctx, channel_name='default-bot-name'):
  _l_(552340)

  guild = _a_(552319, _n_(552318, 'ctx', lambda: ctx), 'guild')
  _l_(552320)
  existing_channel = _c_(552327, _a_(552323, _a_(552322, _n_(552321, 'nextcord', lambda: nextcord), 'utils'), 'get'), _a_(552325, _n_(552324, 'guild', lambda: guild), 'channels'), name=_n_(552326, 'channel_name', lambda: channel_name))
  _l_(552328)

  if not _n_(552329, 'existing_channel', lambda: existing_channel):
    _l_(552339)

    _c_(552332, _n_(552330, 'print', lambda: print), f'The {_n_(552331, "channel_name", lambda: channel_name)} channel has been created')
    _l_(552333)
    await _c_(552337, _a_(552335, _n_(552334, 'guild', lambda: guild), 'create_text_channel'), _n_(552336, 'channel_name', lambda: channel_name))
    _l_(552338)


#//////////////////////////////
@_c_(552343, _a_(552342, _n_(552341, 'bot', lambda: bot), 'command'), name='commands')
async def commands(ctx):
  _l_(552347)

  await _c_(552345, _n_(552344, 'helpCommand', lambda: helpCommand), True)
  _l_(552346)


#///////////////////////////////////////////////////////////


@_c_(552350, _a_(552349, _n_(552348, 'bot', lambda: bot), 'command'), name='crvchannel',
  description='This is a command for admins to create voice channels')
@_c_(552353, _a_(552352, _n_(552351, 'commands', lambda: commands), 'has_any_role'), "That common coder", "The creator")
async def create_voice(ctx, channel_name='default-bot-vc-name'):
  _l_(552376)

  guild = _a_(552355, _n_(552354, 'ctx', lambda: ctx), 'guild')
  _l_(552356)
  existing_channel = _c_(552363, _a_(552359, _a_(552358, _n_(552357, 'nextcord', lambda: nextcord), 'utils'), 'get'), _a_(552361, _n_(552360, 'guild', lambda: guild), 'channels'), name=_n_(552362, 'channel_name', lambda: channel_name))
  _l_(552364)

  if not _n_(552365, 'existing_channel', lambda: existing_channel):
    _l_(552375)

    _c_(552368, _n_(552366, 'print', lambda: print), f'This channel: {_n_(552367, "channel_name", lambda: channel_name)} has been created')
    _l_(552369)
    await _c_(552373, _a_(552371, _n_(552370, 'guild', lambda: guild), 'create_voice_channel'), _n_(552372, 'channel_name', lambda: channel_name))
    _l_(552374)


#////////////////////////////////////////////////////////////


@_c_(552379, _a_(552378, _n_(552377, 'bot', lambda: bot), 'command'), name='ban', help='This is the command to ban users')
@_c_(552382, _a_(552381, _n_(552380, 'commands', lambda: commands), 'has_permissions'), ban_members=True)
async def ban_user(ctx, member: _a_(552384, _n_(552383, 'nextcord', lambda: nextcord), 'Member') = None, *, reason=None):
  _l_(552484)

  sillyshortword = []
  _l_(552385)
  sillymsg = [
    f'That seems kinda {_c_(552389, _a_(552387, _n_(552386, "random", lambda: random), "choice"), _n_(552388, "sillyshortword", lambda: sillyshortword))}',
    f'You are kinda {_c_(552393, _a_(552391, _n_(552390, "random", lambda: random), "choice"), _n_(552392, "sillyshortword", lambda: sillyshortword))}', 'You are kinda sussy'
  ]
  _l_(552394)

  #  await user.create_dm()
  #  await message.author.send()
  if _n_(552395, 'member', lambda: member) == _a_(552398, _a_(552397, _n_(552396, 'ctx', lambda: ctx), 'message'), 'author'):
    _l_(552425)

    _c_(552403, _n_(552399, 'print', lambda: print), f'Someone: {_a_(552402, _a_(552401, _n_(552400, "ctx", lambda: ctx), "message"), "author")} just tried to ban themself! :)')
    _l_(552404)
    await _c_(552410, _a_(552406, _n_(552405, 'ctx', lambda: ctx), 'send'), f'You cannot ban yourself, @{_a_(552409, _a_(552408, _n_(552407, "ctx", lambda: ctx), "message"), "author")}! :slight_smile:')
    _l_(552411)
    #Note to eli: remember to change this emoji code below
    await _c_(552417, _a_(552413, _n_(552412, 'member', lambda: member), 'send'), f'Why would you try to ban yourself,{_a_(552416, _a_(552415, _n_(552414, "ctx", lambda: ctx), "message"), "author")}? :smile:')
    _l_(552418)
    await _c_(552422, _a_(552420, _n_(552419, 'member', lambda: member), 'send'), _n_(552421, 'sillymsg', lambda: sillymsg))
    _l_(552423)
    aux = ""
    _l_(552424)
    return aux
  if _n_(552426, 'member', lambda: member) == None:
    _l_(552441)

    _c_(552431, _n_(552427, 'print', lambda: print), f'{_a_(552430, _a_(552429, _n_(552428, "ctx", lambda: ctx), "message"), "author")} used /ban without any member specified :)')
    _l_(552432)
    await _c_(552438, _a_(552434, _n_(552433, 'ctx', lambda: ctx), 'send'), f'{_a_(552437, _a_(552436, _n_(552435, "ctx", lambda: ctx), "message"), "author")}, you have to specify a member to ban'
                   )
    _l_(552439)
    aux = ""
    _l_(552440)
    return aux
  if _n_(552442, 'reason', lambda: reason) == None:
    _l_(552468)

    await _c_(552446, _a_(552444, _n_(552443, 'member', lambda: member), 'ban'), reason=f'{_n_(552445, "member", lambda: member)} has been banned for (Undefined)')
    _l_(552447)
    await _c_(552453, _a_(552449, _n_(552448, 'member', lambda: member), 'send'), f"You have been banned from {_a_(552452, _a_(552451, _n_(552450, 'ctx', lambda: ctx), 'guild'), 'name')}. The result of the ban was unspecified"
    )
    _l_(552454)
  else:
    await _c_(552458, _a_(552456, _n_(552455, "member", lambda: member), "ban"), reason=_n_(552457, "reason", lambda: reason))
    _l_(552459)
    await _c_(552466, _a_(552461, _n_(552460, "member", lambda: member), "send"), f"You have been banned from {_a_(552464, _a_(552463, _n_(552462, 'ctx', lambda: ctx), 'guild'), 'name')}. The result of the ban was {_n_(552465, 'reason', lambda: reason)}"
    )
    _l_(552467)
  _c_(552472, _n_(552469, "print", lambda: print), f'{_n_(552470, "member", lambda: member)} has just been banned for {_n_(552471, "reason", lambda: reason)}')
  _l_(552473)
  await _c_(552477, _a_(552475, _n_(552474, 'member', lambda: member), 'send'), f'You have been banned for {_n_(552476, "reason", lambda: reason)}')
  _l_(552478)
  await _c_(552482, _a_(552480, _n_(552479, 'ctx', lambda: ctx), 'send'), f'{_n_(552481, "member", lambda: member)} has been banned.')
  _l_(552483)


#////////////////////////////////////////////////////////////


@_a_(552486, _n_(552485, 'bot', lambda: bot), 'event')
async def on_command_error(ctx, error):
  _l_(552502)

  if _c_(552492, _n_(552487, 'isinstance', lambda: isinstance), _n_(552488, 'error', lambda: error), _a_(552491, _a_(552490, _n_(552489, 'commands', lambda: commands), 'errors'), 'CheckFailure')):
    _l_(552501)

    await _c_(552495, _a_(552494, _n_(552493, 'ctx', lambda: ctx), 'send'), 'Sorry, but you do not have the required roles for this command. ERR 1629'
    )
    _l_(552496)
  else:
    await _c_(552499, _a_(552498, _n_(552497, 'ctx', lambda: ctx), 'send'), 'Sorry, there was an undefined error. This error will soon become specified by the bot owner, and it will have a different response. ERR 16295: UNDEFINED'
    )
    _l_(552500)


#tokens
bottoken = _a_(552504, _n_(552503, 'os', lambda: os), 'environ')['token']
_l_(552505)
_c_(552509, _a_(552507, _n_(552506, 'bot', lambda: bot), 'run'), _n_(552508, 'bottoken', lambda: bottoken))
_l_(552510)