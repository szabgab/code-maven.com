import smtplib
from email.mime.text import MIMEText

me = 'Code Maven <gabor@from.com>'
you = [
    'Gabor Szabo <gabor@to.com>',
    'other@gmail.com'
]

msg = MIMEText("Content of the email")
msg['Subject'] = 'The subject line'
msg['From'] = me
msg['To'] = ','.join(you)

s = smtplib.SMTP('localhost')
s.sendmail(me, you, msg.as_string())
s.quit()

