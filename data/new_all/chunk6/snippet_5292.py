# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73307348/typeerror-export-got-an-unexpected-keyword-argument-set-timezone
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(359026, _a_(359025, _n_(359024, "client", lambda: client), "command"))
@_c_(359030, _a_(359028, _n_(359027, "commands", lambda: commands), "has_role"), _n_(359029, "MANAGEMENT_ROLE_ID", lambda: MANAGEMENT_ROLE_ID))
async def archive(channel, archive_channel):
        _l_(359056)

        if _n_(359031, "channel", lambda: channel) and _n_(359032, "archive_channel", lambda: archive_channel):
                _l_(359055)

                transcript = await _c_(359036, _a_(359034, _n_(359033, "chat_exporter", lambda: chat_exporter), "export"), _n_(359035, "channel", lambda: channel), set_timezone='UTC')
                _l_(359037)
                transcript_file = _c_(359048, _a_(359039, _n_(359038, "discord", lambda: discord), "File"), _c_(359045, _a_(359041, _n_(359040, "io", lambda: io), "BytesIO"), _c_(359044, _a_(359043, _n_(359042, "transcript", lambda: transcript), "encode"))), filename=f"{_a_(359047, _n_(359046, 'channel', lambda: channel), 'name')}.html")
                _l_(359049)
                await _c_(359053, _a_(359051, _n_(359050, "archive_channel", lambda: archive_channel), "send"), file=_n_(359052, "transcript_file", lambda: transcript_file))
                _l_(359054)