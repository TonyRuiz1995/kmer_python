import random
import sys

dna = []

####generate a random sequence
for i in range(int(sys.argv[1])):
    dna.append(random.choice("ACTG"))
    
f = open("sequence.txt", "w")
f.write(''.join(dna))
f.close()
