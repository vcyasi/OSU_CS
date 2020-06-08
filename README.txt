********************************
* Vincent Yasi
* CS 370 -Intro to Security-
* Programming Assignment 2
********************************

The program for this assignment is built in Python.
To run it, you need to follow two steps:

1.) install the Python modules "pyqrcode" and "pyotp"
	This can be done on the OSU flip servers with the commands:
		"pip install pyqrcode"
		"pip install pyotp"

2.) run the program with "python submission.py <command>"
	The possible commands are:
		generate-qr  - generates QR code used by Google Authenticator
		get-otp      - determines and displays OTP produced by Google Authenticator


generate-qr
------------
Asks for your username and password, and then creates a QR code
in .svg format which can be scanned into Google Authenticator
to provide your information to the app.

Takes in the information, and then concatenates it into a string,
which is run through pyqrcode.create() to encode into a QR code.
Then, saves the created QR code as a .svg file in the directory of the program.
The QR code filename is <your username>.svg
The organization for this command is hard-coded to be YasiCorp, but the
username and password are collected from user input.


get-otp
------------
Asks for your username and password, and then displays the OTP
that matches the one Google Authenticator produces for those credentials.
Uses built in functions of "pyotp" module to do so with password.
Displays OTP to screen.

Takes in information and feeds it into pyotp.TOTP() to get TOTP.
Then uses system clock to generate current OTP of current time,
and displays it to screen.

***************
* Assumptions *
***************
One assumption I made was assuming we could use pre-built libraries and
did not need to build everything from scratch.  There was nothing about that in the
assignment, so I researched various libraries, etc. which could aid in this assignment,
and I found that Python had ones which made the assignment easier.

I also assumed that the "secret" Google Authenticator wanted was the password.
I could find no firm documentation on what it should be, so I went with a password.

Lastly, I also assumed that we only needed to generate the OTP for the current time,
and not the last and next 30 secs interval, like some applications do.
