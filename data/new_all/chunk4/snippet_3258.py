# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76649673/college-football-analysis-typeerror-when-obtaining-star-player-counts
# concat operation to join the dfs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
teams_join_recruits = _c_(588563, _a_(588560, _n_(588559, "pd", lambda: pd), "concat"), [_n_(588561, "df_teams2013_2020", lambda: df_teams2013_2020), _n_(588562, "df_cfb_recruits", lambda: df_cfb_recruits)], ignore_index=True)
_l_(588564)
try:
    import pandas as pd
    _l_(588566)

except ImportError:
    pass
    
#create the dataframe    
players = _c_(588569, _a_(588568, _n_(588567, "pd", lambda: pd), "DataFrame"), {
'year': [2010,
         2010,
         2010,
         2010,
         ...],       
        'stars': ['5',
         '5',
         '5',
         '5',
         ...], 
        'team': ['Florida State',
         'Florida State',
         'Miami',
         'Miami',
         ...],
        'player': ['Dorial Green-Beckham',
         'Johnathan Gray',
         'Stefon Diggs',
         'Jameis Winston',
          ...]})
_l_(588570)