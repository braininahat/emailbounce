import pyforms
import smtplib
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from smtplib import *

class EmailGUI(BaseWidget):
	def __init__(self):
		super(EmailGUI,self).__init__('EmailGUI')

		#Definition of the forms fields
		self._email = ControlText('Email', 'abc@example.com')
		self._password = ControlText('Password')
		self._receivers = ControlText('Recipients')
		self._message = ControlText('Message')
		self._buttonLogin = ControlButton('Login')
		self._buttonSend = ControlButton('Send')


		#Define the organization of the forms
		self._formset = [{'Tab1':['_email','||','_password','=',(' ','_buttonLogin', ' ')],'Tab2': ['_receivers','||','_message','=',(' ','_buttonSend', ' ')]}]
		#Use dictionaries for tabs
		#Use the sign '=' for a vertical splitter
		#Use the signs '||' for a horizontal splitter

		#Define the button action
		self._buttonLogin.value = self.__buttonLoginAction
		self._buttonSend.value = self.__buttonLoginAction

	def __buttonLoginAction(self):
		"""Button action event"""
	def __buttonSendAction(self):
		""" """

#Execute the application
if __name__ == "__main__":	 pyforms.startApp(EmailGUI)
