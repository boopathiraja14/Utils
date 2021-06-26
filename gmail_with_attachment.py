import os
import pandas as pd
import smtplib
import mimetypes
from email.message import EmailMessage
#


body = """Dear Student, 

Please find your certificate attached, let us know if there are any corrections. All the best.

Thanks,

"""


#
# for filename in os.listdir('C:/Users/C Ramasamy/Downloads/certs'):
#     print(filename)

df = pd.read_csv('C:/Users/C Ramasamy/Downloads/certs/mailids.csv')

for filename, mail_id in zip(df['name'], df['mail']):

    message = EmailMessage()

    message['From'] = "***@gmail.com"
    message['To'] = mail_id

    message['Cc'] = ''
    message['Subject'] = 'Completion Certificate - Machine learning'

    message.set_content(body)

    filename_full = filename + '.pdf'
    filename_full = 'C:/Users/C Ramasamy/Downloads/certs/' + filename_full
    print(filename, mail_id)

    mime_type, _ = mimetypes.guess_type(filename_full)
    mime_type, mime_subtype = mime_type.split('/')
    with open(filename_full, 'rb') as file:
        message.add_attachment(file.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=filename)

    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.set_debuglevel(1)
    mail_server.login("****@gmail.com", 'password')
    mail_server.send_message(message)
    mail_server.quit()

#
