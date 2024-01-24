# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57722270/getting-typeerror-unhashable-type-dict-while-doing-bulk-upload-in-elastics
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
temp_entities_list = []
_l_(418003)
for each_row in _n_(418004, "master_entities", lambda: master_entities):
    _l_(418027)

    entity_data = {}
    _l_(418005)
    _n_(418006, "entity_data", lambda: entity_data)['entity_id'] = _a_(418008, _n_(418007, "each_row", lambda: each_row), "id")
    _l_(418009)
    _n_(418010, "entity_data", lambda: entity_data)['createdat'] = _a_(418012, _n_(418011, "each_row", lambda: each_row), "createdat")
    _l_(418013)
    _n_(418014, "entity_data", lambda: entity_data)['updatedat'] = _a_(418016, _n_(418015, "each_row", lambda: each_row), "updatedat")
    _l_(418017)
    _n_(418018, "entity_data", lambda: entity_data)['individual_business_tag']=_a_(418020, _n_(418019, "each_row", lambda: each_row), "individual_business_tag")
    _l_(418021)
    _c_(418025, _a_(418023, _n_(418022, "temp_entities_list", lambda: temp_entities_list), "append"), _n_(418024, "entity_data", lambda: entity_data))
    _l_(418026)

def indexing(entity_list):
    _l_(418034)

    for entity in _n_(418028, "entity_list", lambda: entity_list):
        _l_(418033)

        index_name = "demo"
        _l_(418029)
        yield{
            "_index":_n_(418030, "index_name", lambda: index_name),
            "_type":"businesses",
            "_source" :{
                "body":_n_(418031, "entity", lambda: entity)
            }
        }
        _l_(418032)
try:
    _l_(418052)

    _c_(418041, _a_(418036, _n_(418035, "helpers", lambda: helpers), "bulk"), _n_(418037, "es", lambda: es),_c_(418040, _n_(418038, "testing", lambda: testing), _n_(418039, "temp_entities_list", lambda: temp_entities_list)))
    _l_(418042)
except _n_(418043, "Exception", lambda: Exception) as exe:
    _l_(418051)

    _c_(418049, _a_(418045, _n_(418044, "indexing_logger", lambda: indexing_logger), "exception"), "Error:"+_c_(418048, _n_(418046, "str", lambda: str), _n_(418047, "exe", lambda: exe)))
    _l_(418050)