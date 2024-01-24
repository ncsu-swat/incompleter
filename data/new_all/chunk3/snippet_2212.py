# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57656994/attributeerror-parent-variable-variable-user-id-dtype-numeric-is-not-t
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
es = _c_(533327, _a_(533325, _n_(533324, "es", lambda: es), "entity_from_dataframe"), entity_id="train", 
                              dataframe=_n_(533326, "df_es_train", lambda: df_es_train),
                              index="impression_id",
                              time_index="impression_time",
                              )
_l_(533328)

es = _c_(533332, _a_(533330, _n_(533329, "es", lambda: es), "entity_from_dataframe"), entity_id="viewlogs", 
                              dataframe=_n_(533331, "df_es_view_logs", lambda: df_es_view_logs),
                              index="index",
                              time_index="server_time",
                              )
_l_(533333)

es = _c_(533337, _a_(533335, _n_(533334, "es", lambda: es), "entity_from_dataframe"), entity_id="itemdata", 
                              dataframe=_n_(533336, "df_es_item_data", lambda: df_es_item_data),
                              index="item_id",
                              )
_l_(533338)

new_relationship_1 = _c_(533343, _a_(533340, _n_(533339, "ft", lambda: ft), "Relationship"), _n_(533341, "es", lambda: es)["itemdata"]["item_id"],
                                   _n_(533342, "es", lambda: es)["viewlogs"]["item_id"])
_l_(533344)
es = _c_(533348, _a_(533346, _n_(533345, "es", lambda: es), "add_relationship"), _n_(533347, "new_relationship_1", lambda: new_relationship_1))
_l_(533349)
new_relationship = _c_(533354, _a_(533351, _n_(533350, "ft", lambda: ft), "Relationship"), _n_(533352, "es", lambda: es)["train"]["user_id"],
                                   _n_(533353, "es", lambda: es)["viewlogs"]["user_id"])
_l_(533355)
es = _c_(533359, _a_(533357, _n_(533356, "es", lambda: es), "add_relationship"), _n_(533358, "new_relationship", lambda: new_relationship))
_l_(533360)