import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main
import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots()
trainers = main.data.query('IN_TREINEIRO == 1')['NU_IDADE']
trainers.hist(bins = 50, figsize = (20, 5), ax = ax1).set_title('Tainers age distribution')

fig2, ax2 = plt.subplots()
notTrainers = main.data.query('IN_TREINEIRO == 0')['NU_IDADE']
notTrainers.hist(bins = 50, figsize = (20, 5), ax = ax2).set_title('Not trainers age distribution')

fileName = __file__.split('/')[-1]
fig1.savefig(f'{fileName}-1.png')
fig2.savefig(f'{fileName}-2.png')