import re 

f = open('dna.txt')
dna = f.read()
startPos = []

#ANT/AAT (N represents any base)
# Abc1 = re.findall(r"^A.T", dna)

#for loop
#finditer returns an iterator

for match in re.finditer(r"A.TAAT", dna):
    length = match.start() + 3
    startPos.append(length)
    #startPos.append(len(match))

#GCRW/TG (R means A or G and W means A or T)
for match in re.finditer(r"GC[AG][AT]TG", dna):
    length = match.start() + 4
    startPos.append(length)
    
startPos.append(0)
startPos.append(len(dna))

startPos.sort()
    
print startPos
#[0, 488, 1143, 1577, 1628, 2012]

count = 0
for num in startPos:
    # print num
    # print "count = %i, count + 1 = %i" % (startPos[count], startPos[count+1] ) 
    #print "%i - %i" % (startPos[count+1], startPos[count])
    length = startPos[count + 1] - startPos[count]
    print "one fragment size is %i" % length
    if count != (len(startPos) - 2):
        count = count + 1


#subtract the numbers using a for loop