import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ages = main.data['NU_IDADE']
graph = ages.hist(bins = 50, figsize = (20, 5), ax = ax).set_title('Age distribution')

fileName = __file__.split('/')[-1]
fig.savefig(f'{fileName}.png')