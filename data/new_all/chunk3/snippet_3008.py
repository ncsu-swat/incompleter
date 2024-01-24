# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54732517/attributeerror-entityset-object-has-no-attribute-plot-in-featuretools
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
es = _c_(573534, _a_(573514, _n_(573513, "es", lambda: es), "entity_from_dataframe"), entity_id = 'orders',
                             dataframe = _n_(573515, "orders", lambda: orders),
                             index = 'order_id',
                             variable_types = {

                                 'user_id' : _a_(573518, _a_(573517, _n_(573516, "ft", lambda: ft), "variable_types"), "Categorical"),

                                 'eval_set' : _a_(573521, _a_(573520, _n_(573519, "ft", lambda: ft), "variable_types"), "Categorical"),

                                 'order_number' : _a_(573524, _a_(573523, _n_(573522, "ft", lambda: ft), "variable_types"), "Numeric"),

                                 'order_dow' : _a_(573527, _a_(573526, _n_(573525, "ft", lambda: ft), "variable_types"), "Numeric"),

                                 'order_hour_of_day' : _a_(573530, _a_(573529, _n_(573528, "ft", lambda: ft), "variable_types"), "Numeric"),

                                 'days_since_prior_order' : _a_(573533, _a_(573532, _n_(573531, "ft", lambda: ft), "variable_types"), "Numeric")
                             })
_l_(573535)

es = _c_(573548, _a_(573537, _n_(573536, "es", lambda: es), "entity_from_dataframe"), entity_id = 'products',
                             dataframe = _n_(573538, "products", lambda: products),
                             index = 'product_id',
                             variable_types = {

                                 'product_name' : _a_(573541, _a_(573540, _n_(573539, "ft", lambda: ft), "variable_types"), "Categorical"),

                                 'aisle_id' : _a_(573544, _a_(573543, _n_(573542, "ft", lambda: ft), "variable_types"), "Categorical"),

                                 'department_id' : _a_(573547, _a_(573546, _n_(573545, "ft", lambda: ft), "variable_types"), "Categorical")
                             })
_l_(573549)

es = _c_(573556, _a_(573551, _n_(573550, "es", lambda: es), "entity_from_dataframe"), entity_id = 'departments',
                             dataframe = _n_(573552, "departments", lambda: departments),
                             index = 'department_id',
                             variable_types = {

                                 'department' : _a_(573555, _a_(573554, _n_(573553, "ft", lambda: ft), "variable_types"), "Categorical")
                             })
_l_(573557)

es = _c_(573564, _a_(573559, _n_(573558, "es", lambda: es), "entity_from_dataframe"), entity_id = 'aisles',
                             dataframe = _n_(573560, "aisles", lambda: aisles),
                             index = 'aisle_id',
                             variable_types = {

                                 'aisle' : _a_(573563, _a_(573562, _n_(573561, "ft", lambda: ft), "variable_types"), "Categorical")
                             })
_l_(573565)