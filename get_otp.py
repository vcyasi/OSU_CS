########################################
# Vincent Yasi
# CS 370 -Intro to Security
# Programming Assignment 2
#
# This file contains the function for the <get-otp> command of submission.py.
# Requires the Python module <pyotp> to be installed
#
# Asks for username and password, and then generates the one-time password
# for those credentials, based on the current time, displaying it to the console.
# Should match the same OTP produced by Google Authenticator with credentials.
#
# Help recieved from pyotp Python module manual
####################################################################################

import pyotp

def get_otp():
	# Get username and password
	user_name = raw_input("Please enter your username: ")
	password = raw_input("Please enter your password: ")

	# produce TOTP
	totp = pyotp.TOTP(password)
	#display TOTP
	print("One-Time Password is:" + totp.now())
	# NOTE: displays OTP for current time
	#	If clocks between host and Google Authenticator
	#	are slightly off (especially if done right at 30 secs
	#	switch-over), OTP may be old and need to be rerun.