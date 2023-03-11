import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Suraj'
email['to'] = 'suraj11nag@gmail.com'
email['subject'] = 'Letter of acceptance to Hogwarts School of Witchcraft and Wizardry!'

email.set_content(html.substitute({'name': 'Harry'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() #encryption mechanism, to connect securely to the server.
    smtp.login('data11scientist@gmail.com', 'password')
    smtp.send_message(email)
    print('Email sent, boss!')