# Celine Manigbas
# Assignment: Prog A1

# returns the AT content by counting the amount of times
# A and T are in the DNA, and divides the sum by the
# length of the DNA stranf
print "Part 1"
dna1 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
at = (dna1.count("A") + dna1.count("T"))/float(len(dna1))
print "The AT content of %s is %.3f" % (dna1, at)

print 

# returns the size of the 2 fragments of the DNA where 
# the recognition site is by finding the recognition site
print "Part 2"
dna2 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
loc = dna2.find("AATTC")
print loc
frag1 = len(dna1[0:loc])
frag2 = len(dna1[loc-1:len(dna1)])
print "the size of two fragments produced when the following DNA sequence"
print dna2
print "is digested with EcoRI are " + str(frag1) + " and " + str(frag2)
print

# returns the complement of the DNA strand
print "Part 3"
dna2 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
#       TGACTAGCTAATGCATATCATAAACGATAGTATGUATAUATAGCTASGCAAGTA"
dna2 = dna2.lower()
complement = dna2.replace('a','T').replace('g', 'C').replace('t', 'A').replace('c', 'G')
print "the following DNA strand and its complement"
print dna2.upper()
print complement

print

# prints the coding bases in upper case and noncoding bases
# in lowercase based on given locations by replacing nucleotide
# with the complement
print "Part 4"
print "In the following DNA strand, the coding bases (exons) are in uppercase and noncoding are lowercase:"
#coding = exons
dna3 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
# up to and not including
print dna3
dnaUL = dna3[0:63] + dna3[63:91].lower() + dna3[91:len(dna3)]
print dnaUL