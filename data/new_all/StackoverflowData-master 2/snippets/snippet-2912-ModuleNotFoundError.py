#Source: https://stackoverflow.com/questions/58583980/typeerror-must-be-real-number-not-stringvar-any-idea-on-fixing
import tkinter as tk

#WINDOW PROPERTIES
GUI = tk.Tk()
GUI.title("Payroll Calculator")
GUI.minsize('305','110')
GUI.maxsize('305','110')

hoursWorked = tk.StringVar()
payRate = tk.StringVar()

#TAXES
states_dict = {'Alabama' : 0.035, 'Arizona' : 0.03565, 'Alaska' : 1, 'Arkansas' : 0.039, 'California' : 0.0715,
        'Colorado' : 1, 'Connecticut' : 0.04995, 'Delaware' : 0.044, 'Florida' : 1, 'Georgia' : 0.035, 'Hawaii' : 0.04825,
        'Idaho' : 4.5, 'Illinois' : 1, 'Indiana' : 1, 'Iowa' : 0.0467, 'Kansas' : 0.0405, 'Kentucky' : 0.04,
        'Louisiana' : 0.04, 'Maine' : 0.06475, 'Maryland' : 0.03875, 'Massachusetts' : 1, 'Michigan' : 1, 'Minnesota' : 0.076,
        'Mississippi' : 0.04, 'Missouri' : 0.0375, 'Montana' : 0.0395, 'Nebraska' : 0.0465, 'Nevada' : 1, 'New Hampshire' : 1,
        'New Jersey' : 0.05185, 'New Mexico' : 0.033, 'New York' : 0.0641, 'North Carolina' : 1, 'North Dakota' : 0.02, 'Ohio' : 0.0275, 'Oklahoma' : 0.0275,
        'Oregon' : 0.0745, 'Pennsylvania' : 1, 'Rhode Island' : 0.0487, 'South Carolina' : 0.035, 'South Dakota' : 1, 'Tennessee' : 1, 'Texas' : 1, 'Utah' : 1,
        'Vermont' : 0.0625, 'Washington' : 1, 'West Virginia' : 0.0475, 'Wisconsin' : 0.05825, 'Wyoming' : 1, 'District of Columbia' : 0.06475}

# NEW CALCULATE FUNCTION /////////////////////////////
def calculate():
    state = opt.get()
    print('state == {}'.format(state))
    tax = states_dict[state]
    print('tax in {} is {}'.format(state, tax))
    salary = (float(hoursWorked.get()) * float(payRate.get())) - (float(payRate.get()) * states_dict[state])
    print('tax in {} is {} result in salary:{}'.format(state, tax, salary))
    result.set(salary)
# ////////////////////////////////////////////////////

result = tk.StringVar()

#ENTRY
tk.Label(GUI, text='Pay Rate:', font="110").grid(row=0)
tk.Label(GUI, text='Hours Worked:', font="110").grid(row=1)

e1 = tk.Entry(GUI, textvariable = payRate)
e2 = tk.Entry(GUI, textvariable = hoursWorked)
e1.grid(row = 0, column = 1, sticky = tk.W)
e2.grid(row = 1, column = 1, sticky = tk.W)

#OPTION MENU
opt = tk.StringVar()
opt.set("Choose a state")

option = tk.OptionMenu(GUI, opt, *states_dict).grid(row=2, column=0)

frame = tk.Frame(GUI)
frame.grid()

results = tk.Label(GUI, textvariable = "Total Pay: $" + "%.2f" % result).grid(row=3, column=1)

button = tk.Button(frame, text='Calculate', fg='red', command=calculate)
button.grid(row=1, column=0)

#SET DEFAULTS
hoursWorked.set(0)
payRate.set(0)

#EVENT LOOP
GUI.mainloop()