import smtplib
from smtplib import *

sender = ''
receivers = ['']

message = """From: From Person <from@fromdomain.com>
To: To Person <>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
  smtpObj = smtplib.SMTP('smtp.gmail.com',587)
  smtpObj.starttls()
  smtpObj.login(sender,'')
  smtpObj.sendmail(sender, receivers, message)
  print "Successfully sent email"
except SMTPException:
 print "Error: unable to send email"
