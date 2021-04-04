import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split


class wealthPredict:
 # Read CSV file into DataFrame df
 #XPredict=np.array([111375,147324,150844,171303,166807,222071,248594,276870,272201,288159,307153,340263,324594]).reshape(-1, 13)
 def __init__(self, XPredict):
        self.XPredict = XPredict

 def predict(self):
  df = pd.read_csv('Wealth.csv', index_col=0)

  df = df[['age', 'location', 'workclass', 'education', 'marital_status', 'occupation', 'sex',  'hours_per_week', 'native_country','MonthyIncome_2020','Networth_2007','Networth_2008','Networth_2009','Networth_2010','Networth_2011','Networth_2012','Networth_2013','Networth_2014','Networth_2015','Networth_2016','Networth_2017','Networth_2018','Networth_2019','Networth_2020']].copy()
 #df.info()

  y_list=df.iloc[:,19:24] #Networth_2020.values
  X_list=df.iloc[:,10:18]    #df.age.values#[:, :1]



  y_array=np.array(y_list).reshape(-1,5)#1
  X_array=np.array(X_list).reshape(-1,8)#13
  print(X_array)
  print("predict wealth,y ", y_array.shape)
  print("predict wealth,x ", X_array.shape)

 # split into train and test datasets
  x_train, x_test, y_train, y_test = train_test_split(X_array, y_array)
  #print(x_train.shape)

 # fit final model
  model = LinearRegression()
  model.fit(x_train, y_train)
  print("intercept",model.intercept_)
  print("coef", model.coef_)
  print("model.score(x_train, y_train)",model.score(x_train, y_train))
  print("model.score(x_test, y_test)",model.score(x_test, y_test))

  ynew = model.predict(self.XPredict)

 # show the inputs and predicted outputs
  for i in range(len(self.XPredict)):
    print("X=%s, Predicted=%s" % (self.XPredict[i], ynew[i]))
    return(ynew[i])




