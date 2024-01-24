# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54732607/attributeerror-module-utils-has-no-attribute-make-labels-in-featuretools-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
es = _c_(678938, _a_(678918, _n_(678917, "es", lambda: es), "entity_from_dataframe"), entity_id = 'orders',
                             dataframe = _n_(678919, "orders", lambda: orders),
                             index = 'order_id',
                             variable_types = {

                                 'user_id' : _a_(678922, _a_(678921, _n_(678920, "ft", lambda: ft), "variable_types"), "Categorical"),

                                 'eval_set' : _a_(678925, _a_(678924, _n_(678923, "ft", lambda: ft), "variable_types"), "Categorical"),

                                 'order_number' : _a_(678928, _a_(678927, _n_(678926, "ft", lambda: ft), "variable_types"), "Numeric"),

                                 'order_dow' : _a_(678931, _a_(678930, _n_(678929, "ft", lambda: ft), "variable_types"), "Numeric"),

                                 'order_hour_of_day' : _a_(678934, _a_(678933, _n_(678932, "ft", lambda: ft), "variable_types"), "Numeric"),

                                 'days_since_prior_order' : _a_(678937, _a_(678936, _n_(678935, "ft", lambda: ft), "variable_types"), "Numeric")
                             })
_l_(678939)

es = _c_(678952, _a_(678941, _n_(678940, "es", lambda: es), "entity_from_dataframe"), entity_id = 'products',
                             dataframe = _n_(678942, "products", lambda: products),
                             index = 'product_id',
                             variable_types = {

                                 'product_name' : _a_(678945, _a_(678944, _n_(678943, "ft", lambda: ft), "variable_types"), "Categorical"),

                                 'aisle_id' : _a_(678948, _a_(678947, _n_(678946, "ft", lambda: ft), "variable_types"), "Categorical"),

                                 'department_id' : _a_(678951, _a_(678950, _n_(678949, "ft", lambda: ft), "variable_types"), "Categorical")
                             })
_l_(678953)

es = _c_(678960, _a_(678955, _n_(678954, "es", lambda: es), "entity_from_dataframe"), entity_id = 'departments',
                             dataframe = _n_(678956, "departments", lambda: departments),
                             index = 'department_id',
                             variable_types = {

                                 'department' : _a_(678959, _a_(678958, _n_(678957, "ft", lambda: ft), "variable_types"), "Categorical")
                             })
_l_(678961)

es = _c_(678968, _a_(678963, _n_(678962, "es", lambda: es), "entity_from_dataframe"), entity_id = 'aisles',
                             dataframe = _n_(678964, "aisles", lambda: aisles),
                             index = 'aisle_id',
                             variable_types = {

                                 'aisle' : _a_(678967, _a_(678966, _n_(678965, "ft", lambda: ft), "variable_types"), "Categorical")
                             })
_l_(678969)