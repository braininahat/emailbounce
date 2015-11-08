import pyforms
import smtplib
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from smtplib import *

sender = "dummystring"
smtpObj = smtplib.SMTP('smtp.gmail.com',587)

class EmailGUI(BaseWidget):
	def __init__(self):
		super(EmailGUI,self).__init__('EmailGUI')

		#Definition of the forms fields
		self._email = ControlText('Email', 'abc@example.com')
		self._password = ControlText('Password')
		self._receiver = ControlText('Recipients')
		self._message = ControlText('Message')
		self._buttonLogin = ControlButton('Login')
		self._buttonSend = ControlButton('Send')
		self._subject = ControlText('Subject')


		#Define the organization of the forms
		self._formset = [{'Tab1':['_email','||','_password','=',(' ','_buttonLogin', ' ')],'Tab2': ['_receiver','||','_subject','||','_message','=',(' ','_buttonSend', ' ')]}]
		#Use dictionaries for tabs
		#Use the sign '=' for a vertical splitter
		#Use the signs '||' for a horizontal splitter

		#Define the button action
		self._buttonLogin.value = self.__buttonLoginAction
		self._buttonSend.value = self.__buttonLoginAction

	def __buttonLoginAction(self):
		global sender
		global smtpObj
		sender = self._email.value
		password = self._password.value
		try:
			smtpObj.ehlo()
			smtpObj.starttls()
			smtpObj.login(sender,password)
		except SMTPResponseException as e:
			error_code = e.smtp_code
			error_message = e.smtp_error
			print str(error_code) + ": " + error_message

	def __buttonSendAction(self):
		global sender
		receiver = self._receiver.value
		subject = self._subject.value
		message = self._message.value
		messageString = """From: From Person <"""+sender+""">
To: To Person <"""+receiver+""">
Subject: """+subject+"""
"""+message+"""
"""
		try:
			smtpObj.sendmail(sender,receiver,messageString)
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

#Execute the application
if __name__ == "__main__":	 pyforms.startApp(EmailGUI)
