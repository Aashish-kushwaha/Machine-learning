import pandas as pd
import numpy as np

data={
    'roll_no':[1,2,3,4],
    'prr_id':[34,56,67,89],
    'marks':[12,34,556,78]
}
print(data)
df1=pd.DataFrame(data)
print(df1)

# setting index
df2=pd.DataFrame(data,index=['a','b','c','d'])
print(df2)

print(df2.loc['a'])
print(df2.iloc[0:2,2:3])

# loading csv file
df=pd.read_csv("iris.csv")
print(df)

#printing starting value of file
print(df.head())

#top 3 rows
print(df.head(3))

#last value of data
print(df.tail())

#size of data
print(df.shape)

#information of data
print(df.info())

#used to give mathematical summary work only on numerical columns
print(df.describe())


#fetch column
sr=df['sepal.length']
print(sr)
print(type(sr))

#fetch multiple column:we pass the  list 
li=df[['sepal.length','sepal.width','petal.length']]
print(li)
print(type(li))


# # missingvalues
# data={
#     'roll_no':[1,2,3,4],
#     'prr_id':[34,56,67,89],
#     'marks':[np.nan,34,556,78]
# }
# df1=pd.DataFrame(data)
# print(df1)

# print(df1.isnull())
# print(df1.isnull().sum())

# df2=df1.fillna(1)
# print(df2)

# # drop null values
# a=df1.dropna()  #removes the entire row
# print(a)


