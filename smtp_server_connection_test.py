import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# python3 -m smtpd -n -c DebuggingServer localhost:1025

msg = MIMEMultipart()
msg['From'] = 'me@gmail.com'
msg['To'] = 'you@gmail.com'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('localhost', 1025)

mailserver.sendmail('me@gmail.com', 'you@gmail.com', msg.as_string())

mailserver.quit()