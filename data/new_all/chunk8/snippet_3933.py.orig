#Source: https://stackoverflow.com/questions/65194399/how-to-fix-attributeerror-partially-initialized-module-sendemail-has-no-attr
import tkinter as tk
import time
from tkinter import filedialog
import SendEmail

# Main Screen
root = tk.Tk()
root.resizable(False, False)
root.title('Mail Sender')

# Icon
icon = tk.PhotoImage(file='icon.png')
root.iconphoto(False, icon)

# Canvas
canvas = tk.Canvas(root, height=600, width=700)
canvas.pack()

# title
titleFrame = tk.Frame(root)
titleFrame.place(relx=0.5, rely=0.025, relwidth=0.75, relheight=0.1, anchor='n')

title = tk.Label(titleFrame, text="Mail Sender", font=('Calibri', 20))
title.pack()

# Main frame
mainframe = tk.Frame(root, bg='#80c1ff', bd=10)
mainframe.place(relx=0.5, rely=0.15, relwidth=1, relheight=0.85, anchor='n')

# Email
email = tk.Label(mainframe, text="Enter Email:", font=('Calibri', 15))
email.place(y=2.5)

email_str = tk.StringVar()

emailEntry = tk.Entry(mainframe, textvariable=email_str, font=('Calibri', 15))
emailEntry.place(y=35, width=300)

# password
password = tk.Label(mainframe, text="Enter Password:", font=('Calibri', 15))
password.place(y=80)

password_str = tk.StringVar()

passwordEntry = tk.Entry(mainframe, textvariable=password_str, show="\u2022", font=('Calibri', 15))
passwordEntry.place(y=115, width=300)

# receiver
receiver = tk.Label(mainframe, text="Enter Receiver Email:", font=('Calibri', 15))
receiver.place(y=150)

receiver_str = tk.StringVar()

receiverEntry = tk.Entry(mainframe, textvariable=receiver_str, font=('Calibri', 15))
receiverEntry.place(y=185, width=300)

# subject
subject = tk.Label(mainframe, text="Enter Subject:", font=('Calibri', 15))
subject.place(y=220)

subject_str = tk.StringVar()

subjectEntry = tk.Entry(mainframe, textvariable=subject_str, font=('Calibri', 15))
subjectEntry.place(y=255, width=300)

# body
body = tk.Label(mainframe, text="Enter Body:", font=('Calibri', 15))
body.place(x=500, y=2.5)

body_str = tk.StringVar()

bodyEntry = tk.Text(mainframe)
bodyEntry.place(x=380, y=35, width=300)

# notification
notif = tk.Label(mainframe, bg='#80c1ff', font=('Calibri', 15))
notif.place(x=250, y=450)

# attachments array
attachments = []


# add attacments function
def add_attachments():
    filename = filedialog.askopenfilename(initialdir='C:/', title="Select a file to attach to the email")
    attachments.append(filename)

    notif.config(text="Attached " + str(len(attachments)) + " file", fg="green")

    root.update()
    time.sleep(2.5)

    notif.config(text="")


def reset_entries():
    emailEntry.delete(0, 'end')
    passwordEntry.delete(0, 'end')
    receiverEntry.delete(0, 'end')
    subjectEntry.delete(0, 'end')
    bodyEntry.delete("1.0", "end-1c")

    notif.config(text="Entries were reset", fg="green")

    root.update()
    time.sleep(2.5)

    notif.config(text="")


# send button
send = tk.Button(mainframe, text="Send Email", font=('Calibri', 15), command=lambda: SendEmail.send_email())
send.place(y=310, width=150)

# reset button
reset = tk.Button(mainframe, text="Reset", font=('Calibri', 15), command=lambda: ResetEntries.reset_entries())
reset.place(x=220, y=310, width=150)

# attachments button
attachment = tk.Button(mainframe, text="Add Attachments", font=('Calibri', 15), command=lambda: add_attachments())
attachment.place(x=90, y=365, width=200)

# Main loop
root.mainloop()