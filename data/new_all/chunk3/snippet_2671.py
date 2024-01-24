# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67318569/attributeerror-int-object-has-no-attribute-pack
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(545596)

except ImportError:
    pass

# Window
window = _c_(545598, _n_(545597, "Tk", lambda: Tk))
_l_(545599)
_c_(545602, _a_(545601, _n_(545600, "window", lambda: window), "title"), 'Minecraft Generator')
_l_(545603)
_c_(545606, _a_(545605, _n_(545604, "window", lambda: window), "geometry"), "1080x600")
_l_(545607)
_c_(545610, _a_(545609, _n_(545608, "window", lambda: window), "minsize"), 1080, 600)
_l_(545611)
_c_(545614, _a_(545613, _n_(545612, "window", lambda: window), "maxsize"), 1080, 600)
_l_(545615)
_c_(545618, _a_(545617, _n_(545616, "window", lambda: window), "iconbitmap"), 'assets/img/logo.ico')
_l_(545619)

# Config
_c_(545622, _a_(545621, _n_(545620, "window", lambda: window), "config"), background='#627f1f')
_l_(545623)

#Composants

    # Main Menu Title
TITLE_FRAME = _c_(545626, _n_(545624, "Frame", lambda: Frame), _n_(545625, "window", lambda: window), bg='#627f1f')
_l_(545627)
MAIN_MENU_TITLE = _c_(545630, _n_(545628, "Label", lambda: Label), _n_(545629, "TITLE_FRAME", lambda: TITLE_FRAME), text='Minecraft Generator' , font=("Courrier", 40), bg='#627f1f' , fg='white')
_l_(545631)
MAIN_MENU_SUBTITLE = _c_(545634, _n_(545632, "Label", lambda: Label), _n_(545633, "TITLE_FRAME", lambda: TITLE_FRAME), text='A Minecraft Generator for all needs !' , font=("Courrier", 15), bg='#627f1f' , fg='white')
_l_(545635)

    # Main Menu TellRaw
MAIN_MENU_TELLRAW_BUTTON = _c_(545638, _n_(545636, "Button", lambda: Button), _n_(545637, "TITLE_FRAME", lambda: TITLE_FRAME), text='Tellraw Command', bg='white' , fg='#627f1f' , font=("Courrier News", 15))
_l_(545639)
MAIN_MENU_TELLRAW_IMAGE = _c_(545642, _n_(545640, "Canvas", lambda: Canvas), _n_(545641, "window", lambda: window), width=157, height=100)
_l_(545643)
MAIN_MENU_TELLRAW_IMAGE = _c_(545648, _a_(545645, _n_(545644, "MAIN_MENU_TELLRAW_IMAGE", lambda: MAIN_MENU_TELLRAW_IMAGE), "create_image"), (157, 100), image=_c_(545647, _n_(545646, "PhotoImage", lambda: PhotoImage), file='assets/img/tellraw_logo.png'))
_l_(545649)

# Packing

    # Title Frame
_c_(545652, _a_(545651, _n_(545650, "MAIN_MENU_TITLE", lambda: MAIN_MENU_TITLE), "pack"))
_l_(545653)
_c_(545656, _a_(545655, _n_(545654, "MAIN_MENU_SUBTITLE", lambda: MAIN_MENU_SUBTITLE), "pack"))
_l_(545657)
_c_(545660, _a_(545659, _n_(545658, "TITLE_FRAME", lambda: TITLE_FRAME), "pack"), side='top')
_l_(545661)

    # TellRaw
_c_(545664, _a_(545663, _n_(545662, "MAIN_MENU_TELLRAW_BUTTON", lambda: MAIN_MENU_TELLRAW_BUTTON), "pack"), pady=25)
_l_(545665)
_c_(545668, _a_(545667, _n_(545666, "MAIN_MENU_TELLRAW_IMAGE", lambda: MAIN_MENU_TELLRAW_IMAGE), "pack"))
_l_(545669)

# Display Window
_c_(545672, _a_(545671, _n_(545670, "window", lambda: window), "mainloop"))
_l_(545673)