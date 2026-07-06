# type Conversion

# Implicit type Conversion
a = 2
b = 4.5
sum = a+b # here "a" is int "b" is float . float is superior than int . So, sum type is float
print(type(sum)) #float

# Type Casting (mannual conversion)
a = "10" # a is strint
b=2.5
c = int(a) # "a" is physically converting to int and storing it in the variable c
print(type(c))
sum = b + c
print(type(sum))#float


pi = 3.142   # type float
x = str(pi) # type float
print(type(pi))
print(type(x))