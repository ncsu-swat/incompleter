# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65083342/error-handler-raising-an-exception-type-error-on-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(631241, _a_(631240, _n_(631239, "commands", lambda: commands), "command"), name='clear', aliases=['clean', 'cleanup'])
@_c_(631244, _a_(631243, _n_(631242, "commands", lambda: commands), "guild_only"))
@_c_(631247, _a_(631246, _n_(631245, "commands", lambda: commands), "has_permissions"), manage_messages=True)
async def clear(self, ctx, message, limit: _n_(631248, "int", lambda: int) = 10) -> None:
        _l_(631282)

        await _c_(631252, _a_(631251, _a_(631250, _n_(631249, "ctx", lambda: ctx), "message"), "add_reaction"), "<:tars_certo:783051315764133910>")
        _l_(631253)
        _c_(631256, _a_(631255, _n_(631254, "time", lambda: time), "sleep"), 2)
        _l_(631257)
        messages = await _c_(631262, _a_(631260, _a_(631259, _n_(631258, "ctx", lambda: ctx), "channel"), "purge"), bulk=True, limit=_n_(631261, "limit", lambda: limit))
        _l_(631263)
        embed=_c_(631270, _a_(631265, _n_(631264, "discord", lambda: discord), "Embed"), title=f"`{_c_(631268, _n_(631266, 'len', lambda: len), _n_(631267, 'messages', lambda: messages))}` mensagens deletadas com sucesso", color=_n_(631269, "COR_PRINCIPAL", lambda: COR_PRINCIPAL))
        _l_(631271)
        _c_(631275, _a_(631273, _n_(631272, "embed", lambda: embed), "set_author"), name="Plugin de comandos do TARS",icon_url=_n_(631274, "ICONE", lambda: ICONE))
        _l_(631276)
        await _c_(631280, _a_(631278, _n_(631277, "ctx", lambda: ctx), "send"), embed=_n_(631279, "embed", lambda: embed), delete_after=5)
        _l_(631281)

@_a_(631284, _n_(631283, "clear", lambda: clear), "error")
async def clear_error(ctx, error):
        _l_(631305)

        if _c_(631288, _n_(631285, "isinstance", lambda: isinstance), _n_(631286, "error", lambda: error), _n_(631287, "MissingPermissions", lambda: MissingPermissions)):
                _l_(631304)

                embed=_c_(631292, _a_(631290, _n_(631289, "discord", lambda: discord), "Embed"), title="<:tars_x:783051246776877057> Erro: Você não tem permissão para usar este comando", color=_n_(631291, "COR_PRINCIPAL", lambda: COR_PRINCIPAL))
                _l_(631293)
                _c_(631297, _a_(631295, _n_(631294, "embed", lambda: embed), "set_author"), name="TARS help",icon_url=_n_(631296, "ICONE", lambda: ICONE))
                _l_(631298)
                await _c_(631302, _a_(631300, _n_(631299, "ctx", lambda: ctx), "send"), embed=_n_(631301, "embed", lambda: embed))
                _l_(631303)