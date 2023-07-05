import requests
import smtplib
import os


EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_notification(email_message):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()  # identify the domain name of the sending host to SMTP before you issue a MAIL FROM command.
        message = f"Subject: SITE DOWN\n{email_message}."
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)

try:
 response = requests.get('http://178-79-190-62.ip.linodeusercontent.com:8080/')
 if response.status_code == 200:
    print('Application is running Succefull')
 else:
    print('Applicatipn Down. Fix it !')
    msg = f'Application is running successfully!{response.status_code}'
    send_notification(msg)

except Exception as ex:
    print(f'Connection error happened: {ex}')
    msg = 'Application not accessible at all'
    send_notification(msg)
