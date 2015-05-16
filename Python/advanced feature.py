# a simple case
L = []
n = 1
while (n <= 99) :
	L.append(n)
	n += 2;
r = []
n = 3
for i in range(n) :
	r.append(L[i])

# the same function with the operation
# slice
r = L[0 : 3]

# some cases with operation slice
# the third parameter in slice is the gap
L = range(100)
L = [:10:2]
# [0, 2, 4, 6, 8]
L = [::5]
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 ... , 95]
L = [::]
# [0, 1, 2, 3, 4, ..., 99]

# tuple is also a kind of list
# it also supports slice
(0, 1, 2, 3, 4, 5)[:3]
# (0, 1, 2)

# string can also be seen as a kind of list
'ABCDEFG'[:3]
# 'ABC'
'ABCDEFG'[::2]
# 'ACEG'

# iteration
# iteration is performed by for ... in in Python
# for... in can be used on all iterable object
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print key
# the storation of dict is not the same lile list
# the order of the result may be different

# to judge whether an object is iterable
from collections import Iterable
isinstance('abc', Iterable)

# realize index loop in Java to list
# use enumerate function
for i, value in enumerate(['A', 'B', 'C']):
	print i, value
# two varabies in loop is common in Python
for x, y in [(1, 2), (2, 3), (3, 9)]
	print x, y

# list comprehensions
# it is a simple and powerful way of creating list in Python
# to create [1*1, 2*2, 3*3,..., 10*10]
# except using loop
[x * x for x in range(1, 11)]
# judgement can also be added to it
[x * x for x in range(1. 11) if x % 2 == 0]
# using two loops creating full permutation
[m + n for m in 'ABC' for n in 'XYZ']
# using list comprehensions, to list all files and directories in current directory
import os
[d for d in os.listdir('.')]
# we can use iteritems() of dict to iterate key and value
d = ['x': 'A', 'y': 'B', 'z': 'C']
for k, v in d.iteritems():
	print k, '=', v
# so, we can also use two varabies in list comprehensions
d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k,v in d.iteritems()]
# two lowercase all string in a list
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

# generator
# it can calculate while looping
# instead of creating the whole thing like list comprehensions
# creating a list
L = [x * x for x in range(10)]
# creating a generator
g = (x * x for x in range(10))
# we can print every elements in list directly
# for generator, wo must use next() 
g.next()
g.next()
g.next()
# the generator stores the algorithm
# each time using next(), it can calculate the next value
# until the last element
# but the correct way of printing every element is using for
# because generator is also iterable
g = (x * x for x in range(10))
for n in g:
	print n
# if the algorithm is complex we can realize generator like a function
# an example in fib
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print b
		a, b = b, a + b
		n = n + 1
fib(6)
# actually fib defines the rule of calculation
# from first element calculate the next util the end
# the logic is very like generator
# to turn the function into generator
# we change print to yield
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
# if a function contains yield
# it becomes generator
# a generator function each time call next()
# it will break if meets yield
# and next call() will be continued from where it breaked
for n in fib(6)
	print n
# the for loop in function generator stops
# if meets return or meets the end of the code