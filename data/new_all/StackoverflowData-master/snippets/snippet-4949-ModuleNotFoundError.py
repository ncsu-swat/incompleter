#Source: https://stackoverflow.com/questions/37910292/temperature-converter-gui-unboundlocalerror-attributeerror-issues
import tkinter
import tkinter.messagebox

class TempConverterGUI:
    def __init__(self):
# create main window, and set a custom window title
        self.main_window = tkinter.Tk()
        self.main_window.wm_title("Convert Temperatures")

# creates a top frame with label to give a title for the application
        self.top_frame = tkinter.Frame(self.main_window)
        self.title_label = tkinter.Label(self.top_frame, text= 'Temperature Converter')
        self.title_label.pack(side='top')
        self.top_frame.pack()
# create middle frame to hold main program components
        self.mid_frame = tkinter.Frame(self.main_window)
#############################################################################################
# create frame to hold the unit lists
        self.lists_frame = tkinter.Frame(self.mid_frame)
        ##########################
# create frame to hold original unit to convert from list components        
        self.from_list_frame = tkinter.Frame(self.lists_frame)
        self.from_label = tkinter.Label(self.from_list_frame, text='Convert from:')
        self.from_label.pack(side='top')

# creates radio button lists to allow user to decide which units to convert from
        self.from_radio = tkinter.StringVar()
        self.fb1 = tkinter.Radiobutton(self.from_list_frame, text= 'Fahrenheit', variable= self.from_radio, value= 'FAHRENHEIT')
        self.fb2 = tkinter.Radiobutton(self.from_list_frame, text= 'Celsius', variable= self.from_radio, value= 'CELSIUS')
        self.fb3 = tkinter.Radiobutton(self.from_list_frame, text= 'Kelvin', variable= self.from_radio, value= 'KELVIN')
        self.fb1.pack()
        self.fb2.pack()
        self.fb3.pack()
        ########################
# create frame to hold list components to decide which unit to convert to       
        self.to_list_frame = tkinter.Frame(self.lists_frame)
        self.to_label = tkinter.Label(self.to_list_frame, text='Convert to:')
        self.to_label.pack(side='top')
# creates radio button lists to allow user to decide which units to convert to
        self.to_radio = tkinter.StringVar()
        self.tb1 = tkinter.Radiobutton(self.to_list_frame, text= 'Fahrenheit', variable= self.to_radio, value= 'FAHRENHEIT')
        self.tb2 = tkinter.Radiobutton(self.to_list_frame, text= 'Celsius', variable= self.to_radio, value= 'CELSIUS')
        self.tb3 = tkinter.Radiobutton(self.to_list_frame, text= 'Kelvin', variable= self.to_radio, value= 'KELVIN')
        self.tb1.pack()
        self.tb2.pack()
        self.tb3.pack()
#############################################################################################       
#Create frame to hold textbox input
        self.entry_frame = tkinter.Frame(self.mid_frame)


        self.temp_prompt_label = tkinter.Label(self.entry_frame, text='Enter a temperature:')
        self.temp_entry = tkinter.Entry(self.entry_frame, width=10)
        self.temp_prompt_label.pack(side='top')
        self.temp_entry.pack(side='top')
############################################################################################################################################################################
############################################################################################################################################################################                    
# create frame to hold convert button components and answer label components        
        self.convert_frame = tkinter.Frame(self.mid_frame)

# label to display answer
        self.answer = tkinter.StringVar()
        self.answer_label = tkinter.Label(self.convert_frame, textvariable=self.answer)
        self.answer_label.pack(side='bottom')
# convert button for actual conversion
        self.convert_button = tkinter.Button(self.convert_frame, text='Convert', command=self.do_convert)##################################
        self.convert_button.pack(side='top')
#####################################################
        ##Consider creating either error box or popup

# create a bottom frame for miscellaneous buttons
        self.bottom_frame = tkinter.Frame(self.main_window)
        # instructions button that makes popup box telling how to use app
        self.instructions_button = tkinter.Button(self.bottom_frame, text='Instructions', command=self.instructions)
        self.instructions_button.pack(side='left')
# quit button that quits app
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.quit_button.pack(side='right')
##############################################      
# packup the frames
        self.from_list_frame.pack(side='left')
        self.to_list_frame.pack(side='left')

        self.lists_frame.pack(side='left')
        self.convert_frame.pack(side='left')
        self.entry_frame.pack(side='right')



        self.mid_frame.pack(side ='top')
        self.bottom_frame.pack(side='bottom')
        # enter main loop

        tkinter.mainloop()
        #print(self.from_radio.get(), self.to_radio.get(), self.temp_entry)####
    def instructions(self):
        tkinter.messagebox.showinfo('Instructions', 'This application allows the user to convert a temperature between Fahrenheit, Celsius, and Kelvin. '\
         'A user may select a unit to convert from, a unit to convert to, and what temperature they would like to convert. '\
          'Using this information they may convert the entered temperature into the desired unit.')
#########################################
# called by the convert button, uses from_radio selection to decide who to convert into(which conversion function to call)
    def do_convert(self):
        #self.converted_temp = None
        if self.from_radio == 'FAHRENHEIT':
            converted_temp = f_convert()
        elif self.from_radio == 'CELSIUS':
            converted_temp = c_convert()
        elif self.from_radio == 'KELVIN':
            converted_temp = k_convert()
# sets self.answer(and so answer label) to value returned into converted_temp
        self.answer.set(converted_temp)
###########################################################
# series of functions for each individual unit to hold conversion formulas for each possible case
# using self.to_radio selection to decide which conversion to perform, then returns the resulting temperature 
# for use in do_convert 
    def f_convert(self):
        if self.to_radio == 'FAHRENHEIT':
            new_temp = self.temp_entry
        elif self.to_radio == 'CELSIUS':
            new_temp = (self.temp_entry - 32)*(5/9.0)
        elif self.to_radio == 'KELVIN':
            new_temp = (self.temp_entry + 459.67)*(5/9.0)

        return new_temp

    def c_convert(self):
        if self.to_radio == 'FAHRENHEIT':
            new_temp = (9/5.0)*self.temp_entry + 32.0
        elif self.to_radio == 'CELSIUS':
            new_temp = self.temp_entry
        elif self.to_radio == 'KELVIN':
            new_temp = self.temp_entry + 273.15 

        return new_temp

    def k_convert(self):
        if self.to_radio == 'FAHRENHEIT':
            new_temp = (9/5.0)*(self.temp_entry-273.15) + 32
        elif self.to_radio == 'CELSIUS':
            new_temp = self.temp_entry - 273.15
        elif self.to_radio == 'KELVIN':
            new_temp = self.temp_entry

        return new_temp

conv_gui = TempConverterGUI()