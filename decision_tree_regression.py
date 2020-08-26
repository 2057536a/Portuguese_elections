import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score



# IMPORTING THE DATA
dataset = pd.read_csv("ElectionData.csv")

dataset = dataset.drop("TimeElapsed", axis=1)
dataset = dataset.drop("time", axis=1)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# ENCODING CATEGORICAL DATA
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0,19])], remainder='passthrough')

# Fit and do the transformation on X. Since the fit_transform returns the transformed matrix, we need
# to save the output to X as a numpy array because this will be expected from the machine learning algo
X = np.array(ct.fit_transform(X))

# SPLITTING THE DATA
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# TRAIN THE DECISION TREE REGRESSION MODEL
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, y_train)

# PREDICTING TEST SET RESULTS
y_pred = regressor.predict(X_test)

# EVALUATING THE SVR PERFORMANCE
print(r2_score(y_test, y_pred))