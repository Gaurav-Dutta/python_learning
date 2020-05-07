#list provides important methods called map, filter, reduce
import math
import functools

myList = [1, 56, 7, 45, 32, 48, 90, 45, 48, 23, 66, 77]

#the map function is used to transform a list to another list, the transformation is done by a function, in this example below
#the function is provided using a lambda

square = lambda x: x * x
result = map(square, myList)
print(list(result))

#the filter function allows to filter a set of items based on some conditions
#in this example we filter the baove list to get the odd numbers only

odd = lambda x: x%2 == 1 
result = filter(odd, myList)
print(list(result))

#the reduce method is used to convert a list to a single item, usually sum or aggregate of things
#reduce requires an accumalater function which combines two items in the list to create a value

acc = lambda x,y: x  * 5 + 6 * y
result = functools.reduce(acc, myList, 0)
print(result)