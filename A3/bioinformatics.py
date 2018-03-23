# returns the atContent of a sequence
def atContent(dna):
    dna = dna.upper()
    at = (dna.count("A") + dna.count("T"))/float(len(dna))
    return at 

#returns the exon when given the start and stop
def extractExon(dna, start, stop):
    exon = dna[start-1:stop]
    return exon

# returns the percent of the protein that one 
# or more amino acids make up
def pctOfProtein(protein, codes):
    protein = protein.lower()
    count = 0
    for code in codes:
        code = code.lower()
        count = protein.count(code) + count
    # print "%i / %i " % (count, len(protein))
    percent = (count/float(len(protein))) * 100
    return percent