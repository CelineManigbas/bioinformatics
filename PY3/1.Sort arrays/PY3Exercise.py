f1 = open('file1.txt')
seq1 = f1.read()
f2 = open('file2.txt')
seq2 = f2.read()
f3 = open('file3.txt')
seq3 = f3.read()

sequences = [seq1, seq2, seq3]
sequences = sorted(sequences, key = str.lower)
print sequences



