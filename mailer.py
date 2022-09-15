import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
import constant as C

username = C.EMAIL_USER
password = C.EMAIL_PASSWORD
default_address = [C.EMAIL_ADRRESS_TO]


def send_mail(send_from: str, subject: str, text: str,
              send_to: list, files=None):
    send_to = default_address if not send_to else send_to
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = ', '.join(send_to)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            ext = f.split('.')[-1:]
            attachedfile = MIMEApplication(fil.read(), _subtype=ext)
            attachedfile.add_header(
                'content-disposition', 'attachment', filename=basename(f))
        msg.attach(attachedfile)

    smtp = smtplib.SMTP(host=C.EMAIL_SMTP_ADDRESS, port=C.EMAIL_SMTP_PORT)
    smtp.starttls()
    try:
        smtp.login(username, password)
        smtp.sendmail(send_from, send_to, msg.as_string())
        print("EMAIL | Success. Email has been sent.")
    except smtplib.SMTPResponseException as e:
        error_code = e.smtp_code
        error_message = e.smtp_error
        print("ERROR: ", error_message)
        print("SMTP ERROR CODE: ", error_code)
    smtp.close()
