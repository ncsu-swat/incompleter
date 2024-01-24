# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65083342/error-handler-raising-an-exception-type-error-on-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(597465, _a_(597464, _n_(597463, "commands", lambda: commands), "command"), name='clear', aliases=['clean', 'cleanup'])
@_c_(597468, _a_(597467, _n_(597466, "commands", lambda: commands), "guild_only"))
@_c_(597471, _a_(597470, _n_(597469, "commands", lambda: commands), "has_permissions"), manage_messages=True)
async def clear(self, ctx, message, limit: _n_(597472, "int", lambda: int) = 10) -> None:
        _l_(597506)

        await _c_(597476, _a_(597475, _a_(597474, _n_(597473, "ctx", lambda: ctx), "message"), "add_reaction"), "<:tars_certo:783051315764133910>")
        _l_(597477)
        _c_(597480, _a_(597479, _n_(597478, "time", lambda: time), "sleep"), 2)
        _l_(597481)
        messages = await _c_(597486, _a_(597484, _a_(597483, _n_(597482, "ctx", lambda: ctx), "channel"), "purge"), bulk=True, limit=_n_(597485, "limit", lambda: limit))
        _l_(597487)
        embed=_c_(597494, _a_(597489, _n_(597488, "discord", lambda: discord), "Embed"), title=f"`{_c_(597492, _n_(597490, 'len', lambda: len), _n_(597491, 'messages', lambda: messages))}` mensagens deletadas com sucesso", color=_n_(597493, "COR_PRINCIPAL", lambda: COR_PRINCIPAL))
        _l_(597495)
        _c_(597499, _a_(597497, _n_(597496, "embed", lambda: embed), "set_author"), name="Plugin de comandos do TARS",icon_url=_n_(597498, "ICONE", lambda: ICONE))
        _l_(597500)
        await _c_(597504, _a_(597502, _n_(597501, "ctx", lambda: ctx), "send"), embed=_n_(597503, "embed", lambda: embed), delete_after=5)
        _l_(597505)

@_a_(597508, _n_(597507, "clear", lambda: clear), "error")
async def clear_error(ctx, error):
        _l_(597529)

        if _c_(597512, _n_(597509, "isinstance", lambda: isinstance), _n_(597510, "error", lambda: error), _n_(597511, "MissingPermissions", lambda: MissingPermissions)):
                _l_(597528)

                embed=_c_(597516, _a_(597514, _n_(597513, "discord", lambda: discord), "Embed"), title="<:tars_x:783051246776877057> Erro: Você não tem permissão para usar este comando", color=_n_(597515, "COR_PRINCIPAL", lambda: COR_PRINCIPAL))
                _l_(597517)
                _c_(597521, _a_(597519, _n_(597518, "embed", lambda: embed), "set_author"), name="TARS help",icon_url=_n_(597520, "ICONE", lambda: ICONE))
                _l_(597522)
                await _c_(597526, _a_(597524, _n_(597523, "ctx", lambda: ctx), "send"), embed=_n_(597525, "embed", lambda: embed))
                _l_(597527)