"""
PROBLEM STATEMENT: The advertising dataset captures sales revenue generated with
respect to advertisements spends across multiple channels like radio,tv,and newspaper.
OBJECTIVE:
build a linear regression model to:
*interpret the coefficient of the model
*make prediction
*find and analyze model residuals
*Evaluate model efficiency using RMSE and R-square values
"""
import inline as inline
import matplotlib
#import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score,mean_squared_error
from math import sqrt
from sklearn.linear_model import LinearRegression


#inporting dataset to pandas dataframe
data=pd.read_csv('D:/machine learning/dataset/Advertising.csv',index_col=0)   #index_col=false can be used to force pandas to not use first column as the index,
print(data.head())
#in this dataframe we have 4 columns with label 'TV','radio',newspaper','sales' which
#indicate the amount in thousand dollar spend on advirtisemesnt on all four media
#and sales is the target variable
data.columns=['TV','Radio','Newspaper','Sales']   #DataFrame.columns return the column labels of the given dataframe
print(data.columns)
print(data.shape)

# let us visualize the relationship between features and targets variable sales using scattered plot
fig,axes=plt.subplots(1,3)
data.plot(kind='scatter',x='TV',y='Sales',ax=axes[0],figsize=(16,8))
data.plot(kind='scatter',x='Radio',y='Sales',ax=axes[1])
data.plot(kind='scatter',x='Newspaper',y='Sales',ax=axes[2])

#to display the plot(also see the image plot1)
plt.show()

#apllying linear regression analysis to estimate the relationship between sales
# and TV ad spending
feature_cols=['TV']
x=data[feature_cols]       #here x is the independent variable
y=data.Sales                #y is the dependent varaible

#initializing the Linear regression model
lm=LinearRegression()
#fitting the model: it is mesure of how well a machine learning model generalizes to similar data to that on which it was trained
lm.fit(x,y)





