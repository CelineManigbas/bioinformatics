seqName1 = "ABC123"
seq1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seqName2 = "DEF456"
seq2 = "ACTGATCGACGATCGATCGATCACGACT"
seqName3 = "HIJ789"
seq3 = "ACTGACACTGTACTGTACATGTG"

file = open('output.txt', 'w')
file.write(">" + seqName1 + "\n")
file.write(seq1 + "\n")
file.write(">" + seqName2 + "\n")
file.write(seq2 + "\n")
file.write(">" + seqName2 + "\n")
file.write(seq2 + "\n")

file.close()
