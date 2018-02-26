def atContent(dna):
    at = (dna.count("A") + dna.count("T"))/float(len(dna))
    return at 
    
def extractExon(dna, start, stop):
    exon = dna[start-1:stop]
    return exon