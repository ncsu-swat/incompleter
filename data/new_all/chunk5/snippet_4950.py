# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37910292/temperature-converter-gui-unboundlocalerror-attributeerror-issues
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter
    _l_(678274)

except ImportError:
    pass
try:
    import tkinter.messagebox
    _l_(678276)

except ImportError:
    pass

class TempConverterGUI:
    _l_(678697)

    def __init__(self):
        _l_(678603)

# create main window, and set a custom window title
        _n_(678277, "self", lambda: self).main_window = _c_(678280, _a_(678279, _n_(678278, "tkinter", lambda: tkinter), "Tk"))
        _l_(678281)
        _c_(678285, _a_(678284, _a_(678283, _n_(678282, "self", lambda: self), "main_window"), "wm_title"), "Convert Temperatures")
        _l_(678286)

# creates a top frame with label to give a title for the application
        _n_(678287, "self", lambda: self).top_frame = _c_(678292, _a_(678289, _n_(678288, "tkinter", lambda: tkinter), "Frame"), _a_(678291, _n_(678290, "self", lambda: self), "main_window"))
        _l_(678293)
        _n_(678294, "self", lambda: self).title_label = _c_(678299, _a_(678296, _n_(678295, "tkinter", lambda: tkinter), "Label"), _a_(678298, _n_(678297, "self", lambda: self), "top_frame"), text= 'Temperature Converter')
        _l_(678300)
        _c_(678304, _a_(678303, _a_(678302, _n_(678301, "self", lambda: self), "title_label"), "pack"), side='top')
        _l_(678305)
        _c_(678309, _a_(678308, _a_(678307, _n_(678306, "self", lambda: self), "top_frame"), "pack"))
        _l_(678310)
# create middle frame to hold main program components
        _n_(678311, "self", lambda: self).mid_frame = _c_(678316, _a_(678313, _n_(678312, "tkinter", lambda: tkinter), "Frame"), _a_(678315, _n_(678314, "self", lambda: self), "main_window"))
        _l_(678317)
#############################################################################################
# create frame to hold the unit lists
        _n_(678318, "self", lambda: self).lists_frame = _c_(678323, _a_(678320, _n_(678319, "tkinter", lambda: tkinter), "Frame"), _a_(678322, _n_(678321, "self", lambda: self), "mid_frame"))
        _l_(678324)
        ##########################
# create frame to hold original unit to convert from list components        
        _n_(678325, "self", lambda: self).from_list_frame = _c_(678330, _a_(678327, _n_(678326, "tkinter", lambda: tkinter), "Frame"), _a_(678329, _n_(678328, "self", lambda: self), "lists_frame"))
        _l_(678331)
        _n_(678332, "self", lambda: self).from_label = _c_(678337, _a_(678334, _n_(678333, "tkinter", lambda: tkinter), "Label"), _a_(678336, _n_(678335, "self", lambda: self), "from_list_frame"), text='Convert from:')
        _l_(678338)
        _c_(678342, _a_(678341, _a_(678340, _n_(678339, "self", lambda: self), "from_label"), "pack"), side='top')
        _l_(678343)

# creates radio button lists to allow user to decide which units to convert from
        _n_(678344, "self", lambda: self).from_radio = _c_(678347, _a_(678346, _n_(678345, "tkinter", lambda: tkinter), "StringVar"))
        _l_(678348)
        _n_(678349, "self", lambda: self).fb1 = _c_(678356, _a_(678351, _n_(678350, "tkinter", lambda: tkinter), "Radiobutton"), _a_(678353, _n_(678352, "self", lambda: self), "from_list_frame"), text= 'Fahrenheit', variable= _a_(678355, _n_(678354, "self", lambda: self), "from_radio"), value= 'FAHRENHEIT')
        _l_(678357)
        _n_(678358, "self", lambda: self).fb2 = _c_(678365, _a_(678360, _n_(678359, "tkinter", lambda: tkinter), "Radiobutton"), _a_(678362, _n_(678361, "self", lambda: self), "from_list_frame"), text= 'Celsius', variable= _a_(678364, _n_(678363, "self", lambda: self), "from_radio"), value= 'CELSIUS')
        _l_(678366)
        _n_(678367, "self", lambda: self).fb3 = _c_(678374, _a_(678369, _n_(678368, "tkinter", lambda: tkinter), "Radiobutton"), _a_(678371, _n_(678370, "self", lambda: self), "from_list_frame"), text= 'Kelvin', variable= _a_(678373, _n_(678372, "self", lambda: self), "from_radio"), value= 'KELVIN')
        _l_(678375)
        _c_(678379, _a_(678378, _a_(678377, _n_(678376, "self", lambda: self), "fb1"), "pack"))
        _l_(678380)
        _c_(678384, _a_(678383, _a_(678382, _n_(678381, "self", lambda: self), "fb2"), "pack"))
        _l_(678385)
        _c_(678389, _a_(678388, _a_(678387, _n_(678386, "self", lambda: self), "fb3"), "pack"))
        _l_(678390)
        ########################
# create frame to hold list components to decide which unit to convert to       
        _n_(678391, "self", lambda: self).to_list_frame = _c_(678396, _a_(678393, _n_(678392, "tkinter", lambda: tkinter), "Frame"), _a_(678395, _n_(678394, "self", lambda: self), "lists_frame"))
        _l_(678397)
        _n_(678398, "self", lambda: self).to_label = _c_(678403, _a_(678400, _n_(678399, "tkinter", lambda: tkinter), "Label"), _a_(678402, _n_(678401, "self", lambda: self), "to_list_frame"), text='Convert to:')
        _l_(678404)
        _c_(678408, _a_(678407, _a_(678406, _n_(678405, "self", lambda: self), "to_label"), "pack"), side='top')
        _l_(678409)
# creates radio button lists to allow user to decide which units to convert to
        _n_(678410, "self", lambda: self).to_radio = _c_(678413, _a_(678412, _n_(678411, "tkinter", lambda: tkinter), "StringVar"))
        _l_(678414)
        _n_(678415, "self", lambda: self).tb1 = _c_(678422, _a_(678417, _n_(678416, "tkinter", lambda: tkinter), "Radiobutton"), _a_(678419, _n_(678418, "self", lambda: self), "to_list_frame"), text= 'Fahrenheit', variable= _a_(678421, _n_(678420, "self", lambda: self), "to_radio"), value= 'FAHRENHEIT')
        _l_(678423)
        _n_(678424, "self", lambda: self).tb2 = _c_(678431, _a_(678426, _n_(678425, "tkinter", lambda: tkinter), "Radiobutton"), _a_(678428, _n_(678427, "self", lambda: self), "to_list_frame"), text= 'Celsius', variable= _a_(678430, _n_(678429, "self", lambda: self), "to_radio"), value= 'CELSIUS')
        _l_(678432)
        _n_(678433, "self", lambda: self).tb3 = _c_(678440, _a_(678435, _n_(678434, "tkinter", lambda: tkinter), "Radiobutton"), _a_(678437, _n_(678436, "self", lambda: self), "to_list_frame"), text= 'Kelvin', variable= _a_(678439, _n_(678438, "self", lambda: self), "to_radio"), value= 'KELVIN')
        _l_(678441)
        _c_(678445, _a_(678444, _a_(678443, _n_(678442, "self", lambda: self), "tb1"), "pack"))
        _l_(678446)
        _c_(678450, _a_(678449, _a_(678448, _n_(678447, "self", lambda: self), "tb2"), "pack"))
        _l_(678451)
        _c_(678455, _a_(678454, _a_(678453, _n_(678452, "self", lambda: self), "tb3"), "pack"))
        _l_(678456)
#############################################################################################       
#Create frame to hold textbox input
        _n_(678457, "self", lambda: self).entry_frame = _c_(678462, _a_(678459, _n_(678458, "tkinter", lambda: tkinter), "Frame"), _a_(678461, _n_(678460, "self", lambda: self), "mid_frame"))
        _l_(678463)


        _n_(678464, "self", lambda: self).temp_prompt_label = _c_(678469, _a_(678466, _n_(678465, "tkinter", lambda: tkinter), "Label"), _a_(678468, _n_(678467, "self", lambda: self), "entry_frame"), text='Enter a temperature:')
        _l_(678470)
        _n_(678471, "self", lambda: self).temp_entry = _c_(678476, _a_(678473, _n_(678472, "tkinter", lambda: tkinter), "Entry"), _a_(678475, _n_(678474, "self", lambda: self), "entry_frame"), width=10)
        _l_(678477)
        _c_(678481, _a_(678480, _a_(678479, _n_(678478, "self", lambda: self), "temp_prompt_label"), "pack"), side='top')
        _l_(678482)
        _c_(678486, _a_(678485, _a_(678484, _n_(678483, "self", lambda: self), "temp_entry"), "pack"), side='top')
        _l_(678487)
############################################################################################################################################################################
############################################################################################################################################################################                    
# create frame to hold convert button components and answer label components        
        _n_(678488, "self", lambda: self).convert_frame = _c_(678493, _a_(678490, _n_(678489, "tkinter", lambda: tkinter), "Frame"), _a_(678492, _n_(678491, "self", lambda: self), "mid_frame"))
        _l_(678494)

# label to display answer
        _n_(678495, "self", lambda: self).answer = _c_(678498, _a_(678497, _n_(678496, "tkinter", lambda: tkinter), "StringVar"))
        _l_(678499)
        _n_(678500, "self", lambda: self).answer_label = _c_(678507, _a_(678502, _n_(678501, "tkinter", lambda: tkinter), "Label"), _a_(678504, _n_(678503, "self", lambda: self), "convert_frame"), textvariable=_a_(678506, _n_(678505, "self", lambda: self), "answer"))
        _l_(678508)
        _c_(678512, _a_(678511, _a_(678510, _n_(678509, "self", lambda: self), "answer_label"), "pack"), side='bottom')
        _l_(678513)
# convert button for actual conversion
        _n_(678514, "self", lambda: self).convert_button = _c_(678521, _a_(678516, _n_(678515, "tkinter", lambda: tkinter), "Button"), _a_(678518, _n_(678517, "self", lambda: self), "convert_frame"), text='Convert', command=_a_(678520, _n_(678519, "self", lambda: self), "do_convert"))##################################
        _l_(678522)##################################
        _c_(678526, _a_(678525, _a_(678524, _n_(678523, "self", lambda: self), "convert_button"), "pack"), side='top')
        _l_(678527)
#####################################################
        ##Consider creating either error box or popup

# create a bottom frame for miscellaneous buttons
        _n_(678528, "self", lambda: self).bottom_frame = _c_(678533, _a_(678530, _n_(678529, "tkinter", lambda: tkinter), "Frame"), _a_(678532, _n_(678531, "self", lambda: self), "main_window"))
        _l_(678534)
        # instructions button that makes popup box telling how to use app
        _n_(678535, "self", lambda: self).instructions_button = _c_(678542, _a_(678537, _n_(678536, "tkinter", lambda: tkinter), "Button"), _a_(678539, _n_(678538, "self", lambda: self), "bottom_frame"), text='Instructions', command=_a_(678541, _n_(678540, "self", lambda: self), "instructions"))
        _l_(678543)
        _c_(678547, _a_(678546, _a_(678545, _n_(678544, "self", lambda: self), "instructions_button"), "pack"), side='left')
        _l_(678548)
# quit button that quits app
        _n_(678549, "self", lambda: self).quit_button = _c_(678557, _a_(678551, _n_(678550, "tkinter", lambda: tkinter), "Button"), _a_(678553, _n_(678552, "self", lambda: self), "bottom_frame"), text='Quit', command=_a_(678556, _a_(678555, _n_(678554, "self", lambda: self), "main_window"), "destroy"))
        _l_(678558)
        _c_(678562, _a_(678561, _a_(678560, _n_(678559, "self", lambda: self), "quit_button"), "pack"), side='right')
        _l_(678563)
##############################################      
# packup the frames
        _c_(678567, _a_(678566, _a_(678565, _n_(678564, "self", lambda: self), "from_list_frame"), "pack"), side='left')
        _l_(678568)
        _c_(678572, _a_(678571, _a_(678570, _n_(678569, "self", lambda: self), "to_list_frame"), "pack"), side='left')
        _l_(678573)

        _c_(678577, _a_(678576, _a_(678575, _n_(678574, "self", lambda: self), "lists_frame"), "pack"), side='left')
        _l_(678578)
        _c_(678582, _a_(678581, _a_(678580, _n_(678579, "self", lambda: self), "convert_frame"), "pack"), side='left')
        _l_(678583)
        _c_(678587, _a_(678586, _a_(678585, _n_(678584, "self", lambda: self), "entry_frame"), "pack"), side='right')
        _l_(678588)



        _c_(678592, _a_(678591, _a_(678590, _n_(678589, "self", lambda: self), "mid_frame"), "pack"), side ='top')
        _l_(678593)
        _c_(678597, _a_(678596, _a_(678595, _n_(678594, "self", lambda: self), "bottom_frame"), "pack"), side='bottom')
        _l_(678598)
        # enter main loop

        _c_(678601, _a_(678600, _n_(678599, "tkinter", lambda: tkinter), "mainloop"))
        _l_(678602)
    def instructions(self):
        _l_(678608)

        _c_(678606, _a_(678605, _a_(678604, tkinter, "messagebox"), "showinfo"), 'Instructions', 'This application allows the user to convert a temperature between Fahrenheit, Celsius, and Kelvin. '\
         'A user may select a unit to convert from, a unit to convert to, and what temperature they would like to convert. '\
          'Using this information they may convert the entered temperature into the desired unit.')
        _l_(678607)
#########################################
# called by the convert button, uses from_radio selection to decide who to convert into(which conversion function to call)
    def do_convert(self):
        _l_(678633)

        #self.converted_temp = None
        if _a_(678610, _n_(678609, "self", lambda: self), "from_radio") == 'FAHRENHEIT':
            _l_(678626)

            converted_temp = _c_(678612, _n_(678611, "f_convert", lambda: f_convert))
            _l_(678613)
        elif _a_(678615, _n_(678614, "self", lambda: self), "from_radio") == 'CELSIUS':
            _l_(678625)

            converted_temp = _c_(678617, _n_(678616, "c_convert", lambda: c_convert))
            _l_(678618)
        elif _a_(678620, _n_(678619, "self", lambda: self), "from_radio") == 'KELVIN':
            _l_(678624)

            converted_temp = _c_(678622, _n_(678621, "k_convert", lambda: k_convert))
            _l_(678623)
# sets self.answer(and so answer label) to value returned into converted_temp
        _c_(678631, _a_(678629, _a_(678628, _n_(678627, "self", lambda: self), "answer"), "set"), _n_(678630, "converted_temp", lambda: converted_temp))
        _l_(678632)
###########################################################
# series of functions for each individual unit to hold conversion formulas for each possible case
# using self.to_radio selection to decide which conversion to perform, then returns the resulting temperature 
# for use in do_convert 
    def f_convert(self):
        _l_(678654)

        if _a_(678635, _n_(678634, "self", lambda: self), "to_radio") == 'FAHRENHEIT':
            _l_(678651)

            new_temp = _a_(678637, _n_(678636, "self", lambda: self), "temp_entry")
            _l_(678638)
        elif _a_(678640, _n_(678639, "self", lambda: self), "to_radio") == 'CELSIUS':
            _l_(678650)

            new_temp = (_a_(678642, _n_(678641, "self", lambda: self), "temp_entry") - 32)*(5/9.0)
            _l_(678643)
        elif _a_(678645, _n_(678644, "self", lambda: self), "to_radio") == 'KELVIN':
            _l_(678649)

            new_temp = (_a_(678647, _n_(678646, "self", lambda: self), "temp_entry") + 459.67)*(5/9.0)
            _l_(678648)
        aux = _n_(678652, "new_temp", lambda: new_temp)
        _l_(678653)

        return aux

    def c_convert(self):
        _l_(678675)

        if _a_(678656, _n_(678655, "self", lambda: self), "to_radio") == 'FAHRENHEIT':
            _l_(678672)

            new_temp = (9/5.0)*_a_(678658, _n_(678657, "self", lambda: self), "temp_entry") + 32.0
            _l_(678659)
        elif _a_(678661, _n_(678660, "self", lambda: self), "to_radio") == 'CELSIUS':
            _l_(678671)

            new_temp = _a_(678663, _n_(678662, "self", lambda: self), "temp_entry")
            _l_(678664)
        elif _a_(678666, _n_(678665, "self", lambda: self), "to_radio") == 'KELVIN':
            _l_(678670)

            new_temp = _a_(678668, _n_(678667, "self", lambda: self), "temp_entry") + 273.15 
            _l_(678669) 
        aux = _n_(678673, "new_temp", lambda: new_temp)
        _l_(678674)

        return aux

    def k_convert(self):
        _l_(678696)

        if _a_(678677, _n_(678676, "self", lambda: self), "to_radio") == 'FAHRENHEIT':
            _l_(678693)

            new_temp = (9/5.0)*(_a_(678679, _n_(678678, "self", lambda: self), "temp_entry")-273.15) + 32
            _l_(678680)
        elif _a_(678682, _n_(678681, "self", lambda: self), "to_radio") == 'CELSIUS':
            _l_(678692)

            new_temp = _a_(678684, _n_(678683, "self", lambda: self), "temp_entry") - 273.15
            _l_(678685)
        elif _a_(678687, _n_(678686, "self", lambda: self), "to_radio") == 'KELVIN':
            _l_(678691)

            new_temp = _a_(678689, _n_(678688, "self", lambda: self), "temp_entry")
            _l_(678690)
        aux = _n_(678694, "new_temp", lambda: new_temp)
        _l_(678695)

        return aux

conv_gui = _c_(678699, _n_(678698, "TempConverterGUI", lambda: TempConverterGUI))
_l_(678700)