#####################################################################################
# Vincent Yasi
# CS 370 -Intro to Security
# Programming Assignment 2
#
# This file contains the function for the <generate-qr> command of submission.py.
# Requires the Python module <pyqrcode> to be installed
#
# Asks for username and password, and then creates a QR code in .svg format
# which can be scanned into Google Authenticator to provide info to the app.
#
# Help recieved from pyqrcode Python module manual and
# https://www.geeksforgeeks.org/python-generate-qr-code-using-pyqrcode-module/
####################################################################################

import pyqrcode
from pyqrcode import QRCode


def generate_qr():
	# Get username and password
	user_name = raw_input("Please enter your username: ")
	password = raw_input("Please enter your password: ")

	# Construct Google URI
	uri = "otpauth://totp/YasiCorp:" + user_name + "?secret=" + password + "&issuer=YasiCorp"

	# Create QR code with URI
	code = pyqrcode.create(uri)

	# Save QR code as svg file
	# Named by the username
	code.svg(user_name + ".svg", scale = 8)
	print("QR code saved as " + user_name + ".svg")