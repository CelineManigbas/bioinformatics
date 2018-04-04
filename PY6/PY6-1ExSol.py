import re

def check(l, exp):
    for acc in l:
        if re.search(exp, acc):
            print acc
    


accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

print "accession name contains the number 5:"
check(accessions, r"5")

print "accession name contains d or e:"
check(accessions, r"[d|e]")

print "accession name contains de:"
check(accessions, r"de")

print "accession name contains d followed by any character followed by e:"
check(accessions, r"d.e")

print "accession name contains d followed by any character followed by e:"
check(accessions, r"d.e")

print "accession name contains de or ed:"
check(accessions, r"de|ed")

print "accession name starts with x or y:"
check(accessions, r"^(x|^y)")

print "accession name starts with x or y and ends with e:"
check(accessions, r"^(x|y).*e$")

print "accession name contains three or more digits in a row:"
check(accessions, r".*[0123456789]{3,}.*")

print "accession name ends with d followed by either a, r, or p"
check(accessions, r"d[arp]$")
