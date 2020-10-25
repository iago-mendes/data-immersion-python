import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tests = ['NU_NOTA_LC', 'NU_NOTA_CH', 'NU_NOTA_CN', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
main.data['NU_NOTA_TOTAL'] = main.data[tests].sum(axis=1)

data_no0 = main.data.query('NU_NOTA_TOTAL != 0')

grades_in = ['NU_NOTA_CH','NU_NOTA_LC', 'NU_NOTA_CN','NU_NOTA_REDACAO']
grade_out = 'NU_NOTA_MT'

data_noNA = data_no0[tests].dropna()
x = data_noNA[grades_in]
y = data_noNA[grade_out]

def tree_regressor(depth, goal = 'get'):
    seed = 1232
    np.random.seed(seed)
    parts = KFold(n_splits = 10, shuffle=True)
    model_tree = DecisionTreeRegressor(max_depth=depth)
    validation = cross_validate(model_tree, x, y, cv= parts, scoring="neg_mean_squared_error", return_train_score=True)
    if goal == 'find':
        return (validation['test_score']*-1).std()
    elif goal == 'get':
        return validation

std_best = {'std': 1000, 'depth': 0}
for i in range(1,21):
    std = tree_regressor(i, goal='find')
    if std < std_best['std']:
        std_best['std'] = std
        std_best['depth'] = i

fig, ax = plt.subplots(figsize=(20,5))
results = tree_regressor(std_best['depth'])
sns.lineplot(results['test_score']*-1, ((results['train_score']*-1-results['test_score']*-1)**2)**(1/2), ax=ax)
ax.set_title('Tree regression score analysis')
ax.set_xlabel('Real score')
ax.set_ylabel('Absolute predicted difference')

fileName = __file__.split('/')[-1]
fig.savefig(f'{fileName}.png')