# coding: utf-8

# In[1]:
import random
import time
#import matplotlib.pyplot as plt
#import seaborn as sns
#import pandas as pd
import sys

# CREATE KMERS
def create_kmers(string, k):
    kmers = []
    n = len(string)
    for i in range(0, n - k + 1):
        kmers.append(string[i:i + k])
    return kmers


##MAPPER FUNCTION
def mapper(kmers):
    # returns dictionary kmers with counts
    x = {}
    for k in kmers:
        # print ('%s\t%s' % (k, 1))
        string = "".join(k)
        x[string] = x.get(string, 0) + 1
    return x


f = open("sequence.txt","r")
string = f.read()
kmers = create_kmers(string, int(sys.argv[1]))

print(mapper(kmers))
