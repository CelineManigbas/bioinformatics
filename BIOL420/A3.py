import BIOL420

def high(sequence) : 
    if BIOL420.atContent(words[1]) > 0.65 :
        return True
    else :
        return False
def medium(sequence) : 
    if BIOL420.atContent(words[1]) >= 0.45 :
        return True
    else :
        return False    

def low(sequence) : 
    if BIOL420.atContent(words[1]) < 0.45 :
        return True
    else :
        return False

file = open('data.csv', 'r')
sequences = []
for line in file :
    words = line.split(",")
    print words[0] + " ",
    print BIOL420.atContent(words[1]),
    if high(words[1]) :
        print "has a high AT Content"
    elif medium(words[1]) :
        print "has a medium AT Content"
    elif low(words[1]) :
        print "has a low AT Content"
    #BIOL420.atContent(words[1])
    

  