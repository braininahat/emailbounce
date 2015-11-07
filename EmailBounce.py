import smtplib
from smtplib import *

sender = 'gordon.kildall@gmail.com'
receivers = ['varun.shijo@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <varun.shijo@gmail.com>
Subject: SMTP e-mail test
This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.starttls()
    smtpObj.login(sender,'pass')
    smtpObj.sendmail(sender,receivers,message)
    print "Successfully sent email"
except SMTPResponseException as e:
    error_code = e.smtp_code
    error_message = e.smtp_error
    if error_code == 422:
        print "Recipient Mailbox Full"
    elif error_code == 431:
        print "Server out of space"
    elif error_code == 447:
        print "Timeout. Try reducing number of recipients"
    elif error_code == 510 or error_code == 511:
        print "One of the addresses in your TO, CC or BBC line doesn't exist. Check again your recipients' accounts and correct any possible misspelling."
    elif error_code == 512:
        print "Check again all your recipients' addresses: there will likely be an error in a domain name (like mail@domain.coom instead of mail@domain.com)"
    elif error_code == 541 or error_code == 554:
        print "Your message has been detected and labeled as spam. You must ask the recipient to whitelist you"
    elif error_code == 550:
        print "Though it can be returned also by the recipient's firewall (or when the incoming server is down), the great majority of errors 550 simply tell that the recipient email address doesn't exist. You should contact the recipient otherwise and get the right address."
    elif error_code == 553:
        print "Check all the addresses in the TO, CC and BCC field. There should be an error or a misspelling somewhere."
    else:
        print str(error_code) + ": " + error_message
