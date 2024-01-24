# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56535875/attributeerror-mygrid-object-has-no-attribute-for-my-function
#!/usr/bin/env python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.uix.gridlayout import GridLayout
    _l_(406589)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(406591)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(406593)

except ImportError:
    pass
try:
    from kivy.uix.label import Label
    _l_(406595)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(406597)

except ImportError:
    pass

class ButtonHolder(_n_(406598, "BoxLayout", lambda: BoxLayout)):
    _l_(406603)

    def colorChange1(self, *args):
        _l_(406602)

        _c_(406600, _n_(406599, "print", lambda: print), "this function works")
        _l_(406601)

_c_(406606, _a_(406605, _n_(406604, "Builder", lambda: Builder), "load_string"), """
<MyGrid>:
  rows: 3
  Label:
    canvas.before:
      Color:
        rgba: 1,0,0,1
      Rectangle:
        pos: self.pos
        size: self.size
    id: toplabel
  Label:
    canvas.before:
      Color:
        rgba:  0,1,0,1
      Rectangle:
        pos: self.pos
        size: self.size
    id: bottomlabel
  ButtonHolder:
    Button:
      effectwidget: toplabel
      on_press: root.colorChange1()
""")
_l_(406607)

class MyGrid(_n_(406608, "GridLayout", lambda: GridLayout)):
    _l_(406610)

    pass
    _l_(406609)

class TheApp(_n_(406611, "App", lambda: App)):
    _l_(406616)

    def build(self):
        _l_(406615)

        aux = _c_(406613, _n_(406612, "MyGrid", lambda: MyGrid))
        _l_(406614)
        return aux

_c_(406620, _a_(406619, _c_(406618, _n_(406617, "TheApp", lambda: TheApp)), "run"))
_l_(406621)