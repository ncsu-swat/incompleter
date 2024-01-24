# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63429198/attributeerror-kivy-graphics-context-instructions-color-object-has-no-attribu
# Program to Show how to create a switch
# import kivy module
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(451935)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(451937)

except ImportError:
    pass

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
_c_(451940, _a_(451939, _n_(451938, "kivy", lambda: kivy), "require"), '1.9.0')
_l_(451941)
try:
    from kivy.lang import Builder
    _l_(451943)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(451945)

except ImportError:
    pass

# You can create your kv code in the Python file
_c_(451948, _a_(451947, _n_(451946, "Builder", lambda: Builder), "load_string"), """ 
<ScreenOne>: 
    BoxLayout: 
        canvas.before:
        Color:
            rgba: (.4, .6, 9, 1)                          #(0,0,0,1)
        Rectangle:
            size: self.size
            pos: self.pos
        canvas:
            Color:
                rgba: (1, 1, 1,1)
            RoundedRectangle:
                size : self.width/2, self.height/3
                pos : self.center_x - self.w

idth/4 , self.center_y - self.height/6                         
                radius: [(40, 40), (40, 40), (40, 40), (40, 40)]
               
        Button: 
            text: "Go to Screen 2" 
            background_color : 0, 0, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_two' 

<ScreenTwo>: 
    BoxLayout: 
        Button: 
            text: "Go to Screen 3" 
            background_color : 1, 1, 0, 1 
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_three' 

<ScreenThree>: 
    BoxLayout: 
        Button: 
            text: "Go to Screen 4" 
            background_color : 1, 0, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_four' 

<ScreenFour>: 
    BoxLayout: 
        Button: 
            text: "Go to Screen 5" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_five' 

<ScreenFive>: 
    BoxLayout: 
        Button: 
            text: "Go to Screen 1" 
            background_color : 1, 0, 0, 1 
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.current = 'screen_one' 


""")
_l_(451949)


# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenOne(_n_(451950, "Screen", lambda: Screen)):
    _l_(451952)

    pass
    _l_(451951)


class ScreenTwo(_n_(451953, "Screen", lambda: Screen)):
    _l_(451955)

    pass
    _l_(451954)


class ScreenThree(_n_(451956, "Screen", lambda: Screen)):
    _l_(451958)

    pass
    _l_(451957)


class ScreenFour(_n_(451959, "Screen", lambda: Screen)):
    _l_(451961)

    pass
    _l_(451960)


class ScreenFive(_n_(451962, "Screen", lambda: Screen)):
    _l_(451964)

    pass
    _l_(451963)


# The ScreenManager controls moving between screens
screen_manager = _c_(451966, _n_(451965, "ScreenManager", lambda: ScreenManager))
_l_(451967)

# Add the screens to the manager and then supply a name
# that is used to switch screens
_c_(451972, _a_(451969, _n_(451968, "screen_manager", lambda: screen_manager), "add_widget"), _c_(451971, _n_(451970, "ScreenOne", lambda: ScreenOne), name="screen_one"))
_l_(451973)
_c_(451978, _a_(451975, _n_(451974, "screen_manager", lambda: screen_manager), "add_widget"), _c_(451977, _n_(451976, "ScreenTwo", lambda: ScreenTwo), name="screen_two"))
_l_(451979)
_c_(451984, _a_(451981, _n_(451980, "screen_manager", lambda: screen_manager), "add_widget"), _c_(451983, _n_(451982, "ScreenThree", lambda: ScreenThree), name="screen_three"))
_l_(451985)
_c_(451990, _a_(451987, _n_(451986, "screen_manager", lambda: screen_manager), "add_widget"), _c_(451989, _n_(451988, "ScreenFour", lambda: ScreenFour), name="screen_four"))
_l_(451991)
_c_(451996, _a_(451993, _n_(451992, "screen_manager", lambda: screen_manager), "add_widget"), _c_(451995, _n_(451994, "ScreenFive", lambda: ScreenFive), name="screen_five"))
_l_(451997)


# Create the App class
class ScreenApp(_n_(451998, "App", lambda: App)):
    _l_(452002)

    def build(self):
        _l_(452001)

        aux = _n_(451999, "screen_manager", lambda: screen_manager)
        _l_(452000)
        return aux


sample_app = _c_(452004, _n_(452003, "ScreenApp", lambda: ScreenApp))
_l_(452005)
_c_(452008, _a_(452007, _n_(452006, "sample_app", lambda: sample_app), "run"))
_l_(452009)