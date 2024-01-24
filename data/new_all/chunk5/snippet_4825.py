# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46757264/testing-python-asyncio-coroutine-with-pytest-asyncio-plugin-raises-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TestController(_n_(693917, "object", lambda: object)):
    _l_(693932)


    @_a_(693919, _a_(693918, pytest, "mark"), "asyncio")
    async def test_get_item(self):
        _l_(693931)


        controller = _c_(693921, _n_(693920, "Controller", lambda: Controller))
        _l_(693922)
        item = await _c_(693925, _a_(693924, _n_(693923, "controller", lambda: controller), "get_item"), 'item-1')
        _l_(693926)
        assert _c_(693929, _a_(693928, _n_(693927, "item", lambda: item), "get"), 'item_id') == 'item-1'
        _l_(693930)