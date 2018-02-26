print "How many malcorps found on Exflon?",
exNum = raw_input()
print "How many malcorps found on Moblies?",
mobNum = raw_input()
print "How many malcorps found on Monsantoes?",
monNum = raw_input()
total = int(exNum) + int(mobNum) + int(monNum)
print "The total number of Malcorps on all planets is %s" % total
print "The average number of malcorps is %s" % (total/3.0)