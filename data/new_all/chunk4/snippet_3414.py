# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74685354/typeerror-actor-failed-to-convert-parameter-socket-name-when-calling-functio
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
pos = _c_(644191, _a_(644190, _n_(644189, "unreal", lambda: unreal), "Vector"), 0,0,0)
_l_(644192)
rot = _c_(644195, _a_(644194, _n_(644193, "unreal", lambda: unreal), "Rotator"), 0,0,0)
_l_(644196)
ac = _c_(644200, _a_(644199, _a_(644198, _n_(644197, "unreal", lambda: unreal), "EditorAssetLibrary"), "load_blueprint_class"), '/Game/Resim/Blueprints/BP_Camera.BP_Camera')
_l_(644201)
ac_pos = _c_(644207, _a_(644204, _a_(644203, _n_(644202, "unreal", lambda: unreal), "EditorLevelLibrary"), "spawn_actor_from_object"), _n_(644205, "ac", lambda: ac), _n_(644206, "cam_location", lambda: cam_location))
_l_(644208)