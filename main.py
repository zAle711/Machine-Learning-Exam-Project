import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.expand_frame_repr', True)

df = pd.read_csv('dataset/water_potability.csv')

print( "Colonne: ", list(df.columns), "\nSize: ", df.size)
def pot(col):
    c = col[8]
    return 'Yes' if c == 1 else 'No'

print(df['Potability'].replace(1, 'Yes'))
print(df['Potability'].replace(0, 'No'))


sns.boxplot(df, x='ph', y='Potability')
plt.tight_layout()
plt.show()