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