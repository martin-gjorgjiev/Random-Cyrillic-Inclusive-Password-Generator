import rcipg

#generate a password with upper, special and cyrillic characters
password=rcipg.generate(8,True,True,True)

#print the password to command line and save it to a file
print(password)
f = open("password.txt", "w", encoding="utf-8")
f.write(password+'\n')