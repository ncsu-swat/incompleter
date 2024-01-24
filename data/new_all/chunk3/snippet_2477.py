# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76367183/command-reload-raised-an-exception-typeerror-botbase-reload-extension-miss
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_a_(542975, _n_(542974, "bot", lambda: bot), "event")
async def on_ready():
        _l_(543034)

        _c_(542980, _n_(542976, "print", lambda: print), f'Logged in as {_a_(542979, _a_(542978, _n_(542977, "bot", lambda: bot), "user"), "name")}')
        _l_(542981)
        for guild in _a_(542983, _n_(542982, 'bot', lambda: bot), 'guilds'):
                _l_(542991)

                _c_(542989, _n_(542984, 'print', lambda: print), f"Bot is in {_a_(542986, _n_(542985, 'guild', lambda: guild), 'name')} with {_a_(542988, _n_(542987, 'guild', lambda: guild), 'member_count')} members")
                _l_(542990)
        _c_(542994, _a_(542993, _n_(542992, "bot", lambda: bot), "remove_command"), 'help')
        _l_(542995)
        for cmd_file in _c_(542999, _a_(542998, _a_(542997, _n_(542996, "settings", lambda: settings), "CMDS_DIR"), "glob"), "*.py"):
                _l_(543015)

                if _a_(543001, _n_(543000, "cmd_file", lambda: cmd_file), "name") != "__init__.py":
                        _l_(543014)

                        extensions = f"extension.{_a_(543003, _n_(543002, 'cmd_file', lambda: cmd_file), 'name')[:-3]}"
                        _l_(543004)
                        await _c_(543008, _a_(543006, _n_(543005, "bot", lambda: bot), "load_extension"), _n_(543007, "extensions", lambda: extensions))
                        _l_(543009)
                        _c_(543012, _n_(543010, "print", lambda: print), f"Loaded extension: {_n_(543011, 'extensions', lambda: extensions)}")
                        _l_(543013)
        try:
                _l_(543033)

                synced = await _c_(543019, _a_(543018, _a_(543017, _n_(543016, "bot", lambda: bot), "tree"), "sync"))
                _l_(543020)
                _c_(543025, _n_(543021, "print", lambda: print), f"Synced {_c_(543024, _n_(543022, 'len', lambda: len), _n_(543023, 'synced', lambda: synced))} slash commands\n")
                _l_(543026)
        except _n_(543027, "Exception", lambda: Exception) as e:
                _l_(543032)

                _c_(543030, _n_(543028, "print", lambda: print), f"Failed to sync slash commands: {_n_(543029, 'e', lambda: e)}")
                _l_(543031)