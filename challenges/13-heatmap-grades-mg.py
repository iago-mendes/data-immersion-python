import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tests = ['NU_NOTA_LC', 'NU_NOTA_CH', 'NU_NOTA_CN', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
main.data['NU_NOTA_TOTAL'] = main.data[tests].sum(axis=1)

data_no0 = main.data.query('NU_NOTA_TOTAL != 0')

correlation = data_no0.query('SG_UF_RESIDENCIA ==  "MG"')[tests].corr()

fig, ax = plt.subplots(figsize=(15, 5))

mask = np.triu(np.ones_like(correlation, dtype=bool))
sns.heatmap(correlation, cmap='Blues', center=0, annot=True, ax=ax, mask=mask)
ax.set_title('Correlation between grades in MG')

fileName = __file__.split('/')[-1]
fig.savefig(f'{fileName}.png')