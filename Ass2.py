# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:29:10 2024

@author: Sanket Tambe
"""


import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("C:\Data Science\DMW\Heart.csv")

# a) Standard deviation and variance
print("Standard deviation:\n", data.std())
print("Variance:\n", data.var())


#--------------------------------------------------------------------------------
# b) Covariance and correlation
#These lines calculate the covariance and correlation matrices using the cov() and corr() 
covariance = data.cov()
print("Covariance matrix:\n", covariance)
correlation = data.corr()
print("Correlation matrix:\n", correlation)


#-------------------------------------------------------------------------------
# c) Independent features
# Assuming numerical features are independent (excluding target variable)
independent_features = len(data.select_dtypes(include=[int, float])) - 1
print("Number of independent features:", independent_features)


#--------------------------------------------------------------------------------
# d) Identify unwanted features
# Compute correlation matrix among features
feature_correlation_matrix = data.corr()

# Identify features highly correlated with each other (redundant features)
highly_correlated_features = (feature_correlation_matrix.abs() > 0.8) & (feature_correlation_matrix.abs() < 1)
highly_correlated_features = highly_correlated_features.unstack().reset_index()
highly_correlated_features.columns = ['Feature 1', 'Feature 2', 'Correlation']
highly_correlated_features = highly_correlated_features[highly_correlated_features['Correlation']]
print("Highly correlated features (correlation > 0.8):\n", highly_correlated_features)

# Identify features with low variance (variance < threshold)
low_variance_features = data.var()[data.var() < 0.01].index.tolist()
print("Low variance features (variance < 0.01):\n", low_variance_features)


#----------------------------------------------------------------------------------
# e) Discretize age using equi-frequency binning
'''pd.qcut(data["Age"], 3, labels=["Low", "Medium", "High"]) divides the "Age" values into three equal-sized groups (quartiles) 
and assigns labels "Low", "Medium", and "High" to each quartile.'''
bins = pd.qcut(data["Age"], 3, labels=["Low", "Medium", "High"])
data["Age_category"] = bins


#--------------------------------------------------------------------------------
# f) Normalize RestBP, chol, and MaxHR
# Min-max normalization
data["RestBP_minmax"] = (data["RestBP"] - data["RestBP"].min()) / (data["RestBP"].max() - data["RestBP"].min())
data["RestBP_minmax"]
data["chol_minmax"] = (data["Chol"] - data["Chol"].min()) / (data["Chol"].max() - data["Chol"].min())
data["chol_minmax"]
data["MaxHR_minmax"] = (data["MaxHR"] - data["MaxHR"].min()) / (data["MaxHR"].max() - data["MaxHR"].min())
data["MaxHR_minmax"] 

# Z-score normalization
data["RestBP_zscore"] = (data["RestBP"] - data["RestBP"].mean()) / data["RestBP"].std()
data["RestBP_zscore"]
data["chol_zscore"] = (data["Chol"] - data["Chol"].mean()) / data["Chol"].std()
data["chol_zscore"] 
data["MaxHR_zscore"] = (data["MaxHR"] - data["MaxHR"].mean()) / data["MaxHR"].std()
data["MaxHR_zscore"]

# Decimal scaling normalization
data["RestBP_decimal"] = data["RestBP"] / 100
data["chol_decimal"] = data["Chol"] / 100
data["MaxHR_decimal"] = data["MaxHR"] / 100

print("Original data:\n", data.head())


#=============================================================================================

