#Source: https://stackoverflow.com/questions/40579983/attributeerror-outlook-application-logon
import win32com.client

def main():  

    session = win32com.client.dynamic.Dispatch("Outlook.Application")
    session.Logon('Outlook') 
    inbox = session.Inbox
    message = inbox.Messages.GetLast()
    attachments = message.Attachments
    for i in range(attachments.Count):
        attachment = attachments.Item(i + 1)
        filename = 'C:\EMAILS\tempfile_%i' % i
        attachment.WriteToFile(filename)
    session.Logoff()

if __name__ == '__main__':
    main()