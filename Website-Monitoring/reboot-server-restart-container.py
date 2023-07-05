import linode_api4
import requests
import smtplib
import os
import paramiko
import time



EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
LINODE_TOKEN = os.environ.get('LINODE_TONKEN')

def send_notification(email_message):
    print('Sending and email....')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()  # identify the domain name of the sending host to SMTP before you issue a MAIL FROM command.
        message = f"Subject: SITE DOWN\n{email_message}."
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)

def restart_container():
    print('Restarting the Application.....')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # automatically add host key
    ssh.connect(hostname='178.79.191.36', username='root', key_filename='/Users/farahomar/.ssh/id_rsa')
    stdin, stdout, stderr = ssh.exec_command('docker start daa93fec603e')
    print(stdout.readlines())
    ssh.close()  # close ssh connection

def restart_server_and_container():
    # restart linode server
    linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = client.load(Linode_api4.Instance, 47483379)
    nginx_server.reboot()

    # restart the application
    while True:
        nginx_server = client.load(Linode_api4.Instance, 47483379)
        if nginx_server.status == 'running':
            time.sleep(5)
            restart_container()
            break



try:
  response = requests.get('http://178-79-191-36.ip.linodeusercontent.com:8080/')
  if False:
      print('Application is running successfully!')
  else:
      print('Application Down. Fix it!')
      msg = f'Application returned {response.status_code}'
      send_notification(msg)


     # restart the application


except Exception as ex:
    print(f'Connection error happened: {ex}')
    msg = 'Application not accessible at all'
    send_notification(msg)
    restart_server_and_container()
