# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62803991/typeerror-when-trying-to-use-regex-on-pandas-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(702592, "df", lambda: df)['Product_Category'] = '-'
_l_(702593)
_n_(702594, "df", lambda: df)['Product_Category'] = _c_(702598, _a_(702596, _n_(702595, "df", lambda: df)['Product_Category'], "apply"), _n_(702597, "str", lambda: str))
_l_(702599)

prod_cat_ssd = _c_(702602, _a_(702601, _n_(702600, "re", lambda: re), "compile"), r'\bSOLIDO\b|\bSSD\b|\bSÃ³LIDO\b')
_l_(702603)
prod_cat_hdd = _c_(702606, _a_(702605, _n_(702604, "re", lambda: re), "compile"), r'\bDURO\b|\bRIGIDO\b|\bRÃ­GIDO\b|\bRIGIDOS\b|\bHDD\b')
_l_(702607)
prod_cat_external_ssd = _c_(702610, _a_(702609, _n_(702608, "re", lambda: re), "compile"), r'\b(EXTERNO|EXTREME)\b.*\b(SOLIDO|SSD|SÃ³LIDO)\b|\b(SOLIDO|SSD|SÃ³LIDO)\b.*\b(EXTERNO|EXTREME)\b')
_l_(702611)
prod_cat_external_hdd = _c_(702614, _a_(702613, _n_(702612, "re", lambda: re), "compile"), r'\b(EXTERNO|EXTREME)\b.*\b(DURO|RIGIDO|RIGIDOS|RÃ­GIDO|HDD)\b|\b(DURO|RIGIDO|RIGIDOS|RÃ­GIDO|HDD)\b.*\b(EXTERNO|EXTREME)\b')
_l_(702615)
_n_(702616, "df", lambda: df)['Product_Category'] = _c_(702626, _a_(702618, _n_(702617, "df", lambda: df), "apply"), lambda row: 'SSD' if _c_(702623, _a_(702620, _n_(702619, "prod_cat_ssd", lambda: prod_cat_ssd), "search"), _a_(702622, _n_(702621, "row", lambda: row), "Titulo_Publicacion")) else _a_(702625, _n_(702624, "row", lambda: row), "Product_Category"), axis=1)
_l_(702627)
_n_(702628, "df", lambda: df)['Product_Category'] = _c_(702638, _a_(702630, _n_(702629, "df", lambda: df), "apply"), lambda row: 'HDD' if _c_(702635, _a_(702632, _n_(702631, "prod_cat_hdd", lambda: prod_cat_hdd), "search"), _a_(702634, _n_(702633, "row", lambda: row), "Titulo_Publicacion")) else _a_(702637, _n_(702636, "row", lambda: row), "Product_Category"), axis=1)
_l_(702639)
_n_(702640, "df", lambda: df)['Product_Category'] = _c_(702650, _a_(702642, _n_(702641, "df", lambda: df), "apply"), lambda row: 'External SSD' if _c_(702647, _a_(702644, _n_(702643, "prod_cat_external_ssd", lambda: prod_cat_external_ssd), "search"), _a_(702646, _n_(702645, "row", lambda: row), "Titulo_Publicacion")) else _a_(702649, _n_(702648, "row", lambda: row), "Product_Category"), axis=1)
_l_(702651)
_n_(702652, "df", lambda: df)['Product_Category'] = _c_(702662, _a_(702654, _n_(702653, "df", lambda: df), "apply"), lambda row: 'External HDD' if _c_(702659, _a_(702656, _n_(702655, "prod_cat_external_hdd", lambda: prod_cat_external_hdd), "search"), _a_(702658, _n_(702657, "row", lambda: row), "Titulo_Publicacion")) else _a_(702661, _n_(702660, "row", lambda: row), "Product_Category"), axis=1)
_l_(702663)