# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65453893/kivymd-attributeerror-mdnavigationdrawer-object-has-no-attribute-toggle-stat
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.app import MDApp
    _l_(405473)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(405475)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(405477)

except ImportError:
    pass



_n_(405478, "Window", lambda: Window).size = (300, 500)
_l_(405479)

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
"""
_l_(405480)


class DemoApp(_n_(405481, "MDApp", lambda: MDApp)):
    _l_(405490)


    def build(self):
        _l_(405489)

        screen = _c_(405485, _a_(405483, _n_(405482, "Builder", lambda: Builder), "load_string"), _n_(405484, "navigation_helper", lambda: navigation_helper))
        _l_(405486)
        aux = _n_(405487, "screen", lambda: screen)
        _l_(405488)
        return aux


_c_(405494, _a_(405493, _c_(405492, _n_(405491, "DemoApp", lambda: DemoApp)), "run"))
_l_(405495)