#Source: https://stackoverflow.com/questions/71795534/traceback-most-recent-call-last-attributeerror-nonetype-object-has-no-attr
from tkinter import *
import pandas as pd


def send_info():
  path = 'Registers.form.xlsx'
  df1 = pd.read_excel(path)
  SeriesA = df1['firstname']
  SeriesB = df1['secondname']
  SeriesC = df1['thirdname']
  SeriesD = df1['age']
  SeriesE = df1['phonenumber']
  SeriesF = df1['Departmentname']
  SeriesG = df1['familymembers']
  SeriesH = df1['bookingdate']
  A = pd.Series(firstname.get)
  B = pd.Series(secondname.get)
  C = pd.Series(thirdname.get)
  D = pd.Series(age.get)
  E = pd.Series(phonenumber.get)
  F = pd.Series(Departmentname.get)
  G = pd.Series(familymembers.get)
  H = pd.Series(bookingdate.get)
  SeriesA = SeriesA.append(A)
  SeriesB = SeriesA.append(B)
  SeriesC = SeriesA.append(C)
  SeriesD = SeriesA.append(D)
  SeriesE = SeriesA.append(E)
  SeriesF = SeriesA.append(F)
  SeriesG = SeriesA.append(G)
  SeriesH = SeriesA.append(H)
  df2 = pd.DataFrame({"firstname": SeriesA, "secondnamer": SeriesB, "thirdname": SeriesC, "age": SeriesD, "phonenumber": SeriesE, "Departmentname": SeriesF, "familymembers": SeriesG, "bookingdate": SeriesH})
  df2.to_excel(path, index=False)











  firstname_entry.delete(0, END)
  secondname_entry.delete(0, END)
  thirdname_entry.delete(0, END)
  age_entry.delete(0, END)
  phonenumber_entry.delete(0, END)
  Departmentname_entry.delete(0, END)
  familymembers_entry.delete(0, END)
  bookingdate_entry.delete(0, END)
  
screen = Tk()
screen.geometry("1080x1080")
screen.title("مديرية شؤون البطاقة الوطنية")
welcome_text = Label(text="أهلا وسهلا بكم في الحجز الالكتروني للبطاقة الموحدة ", fg="white", bg="green",height=2 ,width=1080)
welcome_text.grid()
 
firstname_text = Label(text = "الاسم الاول * ",).grid(row=0)
secondname_text = Label(text = "الاسم الثاني * ",).grid(row=1)
thirdname_text = Label(text = "الاسم الثالث * ",).grid(row=2)
age_text = Label(text = "العمر * ",).grid(row=3)
phonenumber_text = Label(text = "رقم الهاتف * ",).grid(row=4)
Departmentname_text = Label(text = "اسم دائرة الاحوال المدنية * ",).grid(row=5)
familymembers_text = Label(text = "عدد افراد الاسرة * ",).grid(row=6)
bookingdate_text = Label(text = "موعد تاريخ الحجز المطلوب * ",).grid(row=7)

firstname_text.place(x = 540, y = 70)
secondname_text.place(x = 540, y = 130)
thirdname_text.place(x = 540, y = 190)
age_text.place(x = 540, y = 250)
phonenumber_text.place(x = 540, y = 310)
Departmentname_text.place(x = 540, y = 370)
familymembers_text.place(x = 540, y = 430)
bookingdate_text.place(x = 540, y = 490)



firstname = StringVar()
secondname = StringVar()
thirdname = StringVar()
age = StringVar()
phonenumber = StringVar()
Departmentname = StringVar()
familymembers = StringVar()
bookingdate = StringVar()

firstname_entry = Entry(textvariable = firstname, width = "40")
secondname_entry = Entry(textvariable = secondname, width = "40")
thirdname_entry = Entry(textvariable = thirdname, width = "40")
age_entry = Entry(textvariable = age, width = "40")
phonenumber_entry = Entry(textvariable = phonenumber, width = "40")
Departmentname_entry = Entry(textvariable = Departmentname, width = "40")
familymembers_entry = Entry(textvariable = familymembers, width = "40")
bookingdate_entry = Entry(textvariable = bookingdate, width = "40")

firstname_entry.place(x = 450, y = 100)
secondname_entry.place(x = 450, y = 160)
thirdname_entry.place(x = 450, y = 220)
age_entry.place(x = 450, y = 280)
phonenumber_entry.place(x = 450, y = 340)
Departmentname_entry.place(x = 450, y = 400)
familymembers_entry.place(x = 450, y = 460)
bookingdate_entry.place(x = 450, y = 520)

firstname_entry.grid(row=0,column=1)
secondname_entry.grid(row=1,column=1)
thirdname_entry.grid(row=2,column=1)
age_entry.grid(row=3,column=1)
phonenumber_entry.grid(row=4,column=1)
Departmentname_entry.grid(row=5,column=1)
familymembers_entry.grid(row=6,column=1)
bookingdate_entry.grid(row=7,column=1)


register = Button(screen,text = "Register", width = "60", height = "2", command = send_info, bg = "grey").grid(row=3,column=1, pady=4)
register.place(x = 360, y = 600)

screen.mainloop ()