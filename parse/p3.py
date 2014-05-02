#import sys

#kural = sys.argv[1]
input = open('2.txt', "rt", encoding="utf-8").read()
#print infile
#chunk = input.read(4096)

#print( chunk)
#print infile.split('.')[0]

kural = input.split('.')[0].split()
number = kural[-8]
print(number)

kural_text = kural[-7] + " " + kural[-6] + " " + kural[-5] + " " + kural[-4] + "\n" + kural[-3] + " " + kural[-2] + " " + kural[-1]

print(kural_text) 
