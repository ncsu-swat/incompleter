# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60002130/attribute-errors-on-loading-blender-as-module-in-python-windows
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bpy
    _l_(572722)

except ImportError:
    pass


def main(context):
    _l_(572731)

    for ob in _a_(572725, _a_(572724, _n_(572723, "context", lambda: context), "scene"), "objects"):
        _l_(572730)

        _c_(572728, _n_(572726, "print", lambda: print), _n_(572727, "ob", lambda: ob))
        _l_(572729)


class SimpleOperator(_a_(572734, _a_(572733, _n_(572732, "bpy", lambda: bpy), "types"), "Operator")):
    _l_(572748)

    """Tooltip"""
    bl_idname = "object.simple_operator"
    _l_(572735)
    bl_label = "Simple Object Operator"
    _l_(572736)

    @_n_(572737, "classmethod", lambda: classmethod)
    def poll(cls, context):
        _l_(572741)

        aux = _a_(572739, _n_(572738, "context", lambda: context), "active_object") is not None
        _l_(572740)
        return aux

    def execute(self, context):
        _l_(572747)

        _c_(572744, _n_(572742, "main", lambda: main), _n_(572743, "context", lambda: context))
        _l_(572745)
        aux = {'FINISHED'}
        _l_(572746)
        return aux


def register():
    _l_(572755)

    _c_(572753, _a_(572751, _a_(572750, _n_(572749, "bpy", lambda: bpy), "utils"), "register_class"), _n_(572752, "SimpleOperator", lambda: SimpleOperator))
    _l_(572754)


def unregister():
    _l_(572762)

    _c_(572760, _a_(572758, _a_(572757, _n_(572756, "bpy", lambda: bpy), "utils"), "unregister_class"), _n_(572759, "SimpleOperator", lambda: SimpleOperator))
    _l_(572761)


if _n_(572763, "__name__", lambda: __name__) == "__main__":
    _l_(572773)

    _c_(572765, _n_(572764, "register", lambda: register))
    _l_(572766)

    # test call
    _c_(572771, _a_(572770, _a_(572769, _a_(572768, _n_(572767, "bpy", lambda: bpy), "ops"), "object"), "simple_operator"))
    _l_(572772)