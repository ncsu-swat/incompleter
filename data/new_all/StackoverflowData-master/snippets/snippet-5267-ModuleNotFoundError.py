#Source: https://stackoverflow.com/questions/74753310/how-to-solve-this-error-filenotfounderror-errno-2-no-such-file-or-directory
import pandas as pd
from tkinter import *
from tkinter import filedialog as fd

app = Tk()
file_path = ''
def set_file_path(path):
    global file_path
    file_path = path



def open_text_file():
    filetypes = (
        ('Excel files', '*.xlsx'),
        ('All files', '*.*')
    )
    file = fd.askopenfile(filetypes=filetypes)
    set_file_path(file)

def main(row, column, file):
    file = pd.read_excel(file)
    row_new = row - 1
    column_new = column - 1
    text = file[column_new][row_new]
    return text


app.title('XLSX Reader')
app.geometry("400x400")
open_button = Button(app, text='Choose File', command=open_text_file)
open_button.pack()
row = Entry(app)
row.pack()
column = Entry(app)
column.pack()
Submit = Button(app, text='Get Text', command=main(row=row,column=column,file=file_path))
Submit.pack()
output = main()
label = Label(text=output)
label.pack()

app.mainloop()