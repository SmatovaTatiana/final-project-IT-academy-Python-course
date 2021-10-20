from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from basis.dal import get_recipients
from basis.dal import get_content

sender = 'tatsm.reg@gmail.com'
cc = 'stv_stv@tut.by'
subject = "Daily news"


def create_message():
    recipients = get_recipients()
    content = get_content()
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg["Cc"] = cc
    body = MIMEText(content)
    msg.attach(body)
    return msg


def send_email():
    message = create_message()
    try:
        server = SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login('tatsm.reg@gmail.com', 'TatSmReg2019*')
        server.sendmail(message["From"], message["To"].split(",") + message["Cc"].split(","), message.as_string())
        server.quit()
        print("Mail sent successfully")
        return True
    except Exception as ex:
        print("Mail sent failed")
        print(ex)
        return False

#success = send_email()
