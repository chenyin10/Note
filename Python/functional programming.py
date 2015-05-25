# higer-order function
# a fucntion which accepts another function as its parameter
def add(x, y, f):
	return f(x) + f(y)

print add(-5, 6, abs)

# map/reduce

# map() accepts two parameters
# one is a function, another is a sequence
# it returns a new list which contains f(i)
def f(x):
	return x * x;
print map(f, [1, 2, 3, 4, 5])
map(str, [1, 2, 3, 4, 5])
# ['1', '2', '3', '4', '5']

# reduce()
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
	return x + y
reduce(add, [1, 3, 5, 7, 9])
# 25
# can also use built-in function sum()
def fn(x, y):
	return x*10 +y
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
reduce(fn, map(char2num, '13579'))
# 13579
# rewrite it
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))	

# filter()
# to filter sequence
def is_ood(n):
	return n %2 == 1
filter(is_ood, [1, 2, 3, 4, 5])

def not_empty(s):
	return s and s.strip()
filter(not_empty, ['A', '', 'B', None, 'C', ' '])

# sorted
# very like comparator in Java
def cmp_ingnore_case(s1, s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	if u1 > u2:
		return 1
	return 0
sorted(['bob', 'about', 'Zoo', 'Credict'], cmp_ingnore_case)

# return function
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f = lazy_sum(1, 3, 5, 7, 9)
print f()
# 25
# returning a function is called closure
# in trap in closure
def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs
f1, f2, f3 = count()
print f1()		# 9
print f2()		# 9
print f3()		# 9
# because every f refers i
# and when each function executes, i has become 3
# way to solve it
def count():
	fs = []
	for i in range(1, 4):
		def f(j):
			def g():
				return j * j
			return g
		fs.append(f(i))
	return fs
f1, f2, f3 = count()
print f1()			# 1
print f2()			# 4
print f3()			# 9

# anonymous function
lambda x: x * x
# which is equal to 
def f(x):
	return x * x
# anonymous function only has one expression and doesn't have return
# we can also use anonymous function as return value
def build(x, y):
	return lambda: x * x + y * y

# decorator
# to add new things to a function without change its definition
# dynamically add new 'function' while the code is running
# in fact, decorator is a high-order function
def log(func):
	def wrapper(*args, **kw):
		print 'call %s()' % func.__name__
		return func(*args, **kw)
	return wrapper

@log
def now():
	print '2015-9-1'
# which is equal to now = log(now)
# the original now still exists but now refers to a new function
# if the decorator itself needs to pass parameter
# you need to write a high-order function returns decorator
def log(test):
	def decorator(func):
		def wrapper(*args, **kw):
			print '%s %s()' % (test, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print '2015-9-1'
# which is equal to now = log('execute')(now)

# partial function
# to fix some parameter of a function and return a new function
import functools
int2 = functools.partial(int, base = 2)
int2('1000000')
# 64
# int2 just fix base, and you can send other parameter to it
int2('1000000', base = 10)
# 1000000
# when creating partial function we can also send function, *args, **kw
int2 = functools.partial(int, base = 2)
# which means
int2('10010')
# is equal to 
kw = { base: 2 }
int('10010', **kw)
max2 = functools.partial(max, 10)
# it will add 10 as a part of *args to the left
max2(5, 6, 7)
# is equal to
args = (10, 5, 6, 7)
max(*args)

