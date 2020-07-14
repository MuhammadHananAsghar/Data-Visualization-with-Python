import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read DataFrame
data = pd.read_csv(r'birthYearly.csv')


dataP = data.pivot("month","year","births")

sns.heatmap(dataP,annot=True,fmt='d')
plt.show()