import re

sid = raw_input("Enter an MCLA studnet id:")
if (re.search(r"^[Aa][0123456789]{8}", sid)):
    print "That is a valid student id!"
else:
    print "That is a invalid student id!"
    
pn = raw_input("Enter phone number [nnn nnn-nnnn]:")
if (re.search(r"^[0123456789]{3} [0123456789]{3}-[0123456789]{4}$", pn)):
    print "That is a valid phone number!"
else:
    print "That is a invalid phone number!"

