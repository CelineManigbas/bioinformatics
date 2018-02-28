import bioinformatics

print bioinformatics.pctOfProtein("msrslllrfllfllllpplp", ["L"]) # should return 50
print bioinformatics.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ["M"]) # should return 5
print bioinformatics.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) # should return 55
print bioinformatics.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['F', 's', 'L']) # should return 70



