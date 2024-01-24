# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44469465/attributeerror-nonetype-object-has-no-attribute-root-my-case-is-different
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import*
    _l_(347627)

except ImportError:
    pass
decision=0
_l_(347628)
fs = _c_(347630, _n_(347629, "IntVar", lambda: IntVar))
_l_(347631)
def coverscreen():
    _l_(347685)

    slide=_c_(347633, _n_(347632, "Tk", lambda: Tk)) #Init window
    _l_(347634) #Init window
    _c_(347637, _a_(347636, _n_(347635, "slide", lambda: slide), "title"), 'The Castle of Redemption BETA') #Give window a title
    _l_(347638) #Give window a title
    frame=_c_(347641, _n_(347639, "Frame", lambda: Frame), _n_(347640, "slide", lambda: slide))
    _l_(347642)
    btn1=_c_(347647, _n_(347643, "Button", lambda: Button), _n_(347644, "slide", lambda: slide),text='Start Game',command=_a_(347646, _n_(347645, "slide", lambda: slide), "destroy")) #Init 1st            button
    _l_(347648) #Init 1st            button
    fsbox=_c_(347652, _n_(347649, "Checkbutton", lambda: Checkbutton), _n_(347650, "frame", lambda: frame),text='Fullscreen',\
    variable=_n_(347651, "fs", lambda: fs), onvalue=1,offvalue=0)
    _l_(347653)
    img=_c_(347655, _n_(347654, "PhotoImage", lambda: PhotoImage), file='cover.gif') # Init picture
    _l_(347656) # Init picture
    label = _c_(347659, _n_(347657, "Label", lambda: Label), image=_n_(347658, "img", lambda: img)) # Init label that contains picture
    _l_(347660) # Init label that contains picture
    _n_(347661, "label", lambda: label).image = _n_(347662, "img", lambda: img) # keep a reference!
    _l_(347663) # keep a reference!
    _c_(347666, _a_(347665, _n_(347664, "label", lambda: label), "pack")) # Places the label on the window
    _l_(347667) # Places the label on the window
    _c_(347671, _a_(347669, _n_(347668, "btn1", lambda: btn1), "pack"), side=_n_(347670, "BOTTOM", lambda: BOTTOM),pady=5) # Places the 1st button on the window
    _l_(347672) # Places the 1st button on the window
    _c_(347675, _a_(347674, _n_(347673, "fsbox", lambda: fsbox), "pack"))
    _l_(347676)
    _c_(347679, _a_(347678, _n_(347677, "frame", lambda: frame), "pack"), padx=50,pady=50)
    _l_(347680)
    _c_(347683, _a_(347682, _n_(347681, "slide", lambda: slide), "mainloop")) # Starts the window
    _l_(347684) # Starts the window
def page(name,b1,b2,write,f,fscreen):
    _l_(347765)

    slide=_c_(347687, _n_(347686, "Tk", lambda: Tk)) #Init window
    _l_(347688) #Init window
    if _n_(347689, "fscreen", lambda: fscreen) == 1:
        _l_(347706)

        _c_(347692, _a_(347691, _n_(347690, "slide", lambda: slide), "overrideredirect"), True)
        _l_(347693)
        _c_(347704, _a_(347695, _n_(347694, "slide", lambda: slide), "geometry"), _c_(347703, _a_(347696, "{0}x{1}+0+0", "format"), _c_(347699, _a_(347698, _n_(347697, "slide", lambda: slide), "winfo_screenwidth")),     _c_(347702, _a_(347701, _n_(347700, "slide", lambda: slide), "winfo_screenheight"))))
        _l_(347705)
    _c_(347710, _a_(347708, _n_(347707, "slide", lambda: slide), "title"), _n_(347709, "name", lambda: name)) #Give window a title
    _l_(347711) #Give window a title
    btn1=_c_(347717, _n_(347712, "Button", lambda: Button), _n_(347713, "slide", lambda: slide),text=_n_(347714, "b1", lambda: b1),command=_a_(347716, _n_(347715, "slide", lambda: slide), "destroy")) #Init 1st button
    _l_(347718) #Init 1st button
    btn2=_c_(347724, _n_(347719, "Button", lambda: Button), _n_(347720, "slide", lambda: slide),text=_n_(347721, "b2", lambda: b2),command=_a_(347723, _n_(347722, "slide", lambda: slide), "destroy")) #Init 2nd button
    _l_(347725) #Init 2nd button
    txt=_c_(347729, _n_(347726, "Label", lambda: Label), _n_(347727, "slide", lambda: slide),text=_n_(347728, "write", lambda: write))# Init story text
    _l_(347730)# Init story text
    img=_c_(347733, _n_(347731, "PhotoImage", lambda: PhotoImage), file=_n_(347732, "f", lambda: f)) # Init picture
    _l_(347734) # Init picture
    label = _c_(347737, _n_(347735, "Label", lambda: Label), image=_n_(347736, "img", lambda: img)) # Init label that contains picture
    _l_(347738) # Init label that contains picture
    _n_(347739, "label", lambda: label).image = _n_(347740, "img", lambda: img) # keep a reference!
    _l_(347741) # keep a reference!
    _c_(347744, _a_(347743, _n_(347742, "label", lambda: label), "pack")) # Places the label on the window
    _l_(347745) # Places the label on the window
    _c_(347749, _a_(347747, _n_(347746, "btn1", lambda: btn1), "pack"), side=_n_(347748, "BOTTOM", lambda: BOTTOM),pady=5) # Places the 1st button on the window
    _l_(347750) # Places the 1st button on the window
    _c_(347754, _a_(347752, _n_(347751, "btn2", lambda: btn2), "pack"), side=_n_(347753, "BOTTOM", lambda: BOTTOM),pady=5) # Places the 2nd button on the window
    _l_(347755) # Places the 2nd button on the window
    _c_(347759, _a_(347757, _n_(347756, "txt", lambda: txt), "pack"), side=_n_(347758, "TOP", lambda: TOP),pady=5) # Places the text on the window
    _l_(347760) # Places the text on the window
    _c_(347763, _a_(347762, _n_(347761, "slide", lambda: slide), "mainloop")) # Starts the window
    _l_(347764) # Starts the window
_c_(347767, _n_(347766, "coverscreen", lambda: coverscreen))
_l_(347768)
_c_(347773, _n_(347769, "page", lambda: page), 'Start','Continue','Go Back','Example Story Text.','cover.gif',_c_(347772, _a_(347771, _n_(347770, "fs", lambda: fs), "get"))) #Example of the created function 'page'
_l_(347774) #Example of the created function 'page'