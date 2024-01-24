# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65083342/error-handler-raising-an-exception-type-error-on-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(608455, _a_(608454, _n_(608453, "commands", lambda: commands), "command"), name='clear', aliases=['clean', 'cleanup'])
@_c_(608458, _a_(608457, _n_(608456, "commands", lambda: commands), "guild_only"))
@_c_(608461, _a_(608460, _n_(608459, "commands", lambda: commands), "has_permissions"), manage_messages=True)
async def clear(self, ctx, message, limit: _n_(608462, "int", lambda: int) = 10) -> None:
        _l_(608496)

        await _c_(608466, _a_(608465, _a_(608464, _n_(608463, "ctx", lambda: ctx), "message"), "add_reaction"), "<:tars_certo:783051315764133910>")
        _l_(608467)
        _c_(608470, _a_(608469, _n_(608468, "time", lambda: time), "sleep"), 2)
        _l_(608471)
        messages = await _c_(608476, _a_(608474, _a_(608473, _n_(608472, "ctx", lambda: ctx), "channel"), "purge"), bulk=True, limit=_n_(608475, "limit", lambda: limit))
        _l_(608477)
        embed=_c_(608484, _a_(608479, _n_(608478, "discord", lambda: discord), "Embed"), title=f"`{_c_(608482, _n_(608480, 'len', lambda: len), _n_(608481, 'messages', lambda: messages))}` mensagens deletadas com sucesso", color=_n_(608483, "COR_PRINCIPAL", lambda: COR_PRINCIPAL))
        _l_(608485)
        _c_(608489, _a_(608487, _n_(608486, "embed", lambda: embed), "set_author"), name="Plugin de comandos do TARS",icon_url=_n_(608488, "ICONE", lambda: ICONE))
        _l_(608490)
        await _c_(608494, _a_(608492, _n_(608491, "ctx", lambda: ctx), "send"), embed=_n_(608493, "embed", lambda: embed), delete_after=5)
        _l_(608495)

@_a_(608498, _n_(608497, "clear", lambda: clear), "error")
async def clear_error(ctx, error):
        _l_(608519)

        if _c_(608502, _n_(608499, "isinstance", lambda: isinstance), _n_(608500, "error", lambda: error), _n_(608501, "MissingPermissions", lambda: MissingPermissions)):
                _l_(608518)

                embed=_c_(608506, _a_(608504, _n_(608503, "discord", lambda: discord), "Embed"), title="<:tars_x:783051246776877057> Erro: Você não tem permissão para usar este comando", color=_n_(608505, "COR_PRINCIPAL", lambda: COR_PRINCIPAL))
                _l_(608507)
                _c_(608511, _a_(608509, _n_(608508, "embed", lambda: embed), "set_author"), name="TARS help",icon_url=_n_(608510, "ICONE", lambda: ICONE))
                _l_(608512)
                await _c_(608516, _a_(608514, _n_(608513, "ctx", lambda: ctx), "send"), embed=_n_(608515, "embed", lambda: embed))
                _l_(608517)