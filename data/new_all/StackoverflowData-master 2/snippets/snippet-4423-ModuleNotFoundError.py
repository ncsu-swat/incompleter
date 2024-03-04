#Source: https://stackoverflow.com/questions/58016854/attributeerror-unknown-senton-error-in-python-outlook
# -*- coding: latin-1 -*-
import win32com.client
import os
import datetime

today = datetime.date.today()
path = os.path("D:\my_path")

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI") #Opens Microsoft Outlook
inbox = outlook.GetDefaultFolder(6) #N4 Invocie folder
messages = inbox.Items  #Get first email


def saveattachemnts(subject = "Title Maíl - *"):
    for message in messages:
        if message.Subject == subject and message.Unread or message.Senton.date() == today:
            attachments = message.Attachments
            attachment = attachments.Item(1)
            for attachment in message.Attachments:
                attachment.SaveAsFile(os.path.join(path, str(attachment)))
                if message.Subject == subject and message.Unread:
                    message.Unread = False
                break

saveattachemnts()
os.system("this_python.py")