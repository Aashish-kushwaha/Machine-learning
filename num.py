import numpy as np
# creating numpy array

list=[2,3,4,5,6]
arr=np.array(list);

print(list)
print()
print(arr)
print(type(list))
print(type(arr))


print(arr+1);

list1=[[1,2,3,4],
      [5,6,7,8]]
arr=np.array(list1)
print(list1);
# float array

list2=[3,4,5,7];
arr3=np.array(list2,dtype=float);
print(arr3);

# convert float to int
arr3=arr3.astype('int')
print(arr3)

# multi value arrray
arr5=np.array([2,3,4.9,'s'],dtype='object')
print(arr5)

# array to list
list3=arr5.tolist()
print(list3)
print(type(list3))


# array dimension
arr0=np.array(list1)
print(arr0.shape)

# number of elements
print(arr0.size)

# number of dimension
print(arr0.ndim)

# reverse rows
print(arr0[::-1])
# reverse columns
print(arr0[::-1,::-1])
print()
# specific element extraction
print(arr0[0,:])  #0 row and all the columns
print(arr0[:1,: ]) #number of rows before 1 ad all columns
print(arr0[:2:]) #number of rows before row 2 and all columns
print()
print(arr0[:-1:]) #all rows accept last row
print(arr0[:,3]) #last column
print(arr0[:,-1]) #last column


# reshaping and flatting
print(arr0.shape)
print(arr0.reshape(1,8))
print(arr0.reshape(4,2))
print(arr0.reshape(8,1))
print()
# remove all the dimension
print(arr0.flatten())

# random array
arr9=np.arange(10)
print(arr9)
arr2=np.arange(2,10)
print(arr2)
arr4=np.arange(0,10,3)
print(arr4)
arr6=np.arange(10,0,-1)
print(arr6)

arr7=np.linspace(1,10,3)
print(arr7)

# unique values and count
arr8=[[1,1,2,3,45,2,1],[12,3,3,45,7,6,8]]
print(np.unique(arr8))
print(np.unique(arr8,return_counts=True))