print "Enter a sentence to be encrypted"
sentence = raw_input()
sentence = sentence.lower()
length = len(sentence)
encrypted = sentence.replace('a',  str(length)).replace('e',  str(length + 1)).replace('i',  str(length + 2)).replace('o',  str(length + 3)).replace('u',  str(length + 4))
print "The encryption is '%s'" % encrypted
decrypted = encrypted.replace(str(length), 'a').replace(str(length + 1), 'e').replace(str(length + 2), 'i').replace(str(length + 3), 'o').replace(str(length + 4), 'u')
print "the decrypted is '%s'" %decrypted