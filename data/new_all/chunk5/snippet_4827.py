# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46757264/testing-python-asyncio-coroutine-with-pytest-asyncio-plugin-raises-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TestController(_n_(670542, "object", lambda: object)):
    _l_(670557)


    @_a_(670544, _a_(670543, pytest, "mark"), "asyncio")
    async def test_get_item(self):
        _l_(670556)


        controller = _c_(670546, _n_(670545, "Controller", lambda: Controller))
        _l_(670547)
        item = await _c_(670550, _a_(670549, _n_(670548, "controller", lambda: controller), "get_item"), 'item-1')
        _l_(670551)
        assert _c_(670554, _a_(670553, _n_(670552, "item", lambda: item), "get"), 'item_id') == 'item-1'
        _l_(670555)