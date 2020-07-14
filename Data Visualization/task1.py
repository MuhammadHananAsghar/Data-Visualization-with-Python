import pandas as pd
import matplotlib.pyplot as plt

# Creating DataFrame
df = pd.read_json(r'./rain.json')
print(df.head())
print("DF Statistics : ",df.describe())
df.plot(x='Month',y='Temperature')
df.plot(x='Month',y='Rainfall')
plt.show()