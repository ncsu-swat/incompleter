#Source: https://stackoverflow.com/questions/73741857/attributeerror-function-object-has-no-attribute-read-excel
def load():
    path=filedialog.askopenfilename()
    df=pd.read_excel(path)
    print(df)
def save():
    mese = entry2.get()
    altezza = entry3.get()
    peso = entry4.get()
    mmagra = entry5.get()
    mgrassa = entry6.get()
    utente = entry7.get()
    wb = Workbook()
    ws = wb.active
    ws['A1'] = "Mese"
    ws['B1'] = "Altezza"
    ws['C1'] = "Peso"
    ws['D1'] = "Massa Magra"
    ws['E1'] = "Massa Grassa"
    ws['F1'] = "Utente"
    ws['A2'] = mese
    ws['B2'] = altezza
    ws['C2'] = peso
    ws['D2'] = mmagra
    ws['E2'] = mgrassa
    ws['F2'] = utente
    wb.save(r'C:\Users\lricci\Desktop\SERVER\web\Gym Tracker\Gym Tracker v1.0\track.xlsx')
    showinfo("Salvataggio")
    file1 = pd.read_excel("track.xlsx")
    file2 = pd.read_excel("trackn.xlsx")
    all = [file1, file2]
    append = pd.concat(all)
    append.to_excel("track.xlsx", index=False)
def delete():
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)
    entry6.delete(0, tk.END)
    entry7.delete(0, tk.END)

# Main frame
windows = tk.Tk()
windows.geometry("400x350")
windows.title("Gym Tracker")
windows.resizable(False, False)

#Frame 2
frame1 = Frame(windows, width=150, height=30, highlightcolor="white",highlightbackground="black", highlightthickness=1).place(x=120, y=2)
label1= Label(windows, text="GYM TRACKER").place(x=150, y=7)
frame2 = Frame(windows, width=500, height=1, highlightcolor="white",highlightbackground="black", highlightthickness=1).place(x=2, y=45)

# Combobox Mese
label2 = Label(windows, text="Mese").place(x=110, y=60)
combobox = Combobox(windows, values=['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno','Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']).place(x=200, y=60)
entry2 = tk.Entry(windows)

label3 = Label(windows, text="Altezza").place(x=110, y=90)
textbox1 = Text(windows, width=17, height=1).place(x=200, y=90)
entry3 = tk.Entry(windows)

label4 = Label(windows, text="Peso").place(x=110, y=120)
textbox = Text(windows, width=17, height=1).place(x=200, y=120)
entry4 = tk.Entry(windows)

label5 = Label(windows, text="Massa Magra").place(x=110, y=150)
textbox = Text(windows, width=17, height=1).place(x=200, y=150)
entry5 = tk.Entry(windows)

label6 = Label(windows, text="Massa Grassa").place(x=110, y=180)
textbox = Text(windows, width=17, height=1).place(x=200, y=180)
entry6 = tk.Entry(windows)
# Combobox Utente
label7 = Label(windows, text="Utente").place(x=110, y=210)
combobox = Combobox(windows, values=['Erika', 'Lorenzo']).place(x=200, y=210)
entry7 = tk.Entry(windows)

# Bottoni
b1 = tk.Button(windows, text="Elimina", command=delete ,width=8, height=1).place(x=170, y=310)
b2 = tk.Button(windows, text="Load", width=8, height=1,command=load).place(x=300, y=310)
b3 = tk.Button(windows, text="Salva", width=8, height=1, command=save).place(x=50, y=310)
windows.mainloop()