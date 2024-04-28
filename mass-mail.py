import pandas as pd
import smtplib
from email.message import EmailMessage
import csv

your_mail = "your_email"
your_password = "your_smtp_app_password"

# establishing connection with gmail
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(your_mail, your_password)
 
# reading the csv file
df = pd.read_csv('path_to_csv_file')
emails = df['email']

# iterate through the records
for i in range(1):
    email = emails[i]

    print(i, email,'done')

    msg = EmailMessage()
    msg['Subject'] = f'Subject'
    msg['From'] = your_mail
    msg['To'] = email

    # bold text
    msg.set_content(f'''
    <html>
        <body>
            <p style="font-size: 20px; color: #000000;">Dear {email},</p>
            <p style="font-size: 20px; color: #000000;">Greetings!</p>
            <p style="font-size: 20px; color: #000000;">This is a sample email.</p>
            <p style="font-size: 20px; color: #000000;">Thank you.</p>
            <p style="font-size: 20px; color: #000000;">Regards,</p>
            <p style="font-size: 20px; color: #000000;">Sender</p>
        </body>
'''
    )

    print(msg.get_content())
    server.send_message(msg)

server.close()
