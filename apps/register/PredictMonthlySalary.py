import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation


class SalaryPredict():

 def __init__(self, XPredict_salary):
        self.XPredict_salary = XPredict_salary


 def Predict(self):
  df = pd.read_csv('Wealth.csv', index_col=0)
 # Show dataframe
  df = df[['age', 'location', 'workclass', 'education',
           'marital_status', 'occupation', 'sex',  'hours_per_week', 'native_country','MonthyIncome_2020','Networth_2007','Networth_2008','Networth_2009','Networth_2010','Networth_2011','Networth_2012','Networth_2013','Networth_2014','Networth_2015','Networth_2016','Networth_2017','Networth_2018','Networth_2019','Networth_2020']].copy()


  encode_list = df.iloc[:, :10]
  encode_array = np.array(encode_list).reshape(-1, 10)
  enc = OrdinalEncoder()
  enc.fit(encode_array)
  transformed = enc.transform(encode_array)
  Xtransformed = transformed[:, :9]
  y_transformed = transformed[:, 9:]


  x_train, x_test, y_train, y_test = train_test_split(Xtransformed, y_transformed)

  XPredict_transformed = enc.transform(self.XPredict_salary)
  # make a prediction
  clf = DecisionTreeClassifier()

  # Train Decision Tree Classifer
  clf = clf.fit(x_train, y_train)

  # Predict the response for test dataset
  y_pred = clf.predict(x_test)


  ynew = clf.predict(np.array(XPredict_transformed).reshape(1, -1))
  accuracy=metrics.accuracy_score(y_test, y_pred)
  print("Predict salary using decsion tree, Accuracy is:", metrics.accuracy_score(y_test, y_pred))


  ynew_float = ynew[0]

  X_Y = np.append(XPredict_transformed, ynew_float)
  X_Y_reserve = enc.inverse_transform(np.array(X_Y).reshape(1, -1))


  X_reserve = X_Y_reserve[:, :9]
  Y_reserve = X_Y_reserve[:, 9:]

  for i in range(len(XPredict_transformed)):

    return Y_reserve[i]




