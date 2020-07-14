import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create DatFrame
data = pd.read_csv(r'tempYearly.csv')

sns.jointplot("Rainfall","Temperature",data = data,kind="reg")
plt.show()