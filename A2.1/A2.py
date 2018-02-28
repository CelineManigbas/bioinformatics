#uses the bioinformatics module to figure out the percent of
#protein of the given sequences and amino acids

import bioinformatics

dnaSeq = "msrslllrfllfllllpplp"
print "%.f %% of %s is %s" % (bioinformatics.pctOfProtein("msrslllrfllfllllpplp", ["L"]), dnaSeq, 'l') 
    # should return 50
print "%.f %% of %s is %s" %(bioinformatics.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ["M"]), dnaSeq, 'm') 
    # should return 5
print "%.f %% of %s is %s" % (bioinformatics.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']), dnaSeq, "m or l") 
    # should return 55
print "%.f %% of %s is %s" % (bioinformatics.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['F', 's', 'L']), dnaSeq, "f, s, or l") 
    # should return 70



