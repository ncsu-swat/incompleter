# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76026817/unable-to-resolve-the-error-typeerror-nonetype-object-is-not-subscriptable-w
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(619684)

except ImportError:
    pass
try:
    import nltk
    _l_(619686)

except ImportError:
    pass
try:
    import ssl
    _l_(619688)

except ImportError:
    pass
try:
    import streamlit as st
    _l_(619690)

except ImportError:
    pass
try:
    import random
    _l_(619692)

except ImportError:
    pass
try:
    import fastf1 as ff1
    _l_(619694)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(619696)

except ImportError:
    pass
_c_(619699, _a_(619698, _n_(619697, "st", lambda: st), "title"), "F1bot")
_l_(619700)
_c_(619703, _a_(619702, _n_(619701, "st", lambda: st), "write"), "Welcome to the F1bot. Please type a message and press Enter to ask questions related to F1.")
_l_(619704)
counter=0
_l_(619705)
counter += 1
_l_(619706)
_c_(619709, _a_(619708, _n_(619707, "st", lambda: st), "write"), 'Enter the year')
_l_(619710)
year=_c_(619714, _a_(619712, _n_(619711, "st", lambda: st), "number_input"), "You:", key=f"user_input_{_n_(619713, 'counter', lambda: counter)}")
_l_(619715)
counter+=1
_l_(619716)
_c_(619719, _a_(619718, _n_(619717, "st", lambda: st), "write"), 'Enter the venue')
_l_(619720)
venue=_c_(619724, _a_(619722, _n_(619721, "st", lambda: st), "text_input"), "You:", key=f"user_input_{_n_(619723, 'counter', lambda: counter)}")
_l_(619725)
counter+=1
_l_(619726)
_c_(619729, _a_(619728, _n_(619727, "st", lambda: st), "write"), 'Enter the race type whether it is quali or final')
_l_(619730)
rtype=_c_(619734, _a_(619732, _n_(619731, "st", lambda: st), "text_input"), "You:", key=f"user_input_{_n_(619733, 'counter', lambda: counter)}")
_l_(619735)
if _n_(619736, "rtype", lambda: rtype)=='quali':
    _l_(619741)

    rtype='Q'
    _l_(619737)
elif _n_(619738, "rtype", lambda: rtype)=='final':
    _l_(619740)

    rtype='R'
    _l_(619739)
quali = _c_(619747, _a_(619743, _n_(619742, "ff1", lambda: ff1), "get_session"), _n_(619744, "year", lambda: year),_n_(619745, "venue", lambda: venue),_n_(619746, "rtype", lambda: rtype))
_l_(619748)
_c_(619754, _a_(619750, _n_(619749, "st", lambda: st), "write"), "Chatbot:", value=_a_(619752, _n_(619751, "quali", lambda: quali), "event"), height=100, max_chars=None, key=f"chatbot_response_{_n_(619753, 'counter', lambda: counter)}")
_l_(619755)
_c_(619758, _a_(619757, _n_(619756, "st", lambda: st), "write"), "Thank you for chatting with me. Have a great day!")
_l_(619759)
_c_(619762, _a_(619761, _n_(619760, "st", lambda: st), "stop"))
_l_(619763)