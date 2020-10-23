import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax1 = main.data.boxplot(by = 'TP_LINGUA', column = 'NU_NOTA_LC', ax = ax)

plt.title('Comparison of languages')
plt.suptitle('')
ax1.set_xlabel('0: English   |   1: Spanish')

fileName = __file__.split('/')[-1]
fig.savefig(f'{fileName}.png')