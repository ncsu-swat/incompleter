# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53308766/bokehgetting-typeerror-object-of-type-polygon-is-not-json-serializable
# <------- This is where the graph starts------->

# reset the graph
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(689807, _n_(689806, "reset_output", lambda: reset_output))
_l_(689808)

# import data
data = _c_(689811, _a_(689810, _n_(689809, "gpd", lambda: gpd), "read_file"), "/Users/xxxx/Desktop/cb_2015_us_state_500k/cb_2015_us_state_500k.shp", encoding="utf-8")
_l_(689812)
data1 = _n_(689813, "data", lambda: data)[~_c_(689817, _a_(689816, _a_(689815, _n_(689814, "data", lambda: data), "STUSPS"), "isin"), ['AK','AS', 'GU', 'HI', 'PR','MP', 'VI'])]
_l_(689818)
data2 = _n_(689819, "data", lambda: data)[_c_(689823, _a_(689822, _a_(689821, _n_(689820, "data", lambda: data), "STUSPS"), "isin"), ['TX', 'UT'])]
_l_(689824)

# get a list of unique value
unique_state = _c_(689832, _n_(689825, "sorted", lambda: sorted), _c_(689831, _n_(689826, "list", lambda: list), _c_(689830, _a_(689829, _a_(689828, _n_(689827, "data2", lambda: data2), "NAME"), "unique"))))
_l_(689833)
select = _c_(689836, _n_(689834, "Select", lambda: Select), title="State", options=_n_(689835, "unique_state", lambda: unique_state))
_l_(689837)

# get data into ColumnDataSource
source=_c_(689844, _n_(689838, "ColumnDataSource", lambda: ColumnDataSource), _c_(689843, _a_(689840, _n_(689839, "ColumnDataSource", lambda: ColumnDataSource), "from_df"), _a_(689842, _n_(689841, "data2", lambda: data2), "loc")[:]))
_l_(689845)

# crate filtered dataframe
filteredSource = _c_(689849, _n_(689846, "ColumnDataSource", lambda: ColumnDataSource), data=_c_(689848, _n_(689847, "dict", lambda: dict), STUSPS=[],NAME=[],ALAND=[]))
_l_(689850)

columns = [_c_(689852, _n_(689851, "TableColumn", lambda: TableColumn), field="NAME",title="NAME",sortable=True),
           _c_(689854, _n_(689853, "TableColumn", lambda: TableColumn), field="STUSPS",title="STUSPS",sortable=True),
           _c_(689856, _n_(689855, "TableColumn", lambda: TableColumn), field="ALAND",title="ALAND",sortable=True),
           _c_(689858, _n_(689857, "TableColumn", lambda: TableColumn), field="geometry",title="geometry",sortable=True)]
_l_(689859)

data_table=_c_(689863, _n_(689860, "DataTable", lambda: DataTable), source=_n_(689861, "filteredSource", lambda: filteredSource),columns=_n_(689862, "columns", lambda: columns), width=800 )
_l_(689864)

# <---- Call back starts ---->
callback = _c_(689871, _n_(689865, "CustomJS", lambda: CustomJS), args=_c_(689870, _n_(689866, "dict", lambda: dict), source=_n_(689867, "source", lambda: source),
                              filteredSource=_n_(689868, "filteredSource", lambda: filteredSource),
                              data_table=_n_(689869, "data_table", lambda: data_table)), code="""
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
_l_(689872)

_c_(689876, _a_(689874, _n_(689873, "select", lambda: select), "js_on_change"), 'value',_n_(689875, "callback", lambda: callback))
_l_(689877)

layout = _c_(689883, _n_(689878, "column", lambda: column), _c_(689882, _n_(689879, "widgetbox", lambda: widgetbox), _n_(689880, "select", lambda: select), _n_(689881, "data_table", lambda: data_table)))
_l_(689884)

# output_file("filter.html", title="filter example")

_c_(689887, _n_(689885, "show", lambda: show), _n_(689886, "layout", lambda: layout))
_l_(689888)