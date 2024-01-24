# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37910292/temperature-converter-gui-unboundlocalerror-attributeerror-issues
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter
    _l_(655369)

except ImportError:
    pass
try:
    import tkinter.messagebox
    _l_(655371)

except ImportError:
    pass

class TempConverterGUI:
    _l_(655792)

    def __init__(self):
        _l_(655698)

# create main window, and set a custom window title
        _n_(655372, "self", lambda: self).main_window = _c_(655375, _a_(655374, _n_(655373, "tkinter", lambda: tkinter), "Tk"))
        _l_(655376)
        _c_(655380, _a_(655379, _a_(655378, _n_(655377, "self", lambda: self), "main_window"), "wm_title"), "Convert Temperatures")
        _l_(655381)

# creates a top frame with label to give a title for the application
        _n_(655382, "self", lambda: self).top_frame = _c_(655387, _a_(655384, _n_(655383, "tkinter", lambda: tkinter), "Frame"), _a_(655386, _n_(655385, "self", lambda: self), "main_window"))
        _l_(655388)
        _n_(655389, "self", lambda: self).title_label = _c_(655394, _a_(655391, _n_(655390, "tkinter", lambda: tkinter), "Label"), _a_(655393, _n_(655392, "self", lambda: self), "top_frame"), text= 'Temperature Converter')
        _l_(655395)
        _c_(655399, _a_(655398, _a_(655397, _n_(655396, "self", lambda: self), "title_label"), "pack"), side='top')
        _l_(655400)
        _c_(655404, _a_(655403, _a_(655402, _n_(655401, "self", lambda: self), "top_frame"), "pack"))
        _l_(655405)
# create middle frame to hold main program components
        _n_(655406, "self", lambda: self).mid_frame = _c_(655411, _a_(655408, _n_(655407, "tkinter", lambda: tkinter), "Frame"), _a_(655410, _n_(655409, "self", lambda: self), "main_window"))
        _l_(655412)
#############################################################################################
# create frame to hold the unit lists
        _n_(655413, "self", lambda: self).lists_frame = _c_(655418, _a_(655415, _n_(655414, "tkinter", lambda: tkinter), "Frame"), _a_(655417, _n_(655416, "self", lambda: self), "mid_frame"))
        _l_(655419)
        ##########################
# create frame to hold original unit to convert from list components        
        _n_(655420, "self", lambda: self).from_list_frame = _c_(655425, _a_(655422, _n_(655421, "tkinter", lambda: tkinter), "Frame"), _a_(655424, _n_(655423, "self", lambda: self), "lists_frame"))
        _l_(655426)
        _n_(655427, "self", lambda: self).from_label = _c_(655432, _a_(655429, _n_(655428, "tkinter", lambda: tkinter), "Label"), _a_(655431, _n_(655430, "self", lambda: self), "from_list_frame"), text='Convert from:')
        _l_(655433)
        _c_(655437, _a_(655436, _a_(655435, _n_(655434, "self", lambda: self), "from_label"), "pack"), side='top')
        _l_(655438)

# creates radio button lists to allow user to decide which units to convert from
        _n_(655439, "self", lambda: self).from_radio = _c_(655442, _a_(655441, _n_(655440, "tkinter", lambda: tkinter), "StringVar"))
        _l_(655443)
        _n_(655444, "self", lambda: self).fb1 = _c_(655451, _a_(655446, _n_(655445, "tkinter", lambda: tkinter), "Radiobutton"), _a_(655448, _n_(655447, "self", lambda: self), "from_list_frame"), text= 'Fahrenheit', variable= _a_(655450, _n_(655449, "self", lambda: self), "from_radio"), value= 'FAHRENHEIT')
        _l_(655452)
        _n_(655453, "self", lambda: self).fb2 = _c_(655460, _a_(655455, _n_(655454, "tkinter", lambda: tkinter), "Radiobutton"), _a_(655457, _n_(655456, "self", lambda: self), "from_list_frame"), text= 'Celsius', variable= _a_(655459, _n_(655458, "self", lambda: self), "from_radio"), value= 'CELSIUS')
        _l_(655461)
        _n_(655462, "self", lambda: self).fb3 = _c_(655469, _a_(655464, _n_(655463, "tkinter", lambda: tkinter), "Radiobutton"), _a_(655466, _n_(655465, "self", lambda: self), "from_list_frame"), text= 'Kelvin', variable= _a_(655468, _n_(655467, "self", lambda: self), "from_radio"), value= 'KELVIN')
        _l_(655470)
        _c_(655474, _a_(655473, _a_(655472, _n_(655471, "self", lambda: self), "fb1"), "pack"))
        _l_(655475)
        _c_(655479, _a_(655478, _a_(655477, _n_(655476, "self", lambda: self), "fb2"), "pack"))
        _l_(655480)
        _c_(655484, _a_(655483, _a_(655482, _n_(655481, "self", lambda: self), "fb3"), "pack"))
        _l_(655485)
        ########################
# create frame to hold list components to decide which unit to convert to       
        _n_(655486, "self", lambda: self).to_list_frame = _c_(655491, _a_(655488, _n_(655487, "tkinter", lambda: tkinter), "Frame"), _a_(655490, _n_(655489, "self", lambda: self), "lists_frame"))
        _l_(655492)
        _n_(655493, "self", lambda: self).to_label = _c_(655498, _a_(655495, _n_(655494, "tkinter", lambda: tkinter), "Label"), _a_(655497, _n_(655496, "self", lambda: self), "to_list_frame"), text='Convert to:')
        _l_(655499)
        _c_(655503, _a_(655502, _a_(655501, _n_(655500, "self", lambda: self), "to_label"), "pack"), side='top')
        _l_(655504)
# creates radio button lists to allow user to decide which units to convert to
        _n_(655505, "self", lambda: self).to_radio = _c_(655508, _a_(655507, _n_(655506, "tkinter", lambda: tkinter), "StringVar"))
        _l_(655509)
        _n_(655510, "self", lambda: self).tb1 = _c_(655517, _a_(655512, _n_(655511, "tkinter", lambda: tkinter), "Radiobutton"), _a_(655514, _n_(655513, "self", lambda: self), "to_list_frame"), text= 'Fahrenheit', variable= _a_(655516, _n_(655515, "self", lambda: self), "to_radio"), value= 'FAHRENHEIT')
        _l_(655518)
        _n_(655519, "self", lambda: self).tb2 = _c_(655526, _a_(655521, _n_(655520, "tkinter", lambda: tkinter), "Radiobutton"), _a_(655523, _n_(655522, "self", lambda: self), "to_list_frame"), text= 'Celsius', variable= _a_(655525, _n_(655524, "self", lambda: self), "to_radio"), value= 'CELSIUS')
        _l_(655527)
        _n_(655528, "self", lambda: self).tb3 = _c_(655535, _a_(655530, _n_(655529, "tkinter", lambda: tkinter), "Radiobutton"), _a_(655532, _n_(655531, "self", lambda: self), "to_list_frame"), text= 'Kelvin', variable= _a_(655534, _n_(655533, "self", lambda: self), "to_radio"), value= 'KELVIN')
        _l_(655536)
        _c_(655540, _a_(655539, _a_(655538, _n_(655537, "self", lambda: self), "tb1"), "pack"))
        _l_(655541)
        _c_(655545, _a_(655544, _a_(655543, _n_(655542, "self", lambda: self), "tb2"), "pack"))
        _l_(655546)
        _c_(655550, _a_(655549, _a_(655548, _n_(655547, "self", lambda: self), "tb3"), "pack"))
        _l_(655551)
#############################################################################################       
#Create frame to hold textbox input
        _n_(655552, "self", lambda: self).entry_frame = _c_(655557, _a_(655554, _n_(655553, "tkinter", lambda: tkinter), "Frame"), _a_(655556, _n_(655555, "self", lambda: self), "mid_frame"))
        _l_(655558)


        _n_(655559, "self", lambda: self).temp_prompt_label = _c_(655564, _a_(655561, _n_(655560, "tkinter", lambda: tkinter), "Label"), _a_(655563, _n_(655562, "self", lambda: self), "entry_frame"), text='Enter a temperature:')
        _l_(655565)
        _n_(655566, "self", lambda: self).temp_entry = _c_(655571, _a_(655568, _n_(655567, "tkinter", lambda: tkinter), "Entry"), _a_(655570, _n_(655569, "self", lambda: self), "entry_frame"), width=10)
        _l_(655572)
        _c_(655576, _a_(655575, _a_(655574, _n_(655573, "self", lambda: self), "temp_prompt_label"), "pack"), side='top')
        _l_(655577)
        _c_(655581, _a_(655580, _a_(655579, _n_(655578, "self", lambda: self), "temp_entry"), "pack"), side='top')
        _l_(655582)
############################################################################################################################################################################
############################################################################################################################################################################                    
# create frame to hold convert button components and answer label components        
        _n_(655583, "self", lambda: self).convert_frame = _c_(655588, _a_(655585, _n_(655584, "tkinter", lambda: tkinter), "Frame"), _a_(655587, _n_(655586, "self", lambda: self), "mid_frame"))
        _l_(655589)

# label to display answer
        _n_(655590, "self", lambda: self).answer = _c_(655593, _a_(655592, _n_(655591, "tkinter", lambda: tkinter), "StringVar"))
        _l_(655594)
        _n_(655595, "self", lambda: self).answer_label = _c_(655602, _a_(655597, _n_(655596, "tkinter", lambda: tkinter), "Label"), _a_(655599, _n_(655598, "self", lambda: self), "convert_frame"), textvariable=_a_(655601, _n_(655600, "self", lambda: self), "answer"))
        _l_(655603)
        _c_(655607, _a_(655606, _a_(655605, _n_(655604, "self", lambda: self), "answer_label"), "pack"), side='bottom')
        _l_(655608)
# convert button for actual conversion
        _n_(655609, "self", lambda: self).convert_button = _c_(655616, _a_(655611, _n_(655610, "tkinter", lambda: tkinter), "Button"), _a_(655613, _n_(655612, "self", lambda: self), "convert_frame"), text='Convert', command=_a_(655615, _n_(655614, "self", lambda: self), "do_convert"))##################################
        _l_(655617)##################################
        _c_(655621, _a_(655620, _a_(655619, _n_(655618, "self", lambda: self), "convert_button"), "pack"), side='top')
        _l_(655622)
#####################################################
        ##Consider creating either error box or popup

# create a bottom frame for miscellaneous buttons
        _n_(655623, "self", lambda: self).bottom_frame = _c_(655628, _a_(655625, _n_(655624, "tkinter", lambda: tkinter), "Frame"), _a_(655627, _n_(655626, "self", lambda: self), "main_window"))
        _l_(655629)
        # instructions button that makes popup box telling how to use app
        _n_(655630, "self", lambda: self).instructions_button = _c_(655637, _a_(655632, _n_(655631, "tkinter", lambda: tkinter), "Button"), _a_(655634, _n_(655633, "self", lambda: self), "bottom_frame"), text='Instructions', command=_a_(655636, _n_(655635, "self", lambda: self), "instructions"))
        _l_(655638)
        _c_(655642, _a_(655641, _a_(655640, _n_(655639, "self", lambda: self), "instructions_button"), "pack"), side='left')
        _l_(655643)
# quit button that quits app
        _n_(655644, "self", lambda: self).quit_button = _c_(655652, _a_(655646, _n_(655645, "tkinter", lambda: tkinter), "Button"), _a_(655648, _n_(655647, "self", lambda: self), "bottom_frame"), text='Quit', command=_a_(655651, _a_(655650, _n_(655649, "self", lambda: self), "main_window"), "destroy"))
        _l_(655653)
        _c_(655657, _a_(655656, _a_(655655, _n_(655654, "self", lambda: self), "quit_button"), "pack"), side='right')
        _l_(655658)
##############################################      
# packup the frames
        _c_(655662, _a_(655661, _a_(655660, _n_(655659, "self", lambda: self), "from_list_frame"), "pack"), side='left')
        _l_(655663)
        _c_(655667, _a_(655666, _a_(655665, _n_(655664, "self", lambda: self), "to_list_frame"), "pack"), side='left')
        _l_(655668)

        _c_(655672, _a_(655671, _a_(655670, _n_(655669, "self", lambda: self), "lists_frame"), "pack"), side='left')
        _l_(655673)
        _c_(655677, _a_(655676, _a_(655675, _n_(655674, "self", lambda: self), "convert_frame"), "pack"), side='left')
        _l_(655678)
        _c_(655682, _a_(655681, _a_(655680, _n_(655679, "self", lambda: self), "entry_frame"), "pack"), side='right')
        _l_(655683)



        _c_(655687, _a_(655686, _a_(655685, _n_(655684, "self", lambda: self), "mid_frame"), "pack"), side ='top')
        _l_(655688)
        _c_(655692, _a_(655691, _a_(655690, _n_(655689, "self", lambda: self), "bottom_frame"), "pack"), side='bottom')
        _l_(655693)
        # enter main loop

        _c_(655696, _a_(655695, _n_(655694, "tkinter", lambda: tkinter), "mainloop"))
        _l_(655697)
    def instructions(self):
        _l_(655703)

        _c_(655701, _a_(655700, _a_(655699, tkinter, "messagebox"), "showinfo"), 'Instructions', 'This application allows the user to convert a temperature between Fahrenheit, Celsius, and Kelvin. '\
         'A user may select a unit to convert from, a unit to convert to, and what temperature they would like to convert. '\
          'Using this information they may convert the entered temperature into the desired unit.')
        _l_(655702)
#########################################
# called by the convert button, uses from_radio selection to decide who to convert into(which conversion function to call)
    def do_convert(self):
        _l_(655728)

        #self.converted_temp = None
        if _a_(655705, _n_(655704, "self", lambda: self), "from_radio") == 'FAHRENHEIT':
            _l_(655721)

            converted_temp = _c_(655707, _n_(655706, "f_convert", lambda: f_convert))
            _l_(655708)
        elif _a_(655710, _n_(655709, "self", lambda: self), "from_radio") == 'CELSIUS':
            _l_(655720)

            converted_temp = _c_(655712, _n_(655711, "c_convert", lambda: c_convert))
            _l_(655713)
        elif _a_(655715, _n_(655714, "self", lambda: self), "from_radio") == 'KELVIN':
            _l_(655719)

            converted_temp = _c_(655717, _n_(655716, "k_convert", lambda: k_convert))
            _l_(655718)
# sets self.answer(and so answer label) to value returned into converted_temp
        _c_(655726, _a_(655724, _a_(655723, _n_(655722, "self", lambda: self), "answer"), "set"), _n_(655725, "converted_temp", lambda: converted_temp))
        _l_(655727)
###########################################################
# series of functions for each individual unit to hold conversion formulas for each possible case
# using self.to_radio selection to decide which conversion to perform, then returns the resulting temperature 
# for use in do_convert 
    def f_convert(self):
        _l_(655749)

        if _a_(655730, _n_(655729, "self", lambda: self), "to_radio") == 'FAHRENHEIT':
            _l_(655746)

            new_temp = _a_(655732, _n_(655731, "self", lambda: self), "temp_entry")
            _l_(655733)
        elif _a_(655735, _n_(655734, "self", lambda: self), "to_radio") == 'CELSIUS':
            _l_(655745)

            new_temp = (_a_(655737, _n_(655736, "self", lambda: self), "temp_entry") - 32)*(5/9.0)
            _l_(655738)
        elif _a_(655740, _n_(655739, "self", lambda: self), "to_radio") == 'KELVIN':
            _l_(655744)

            new_temp = (_a_(655742, _n_(655741, "self", lambda: self), "temp_entry") + 459.67)*(5/9.0)
            _l_(655743)
        aux = _n_(655747, "new_temp", lambda: new_temp)
        _l_(655748)

        return aux

    def c_convert(self):
        _l_(655770)

        if _a_(655751, _n_(655750, "self", lambda: self), "to_radio") == 'FAHRENHEIT':
            _l_(655767)

            new_temp = (9/5.0)*_a_(655753, _n_(655752, "self", lambda: self), "temp_entry") + 32.0
            _l_(655754)
        elif _a_(655756, _n_(655755, "self", lambda: self), "to_radio") == 'CELSIUS':
            _l_(655766)

            new_temp = _a_(655758, _n_(655757, "self", lambda: self), "temp_entry")
            _l_(655759)
        elif _a_(655761, _n_(655760, "self", lambda: self), "to_radio") == 'KELVIN':
            _l_(655765)

            new_temp = _a_(655763, _n_(655762, "self", lambda: self), "temp_entry") + 273.15 
            _l_(655764) 
        aux = _n_(655768, "new_temp", lambda: new_temp)
        _l_(655769)

        return aux

    def k_convert(self):
        _l_(655791)

        if _a_(655772, _n_(655771, "self", lambda: self), "to_radio") == 'FAHRENHEIT':
            _l_(655788)

            new_temp = (9/5.0)*(_a_(655774, _n_(655773, "self", lambda: self), "temp_entry")-273.15) + 32
            _l_(655775)
        elif _a_(655777, _n_(655776, "self", lambda: self), "to_radio") == 'CELSIUS':
            _l_(655787)

            new_temp = _a_(655779, _n_(655778, "self", lambda: self), "temp_entry") - 273.15
            _l_(655780)
        elif _a_(655782, _n_(655781, "self", lambda: self), "to_radio") == 'KELVIN':
            _l_(655786)

            new_temp = _a_(655784, _n_(655783, "self", lambda: self), "temp_entry")
            _l_(655785)
        aux = _n_(655789, "new_temp", lambda: new_temp)
        _l_(655790)

        return aux

conv_gui = _c_(655794, _n_(655793, "TempConverterGUI", lambda: TempConverterGUI))
_l_(655795)