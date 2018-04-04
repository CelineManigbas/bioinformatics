################################
# import the module
################################
import re

################################
# alternation
################################
dna = "ATCGGACCGAATTCAC"
if re.search(r"GG(A|T)CC", dna): # A or T
    print "A) pattern found!"

################################
# character groups
################################
dna = "ATCGCTGCGAATTCAC"
if re.search(r"GC[ATGC]GC", dna): # A or T or G or C
    print "B) pattern found!"

################################
# quantifiers
################################
dna = "ATCGCTGCGATTCAC"
if re.search(r"GAA?TT", dna): # the second A must appear zero or one time
    print "C) pattern found!"

dna = "ATCGCTGGGTAACAC"
if re.search(r"T(GGG)?T", dna): # GGG must appear zero or one time
    print "D) pattern found!"

dna = "ATCGCTGCGATTCAC"
if re.search(r"GAA+TT", dna): # the second A must appear one or more times
    print "E) pattern found!"

dna = "ATCGCTGGGTAACAC"
if re.search(r"T(GGG)+T", dna): # GGG must appear one or more times
    print "F) pattern found!"

dna = "ATCGCTGCGATTCAC"
if re.search(r"GAA*TT", dna): # the second A must appear zero or more times
    print "G) pattern found!"

dna = "ATCGCTGGGTAACAC"
if re.search(r"T(GGG)*T", dna): # GGG must appear zero or more times
    print "H) pattern found!"

dna = "ATCGCTGCGAAAAAATTCAC"
if re.search(r"GAA{5}TT", dna): # the second A must appear exactly 5 times
    print "I) pattern found!"

dna = "ATCGCTGGGGGGGGGGGGGGGTAACAC"
if re.search(r"T(GGG){5}T", dna): # GGG must appear exactly 5 times
    print "J) pattern found!"

dna = "ATCGCTGCGAAAATTCAC"
if re.search(r"GAA{2,5}TT", dna): # the second A must appear between 2 and 5 times (inclusive)
    print "K) pattern found!"

dna = "ATCGCTGGGGGGTAACAC"
if re.search(r"T(GGG){2,5}T", dna): # GGG must appear between 2 and 5 times (inclusive)
    print "L) pattern found!"

dna = "ATCGCTGCGAAATTCAC"
if re.search(r"GAA{2,}TT", dna): # the second A must appear 2 or more times
    print "M) pattern found!"

dna = "ATCGCTGGGGGGTAACAC"
if re.search(r"T(GGG){2,}T", dna): # GGG must appear 2 or more times
    print "N) pattern found!"

dna = "ATCGCTGCGATTCAC"
if re.search(r"GAA{,5}TT", dna): # the second A must appear up to 5 times
    print "O) pattern found!"

dna = "ATCGCTGGGTAACAC"
if re.search(r"T(GGG){,5}T", dna): # GGG must appear up to 5 times
    print "P) pattern found!"

################################
# positions
################################
dna = "ATCGCTGGGTAACAC"
if re.search(r"^ATC", dna): # must start with ATC
    print "Q) pattern found!"
    print re.findall(r"^ATC", dna)

dna = "ATCGCTGGGTAACAC"
if re.search(r"CAC$", dna): # must end with CAC
    print "R) pattern found!"

################################
# any character
################################
dna = "ATCGCTGGGTAACAC"
if re.search(r"A.C", dna): # A followed by any character folowed by C
    print "S) pattern found!"

################################
# match if there is not a match
################################
dna = "ATCGCTGGGAGGCAC"
if re.search(r"A[^ATC]G", dna): # A be something other than A, T, or C
    print "T) pattern found!"
    
################################
# complex expressions
################################
dna = "AUGAAAAAUUUUUGGGGGAAAAAUUUUUAAAAUAAAAA"
if re.search(r"^AUG[AUGC] {30,1000}A{5,10}$", dna):
    print "U) pattern found!"
    print re.findall(r"^AUG[AUGC]{30,1000}A{5,10}$", dna)
    
################################
# what matched
################################
dna = "GGGGGATATGAGGGGGG"
matches = re.findall(r"A.ATGAG", dna)
print matches

dna = "GGGGGATATGAGGGGGG"
matches = re.findall(r"(A.A)T(G[ATC])G", dna)
# print "look"
# print matches

################################
# splitting a string with regex
################################
dna = "GGG-GATCTA-GTT-AGG"
tokens = re.split(r"[^ACGT]", dna)
print tokens