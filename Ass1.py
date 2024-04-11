# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:33:24 2024

@author: Dell
"""

#pad method--> fill with the nan value with previous value 
#befill method--> fill with nan value with next value
'''title
probelm defination
objective 
expected input  dataset column and name of the dataset
expected output getting the value
theory      
algo/techq
result
observation
conclusion
refer
'''

'''About Dataset
Exploring Heart Data using the "heart.csv" Dataset
Introduction:
In this notebook, we intend to analyze data related to cardiac features of patients from the "heart.csv" dataset. This dataset provides various information about patients, including age, gender, blood pressure, cholesterol levels, electrocardiographic (ECG) features, and more.

Dataset Information:
This dataset includes the following features:

age: The age of the patient.
sex: Gender of the patient (0: female, 1: male).
cp: Type of chest pain.
trestbps: Resting blood pressure.
chol: Serum cholesterol.
fbs: Fasting blood sugar > 120 mg/dl.
restecg: Resting electrocardiographic results.
thalach: Maximum heart rate achieved.
exang: Exercise induced angina.
oldpeak: ST depression induced by exercise relative to rest'''


import pandas as pd
import numpy as np

df=pd.read_csv("C:/Users/suraj/OneDrive/Desktop/TY-SEM-2/DMWT_Practical/ass1/Heart.csv")
###############################
# checking the sample of the dataset 
df.head()
################################
#column in the dataset
df.columns
'''Out[6]: 
Index(['Unnamed: 0', 'Age', 'Sex', 'ChestPain', 'RestBP', 'Chol', 'Fbs',
       'RestECG', 'MaxHR', 'ExAng', 'Oldpeak', 'Slope', 'Ca', 'Thal', 'AHD'],
      dtype='object')'''
##################################
#info of the dataset
df.info()
##############################
'''h) Find shape of data.'''
#shape of the dataset
df.shape
#Out[7]: (303, 15)
##############################
#cheking the size of the dataset
df.size
#Out[12]: 4545
################################
#data types of' the dataset col'umn
'''e) Find data type of each column.'''
df.dtypes
'''Unnamed: 0      int64
Age             int64
Sex             int64
ChestPain      object
RestBP          int64
Chol            int64
Fbs             int64
RestECG         int64
MaxHR           int64
ExAng           int64
Oldpeak       float64
Slope           int64
Ca            float64
Thal           object
AHD            object
dtype: object'''
###################################
# drop the unnamed column which is not useable
df1=df.drop(['Unnamed: 0'], axis=1) 
df1
##################################
#now we can check again the dataset 
df1.shape
#Out[21]: (303, 14)
###################################
#describe the dataset value
b=df1.describe()
b
###############################
a=df1.isnull()
a.sum()
'''Out[11]: 
Unnamed: 0    0
Age           0
Sex           0
ChestPain     0
RestBP        0
Chol          0
Fbs           0
RestECG       0
MaxHR         0
ExAng         0
Oldpeak       0
Slope         0
Ca            4
Thal          2
AHD           0
dtype: int64'''
#in the above dataset Ca and Thal column has the null value and other column
#dose not have the null value 
#so we want to fill that null value
#####################################
'''a) Find Missing Values and replace the missing values
with suitable alternative.'''
##fill the null value
#we fill the nan value in the object datatype Thal Column AND 
#PLACING THE MEAN VALUE IN THE DATASET Ca column
thal_main=df1['Thal'].mode()
df1['Thal']=df1['Thal'].fillna(thal_main[0])

ca_main=df1['Ca'].mode()
df1['Ca']=df1['Ca'].fillna(ca_main[0])
# again checking the null value in the dataset
d=df1.isnull().sum()
d
#  no null value is present in the dataset
#############################
'''b) Remove inconsistency (if any) in the dataset.'''
#################################
'''f) Finding out Zero's.'''
#############################
'''g) Find Mean age of patients considering above dataset.'''
df1['Age'].mean()
###############################
'''c) Prepare boxplot analysis for each numerical attribute.'''
import matplotlib.pyplot as plt
plt.boxplot(df1['Age'])