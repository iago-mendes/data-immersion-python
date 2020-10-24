import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main
import seaborn as sns
import matplotlib.pyplot as plt

incomes = main.data['Q006'].unique()
incomes.sort()

fig, ax = plt.subplots()

plt.figure(figsize = (20,5))
sns.countplot(data = main.data, x = 'Q006', order = incomes, hue = 'IN_TREINEIRO', ax = ax)
plt.title('Trainers proportion by income')

fileName = __file__.split('/')[-1]
fig.savefig(f'{fileName}.png')