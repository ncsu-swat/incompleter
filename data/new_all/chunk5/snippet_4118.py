# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62803991/typeerror-when-trying-to-use-regex-on-pandas-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(687972, "df", lambda: df)['Product_Category'] = '-'
_l_(687973)
_n_(687974, "df", lambda: df)['Product_Category'] = _c_(687978, _a_(687976, _n_(687975, "df", lambda: df)['Product_Category'], "apply"), _n_(687977, "str", lambda: str))
_l_(687979)

prod_cat_ssd = _c_(687982, _a_(687981, _n_(687980, "re", lambda: re), "compile"), r'\bSOLIDO\b|\bSSD\b|\bSÃ³LIDO\b')
_l_(687983)
prod_cat_hdd = _c_(687986, _a_(687985, _n_(687984, "re", lambda: re), "compile"), r'\bDURO\b|\bRIGIDO\b|\bRÃ­GIDO\b|\bRIGIDOS\b|\bHDD\b')
_l_(687987)
prod_cat_external_ssd = _c_(687990, _a_(687989, _n_(687988, "re", lambda: re), "compile"), r'\b(EXTERNO|EXTREME)\b.*\b(SOLIDO|SSD|SÃ³LIDO)\b|\b(SOLIDO|SSD|SÃ³LIDO)\b.*\b(EXTERNO|EXTREME)\b')
_l_(687991)
prod_cat_external_hdd = _c_(687994, _a_(687993, _n_(687992, "re", lambda: re), "compile"), r'\b(EXTERNO|EXTREME)\b.*\b(DURO|RIGIDO|RIGIDOS|RÃ­GIDO|HDD)\b|\b(DURO|RIGIDO|RIGIDOS|RÃ­GIDO|HDD)\b.*\b(EXTERNO|EXTREME)\b')
_l_(687995)
_n_(687996, "df", lambda: df)['Product_Category'] = _c_(688006, _a_(687998, _n_(687997, "df", lambda: df), "apply"), lambda row: 'SSD' if _c_(688003, _a_(688000, _n_(687999, "prod_cat_ssd", lambda: prod_cat_ssd), "search"), _a_(688002, _n_(688001, "row", lambda: row), "Titulo_Publicacion")) else _a_(688005, _n_(688004, "row", lambda: row), "Product_Category"), axis=1)
_l_(688007)
_n_(688008, "df", lambda: df)['Product_Category'] = _c_(688018, _a_(688010, _n_(688009, "df", lambda: df), "apply"), lambda row: 'HDD' if _c_(688015, _a_(688012, _n_(688011, "prod_cat_hdd", lambda: prod_cat_hdd), "search"), _a_(688014, _n_(688013, "row", lambda: row), "Titulo_Publicacion")) else _a_(688017, _n_(688016, "row", lambda: row), "Product_Category"), axis=1)
_l_(688019)
_n_(688020, "df", lambda: df)['Product_Category'] = _c_(688030, _a_(688022, _n_(688021, "df", lambda: df), "apply"), lambda row: 'External SSD' if _c_(688027, _a_(688024, _n_(688023, "prod_cat_external_ssd", lambda: prod_cat_external_ssd), "search"), _a_(688026, _n_(688025, "row", lambda: row), "Titulo_Publicacion")) else _a_(688029, _n_(688028, "row", lambda: row), "Product_Category"), axis=1)
_l_(688031)
_n_(688032, "df", lambda: df)['Product_Category'] = _c_(688042, _a_(688034, _n_(688033, "df", lambda: df), "apply"), lambda row: 'External HDD' if _c_(688039, _a_(688036, _n_(688035, "prod_cat_external_hdd", lambda: prod_cat_external_hdd), "search"), _a_(688038, _n_(688037, "row", lambda: row), "Titulo_Publicacion")) else _a_(688041, _n_(688040, "row", lambda: row), "Product_Category"), axis=1)
_l_(688043)