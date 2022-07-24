#Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

asciidict = dict()

for l in range(97,123):
   asciidict[chr(l)]= l
print(asciidict)