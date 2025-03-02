import numpy as np

list1 = [2, 4, 6, 8]
arr = np.array(list1)

print(arr)

arr1 = np.array([20,30,40,50,60,88])
print(arr1)

arr2 = np.zeros(5)
print(arr2)

arr3 = np.arange(8)
print(arr3)

arr4 = np.random.rand(6)
print(arr4)

arr5 = np.empty(4)
print(arr5)

arr6 = np.array([[10,20,30,40],
                 [50,60,70,80]])
print(arr6)

arr6 = np.array([[[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]],
                 
                [[10,20,30,40],
                 [50,60,70,80],
                 [90,100,110,120]],

                 [[11,22,33,44],
                 [55,66,77,88],
                 [99,110,111,112]]])

print(arr6)

arr7 = np.zeros((2,3))
print(arr7)

arr8 = np.zeros((2,3,4))
print(arr8)




newarr3 = np.empty((3,4,2))
print(newarr3)

print(newarr3. dtype)
print(newarr2.dtype)



myarr1 = np.array([1,3,7])
print(myarr1.dtype)
myarr2 = np.array(myarr1, dtype = 'float64')
print(myarr2)
print(myarr2.dtype)

newarr = np.full((2,5), 7)
print(newarr)

newarr2 = np.random.rand(2,4,3)
print(newarr2)

print(newarr.ndim)
print(newarr2.ndim)

print(newarr.size)

print(newarr.shape)

print(newarr.data)

myarr1 = np.array([[[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]],
                 
                [[10,20,30,40],
                 [50,60,70,80],
                 [90,100,110,120]],

                 [[11,22,33,44],
                 [55,66,77,88],
                 [99,110,111,112]]])

print(myarr1)
#print(myarr1[1,2,1])
print()
print(myarr1[-2])


myarr2 = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12]])

print(myarr2)
print(myarr2[1,2])

arr3 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
    ])

#print(arr3)

sec_row = arr3[1, :]
#print(sec_row)

third_col = arr3[ : , 2]
print(third_col)

array1 = np.array([
    [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 11, 12]
        ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ],
    [
        [25, 26, 27, 28],
        [29, 30, 31, 32],
        [33, 34, 35, 36]
        ]
    ])


print(array1)


elem = array1[1, 2, 1]
print(elem)


#fetch 32
elem2 = array1[2, 1, 3]
print(elem2)


print(array1[0:2])


print(array1[0:3:2])

print(array1[1:])

print(array1[:2])


numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(numbers)

numbers2 = np.arange(1,28)

new_nums = np.reshape(numbers2,(3, 3, 3))
print(new_nums)

flatten_array = np.reshape(new_nums, -1)
print(flatten_array)

array2 = np.arange(11, 20)
print(array1)
print(array2)

addition_res = np.add(array1, array2)
print(addition_res)

sub_res = np.subtract(array1, array2)
print(sub_res)

mult = np.multiply(array1, array2)
print(mult)


div = np.divide(array1, array2)
print(div)


power_res = np.power(array1, array2)
print(power_res)

mod_res = np.mod(array1, array2)
print(mod_res)

array5 = np.array([
    [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 11, 12]
        ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ],
    [
        [25, 26, 27, 28],
        [29, 30, 31, 32],
        [33, 34, 35, 36]
        ]
    ])

print(array5)

array6 = np.transpose(array5)
print(array6)

array1 = np.arange(1, 10)
#print(array1)
#print(np.sqrt(array1))

#print(np.mean(array1))

#print(np.median(array1))

#print(np.max(array1))

#print(np.min(array1))

a = np.array([2, 5, 8])
b = np.array([3, 5, 7])

print(a)
print(b)
print(np.less(a, b))

strings = np.array(["HELLO", "WORLD"])
print(strings)
#print(np.char.capitalize(strings))
#print(np.char.upper(strings))
print(np.char.lower(strings))
