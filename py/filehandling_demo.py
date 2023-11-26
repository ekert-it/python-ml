'''File handling demo'''
import os
import pandas as pd

# We are here:
path=os.path.dirname(os.path.abspath(__file__))
print ('We are here: ' + path)

# Our file:
filename=path+'/../data/atlantis.csv'

# Open CSV as file:
with open(filename, 'r', encoding='UTF-8') as f:
    print ('\n\nFile access mode is: ', f.mode)
    print ('File name is:        ', f.name)
    print ('\n')
    # print (f.read())

# Open CSV as Pandas DataFrame
with open(filename, 'r', encoding='UTF-8') as f:
    df=pd.read_csv(f)

print ("------------------------------------------------------------")
print ("df.head(5)")
print ("------------------------------------------------------------")
print(df.head(5))
print ("------------------------------------------------------------")
print("df.info()")
print ("------------------------------------------------------------")
print(df.info())
print ("------------------------------------------------------------")
print("df.max()")
print ("------------------------------------------------------------")
print(df.max())
