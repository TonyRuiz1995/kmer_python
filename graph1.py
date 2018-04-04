import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#using hadoop mapreduce
df = pd.read_csv('/home/tony/WMU/kmer_python/hadoop_data.txt')
print(df)

df1 = pd.DataFrame()
#df1.columns = ["Sequence_Size","k3", "k4", "k6", "k8", "k10"]
df1["Sequence_Size"] = [10000, 100000,1000000, 10000000]
#s = pd.Series
#s = df[4:8].values
#print(s)
#print(df.iloc[:4])

df1["k2"] = df[:4]
df1["k3"] = df[4:8].values
df1["k4"] = df[8:12].values
df1["k6"] = df[12:16].values
df1["k8"] = df[16:20].values
df1["k10"] = df[20:24].values


print(df1)

##using regular python

df1 = df1.melt('Sequence_Size', var_name='k_size',  value_name='time_elapsed')
print(df1)
g = sns.factorplot(x="Sequence_Size", y="time_elapsed", hue='k_size', data=df1)
plt.show()

df = pd.read_csv('/home/tony/WMU/kmer_python/kmer_data.txt')
print(df)

df1 = pd.DataFrame()
#df1.columns = ["Sequence_Size","k3", "k4", "k6", "k8", "k10"]
df1["Sequence_Size"] = [10000, 100000,1000000, 10000000]
#s = pd.Series
#s = df[4:8].values
#print(s)
#print(df.iloc[:4])

df1["k2"] = df[:4]
df1["k3"] = df[4:8].values
df1["k4"] = df[8:12].values
df1["k6"] = df[12:16].values
df1["k8"] = df[16:20].values
df1["k10"] = df[20:24].values


print(df1)



df1 = df1.melt('Sequence_Size', var_name='k_size',  value_name='time_elapsed')
print(df1)
g = sns.factorplot(x="Sequence_Size", y="time_elapsed", hue='k_size', data=df1)
plt.show()

