import string
import secrets

def rollagain(n,list1):
    x=secrets.randbelow(n)
    if x in list1:
        x=rollagain(n,list1)
    return x

def generate(strSize, uppercaseChar, specialChar, cyrillicChar):
    #initialise characters
    lowerAscii=string.ascii_lowercase
    numeric=string.digits
    punctuation=string.punctuation
    cyrillic=['љњертѕуиопшѓасдфгхјклчќжзџцвбнм']
    password=''
    listType=[]
    
    if specialChar:
        listType.append(2)

    if specialChar:
        listType.append(3)

    #check of parameters
    #strSize must be number
    if type(strSize)!='int' and strSize<0:
        return 'strSize is not a number or smaller than 0'

    #upperChar, specialChar, cyrillicChar must be bool
    if type(uppercaseChar)!='bool' or type(specialChar)!='bool' or type(cyrillicChar)!='bool':
        return 'upperChar, specialChar or cyrillicChar is not a bool'

    #for the number of characters in string, how long is the password
    for i in range (0,strSize):
        x=rollagain(4,listType)
        if x==0:
            char = secrets.choice(lowerAscii)
            if uppercaseChar and secrets.randbelow(2):
                char= char.upper()
            password += str(char) #here
        elif x==1:
            pass
        elif x==2:
            pass
        elif x==3:
            pass
        
