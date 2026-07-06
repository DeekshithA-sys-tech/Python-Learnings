# List : list is similar to array but it stores different data types

# List is mutable
# List is ordered
# List is indexed
# List is changeable

# student  = [ "Ram" , 94.8 , "delhi"]
# print(type(student))
# print(student)
# print(len(student))
# print(student[0])
# print(student[1])
# print(student[2])

# List Methods
# append()
# insert()
# remove()
# pop()
# clear()
# sort()
# reverse()

# append() : adds an element at the end
# arr = [1,2,3,4,5,6]
# arr.append(10)
# print(arr) # output : [1, 2, 3, 4, 5, 6, 10]

# insert() : adds an element at the specified index
# arr = [1,2,3,4,5,6]
# arr.insert(2,10) 
# print(arr) # output : [1, 2, 10, 3, 4, 5, 6]

# remove() : removes an first occurance of an element from the list
# arr = [1,2,3,4,5,6]
# arr.remove(4) # output : [1, 2, 3, 5, 6]
# print(arr)
# arr.remove(10)
# print(arr) # output - IndexError: list.remove(x): x not in list

# pop() : removes an element from the list at the specified index
# arr = [1,2,3,4,5,6,20]
# arr.pop(2) # output - [1, 2, 4, 5, 6]
# print(arr)
# # arr.pop(10) # output - pop index out of range
# # print(arr)
# print(arr.pop()) # remove last element
# print(arr) # output - 20

# clear() : removes all elements from the list
# arr = [1,2,3,4,5,6]
# print(arr)
# arr.clear()
# print(arr) # output - []

# sort() : sorts the list
# arr = [1,2,3,4,5,6]
# print(arr)
# arr.sort()
# print(arr) # output - [1, 2, 3, 4, 5, 6]
# arr = [0,21,120]
# arr.sort() # ascending order
# print(arr)
# arr.sort(reverse=True) # descending order
# print(arr)
# arr = ["Apple","banana"]
# print(arr)
# arr.sort()
# print(arr) # output - ['Apple', 'Banana', 'apple', 'banana']

# reverse() : reverse the list
# arr = [1,2,3,4,5,6]
# print(arr)
# arr.reverse()
# print(arr) # output - [6, 5, 4, 3, 2, 1]


# ascii (ordinal value) value of a character
# print(ord("A")) # output - 65

# chr (character) value of a ascii value
# print(chr(65)) # output - A

# Tuple : A built in data type which is immutable
# Tuple is ordered 
# Tuple is indexed
# Tuple is unchangeable
# syntax : tuple_name = (value1 , value2 , value3 , value4)

# tuple1 = (1,2,3,4,5,6)
# print(type(tuple1))
# print(tuple1)
# print(tuple1[0])
# print(tuple1[1])

# tuple1[0] = 10 # tuple is immutable

# x = (1)
# print(type(x)) # output - <class 'int'>
# string =("str")
# print(type(string)) # output - <class 'str'>

# x = (1,)
# print(type(x)) # output - <class 'tuple'>
# tuple = ("str",) 
# print(type(tuple)) # output - <class 'tuple'>


tuple1 = (1,2,3,4,5,6)
print(tuple1[0:4]) # output - (1, 2, 3, 4) (slice method)

tuple1 = (1,2,3,4,5,6)
print(tuple1[1:]) # output - (2, 3, 4, 5, 6)

# tuple1.append(10)
# print(tuple1)   #(immutable) output - TypeError: 'tuple' object does not support item assignment

# tuple1 = (1,2,3,2,4,5,6)
# print(tuple1.count(1)) # output - 1
# print(tuple1.count(2)) # output - 2
# print(tuple1.index(2)) # output - 1