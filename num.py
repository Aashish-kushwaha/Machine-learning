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


print()