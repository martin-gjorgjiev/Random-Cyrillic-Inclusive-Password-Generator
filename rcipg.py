#import modules
import string
import secrets

# define cyrillic char set
cyrillic=u'љњертѕуиопшѓасдфгхјклчќжзџцвбнмйьюяъщђћз́с́ёыэґіўїє'

# old code from first idea
def rollAgain(n, list1):
    x=secrets.randbelow(n)
    if x in list1:
        x=rollAgain(n, list1)
    return x

# generate random string based on size and source of characters
def buildPassword(size, charSet):
    password = ''
    for i in range (0, size):
        password+=secrets.choice(charSet)
    return password

# check if the size input is within specifications
def checkSize(size):
    if type(size) is not int or size < 1:
        raise ValueError('strSize is not a number or smaller than 0')
    return True

# check if there is a numeric character in the string
def checkNumeric(text):
    for c in text:
        if c.isnumeric():
            return True
    return False

# check if there is a character with uppercase
def checkUpper(text):
    if text == text.lower():
        return False
    return True

# check if there is a special character in the string
def checkSpecial(text):
    for c in text:
        if c in string.punctuation:
            return True
    return False

# check if there is a cyrillic character in the string
def checkCyrillic(text):
    for c in text:
        if c in cyrillic:
            return True
    return False

#main function for generating the password
def generate(strSize, uppercaseChar, specialChar, cyrillicChar):
    # initialise the set of characters
    charSet = string.ascii_lowercase
    if type(uppercaseChar) != 'bool' and uppercaseChar:
        charSet += string.ascii_uppercase
    charSet += string.digits
    if type(specialChar) != 'bool' and specialChar:
        charSet += string.punctuation
    if type(cyrillicChar) != 'bool' and cyrillicChar:
        charSet += cyrillic
        if type(uppercaseChar) != 'bool' and uppercaseChar:
            charSet += cyrillic.upper()

    # strSize must be whole number an bigger than zero
    checkSize(strSize)

    # generate password
    password = ''
    # generate passwords until criteria is met
    while True:
        check1 = False
        password = buildPassword(strSize, charSet)
        # must have at least one numeric value, at least one special character and at least one cyrillic character
        check1 = checkNumeric(password)
        if(uppercaseChar):
            check1 = check1 and checkUpper(password)
        if(specialChar):
            check1 = check1 and checkSpecial(password)
        if(cyrillicChar):
            check1 = check1 and checkCyrillic(password)
        # break the loop once criteria is met
        if(check1):
            break
        
    return password
