import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder


class SalaryPredict():

 def __init__(self, XPredict_salary):
        self.XPredict_salary = XPredict_salary

 def Predict(self):
  df = pd.read_csv('Wealth.csv', index_col=0)
 # Show dataframe
  df = df[['age', 'location', 'workclass', 'education',
           'marital_status', 'occupation', 'sex',  'hours_per_week', 'native_country','MonthyIncome_2020','Networth_2007','Networth_2008','Networth_2009','Networth_2010','Networth_2011','Networth_2012','Networth_2013','Networth_2014','Networth_2015','Networth_2016','Networth_2017','Networth_2018','Networth_2019','Networth_2020']].copy()

  y_list=df.MonthyIncome_2020.values
  X_list=df.iloc[:,:9]

  y_array=np.array(y_list).reshape(-1,1)
  X_array=np.array(X_list).reshape(-1,9)
  enc = OrdinalEncoder()
  enc.fit(X_array)
  Xtransformed=enc.transform(X_array)
  print(enc.transform(X_array))


 # split into train and test datasets
  x_train, x_test, y_train, y_test = train_test_split(Xtransformed, y_array)
  print(x_train.shape)


 # fit final model
  model = LinearRegression()
  model.fit(x_train, y_train)
  print("intercept",model.intercept_)
  print("coef", model.coef_)
  print("model.score(x_train, y_train)",model.score(x_train, y_train))
  print("model.score(x_test, y_test)",model.score(x_test, y_test))


  XPredict_transformed = enc.transform(self.XPredict_salary)
  # make a prediction
  ynew = model.predict(XPredict_transformed)
  print("model.score(x_pred, y_pred)",model.score(XPredict_transformed, ynew))
  # show the inputs and predicted outputs
  for i in range(len(XPredict_transformed)):
    print("X=%s, Predicted=%s" % (XPredict_transformed[i], ynew[i]))
    return ynew[i]




