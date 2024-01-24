# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71014901/attributeerror-nonetype-object-has-no-attribute-get-member
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Rostercheck(_a_(549005, _n_(549004, "commands", lambda: commands), "Cog"), name='Rostercheck'):
    _l_(549173)

    def __init__(self, bot):
        _l_(549022)

        _n_(549006, "self", lambda: self).bot = _n_(549007, "bot", lambda: bot)
        _l_(549008)
        _n_(549009, "self", lambda: self).roster = {
            "sast" : {"roster": "PLACEHOLDER", "discordid_range":'PLACEHOLDER'}
        }   
        _l_(549010)   
        _n_(549011, "self", lambda: self).guild_metadata = {"sast": _n_(549012, "PLACEHOLDER", lambda: PLACEHOLDER)}
        _l_(549013)
        _n_(549014, "self", lambda: self).channel_metadata = {
            "sast": {"roster_check": _n_(549015, "PLACEHOLDER", lambda: PLACEHOLDER)}
        }
        _l_(549016)
        _c_(549020, _a_(549019, _a_(549018, _n_(549017, "self", lambda: self), "check_discord_members"), "start"))
        _l_(549021)

    async def send_message(self, content, channel=None):
        _l_(549035)

        try:
            _l_(549034)

            await _c_(549026, _a_(549024, _n_(549023, "channel", lambda: channel), "send"), _n_(549025, "content", lambda: content))
            _l_(549027)
        except _n_(549028, "Exception", lambda: Exception) as e:
            _l_(549033)

            _c_(549031, _n_(549029, "print", lambda: print), f"Encountered exception: {_n_(549030, 'e', lambda: e)}")
            _l_(549032)

    async def get_roster_sheet(self, dept_name):
        _l_(549073)

        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        _l_(549036)
        service_account_file = './keys.json'
        _l_(549037)
        creds = _c_(549043, _a_(549040, _a_(549039, _n_(549038, "service_account", lambda: service_account), "Credentials"), "from_service_account_file"), _n_(549041, "service_account_file", lambda: service_account_file), scopes=_n_(549042, "scopes", lambda: scopes))
        _l_(549044)
        service = _c_(549047, _n_(549045, "build", lambda: build), 'sheets', 'v4', credentials=_n_(549046, "creds", lambda: creds))
        _l_(549048)
        my_dept_roster = _c_(549053, _a_(549051, _a_(549050, _n_(549049, "self", lambda: self), "roster"), "get"), _n_(549052, "dept_name", lambda: dept_name))
        _l_(549054)
        sheet = _c_(549057, _a_(549056, _n_(549055, "service", lambda: service), "spreadsheets"))
        _l_(549058)
        aux = _c_(549071, _a_(549070, _c_(549069, _a_(549062, _c_(549061, _a_(549060, _n_(549059, "sheet", lambda: sheet), "values")), "get"), spreadsheetId=_c_(549065, _a_(549064, _n_(549063, "my_dept_roster", lambda: my_dept_roster), "get"), "roster"),range=_c_(549068, _a_(549067, _n_(549066, "my_dept_roster", lambda: my_dept_roster), "get"), "discordid_range")), "execute"))
        _l_(549072)
        return aux

    @_c_(549075, _a_(549074, tasks, "loop"), seconds=100)
    async def check_discord_members(self):
        _l_(549172)

        _c_(549077, _n_(549076, "print", lambda: print), "yo")
        _l_(549078)
        for dept_name in _c_(549082, _a_(549081, _a_(549080, _n_(549079, "self", lambda: self), "roster"), "keys")):
            _l_(549171)

            _c_(549085, _n_(549083, "print", lambda: print), _n_(549084, "dept_name", lambda: dept_name))
            _l_(549086)
            google_sheet = await _c_(549090, _a_(549088, _n_(549087, "self", lambda: self), "get_roster_sheet"), _n_(549089, "dept_name", lambda: dept_name))
            _l_(549091)
            _c_(549094, _n_(549092, "print", lambda: print), _n_(549093, "google_sheet", lambda: google_sheet))
            _l_(549095)
            for value_list in _c_(549098, _a_(549097, _n_(549096, "google_sheet", lambda: google_sheet), "get"), "values"):
                _l_(549170)

                _c_(549101, _n_(549099, "print", lambda: print), _n_(549100, "value_list", lambda: value_list))
                _l_(549102)
                if _c_(549105, _n_(549103, "len", lambda: len), _n_(549104, "value_list", lambda: value_list)) != 1 or _n_(549106, "value_list", lambda: value_list) is None or "Discord ID" in _n_(549107, "value_list", lambda: value_list):
                    _l_(549109)

                    continue
                    _l_(549108)
                value = _n_(549110, "value_list", lambda: value_list)[0]
                _l_(549111)
                _c_(549114, _n_(549112, "print", lambda: print), _n_(549113, "value", lambda: value))
                _l_(549115)
                discord_server = _c_(549124, _a_(549118, _a_(549117, _n_(549116, "self", lambda: self), "bot"), "get_guild"), _c_(549123, _a_(549121, _a_(549120, _n_(549119, "self", lambda: self), "guild_metadata"), "get"), _n_(549122, "dept_name", lambda: dept_name)))
                _l_(549125)
                _c_(549128, _n_(549126, "print", lambda: print), _n_(549127, "discord_server", lambda: discord_server))
                _l_(549129)
                discord_member = _c_(549138, _a_(549131, _n_(549130, "discord_server", lambda: discord_server), "get_member"), _c_(549137, _n_(549132, "int", lambda: int), _c_(549136, _a_(549134, _n_(549133, "re", lambda: re), "sub"), "[^0-9]", "", _n_(549135, "value", lambda: value))))
                _l_(549139)
                _c_(549142, _n_(549140, "print", lambda: print), _n_(549141, "discord_member", lambda: discord_member))
                _l_(549143)
                if _n_(549144, "discord_member", lambda: discord_member) is None:
                    _l_(549169)

                    my_chan = _c_(549155, _a_(549147, _a_(549146, _n_(549145, "self", lambda: self), "bot"), "get_channel"), id=_c_(549154, _a_(549153, _c_(549152, _a_(549150, _a_(549149, _n_(549148, "self", lambda: self), "channel_metadata"), "get"), _n_(549151, "dept_name", lambda: dept_name)), "get"), "roster_check"))
                    _l_(549156)
                    _c_(549159, _n_(549157, "print", lambda: print), _n_(549158, "my_chan", lambda: my_chan))
                    _l_(549160)
                    await _c_(549167, _a_(549162, _n_(549161, "self", lambda: self), "send_message"), f"{_n_(549163, 'value', lambda: value)} - <@{_n_(549164, 'value', lambda: value)}> is not within the {_n_(549165, 'dept_name', lambda: dept_name)} roster, are you sure they are still in your department?", _n_(549166, "my_chan", lambda: my_chan))  
                    _l_(549168)  

def setup(bot):
    _l_(549181)

    _c_(549179, _a_(549175, _n_(549174, "bot", lambda: bot), "add_cog"), _c_(549178, _n_(549176, "Rostercheck", lambda: Rostercheck), _n_(549177, "bot", lambda: bot)))
    _l_(549180)