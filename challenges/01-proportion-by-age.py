import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main

total = len(main.data['NU_IDADE'])
ages = main.data['NU_IDADE'].value_counts()

for age, qtd in ages.items():
    ages[age] = float(qtd*100/total)

print(ages.sort_values(ascending=False))