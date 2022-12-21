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



# df['Potability'] = df['Potability'].apply(str)
#ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity,
# sns.boxplot(df, x='ph', y='Potability', ax=axs[0,0]).set(title='ph')
# sns.boxplot(df, x='Hardness', y='Potability', ax=axs[0,1]).set(title='Hardness')
# sns.boxplot(df, x='Solids', y='Potability', ax=axs[0,2]).set(title='Solids')
# sns.boxplot(df, x='Chloramines', y='Potability', ax=axs[1,0]).set(title='Chloramines')
# sns.boxplot(df, x='Sulfate', y='Potability', ax=axs[1,1]).set(title='Sulfate')
# sns.boxplot(df, x='Conductivity', y='Potability', ax=axs[1,2]).set(title='Conductivity')
# sns.boxplot(df, x='Organic_carbon', y='Potability', ax=axs[2,0]).set(title='Organic_carbon')
# sns.boxplot(df, x='Trihalomethanes', y='Potability', ax=axs[2,1]).set(title='Trihalomethanes')
# sns.boxplot(df, x='Turbidity', y='Potability', ax=axs[2,2]).set(title='Turbidity')

#sns.kdeplot(df, x='Trihalomethanes', hue='Potability', ax=axs[2,2], fill=True)

# fig, axs = plt.subplots(3,3, figsize=(12,8))

# sns.histplot(df, x='ph', hue='Potability', ax=axs[0,0], kde=True).set(title='ph')
# sns.histplot(df, x='Hardness', hue='Potability', ax=axs[0,1], kde=True).set(title='Hardness')
# sns.histplot(df, x='Solids', hue='Potability', ax=axs[0,2], kde=True).set(title='Solids')
# sns.histplot(df, x='Chloramines', hue='Potability', ax=axs[1,0], kde=True).set(title='Chloramines')
# sns.histplot(df, x='Sulfate', hue='Potability', ax=axs[1,1], kde=True).set(title='Sulfate')
# sns.histplot(df, x='Conductivity', hue='Potability', ax=axs[1,2], kde=True).set(title='Conductivity')
# sns.histplot(df, x='Organic_carbon', hue='Potability', ax=axs[2,0], kde=True).set(title='Organic_carbon')
# sns.histplot(df, x='Trihalomethanes', hue='Potability', ax=axs[2,1], kde=True).set(title='Trihalomethanes')
# sns.histplot(df, x='Turbidity', hue='Potability', ax=axs[2,2], kde=True).set(title='Turbidity')


# plt.tight_layout()
# plt.show()