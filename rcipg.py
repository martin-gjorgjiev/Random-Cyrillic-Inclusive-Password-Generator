import string
import secrets

def rollAgain(n, list1):
    x=secrets.randbelow(n)
    if x in list1:
        x=rollAgain(n, list1)
    return x

def buildPassword(size, charSet):
    # for the number of characters in string, for how long is the password
    password = ''
    for i in range (0, size):
        password+=secrets.choice(charSet)

    return password

def checkSize(size):
    if type(size) != 'int' and size < 0:
        return 'strSize is not a number or smaller than 0'


def generate(strSize, uppercaseChar, specialChar, cyrillicChar):
    # initialise characters
    cyrillic=u'љњертѕуиопшѓасдфгхјклчќжзџцвбнмйьюяъщђћз́с́ёыэґіўїє'
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

    # strSize must be number an bigger than zero
    checkSize(strSize)

    # generate password
    return buildPassword(strSize, charSet) 
