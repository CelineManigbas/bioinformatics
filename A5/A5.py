import bioinformatics

# input sequence is easy
print bioinformatics.translate_dna("ATGTTCGGT") #works ? 
print bioinformatics.translate_dna("ACAACCAGT") 
print bioinformatics.translate_dna("GACTCCTTTGAGGGA") # should be returning DTSFEG, missing t