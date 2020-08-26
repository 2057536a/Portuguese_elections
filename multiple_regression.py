import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score



# Importing the data
dataset = pd.read_csv("ElectionData.csv")

dataset = dataset.drop("TimeElapsed", axis=1)
dataset = dataset.drop("time", axis=1)

# pd.set_option('display.max_rows', dataset.shape[0]+1)
print(dataset.columns)

ind = 0
for col in dataset.columns:
	print("Column at index {}, or type {}: {}".format(ind, dataset[col].dtypes, col))
	print(dataset[col])
	print("\n\n\n\n")
	print("#########################")
	ind += 1

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Encoding categorical data
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 19])], remainder='passthrough')

# Fit and do the transformation on X. Since the fit_transform returns the transformed matrix, we need
# to save the output to X as a numpy array because this will be expected from the machine learning algo
X = np.array(ct.fit_transform(X))


# Make the split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train the multiple regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting test set results
y_pred = regressor.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

print(regressor.coef_)
print(regressor.intercept_)

print(r2_score(y_test, y_pred))