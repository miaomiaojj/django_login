import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.feature_selection import SelectKBest


from sklearn.feature_selection import chi2

class FactorAnalysisFunction:
 # Read CSV file into DataFrame df
 df = pd.read_csv('Adult.csv', index_col=0)

 # Show dataframe

 #age,workclass,fnlwgt,education,education-num,marital-status,occupation,relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,Income
 df = df[['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country','Income']].copy()
 df.info()
 #statistics = df[["age", "Income"]].describe()
# print(statistics)

 count = pd.crosstab(df.marital_status, df.Income)
 #print(df.Income.count)
#---------------------sex--------------------
#count.T.plot(kind='bar')
#---------------------Age--------------------
# count.T.plot(kind='area', stacked=False)
#---------------------workclass--------------
#count.T.plot(kind='area', stacked=False)
#---------------------education------------
#count.T.plot(kind='bar')
#---------------------education_num-------
#count.T.plot(kind='area', stacked=False)
#--------------------marital_status-------
 count.T.plot(kind='bar', stacked=False)
#--------------------occuption------------
 #count.T.plot(kind='bar')
# --------------------occuption------------
#count.T.plot(kind='bar')
#relationship

 #count.T.plot(kind='area', subplots=True, figsize=(8, 4))


 #df.plot(kind='scatter', x=df.hours_per_week, y=df.Income)

 #count.T.plot(kind='box',  sym='r+')
 fig1 = plt.gcf()

 #df.plot(kind='area',x=df.capital_gain, y=df.Income)
 plt.show()
 plt.draw()
#apps/register/templates/register/AdultDataset
 fig1.savefig('templates/'+ 'maritalStatus_income' + '.png')  # Use fig. here

