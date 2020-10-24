import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

tests = ['NU_NOTA_LC', 'NU_NOTA_CH', 'NU_NOTA_CN', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
main.data['NU_NOTA_TOTAL'] = main.data[tests].sum(axis=1)

plt.figure(figsize = (10,5))
sns.boxplot(x = 'Q025', y = 'NU_NOTA_TOTAL', data = main.data, order = ['A', 'B'], ax = ax)
plt.title('Grade comparison between people with and without access to the internet')
plt.xlabel('A: Without access   |   B: With access')

fileName = __file__.split('/')[-1]
fig.savefig(f'{fileName}.png')