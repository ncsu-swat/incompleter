#Source: https://stackoverflow.com/questions/71251272/typeerror-type-object-is-not-iterable
from msilib import make_id
from tkinter import simpledialog,Tk
def number():
    win = make_id('')
def winner_number():
    numberd = 'c4'
def get_task():
    task=simpledialog.askstring("id製造器",'你要製造id嗎?')
    return task
def get_message():
    message=simpledialog.askstring('你的id是:',number,'中獎號碼:',winner_number)
    return message
screen = Tk()

while True:
    task=get_task()
    if task == "要":
        massage= get_message
        number = make_id
        if number(str) in winner_number():
            print('你的運氣超好!!')
    elif task=='cancel':
        print('你失敗了!!')
    else:
        break