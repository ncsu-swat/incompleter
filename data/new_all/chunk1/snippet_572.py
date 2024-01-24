# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48669373/invalid-column-name-error-when-writing-pandas-dataframe-to-sql
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cnxn = _c_(400621, _a_(400620, _n_(400619, "sqlalchemy", lambda: sqlalchemy), "create_engine"), "mssql+pyodbc://@HOST:PORT/DATABASE?driver=SQL+Server") 
_l_(400622) 
_c_(400626, _a_(400624, _n_(400623, "df", lambda: df), "to_sql"), 'DATABASE.dbo.TABLENAME', _n_(400625, "cnxn", lambda: cnxn), if_exists='append', index=False)
_l_(400627)