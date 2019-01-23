#---------------------------------------------------
# Code Start
#---------------------------------------------------
#---------------------------------------------------
# Import Libraries
#---------------------------------------------------
import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
import numpy as np

#---------------------------------------------------
# Generate train/test split
#---------------------------------------------------
dataInput = pd.read_csv('../input/iris-data.csv', header=0)

#---------------------------------------------------
# Getting the lengths of things
#---------------------------------------------------
data_length = (len(dataInput))
test_length = int(round(data_length*(0.2), 0))

#---------------------------------------------------
# Break into train/test split
#---------------------------------------------------
import random
test_numbers = sorted(set(random.sample(range(0, data_length), test_length)))
test_frame = pd.DataFrame()

for k in test_numbers:
    test_frame = test_frame.append(dataInput.loc[k])
    dataInput = dataInput.drop(k)
del (test_frame['Iris-Type'])

#---------------------------------------------------
# Set features
#---------------------------------------------------
numeric_columns = ["sepal_length","sepal_width",'petal_length','petal_width']
nonnumeric_columns = ["Iris-Type"]

#---------------------------------------------------
# This part of the code is where you might fix the input data if there are
# issues with the data having gaps.
#---------------------------------------------------
#---------------------------------------------------
# Encode the features
''' As xgboost cannot use catagorical data, you've got to change it into
    intergers instead'''
#---------------------------------------------------
le = LabelEncoder()
for feature in nonnumeric_columns:
    dataInput[feature]  = le.fit_transform(dataInput[feature])

#---------------------------------------------------
# Set features
#---------------------------------------------------
'''
#---------------------------------------------------
# Prepare the Data Inputs
#---------------------------------------------------
train_X = big_X_imputed[0:train_df.shape[0]].as_matrix()
test_X = big_X_imputed[train_df.shape[0]::].as_matrix()
train_y = train_df['Survived']

#---------------------------------------------------
# Runs XGBoost
#---------------------------------------------------
gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.05).fit(train_X, train_y)
predictions = gbm.predict(test_X)

#---------------------------------------------------
# Compiles and prints out submission results
#---------------------------------------------------
submission = pd.DataFrame({ 'PassengerId': test_df['PassengerId'],
                            'Survived': predictions })
submission.to_csv("submission.csv", index=False)
print(submission)

#---------------------------------------------------
#Fin
#---------------------------------------------------
'''
