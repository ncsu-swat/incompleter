# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65432781/kivy-multiprocessing-throws-a-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.app import App
    _l_(575337)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(575339)

except ImportError:
    pass
try:
    from multiprocessing import Process
    _l_(575341)

except ImportError:
    pass

class myApp(_n_(575342, "App", lambda: App)):
    _l_(575369)

    def f(self):
        _l_(575346)

        _c_(575344, _n_(575343, "print", lambda: print), 'test')
        _l_(575345)

    def test(self, caller):
        _l_(575356)

        pr = _c_(575350, _n_(575347, "Process", lambda: Process), target=_a_(575349, _n_(575348, "self", lambda: self), "f"))
        _l_(575351)
        _c_(575354, _a_(575353, _n_(575352, "pr", lambda: pr), "start"))
        _l_(575355)

    def build(self):
        _l_(575368)

        btn = _c_(575358, _n_(575357, "Button", lambda: Button), text='Go')
        _l_(575359)
        _c_(575364, _a_(575361, _n_(575360, "btn", lambda: btn), "bind"), on_press=_a_(575363, _n_(575362, "self", lambda: self), "test"))
        _l_(575365)
        aux = _n_(575366, "btn", lambda: btn)
        _l_(575367)

        return aux

if _n_(575370, "__name__", lambda: __name__) == '__main__':
    _l_(575376)

    _c_(575374, _a_(575373, _c_(575372, _n_(575371, "myApp", lambda: myApp)), "run"))
    _l_(575375)