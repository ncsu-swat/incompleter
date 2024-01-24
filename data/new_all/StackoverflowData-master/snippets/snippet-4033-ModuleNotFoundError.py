#Source: https://stackoverflow.com/questions/63841577/attributeerror-module-comtypes-gen-word-has-no-attribute-application-when
from tkinter import filedialog
from tkinter import *
import sys
import os
import comtypes.client

window = Tk()
window.geometry("300x300")
window.title("Hi")

label1 = Label(window, text="Hi", font=("arial", 16, "bold")).pack()


# start of select file button
def select_file():
    window.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("word documents", "*.docx"), ("all files", "*.*")))
    print(window.filename)
    print("work")

    wdFormatPDF = 17

    in_file = window.filename
    out_file = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


b = Button(window, text="Test", command=select_file)
b.pack()
# end of select file button

window.mainloop()