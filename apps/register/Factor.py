import numpy as np
import pandas as pd


from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

class FactorAnalysisFunction:
 # Read CSV file into DataFrame df
 df = pd.read_csv('Adult.csv', index_col=0)

 # Show dataframe
 df = df[['age', 'workclass', 'fnlwgt', 'education', 'education_num',
          'marital_status', 'occupation', 'relationship', 'race',
          'sex', 'capital_gain', 'capital_loss', 'hours_per_week',
          'native_country','Income']].copy()
 df.info()

 df.workclass.unique()

 df.loc[df['workclass'] == ' Private', 'workclass'] = 1
 df.loc[df['workclass'] == ' Self-emp-not-inc', 'workclass'] = 2
 df.loc[df['workclass'] == ' Self-emp-inc', 'workclass'] = 3
 df.loc[df['workclass'] == ' Federal-gov', 'workclass'] = 4
 df.loc[df['workclass'] == ' Local-gov', 'workclass'] = 5
 df.loc[df['workclass'] == ' State-gov', 'workclass'] = 6
 df.loc[df['workclass'] == ' Without-pay', 'workclass'] = 7
 df.loc[df['workclass'] == ' Never-worked', 'workclass'] = 8

 df.education.unique()
 #education

 df.loc[df['education'] == ' Preschool', 'education'] = 1
 df.loc[df['education'] == ' 1st-4th', 'education'] = 2
 df.loc[df['education'] == ' 5th-6th', 'education'] = 3
 df.loc[df['education'] == ' 7th-8th', 'education'] = 4
 df.loc[df['education'] == ' 9th', 'education'] = 5
 df.loc[df['education'] == ' 10th', 'education'] = 6
 df.loc[df['education'] == ' 11th', 'education'] = 7
 df.loc[df['education'] == ' 12th', 'education'] = 8
 df.loc[df['education'] == ' HS-grad', 'education'] = 9
 df.loc[df['education'] == ' Assoc-acdm', 'education'] = 10
 df.loc[df['education'] == ' Prof-school', 'education'] = 11
 df.loc[df['education'] == ' Assoc-voc', 'education'] = 12
 df.loc[df['education'] == ' Some-college', 'education'] = 13
 df.loc[df['education'] == ' Bachelors', 'education'] = 14
 df.loc[df['education'] == ' Masters', 'education'] = 15
 df.loc[df['education'] == ' Doctorate', 'education'] = 16

 df.marital_status.unique()
 # 数值转换
 df.loc[df['marital_status'] == ' Married-civ-spouse', 'marital_status'] = 1
 df.loc[df['marital_status'] == ' Divorced', 'marital_status'] = 2
 df.loc[df['marital_status'] == ' Never-married', 'marital_status'] = 3
 df.loc[df['marital_status'] == ' Separated', 'marital_status'] = 4
 df.loc[df['marital_status'] == ' Widowed', 'marital_status'] = 5
 df.loc[df['marital_status'] == ' Married-spouse-absent', 'marital_status'] = 6
 df.loc[df['marital_status'] == ' Married-AF-spouse', 'marital_status'] = 6

 df.occupation.unique()
 # 数值转换
 df.loc[df['occupation'] == ' Tech-support', 'occupation'] = 1
 df.loc[df['occupation'] == ' Craft-repair', 'occupation'] = 2
 df.loc[df['occupation'] == ' Other-service', 'occupation'] = 3
 df.loc[df['occupation'] == ' Sales', 'occupation'] = 4
 df.loc[df['occupation'] == ' Exec-managerial', 'occupation'] = 5
 df.loc[df['occupation'] == ' Prof-specialty', 'occupation'] = 6
 df.loc[df['occupation'] == ' Handlers-cleaners', 'occupation'] = 7
 df.loc[df['occupation'] == ' Machine-op-inspct', 'occupation'] = 8
 df.loc[df['occupation'] == ' Adm-clerical', 'occupation'] = 9
 df.loc[df['occupation'] == ' Farming-fishing', 'occupation'] = 10
 df.loc[df['occupation'] == ' Transport-moving', 'occupation'] = 11
 df.loc[df['occupation'] == ' Priv-house-serv', 'occupation'] = 12
 df.loc[df['occupation'] == ' Protective-serv', 'occupation'] = 13
 df.loc[df['occupation'] == ' Armed-Forces', 'occupation'] = 14

 df.relationship.unique()
 # 数值转换
 df.loc[df['relationship'] == ' Wife', 'relationship'] = 1
 df.loc[df['relationship'] == ' Own-child', 'relationship'] = 2
 df.loc[df['relationship'] == ' Husband', 'relationship'] = 3
 df.loc[df['relationship'] == ' Not-in-family', 'relationship'] = 4
 df.loc[df['relationship'] == ' Other-relative', 'relationship'] = 5
 df.loc[df['relationship'] == ' Unmarried', 'relationship'] = 6

 df.race.unique()
 # 数值转换
 df.loc[df['race'] == ' White', 'race'] = 1
 df.loc[df['race'] == ' Asian-Pac-Islander', 'race'] = 2
 df.loc[df['race'] == ' Amer-Indian-Eskimo', 'race'] = 3
 df.loc[df['race'] == ' Wife', 'race'] = 4
 df.loc[df['race'] == ' Black', 'race'] = 5
 df.loc[df['race'] == ' Other', 'race'] = 5

 df.sex.unique()
 # 数值转换
 df.loc[df['sex'] == ' Female', 'sex'] = 0
 df.loc[df['sex'] == ' Male', 'sex'] = 1

 df.native_country.unique()
 # 数值转换
 df.loc[df['native_country'] == ' United-States', 'native_country'] = 0
 df.loc[df['native_country'] == ' Cambodia', 'native_country'] =1
 df.loc[df['native_country'] == ' England', 'native_country'] = 2
 df.loc[df['native_country'] == ' Puerto-Rico', 'native_country'] = 3
 df.loc[df['native_country'] == ' Canada', 'native_country'] = 4
 df.loc[df['native_country'] == ' Germany', 'native_country'] = 5
 df.loc[df['native_country'] == ' Outlying-US(Guam-USVI-etc)', 'native_country'] = 6
 df.loc[df['native_country'] == ' India', 'native_country'] = 7
 df.loc[df['native_country'] == ' Japan', 'native_country'] = 8
 df.loc[df['native_country'] == ' Greece', 'native_country'] = 9
 df.loc[df['native_country'] == ' South', 'native_country'] = 10
 df.loc[df['native_country'] == ' China', 'native_country'] = 11
 df.loc[df['native_country'] == ' Cuba', 'native_country'] = 12
 df.loc[df['native_country'] == ' Iran', 'native_country'] = 13
 df.loc[df['native_country'] == ' Honduras', 'native_country'] = 14
 df.loc[df['native_country'] == ' Philippines', 'native_country'] = 15
 df.loc[df['native_country'] == ' Italy', 'native_country'] = 16
 df.loc[df['native_country'] == ' Poland', 'native_country'] = 17
 df.loc[df['native_country'] == ' Jamaica', 'native_country'] = 18
 df.loc[df['native_country'] == ' Vietnam', 'native_country'] = 19
 df.loc[df['native_country'] == ' Mexico', 'native_country'] = 20
 df.loc[df['native_country'] == ' Portugal', 'native_country'] = 21
 df.loc[df['native_country'] == ' Ireland', 'native_country'] = 22
 df.loc[df['native_country'] == ' France', 'native_country'] = 23
 df.loc[df['native_country'] == ' Dominican-Republic', 'native_country'] = 24
 df.loc[df['native_country'] == ' Laos', 'native_country'] = 25
 df.loc[df['native_country'] == ' Ecuador', 'native_country'] = 26
 df.loc[df['native_country'] == ' Taiwan', 'native_country'] = 27
 df.loc[df['native_country'] == ' Haiti', 'native_country'] = 28
 df.loc[df['native_country'] == ' Columbia', 'native_country'] = 29
 df.loc[df['native_country'] == ' Hungary', 'native_country'] = 30
 df.loc[df['native_country'] == ' Guatemala', 'native_country'] = 31
 df.loc[df['native_country'] == ' Nicaragua', 'native_country'] = 32
 df.loc[df['native_country'] == ' Scotland', 'native_country'] = 33
 df.loc[df['native_country'] == ' Thailand', 'native_country'] = 34
 df.loc[df['native_country'] == ' Yugoslavia', 'native_country'] = 35
 df.loc[df['native_country'] == ' El-Salvador', 'native_country'] = 36
 df.loc[df['native_country'] == ' Trinadad&Tobago', 'native_country'] = 37
 df.loc[df['native_country'] == ' Peru', 'native_country'] = 38
 df.loc[df['native_country'] == ' Hong', 'native_country'] = 39
 df.loc[df['native_country'] == ' Holand-Netherlands', 'native_country'] = 40

 df.Income.unique()

 df.loc[df['Income'] == ' <=50K', 'Income'] = 0
 df.loc[df['Income'] == ' >50K', 'Income'] =1

 y = df.pop('Income')
 X = df

 best_features = SelectKBest(score_func=chi2, k=len(X.columns))
 fit = best_features.fit(X, y)


 df_scores = pd.DataFrame(fit.scores_)
 df_columns = pd.DataFrame(X.columns)


 # 合并
 df_feature_scores = pd.concat([df_columns, df_scores], axis=1)

 #  定义列名
 df_feature_scores.columns = ['Feature', 'Score']
 # 按照score排序

 final_result_score=df_feature_scores.sort_values(by='Score', ascending=False)
 print(final_result_score)

