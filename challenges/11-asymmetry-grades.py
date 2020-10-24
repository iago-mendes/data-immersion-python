import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main
import seaborn as sns
import matplotlib.pyplot as plt

tests = ['NU_NOTA_LC', 'NU_NOTA_CH', 'NU_NOTA_CN', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
main.data['NU_NOTA_TOTAL'] = main.data[tests].sum(axis=1)

data_no0 = main.data.query('NU_NOTA_TOTAL != 0')

fig, (ax1, ax2) = plt.subplots(2, figsize=(20,5))

# NU_NOTA_LC

mean1 = data_no0.query('NU_NOTA_LC != 0')['NU_NOTA_LC'].mean()
median1 = data_no0.query('NU_NOTA_LC != 0')['NU_NOTA_LC'].median()
mode1 = data_no0.query('NU_NOTA_LC != 0')['NU_NOTA_LC'].mode()[0]

ax1.axvline(mean1, color='r', linestyle='-')
ax1.axvline(median1, color='g', linestyle='-')
ax1.axvline(mode1, color='b', linestyle='-')
ax1.legend({'Mean':mean1,'Median':median1,'Mode':mode1})
ax1.text(700, 1500, 'Asymmetry in the left', fontsize = 15)

sns.histplot(data_no0.query('NU_NOTA_LC != 0'), x = 'NU_NOTA_LC', ax = ax1)

# NU_NOTA_MT

mean2 = data_no0.query('NU_NOTA_MT != 0')['NU_NOTA_MT'].mean()
median2 = data_no0.query('NU_NOTA_MT != 0')['NU_NOTA_MT'].median()
mode2 = data_no0.query('NU_NOTA_MT != 0')['NU_NOTA_MT'].mode()[0]

ax2.axvline(mean2, color='r', linestyle='-')
ax2.axvline(median2, color='g', linestyle='-')
ax2.axvline(mode2, color='b', linestyle='-')
ax2.legend({'Mean':mean2,'Median':median2,'Mode':mode2})
ax2.text(850, 1750, 'Asymmetry in the right', fontsize = 15)

sns.histplot(data_no0.query('NU_NOTA_MT != 0'), x = 'NU_NOTA_MT', ax = ax2)

fileName = __file__.split('/')[-1]
fig.savefig(f'{fileName}.png')