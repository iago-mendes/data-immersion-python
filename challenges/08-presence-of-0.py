import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main

tests = ['NU_NOTA_LC', 'NU_NOTA_CH', 'NU_NOTA_CN', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
main.data['NU_NOTA_TOTAL'] = main.data[tests].sum(axis=1)

presences = ['TP_PRESENCA_LC', 'TP_PRESENCA_CH', 'TP_PRESENCA_CN', 'TP_PRESENCA_MT']
result = main.data.query('NU_NOTA_TOTAL == 0')[presences].value_counts()
print(result)