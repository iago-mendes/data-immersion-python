import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main

states13 = main.data.query('NU_IDADE == 13')['SG_UF_RESIDENCIA']
for state in states13.values:
    print(state)