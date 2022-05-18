import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from student_attendence import student

body_file = open('body.txt', 'r')

username = '#'
password = '#'

body = body_file.read()


def send_mail(text=body, subject='Ward Absent',
              from_email=' DPS <site39617@gmail.com>', to_emails=None, html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = "-".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)
    msg_str = msg.as_string()

    # login to my smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()
    print('Email Sent!')


# iterating, to send multiple emails
# send_mail(to_emails=[student])

for x in student:
    send_mail(to_emails=[x])
