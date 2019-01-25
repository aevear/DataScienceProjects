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
test_results = test_frame['Iris-Type']
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
encoder = LabelEncoder()
for feature in nonnumeric_columns:
    dataInput[feature]  = encoder.fit_transform(dataInput[feature])
    test_frame[feature]  = encoder.fit_transform(test_frame[feature])
#---------------------------------------------------
# Prepare data inputs
#---------------------------------------------------
train_X = dataInput[0:dataInput.shape[0]].as_matrix()
test_X = test_frame[0:test_frame.shape[0]].as_matrix()
train_y = dataInput['Iris-Type']
print(train_y)

#---------------------------------------------------
# Run XGBoost
#---------------------------------------------------
gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.05).fit(train_X, train_y)
predictions = gbm.predict(test_X)

print(predictions)
#---------------------------------------------------
# Prepare output values
#---------------------------------------------------











#---------------------------------------------------
# Based in part on https://www.kaggle.com/datacanary/xgboost-example-python
#---------------------------------------------------
#Fin
#---------------------------------------------------
