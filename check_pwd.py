###############################################################################
# Vincent Yasi
# A2: TDD Hands On
###############################################################################
# The password checking function for A2: TDD Hands On.
# Function is called check_pwd().
#
# Function checks that passed password is valid by checking:
# - 8 to 20 characters
# - at least one upper- and one lower-case letter
# - at least one digit
# - at least one symbol from ~`!@#$%^&*()_+-=
#
# Function was constructed step by step using TTD method in conjunction
# with tests.py
###############################################################################

def check_pwd(inPwd):
	# check password length
	if len(inPwd) >= 8 and len(inPwd) <= 20:
		# check each char in inPwd to see if at least one uppercase
		upper = 0 # if even one letter is uppercase, will be greater than 0
		for charLetter in inPwd:
			# if char is uppercase, will increment upper by 1
			# if not, will just add 0
			upper = upper + charLetter.isupper()
		# check if upper is greater than 0 (found uppercase)
		if upper > 0:
			# check there is at least one digit
			# use similar test to above, but with digits
			digit = 0
			for charDigit in inPwd:
				# if char is digit, will increment digit by 1
				# if not, will just add 0
				digit = digit + charDigit.isdigit()
			# check digit is greater than 0 (found digit)
			if digit > 0:
				# check each char to see if it is one of the appropriate symbols
				# similar method as above
				symbol = 0 # counter to count number of valid sysmbols found
				for charSym in inPwd:
					if charSym == '~':
						symbol = symbol + 1
					elif charSym == '`':
						symbol = symbol + 1
					elif charSym == '!':
						symbol = symbol + 1
					elif charSym == '@':
						symbol = symbol + 1
					elif charSym == '#':
						symbol = symbol + 1
					elif charSym == '$':
						symbol = symbol + 1
					elif charSym == '%':
						symbol = symbol + 1
					elif charSym == '^':
						symbol = symbol + 1
					elif charSym == '&':
						symbol = symbol + 1
					elif charSym == '*':
						symbol = symbol + 1
					elif charSym == '(':
						symbol = symbol + 1
					elif charSym == ')':
						symbol = symbol + 1
					elif charSym == '_':
						symbol = symbol + 1
					elif charSym == '+':
						symbol = symbol + 1
					elif charSym == '-':
						symbol = symbol + 1
					elif charSym == '=':
						symbol = symbol + 1
					else:
						symbol = symbol + 0

				if symbol > 0:
					# lowercase checker that works just like uppercase one
					lower = 0 # if even one letter is lowercase, will be greater than 0
					for charLower in inPwd:
					# if char is lowercase, will increment lower by 1
					# if not, will just add 0
						lower = lower + charLower.islower()
					# check if lower is greater than 0 (found lowercase)
					if lower > 0:
						return True

					else:
						return False

				else:
					return False

			else:
				return False

		else:
			return False

	else:
		return False