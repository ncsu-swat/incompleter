# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74685354/typeerror-actor-failed-to-convert-parameter-socket-name-when-calling-functio
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
level_actors = _c_(580239, _a_(580238, _a_(580237, _n_(580236, "unreal", lambda: unreal), "EditorLevelLibrary"), "get_all_level_actors"))
_l_(580240)
filtered_list = _c_(580249, _a_(580243, _a_(580242, _n_(580241, "unreal", lambda: unreal), "EditorFilterLibrary"), "by_actor_tag"), _n_(580244, "level_actors", lambda: level_actors), _n_(580245, "Car_tag", lambda: Car_tag), filter_type=_a_(580248, _a_(580247, _n_(580246, "unreal", lambda: unreal), "EditorScriptingFilterType"), "INCLUDE"))
_l_(580250)
actor = _n_(580251, "filtered_list", lambda: filtered_list)[0]
_l_(580252)