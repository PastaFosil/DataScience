import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

from sklearn.datasets import load_diabetes

diabetes = load_diabetes()

df = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)

df_target = pd.DataFrame(data=diabetes.target, columns=["target"])

#MODELO SIMPLE
X = df[["bmi"]]
Y = df_target

X_train,X_test,y_train,y_test = train_test_split(X,Y, test_size=0.2,random_state=0)

modelo_regresionSimple = LinearRegression()
modelo_regresionSimple.fit(X_train,y_train)
y_pred = modelo_regresionSimple.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test,y_pred)
print("MSE: {:.2f}".format(mse))
print("r2: {:.2f}".format(r2))

print("Pendiente: ", modelo_regresionSimple.coef_)
print("Intercepto: ", modelo_regresionSimple.intercept_)

m = modelo_regresionSimple.coef_
b = modelo_regresionSimple.intercept_
z = np.linspace(X.min(), X.max(), 100)

fig, a = plt.subplots(figsize=(6,6))
a.plot(X.values, Y.values, "ob", alpha=.3)
a.plot(z,m*z+b, ls="--",color="orange",lw=2)
plt.plot(X_test.values, y_pred, "^", color="orange",ms=8)
a.set_xlabel("BMI")
a.set_ylabel("Disease progression")
plt.show()

#MODELO CON MULTIPLES VARIABLES
X = df[["bmi","bp"]]
Y = df_target

X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.2, random_state=0)
modelo_regresionMultiple = LinearRegression()
modelo_regresionMultiple.fit(X_train,y_train)
y_pred = modelo_regresionMultiple.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test,y_pred)
print("MSE: {:.2f}".format(mse))
print("r2: {:.2f}".format(r2))

fig, a = plt.subplots(figsize=(6,6))
a = plt.axes(projection="3d")
a.scatter(X_test["bmi"].values, X_test["bp"].values,Y)
plt.show()


#MODELO POLINOMIAL
X = df[["bmi"]]
Y = df_target

X_train,X_test,y_train,y_test = train_test_split(X,Y, test_size=0.2,random_state=0)
modelo_regresionPolinomial = np.polyfit(np.reshape(X_train.values,len(X_train.values)), np.reshape(y_train.values,len(y_train.values)), 2)

modelo_regresionPolinomial.fit(X_train,y_train)
y_pred = modelo_regresionPolinomial.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test,y_pred)
print("MSE: {:.2f}".format(mse))
print("r2: {:.2f}".format(r2))

print("Pendientes: ", modelo_regresionPolinomial.named_steps.linearregression.coef_)
#print("Interceptos: ", modelo_regresionPolinomial.intercept_)

m = modelo_regresionSimple.coef_
b = modelo_regresionSimple.intercept_
z = np.linspace(X.min(), X.max(), 100)

fig, a = plt.subplots(figsize=(6,6))
a.plot(X.values, Y.values, "ob", alpha=.3)
a.plot(z,m*z+b, ls="--",color="orange",lw=2)
plt.plot(X_test.values, y_pred, "^", color="orange",ms=8)
a.set_xlabel("BMI")
a.set_ylabel("Disease progression")
plt.show()