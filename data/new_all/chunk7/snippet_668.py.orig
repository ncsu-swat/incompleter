#Source: https://stackoverflow.com/questions/63063811/typeerror-utf8-is-an-invalid-keyword-argument-for-compat32-smtplib-email-erro
import csv
from string import Template
import smtplib
import random
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




template_file = r'C:\Users\91880\Desktop\template.txt'
filename = r'C:\Users\91880\Downloads\2307.csv'


#  reads the file and returns the names, emails in a list
def get_contacts(file):
    names_list = []
    emails_list = []
    with open(file, 'r') as mail_data:
        data = csv.reader(mail_data)
        for details in data:
            names_list.append(details[0])
            emails_list.append(details[1])
    return names_list, emails_list


# reads the template from a text file and returns
def get_template(file):
    with open(file, 'r') as template_info:
        template_data = template_info.read()
    return Template(template_data)


def main():
    email_user = 'myemail@mail.com'
    password = 'mypassword'

    subs = ['Hi', 'Hello']

    names, emails = get_contacts(filename)
    template = get_template(template_file)

    with smtplib.SMTP('smtp.office365.com', '587') as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_user, password)
        for name, email in zip(names, emails):
            subject = random.choice(subs)
            number = random.randint(10, 30)
            msg = MIMEMultipart()
            message = template.substitute(name=name.title())
            msg['From'] = email_user
            msg['To'] = email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'html'))
            smtp.send_message(msg)
            print(f'sent email to {name} at {email}')
            del msg
            time.sleep(number)


if __name__ == '__main__':
    main()