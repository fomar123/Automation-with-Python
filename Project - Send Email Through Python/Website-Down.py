import requests
import smtplib
import os


EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


response = requests.get('http://178-79-190-62.ip.linodeusercontent.com:8080/')
if False:
    print('Application is running Succefull')
else:
    print('Applicatipn Down. Fix it !')
    # send email to me
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo() #  identify the domain name of the sending host to SMTP before you issue a MAIL FROM command.
        msg = f"Subject: SITE DOWN\nFix the issue! Restart the application."
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
