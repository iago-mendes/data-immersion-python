import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import main

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVR, SVR
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error, r2_score

tests = ['NU_NOTA_LC', 'NU_NOTA_CH', 'NU_NOTA_CN', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
main.data['NU_NOTA_TOTAL'] = main.data[tests].sum(axis=1)

data_no0 = main.data.query('NU_NOTA_TOTAL != 0')

grades_in = ['NU_NOTA_CH','NU_NOTA_LC', 'NU_NOTA_CN','NU_NOTA_REDACAO']
grade_out = 'NU_NOTA_MT'

data_noNA = data_no0[tests].dropna()
x = data_noNA[grades_in]
y = data_noNA[grade_out]

seed = 4321
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=seed)

model_linear = LinearSVR(random_state=seed)
model_linear.fit(x_train, y_train)
predictions_linear = model_linear.predict(x_test)

model_svr = SVR()
model_svr.fit(x_train, y_train)
predictions_svr = model_svr.predict(x_test)

model_dummy = DummyRegressor()
model_dummy.fit(x_train, y_train)
predictions_dummy = model_dummy.predict(x_test)

linear = mean_squared_error(y_test, predictions_linear)**(1/2)
svr = mean_squared_error(y_test, predictions_svr)**(1/2)
dummy = mean_squared_error(y_test, predictions_dummy)**(1/2)
print(f'-=- Mean error of models -=-\nlinear: {linear}, svr: {svr}, dummy: {dummy}')

linear = r2_score(y_test, predictions_linear)
svr = r2_score(y_test, predictions_svr)
dummy = r2_score(y_test, predictions_dummy)
print(f'-=- R2 of models -=-\nlinear: {linear}, svr: {svr}, dummy: {dummy}')