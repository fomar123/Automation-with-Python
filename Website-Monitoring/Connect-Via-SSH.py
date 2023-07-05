import requests
import smtplib
import os
import paramiko



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
  response = requests.get('http://178-79-191-36.ip.linodeusercontent.com:8080/')
  if False:
      print('Application is running successfully!')
  else:
      print('Application Down. Fix it!')
      msg = f'Application returned {response.status_code}'
      send_notification(msg)


     # restart the application
      ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # automatically add host key
  ssh.connect(hostname='178.79.191.36', username='root', key_filename='/Users/farahomar/.ssh/id_rsa')
  stdin, stdout, stderr = ssh.exec_command('docker ps')
  print(stdout.readlines())
  ssh.connect() # close ssh connection

except Exception as ex:
    print(f'Connection error happened: {ex}')
    msg = 'Application not accessible at all'
    send_notification(msg)

