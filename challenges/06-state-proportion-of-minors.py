import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

states = main.data.query('NU_IDADE < 18')['SG_UF_RESIDENCIA'].value_counts(normalize = True)
states.plot.bar(figsize = (20, 5), ax = ax).set_title('State proportion of minors')

fileName = __file__.split('/')[-1]
fig.savefig(f'{fileName}.png')