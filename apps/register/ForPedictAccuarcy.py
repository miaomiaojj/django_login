import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
import matplotlib.pyplot as plt
import statistics
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation


class SalaryPredict():
  df = pd.read_csv('Wealth.csv', index_col=0)
 # Show dataframe
  df = df[['age', 'location', 'workclass', 'education',
           'marital_status', 'occupation', 'sex',  'hours_per_week', 'native_country','MonthyIncome_2020','Networth_2007','Networth_2008','Networth_2009','Networth_2010','Networth_2011','Networth_2012','Networth_2013','Networth_2014','Networth_2015','Networth_2016','Networth_2017','Networth_2018','Networth_2019','Networth_2020']].copy()

  y_list=df.MonthyIncome_2020.values
  X_list=df.iloc[:,:9]#9

  encode_list=df.iloc[:,:10]
  encode_array=np.array(encode_list).reshape(-1,10)
  enc = OrdinalEncoder()
  enc.fit(encode_array)
  transformed = enc.transform(encode_array)
  print(enc.transform(encode_array)[:10,9])

  Xtransformed=transformed[:,:9]
  print(Xtransformed)
  y_transformed=transformed[:,9:]
  print(y_transformed)



  x_train, x_test, y_train, y_test = train_test_split(Xtransformed, y_transformed)
  print(x_train.shape)



  XPredict_salary=np.array([27, 'Singapore', 'Private', 'Doctorate' ,'Never-married', 'Armed-Forces','Female', 40, 'Singapore'],dtype=object).reshape(1, -1)

  XPredict_transformed = enc.transform(XPredict_salary)

  clf = DecisionTreeClassifier()

  # Train Decision Tree Classifer
  clf = clf.fit(x_train, y_train)

  # Predict the response for test dataset
  y_pred = clf.predict(x_test)
  print(np.array(x_test[0]).reshape(1, -1))
  print(np.array(XPredict_transformed).reshape(1, -1))

  ynew = clf.predict(np.array(XPredict_transformed).reshape(1, -1))
  print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
  print(ynew)



  ynew_float = ynew[0]



  X_Y=np.append(XPredict_transformed, ynew_float)
  print(X_Y)
  X_Y_reserve=enc.inverse_transform(np.array(X_Y).reshape(1, -1) )
  print(X_Y_reserve)
  #print("model.score(x_pred, y_pred)",model.score(XPredict_transformed, ynew))
  X_reserve=X_Y_reserve[:,:9]
  Y_reserve=X_Y_reserve[:,9:]

  #-----------------------------------




  # show the inputs and predicted outputs
  for i in range(len(XPredict_transformed)):
    print("X=%s, Predicted=%s" % (X_reserve[i], Y_reserve[i]))
    #return ynew[i]




