# str1 = 'this is string.'
# str2 = "He can't do that."

# #Basic Operation

# # String Catination
# strConcate = str1+str2
# print(strConcate)

# # Length of String
# strLength = len(str1)
# print(strLength)
# strLength = len(str2)
# print(strLength)

# # Indexing
# str1 = "Too Good"
# print(str1[0]) # first character of str1 - T
# print(str1[len(str1)-1]) # last character of str1 - d

# # Slicing - accessing part of the string

# # syntax : str[starting_indx : ending_indx] 
# # Note : ending index is excluded
# str1 = "Too Good"
# print(str1[0:4]) # output - too
# print(str1[:]) # str1[0:str[len(x)]] . output - Too Good
# print(str1[0:len(str1)]) # str1[0:str[len(x)]] . output - Too Good
# print(str1[4:len(str1)])# str1[4:str[len(x)]] . output - Good

# String Functions

# #endswith("substring") - returns true if cantains or eles false
# str1 = "Im Coder"
# ans = str1.endswith("Coder")
# print(type(ans)) # output - bool

# #startswith("substring") - returns true if cantains or eles false
# str1 = "Im Coder"
# print(str1.startswith("Im"))

# #find("substring") - returns index of substring
# str1 = "Im Coder"
# ans = str1.find("C")
# print(ans) # output - 3
# print(type(ans)) # output - int

# #replace("substring1","substring2") - returns new string with substring1 replaced by substring2
# str1 = "Im Coder"
# ans = str1.replace("Coder","Programmer")
# print(ans) # output - Im Programmer

# #count("substring") - returns count of substring
# str1 = "Im C Coder "
# ans = str1.count("C")
# print(ans) # output - 2

# #split() - returns list of substrings
# str1 = "Im Coder"
# ans = str1.split()
# print(type(ans)) # output - list
# print(ans) # output - ['Im', 'Coder']

# #capitalize() - returns string with first letter capital
# str1 = "im coder"
# ans = str1.capitalize()
# print(ans) # output - Im coder

# #upper() - returns string with all letters capital
# str1 = "im coder"
# ans = str1.upper()
# print(ans) # output - IM CODER

# #lower() - returns string with all letters small
# str1 = "IM CODER"
# ans = str1.lower()
# print(ans) # output - im coder

# #strip() - returns string with leading and trailing spaces removed
str1 = "    Im Coder    "
ans = str1.strip()
print(ans) # output - Im Coder

# #isalpha() - returns true if string contains only alphabets
# str1 = "abc"
# ans = str1.isalpha()
# print(ans) # output - true
# str1 = "Im Coder"
# ans = str1.isalpha()
# print(ans) # output - false

# #isdigit() - returns true if string contains only digits (0-9)
# str1 = "123"
# ans = str1.isdigit()
# print(ans) # output - true
# str1 = "Im Coder"
# ans = str1.isdigit()
# print(ans) # output - false

# #isalnum() - returns true if string contains only digits and alphabets (0-9, a-z, A-Z)
# str1 = "123abc"
# ans = str1.isalnum()
# print(ans) # output - true
# str1 = "Im Coder"
# ans = str1.isalnum()
# print(ans) # output - false

# #isnumeric() - returns true if string contains only digits (all fractions roman numerals are not considered as digits)
# str1 = "5"
# ans = str1.isnumeric()
# print(ans) # output - true
# str1 = "Im Coder"
# ans = str1.isnumeric()
# print(ans) # output - false


# Conditions

# if

# if(condition):
#     statement1
# age = int(input("Enter your age: "))
# if(age>=18):
#     print("You are eligible for voting.")

# if else

# if(condition):
#     statement1
# else:
#     statement2
# age = int(input("Enter your age: "))
# if(age>=18):
#     print("You are eligible for voting.")
# else:
#     print("You are not eligible for voting.")

# if elif else

# if(condition):
#     statement1
# elif(condition):
#     statement2
# else:
#     statement3
# grade = input("Enter your grade: ")
# if(grade == "A"):
#     print("Excellent")
# elif(grade == "B"):
#     print("Good")
# elif(grade == "C"):
#     print("Average")
# else:
#     print("Fail")

# nested if

# if(condition):
#     if(condition):
#         statement1
#     else:
#         if(condition):
#             statement2
#         else:
#             statement3
# else:
#     statement4
age = int(input("Enter your age: "))
if(age>=18):
    print("You are eligible for voting.")
    if(age<=60):
        print("You are eligible for Driving.")
    else:
        print("You are not eligible for Driving.")
else:
    print("You are not eligible for voting.")
    print("You are not eligible for Driving.")