import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


df = pd.read_csv('/home/tony/WMU/kmer/dat.txt',
                 delim_whitespace=True)




df.columns = ["Sequence_Size","k3", "k4", "k6", "k8", "k10"]

print(df)


df = df.melt('Sequence_Size', var_name='k_size',  value_name='time_elapsed')


print(df)



g = sns.factorplot(x="Sequence_Size", y="time_elapsed", hue='k_size', data=df)
plt.show()

'''
Results:
Changing the length of K has no
impact on run time of algorithm

'''
'''
df["X"] = seq
df["Y"] = times

ax = sns.regplot(x="X", y= "Y", data = df)
plt.show()

'''
