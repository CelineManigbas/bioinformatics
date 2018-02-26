# open the three files...
f1 = open("file1.txt")
f2 = open("file2.txt")
f3 = open("file3.txt")
# read each file into the list...
dna = []
dna.append(f1.read().rstrip('\n'))
dna.append(f2.read().rstrip('\n'))
dna.append(f3.read().rstrip('\n'))
# sort the list and print...
dna.sort()
print(dna)