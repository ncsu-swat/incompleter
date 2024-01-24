# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53308766/bokehgetting-typeerror-object-of-type-polygon-is-not-json-serializable
# <------- This is where the graph starts------->

# reset the graph
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(697379, _n_(697378, "reset_output", lambda: reset_output))
_l_(697380)

# import data
data = _c_(697383, _a_(697382, _n_(697381, "gpd", lambda: gpd), "read_file"), "/Users/xxxx/Desktop/cb_2015_us_state_500k/cb_2015_us_state_500k.shp", encoding="utf-8")
_l_(697384)
data1 = _n_(697385, "data", lambda: data)[~_c_(697389, _a_(697388, _a_(697387, _n_(697386, "data", lambda: data), "STUSPS"), "isin"), ['AK','AS', 'GU', 'HI', 'PR','MP', 'VI'])]
_l_(697390)
data2 = _n_(697391, "data", lambda: data)[_c_(697395, _a_(697394, _a_(697393, _n_(697392, "data", lambda: data), "STUSPS"), "isin"), ['TX', 'UT'])]
_l_(697396)

# get a list of unique value
unique_state = _c_(697404, _n_(697397, "sorted", lambda: sorted), _c_(697403, _n_(697398, "list", lambda: list), _c_(697402, _a_(697401, _a_(697400, _n_(697399, "data2", lambda: data2), "NAME"), "unique"))))
_l_(697405)
select = _c_(697408, _n_(697406, "Select", lambda: Select), title="State", options=_n_(697407, "unique_state", lambda: unique_state))
_l_(697409)

# get data into ColumnDataSource
source=_c_(697416, _n_(697410, "ColumnDataSource", lambda: ColumnDataSource), _c_(697415, _a_(697412, _n_(697411, "ColumnDataSource", lambda: ColumnDataSource), "from_df"), _a_(697414, _n_(697413, "data2", lambda: data2), "loc")[:]))
_l_(697417)

# crate filtered dataframe
filteredSource = _c_(697421, _n_(697418, "ColumnDataSource", lambda: ColumnDataSource), data=_c_(697420, _n_(697419, "dict", lambda: dict), STUSPS=[],NAME=[],ALAND=[]))
_l_(697422)

columns = [_c_(697424, _n_(697423, "TableColumn", lambda: TableColumn), field="NAME",title="NAME",sortable=True),
           _c_(697426, _n_(697425, "TableColumn", lambda: TableColumn), field="STUSPS",title="STUSPS",sortable=True),
           _c_(697428, _n_(697427, "TableColumn", lambda: TableColumn), field="ALAND",title="ALAND",sortable=True),
           _c_(697430, _n_(697429, "TableColumn", lambda: TableColumn), field="geometry",title="geometry",sortable=True)]
_l_(697431)

data_table=_c_(697435, _n_(697432, "DataTable", lambda: DataTable), source=_n_(697433, "filteredSource", lambda: filteredSource),columns=_n_(697434, "columns", lambda: columns), width=800 )
_l_(697436)

# <---- Call back starts ---->
callback = _c_(697443, _n_(697437, "CustomJS", lambda: CustomJS), args=_c_(697442, _n_(697438, "dict", lambda: dict), source=_n_(697439, "source", lambda: source),
                              filteredSource=_n_(697440, "filteredSource", lambda: filteredSource),
                              data_table=_n_(697441, "data_table", lambda: data_table)), code="""
var data = source.data;
var f = cb_obj.value;
var d2 = filteredSource.data;
d2['STUSPS']=[]
d2['NAME']=[]
d2['ALAND']=[]
d2['geometry']=[]


for(i = 0; i < data['NAME'].length;i++){

if(data['NAME'][i]==f){

    d2['STUSPS'].push(data['STUSPS'][i])
    d2['NAME'].push(data['NAME'][i])
    d2['ALAND'].push(data['ALAND'][i])
    d2['geometry'].push(data['geometry'][i])
}

}

filteredSource.change.emit()
// trigger change on datatable
data_table.change.emit()

""")
_l_(697444)

_c_(697448, _a_(697446, _n_(697445, "select", lambda: select), "js_on_change"), 'value',_n_(697447, "callback", lambda: callback))
_l_(697449)

layout = _c_(697455, _n_(697450, "column", lambda: column), _c_(697454, _n_(697451, "widgetbox", lambda: widgetbox), _n_(697452, "select", lambda: select), _n_(697453, "data_table", lambda: data_table)))
_l_(697456)

# output_file("filter.html", title="filter example")

_c_(697459, _n_(697457, "show", lambda: show), _n_(697458, "layout", lambda: layout))
_l_(697460)