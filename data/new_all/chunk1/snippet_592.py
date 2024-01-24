# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53474945/cannot-plot-dataframe-as-barh-because-typeerror-empty-dataframe-no-numeric-d
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(394771)

except ImportError:
    pass
try:
    import pandas
    _l_(394773)

except ImportError:
    pass
try:
    import numpy
    _l_(394775)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(394777)

except ImportError:
    pass
try:
    from matplotlib.ticker import StrMethodFormatter
    _l_(394779)

except ImportError:
    pass

set_of_teams = _c_(394781, _n_(394780, "set", lambda: set))
_l_(394782)

def load_epl_games(file_name):
    _l_(394837)

    with _c_(394785, _n_(394783, "open", lambda: open), _n_(394784, "file_name", lambda: file_name), newline='') as csvfile:
        _l_(394834)

        reader = _c_(394789, _a_(394787, _n_(394786, "csv", lambda: csv), "DictReader"), _n_(394788, "csvfile", lambda: csvfile))
        _l_(394790)
        raw_data = {"HomeTeam": [], "AwayTeam": [], "FTHG": [], "FTAG": [], "FTR": []}
        _l_(394791)
        for row in _n_(394792, "reader", lambda: reader):
            _l_(394828)

            _c_(394796, _a_(394794, _n_(394793, "set_of_teams", lambda: set_of_teams), "add"), _n_(394795, "row", lambda: row)["HomeTeam"])
            _l_(394797)
            _c_(394801, _a_(394799, _n_(394798, "set_of_teams", lambda: set_of_teams), "add"), _n_(394800, "row", lambda: row)["AwayTeam"])
            _l_(394802)
            _c_(394806, _a_(394804, _n_(394803, "raw_data", lambda: raw_data)["HomeTeam"], "append"), _n_(394805, "row", lambda: row)["HomeTeam"])
            _l_(394807)
            _c_(394811, _a_(394809, _n_(394808, "raw_data", lambda: raw_data)["AwayTeam"], "append"), _n_(394810, "row", lambda: row)["AwayTeam"])
            _l_(394812)
            _c_(394816, _a_(394814, _n_(394813, "raw_data", lambda: raw_data)["FTHG"], "append"), _n_(394815, "row", lambda: row)["FTHG"])
            _l_(394817)
            _c_(394821, _a_(394819, _n_(394818, "raw_data", lambda: raw_data)["FTAG"], "append"), _n_(394820, "row", lambda: row)["FTAG"])
            _l_(394822)
            _c_(394826, _a_(394824, _n_(394823, "raw_data", lambda: raw_data)["FTR"], "append"), _n_(394825, "row", lambda: row)["FTR"])
            _l_(394827)
        data_frame = _c_(394832, _a_(394830, _n_(394829, "pandas", lambda: pandas), "DataFrame"), data=_n_(394831, "raw_data", lambda: raw_data))
        _l_(394833)
    aux = _n_(394835, "data_frame", lambda: data_frame)
    _l_(394836)
    return aux

def calc_points(team, table):
    _l_(394880)

    points = 0
    _l_(394838)
    for row_number in _c_(394843, _n_(394839, "range", lambda: range), _c_(394842, _a_(394841, _n_(394840, "table", lambda: table)["HomeTeam"], "count"))):
        _l_(394877)

        home_team = _a_(394845, _n_(394844, "table", lambda: table), "loc")[_n_(394846, "row_number", lambda: row_number), "HomeTeam"]
        _l_(394847)
        away_team = _a_(394849, _n_(394848, "table", lambda: table), "loc")[_n_(394850, "row_number", lambda: row_number), "AwayTeam"]
        _l_(394851)
        if _n_(394852, "team", lambda: team) in [_n_(394853, "home_team", lambda: home_team), _n_(394854, "away_team", lambda: away_team)]:
            _l_(394876)

            home_team_points = 0
            _l_(394855)
            away_team_points = 0
            _l_(394856)
            winner = _a_(394858, _n_(394857, "table", lambda: table), "loc")[_n_(394859, "row_number", lambda: row_number), "FTR"]
            _l_(394860)
            if _n_(394861, "winner", lambda: winner) == 'H':
                _l_(394868)

                home_team_points = 3
                _l_(394862)
            elif _n_(394863, "winner", lambda: winner) == 'A':
                _l_(394867)

                away_team_points = 3
                _l_(394864)
            else:
                home_team_points = 1
                _l_(394865)
                away_team_points = 1
                _l_(394866)
            if _n_(394869, "team", lambda: team) == _n_(394870, "home_team", lambda: home_team):
                _l_(394875)

                points += _n_(394871, "home_team_points", lambda: home_team_points)
                _l_(394872)
            else:
                points += _n_(394873, "away_team_points", lambda: away_team_points)
                _l_(394874)
    aux = _n_(394878, "points", lambda: points)
    _l_(394879)
    return aux

def get_goals_scored_conceded(team, table):
    _l_(394931)

    scored = 0
    _l_(394881)
    conceded = 0
    _l_(394882)
    for row_number in _c_(394887, _n_(394883, "range", lambda: range), _c_(394886, _a_(394885, _n_(394884, "table", lambda: table)["HomeTeam"], "count"))):
        _l_(394927)

        home_team = _a_(394889, _n_(394888, "table", lambda: table), "loc")[_n_(394890, "row_number", lambda: row_number), "HomeTeam"]
        _l_(394891)
        away_team = _a_(394893, _n_(394892, "table", lambda: table), "loc")[_n_(394894, "row_number", lambda: row_number), "AwayTeam"]
        _l_(394895)
        if _n_(394896, "team", lambda: team) in [_n_(394897, "home_team", lambda: home_team), _n_(394898, "away_team", lambda: away_team)]:
            _l_(394926)

            if _n_(394899, "team", lambda: team) == _n_(394900, "home_team", lambda: home_team):
                _l_(394925)

                scored += _c_(394905, _n_(394901, "int", lambda: int), _a_(394903, _n_(394902, "table", lambda: table), "loc")[_n_(394904, "row_number", lambda: row_number), "FTHG"])
                _l_(394906)
                conceded += _c_(394911, _n_(394907, "int", lambda: int), _a_(394909, _n_(394908, "table", lambda: table), "loc")[_n_(394910, "row_number", lambda: row_number), "FTAG"])
                _l_(394912)
            else:
                scored += _c_(394917, _n_(394913, "int", lambda: int), _a_(394915, _n_(394914, "table", lambda: table), "loc")[_n_(394916, "row_number", lambda: row_number), "FTAG"])
                _l_(394918)
                conceded += _c_(394923, _n_(394919, "int", lambda: int), _a_(394921, _n_(394920, "table", lambda: table), "loc")[_n_(394922, "row_number", lambda: row_number), "FTHG"])
                _l_(394924)
    aux = (_n_(394928, "scored", lambda: scored), _n_(394929, "conceded", lambda: conceded))
    _l_(394930)
    return aux

def compute_table(df):
    _l_(394988)

    raw_data = {"Team": [], "Points": [], "GoalDifference":[], "Goals": []}
    _l_(394932)
    for team in _n_(394933, "set_of_teams", lambda: set_of_teams):
        _l_(394963)

        goal_data = _c_(394937, _n_(394934, "get_goals_scored_conceded", lambda: get_goals_scored_conceded), _n_(394935, "team", lambda: team), _n_(394936, "df", lambda: df))
        _l_(394938)
        _c_(394942, _a_(394940, _n_(394939, "raw_data", lambda: raw_data)["Team"], "append"), _n_(394941, "team", lambda: team))
        _l_(394943)
        _c_(394950, _a_(394945, _n_(394944, "raw_data", lambda: raw_data)["Points"], "append"), _c_(394949, _n_(394946, "calc_points", lambda: calc_points), _n_(394947, "team", lambda: team), _n_(394948, "df", lambda: df)))
        _l_(394951)
        _c_(394956, _a_(394953, _n_(394952, "raw_data", lambda: raw_data)["GoalDifference"], "append"), _n_(394954, "goal_data", lambda: goal_data)[0] - _n_(394955, "goal_data", lambda: goal_data)[1])
        _l_(394957)
        _c_(394961, _a_(394959, _n_(394958, "raw_data", lambda: raw_data)["Goals"], "append"), _n_(394960, "goal_data", lambda: goal_data)[0])
        _l_(394962)
    data_frame = _c_(394967, _a_(394965, _n_(394964, "pandas", lambda: pandas), "DataFrame"), data=_n_(394966, "raw_data", lambda: raw_data))
    _l_(394968)
    data_frame = _c_(394973, _a_(394972, _c_(394971, _a_(394970, _n_(394969, "data_frame", lambda: data_frame), "sort_values"), ["Points", "GoalDifference", "Goals"], ascending=[False, False, False]), "reset_index"), drop=True)
    _l_(394974)
    _n_(394975, "data_frame", lambda: data_frame).index = _c_(394981, _a_(394977, _n_(394976, "numpy", lambda: numpy), "arange"), 1,_c_(394980, _n_(394978, "len", lambda: len), _n_(394979, "data_frame", lambda: data_frame))+1)
    _l_(394982)
    _a_(394984, _n_(394983, "data_frame", lambda: data_frame), "index").names = ["Finish"]
    _l_(394985)
    aux = _n_(394986, "data_frame", lambda: data_frame)
    _l_(394987)
    return aux

def get_finish(team, table):
    _l_(394997)

    aux = _c_(394995, _a_(394994, _a_(394993, _n_(394989, "table", lambda: table)[_a_(394991, _n_(394990, "table", lambda: table), "Team")==_n_(394992, "team", lambda: team)], "index"), "item"))
    _l_(394996)
    return aux

def get_points(team, table):
    _l_(395006)

    aux = _c_(395004, _a_(395003, _a_(395002, _n_(394998, "table", lambda: table)[_a_(395000, _n_(394999, "table", lambda: table), "Team")==_n_(395001, "team", lambda: team)], "Points"), "item"))
    _l_(395005)
    return aux

def display_hbar(tables):
    _l_(395058)

    raw_data = {"Team": [], "Points": []}
    _l_(395007)
    for row_number in _c_(395012, _n_(395008, "range", lambda: range), _c_(395011, _a_(395010, _n_(395009, "tables", lambda: tables)["Team"], "count"))):
        _l_(395029)

        _c_(395018, _a_(395014, _n_(395013, "raw_data", lambda: raw_data)["Team"], "append"), _a_(395016, _n_(395015, "tables", lambda: tables), "loc")[_n_(395017, "row_number", lambda: row_number)+1, "Team"])
        _l_(395019)
        _c_(395027, _a_(395021, _n_(395020, "raw_data", lambda: raw_data)["Points"], "append"), _c_(395026, _n_(395022, "int", lambda: int), _a_(395024, _n_(395023, "tables", lambda: tables), "loc")[_n_(395025, "row_number", lambda: row_number)+1, "Points"]))
        _l_(395028)
    df = _c_(395033, _a_(395031, _n_(395030, "pandas", lambda: pandas), "DataFrame"), data=_n_(395032, "raw_data", lambda: raw_data))
    _l_(395034)
    #df = pandas.DataFrame(tables, columns=["Team", "Points"])
    _c_(395037, _n_(395035, "print", lambda: print), _n_(395036, "df", lambda: df))
    _l_(395038)
    _c_(395042, _n_(395039, "print", lambda: print), _a_(395041, _n_(395040, "df", lambda: df), "dtypes"))
    _l_(395043)
    _c_(395047, _a_(395045, _n_(395044, "df", lambda: df)["Points"], "apply"), _n_(395046, "int", lambda: int))
    _l_(395048)
    _c_(395052, _n_(395049, "print", lambda: print), _a_(395051, _n_(395050, "df", lambda: df), "dtypes"))
    _l_(395053)
    _c_(395056, _a_(395055, _n_(395054, "df", lambda: df), "plot"), kind='barh',x='Points',y='Team')
    _l_(395057)

games = _c_(395060, _n_(395059, "load_epl_games", lambda: load_epl_games), 'epl2016.csv')
_l_(395061)
final_table = _c_(395064, _n_(395062, "compute_table", lambda: compute_table), _n_(395063, "games", lambda: games))
_l_(395065)
#print(final_table)
#print(get_finish("Tottenham", final_table))
#print(get_points("West Ham", final_table))
_c_(395068, _n_(395066, "display_hbar", lambda: display_hbar), _n_(395067, "final_table", lambda: final_table))
_l_(395069)