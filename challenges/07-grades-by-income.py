import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main
import seaborn as sns
import matplotlib.pyplot as plt

incomes = main.data['Q006'].unique()
incomes.sort()

def createPlot(grades, ax):
  plt.figure(figsize = (20,5))
  sns.boxplot(x = 'Q006', y = grades, data = main.data, order = incomes, ax = ax)
  plt.title('Grades by income')
  return plt.show()

fileName = __file__.split('/')[-1]

fig1, ax1 = plt.subplots()
createPlot('NU_NOTA_MT', ax1)
fig1.savefig(f'{fileName}-1.png')

tests = ['NU_NOTA_LC', 'NU_NOTA_CH', 'NU_NOTA_CN', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
main.data['NU_NOTA_TOTAL'] = main.data[tests].sum(axis=1)

fig2, ax2 = plt.subplots()
createPlot('NU_NOTA_TOTAL', ax2)
fig2.savefig(f'{fileName}-2.png')