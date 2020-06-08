###############################################################################
# Clinton Hawkes, Alessio Peterson, and Vincent Yasi
# Group Project
###############################################################################
# These are the three functions for Part 2 of the Group Project.
#
# The first function converts a string to a base-10 number.
#
# The second function converts seconds to a date.
#
# The third function converts an integer into hex, with a certain endian form.
#
# This file was created under a Continous Integration workflow by the three
# of us on GitHub (https://github.com/clinthawkes/cs362_group_5)
###############################################################################


# Function 1 -String to Base-10-
def conv_num(num_str):
    return True


###############################################################################
# Subfunction to Find Years from Seconds
# Takes in seconds and returns the year and remaining seconds
def find_year(inSecs):
    year = 1970

    # While there is at least one year's worth of seconds left,
    # increment year, figure out if leap year,
    # and subtract appropriate amount of seconds
    # (# secs in a normal year: 31536000)
    # (# secs in a leap year: 31622400)
    while inSecs >= 31536000:
        year = year + 1

        if year % 4 != 0:
            inSecs = inSecs - 31536000

        elif year % 100 != 0:
            inSecs = inSecs - 31622400

        elif year % 400 != 0:
            inSecs = inSecs - 31536000

        else:
            inSecs = inSecs - 31622400

    # return year and remainings seconds
    return (year, inSecs)


# Subfunctions to Find Month from Seconds
# Takes in seconds and year and subtracts seconds until find month
# Unfortunately, no real pattern to month length,
# so need to check and subtract each one by one
# Broken into two parts as flake8 claimed too complex
def check_month(inSecs, inMonth):
    if inSecs <= inMonth:
        return True
    else:
        return False


def find_month(inSecs, year):
    # number of seconds in each month based on length
    month30 = 2592000
    month31 = 2678400
    month28 = 2419200
    month29 = 2505600

    # hold number of month
    month = 0

    # array with order of month lengths
    # two arrays for leap vs regular
    reg_lengths = [month31, month28, month31, month30, month31, month30,
                   month31, month31, month30, month31, month30, month31]
    leap_lengths = [month31, month29, month31, month30, month31, month30,
                    month31, month31, month30, month31, month30, month31]

    # loop regulating variable
    found = False

    # array iterator
    i = 0

    # leap variable
    leap = False

    # determine if year is leap year
    if year % 4 != 0:
        leap = False

    elif year % 100 != 0:
        leap = True

    elif year % 400 != 0:
        leap = False

    else:
        leap = True

    # check each month to see if it is the one (two versions based on leap)
    # if so, mark month
    # if not, subtract that month's seconds and move to next
    if leap is True:
        while found is False:
            found = check_month(inSecs, leap_lengths[i])
            if found is True:
                month = i + 1
                inSecs = inSecs + 86400
            else:
                inSecs = inSecs - leap_lengths[i]
                i = i + 1

    elif leap is False:
        while found is False:
            found = check_month(inSecs, reg_lengths[i])
            if found is True:
                month = i + 1
            else:
                inSecs = inSecs - reg_lengths[i]
                i = i + 1

    return (month, inSecs)


# Function 2 -Seconds to Date-
# Uses two subfunctions to take the seconds since Epoch
# and converts it into MM-DD-YYYY format of date
def my_datetime(num_sec):
    ###########################
    # Get The Year of The Date
    ###########################

    year, secs = find_year(num_sec)

    ########################
    # Get Month of The Date
    ########################

    month, secs = find_month(secs, year)

    if month < 10:
        month = '0' + str(month)

    else:
        month = str(month)

    ######################
    # Get Day of The Date
    ######################

    # As we have stripped away year and month seconds,
    # we just need to subtract days until we have less than one day left
    # (86400 seconds in a day)

    day = 1

    while secs > 86400:
        secs = secs - 86400
        day = day + 1

    # save as string
    # see if '0' needs to be added to front
    if day < 10:
        day = '0' + str(day)

    else:
        day = str(day)

    ###################################
    # Build Date String and Return It
    ###################################
    date = month + "-" + day + "-" + str(year)

    return date
###############################################################################


# Function 3 -Integer to Hexadecimal-
def conv_endian(num, endian):
    return True
