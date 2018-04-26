# returns the atContent of a sequence
def atContent(dna):
    at = (dna.count("a") + dna.count("t"))/float(len(dna))
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
    
def translate_dna(sequence):
    gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    count = 0; 
    aminoAcids = ""
    while count < len(sequence):  
        codon = sequence[count:count + 3] #up to and not including count + 3
        if codon in gencode:
            aminoAcids = aminoAcids + gencode[codon]
        count = count + 3
    return aminoAcids

    