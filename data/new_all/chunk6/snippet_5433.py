# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52488617/typeerror-slice-indices-must-be-integers-or-none-or-have-an-index-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df = _c_(345465, _a_(345464, _n_(345463, "pd", lambda: pd), "DataFrame"), {'Date':[], 'Link':[], 'APR Rate':[]})
_l_(345466)
#cycle through links in array until it finds APR rates/fixed or variable using regex
for link in _n_(345467, "plcompetitors", lambda: plcompetitors):
    _l_(345541)

    cdate = _c_(345471, _a_(345470, _a_(345469, _n_(345468, "datetime", lambda: datetime), "date"), "today"))
    _l_(345472)
    sdate = _c_(345475, _n_(345473, "str", lambda: str), _n_(345474, "cdate", lambda: cdate))
    _l_(345476)
    l = _c_(345480, _a_(345478, _n_(345477, "r", lambda: r), "get"), _n_(345479, "link", lambda: link))
    _l_(345481)
    _n_(345482, "l", lambda: l).encoding = 'utf-8'
    _l_(345483)
    data = _a_(345485, _n_(345484, "l", lambda: l), "text")
    _l_(345486)
    soup = _c_(345489, _n_(345487, "bs", lambda: bs), _n_(345488, "data", lambda: data), 'html.parser')
    _l_(345490)
    paragraph = _c_(345496, _a_(345492, _n_(345491, "soup", lambda: soup), "find_all"), text=_c_(345495, _a_(345494, _n_(345493, "re", lambda: re), "compile"), '[0-9]%'))
    _l_(345497)
    for n in _n_(345498, "paragraph", lambda: paragraph):
        _l_(345540)

        matches = _c_(345503, _a_(345500, _n_(345499, "re", lambda: re), "findall"), '(?i)\d+(?:\.\d+)?%\s*(?:to|-)\s*\d+(?:\.\d+)?%', _a_(345502, _n_(345501, "n", lambda: n), "string"))
        _l_(345504)
        try:
            _l_(345539)

            irate = _c_(345507, _n_(345505, "str", lambda: str), _n_(345506, "matches", lambda: matches)[0])
            _l_(345508)
            df2 = _c_(345514, _a_(345510, _n_(345509, "pd", lambda: pd), "DataFrame"), {'Date':[_n_(345511, "cdate", lambda: cdate)], 'Link':[_n_(345512, "link", lambda: link)], 'APR Rate':[_n_(345513, "irate", lambda: irate)]})
            _l_(345515)
            df = _c_(345520, _a_(345517, _n_(345516, "pd", lambda: pd), "concat"), [_n_(345518, "df", lambda: df), _n_(345519, "df2", lambda: df2)], join="inner")
            _l_(345521)
            _c_(345524, _a_(345523, _n_(345522, "df", lambda: df), "drop_duplicates"), subset='Link', keep='first', inplace=True)
            _l_(345525)
            s1 = _c_(345529, _a_(345528, _a_(345527, _n_(345526, "df", lambda: df)['APR Rate'], "values"), "tolist"))
            _l_(345530)
            _c_(345534, _a_(345532, _n_(345531, "s1", lambda: s1), "insert"), 0, _n_(345533, "sdate", lambda: sdate))
            _l_(345535)
        except _n_(345536, "IndexError", lambda: IndexError):
            _l_(345538)

            pass
            _l_(345537)
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
_l_(345542)
def main():
    _l_(345599)

    store = _c_(345545, _a_(345544, _n_(345543, "file", lambda: file), "Storage"), 'token.json')
    _l_(345546)
    creds = _c_(345549, _a_(345548, _n_(345547, "store", lambda: store), "get"))
    _l_(345550)
    if not _n_(345551, "creds", lambda: creds) or _a_(345553, _n_(345552, "creds", lambda: creds), "invalid"):
        _l_(345565)

        flow = _c_(345557, _a_(345555, _n_(345554, "client", lambda: client), "flow_from_clientsecrets"), 'credentials.json', _n_(345556, "SCOPES", lambda: SCOPES))
        _l_(345558)
        creds = _c_(345563, _a_(345560, _n_(345559, "tools", lambda: tools), "run_flow"), _n_(345561, "flow", lambda: flow), _n_(345562, "store", lambda: store))
        _l_(345564)
    service = _c_(345572, _n_(345566, "build", lambda: build), 'sheets', 'v4', http=_c_(345571, _a_(345568, _n_(345567, "creds", lambda: creds), "authorize"), _c_(345570, _n_(345569, "Http", lambda: Http))))
    _l_(345573)

    spreadsheet_id = '1vk5uZQ-nJgTURH6P9Gq0QyyixsMN8e8hionS_ucko2g'
    _l_(345574)
    range_ = "'Personal Loan'!B1:D"
    _l_(345575)
    value_input_option = 'RAW'
    _l_(345576)
    value_range_body = {
        "majorDimensions": "ROWS"
        ["values":
            _n_(345577, "s1", lambda: s1)
        ]
    }
    _l_(345578)
    request = _c_(345589, _a_(345584, _c_(345583, _a_(345582, _c_(345581, _a_(345580, _n_(345579, "service", lambda: service), "spreadsheets")), "values")), "update"), spreadsheetId=_n_(345585, "spreadsheet_id", lambda: spreadsheet_id), range=_n_(345586, "range_", lambda: range_),
                                                 valueInputOption=_n_(345587, "value_input_option", lambda: value_input_option), body=_n_(345588, "value_range_body", lambda: value_range_body))
    _l_(345590)
    response = _c_(345593, _a_(345592, _n_(345591, "request", lambda: request), "execute"))
    _l_(345594)
    _c_(345597, _n_(345595, "pprint", lambda: pprint), _n_(345596, "response", lambda: response))
    _l_(345598)

if _n_(345600, "__name__", lambda: __name__) == '__main__':
    _l_(345604)

    _c_(345602, _n_(345601, "main", lambda: main))
    _l_(345603)