# open the genomic dna file and read the contents
genomic_dna = open("genomic_dna.txt").read()
# open the exons locations file
exon_locations = open("exons.txt")
# create a variable to hold the coding sequence
coding_sequence = ""
# go through each line in the exon locations file
for line in exon_locations:
    # get the start and stop positions
    start = int(line[0:line.find(',')])
    stop = int(line[line.find(',')+1:])
    # spliting the line using a comma also works!# 
    positions = line.split(',')# 
    start = int(positions[0])# 
    stop = int(positions[1])
    # extract the exon from the genomic dna
    exon = genomic_dna[start:stop]
    # append the exon to the end of the current coding sequence
    coding_sequence = coding_sequence + exon
# write the coding sequence to an output file
output = open("coding_sequence.txt", "w")
output.write(coding_sequence)
output.close()

# f1 = open('genomic_dna.txt')
# f2 = open('exons.txt')
# sspairs = []

# dna = f1.read()
# exons = f2.readlines()

# for line in exons :
#     line.rstip('\n')

# print exons



   

