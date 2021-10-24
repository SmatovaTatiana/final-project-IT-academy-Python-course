from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import datetime
from datetime import datetime
from basis.dal import get_recipients
from basis.dal import get_content

sender = 'tatsm.reg@gmail.com'
subject = "Daily news"


def format_content():
    content = get_content()
    body = ''
    lines = content.split(',')
    cnt = 0
    for line in lines:
        if line:
            line += '\n'
            cnt += 1
            if cnt == 2:
                line += '\n'
                cnt = 0
            body += line

    return body


def create_message():
    recipients = get_recipients()
    content = format_content()
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    body = MIMEText(content)
    msg.attach(body)
    return msg


def send_email():
    print("Mailing started at ", datetime.now(), '.\n')
    message = create_message()
    try:
        server = SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login('tatsm.reg@gmail.com', 'TatSmReg2019*')
        server.sendmail(message["From"], message["To"].split(","), message.as_string())
        server.quit()
        print("News sent successfully at ", datetime.now(), '.\n')
        return True
    except Exception as ex:
        print('News send failed', ex, '\n')
        return False

# success = send_email()
