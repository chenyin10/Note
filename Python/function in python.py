# data type convention
int('123')
str(1.23)
unicode(100)

# name of funtion is actually a reference to the function object
# you can assign the name to a variable
# just to have another for the function
a = abs
a(-1)

# define a function
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

# empty function
def nop():
	pass

# type check
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

# return several values
# just an illusion
# it returns a tuple
import math

def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
x, y = move(100, 100, 60, math.pi / 6)     # pay attention
print x, y
r = move(100, 100, 60, math.pi / 6)
print r

# without return, function returns None

# default parameter
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# a trap in default parameter
def add_end(L=[]):
    L.append('END')
    return L
# each time you use add_end
# L has memory
# so, default parameter must be const object
# revise the code
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# varying parameter
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# with *, inside the function, it recieves a tuple
cal(1, 2, 3)

# you can add * before list or tuple to make them
# as varying parameter into a function
num = [1, 2, 3]
calc(*num)

# keyword parameter
# it is quite same as varying parameter 
# except for it will become dictionary
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
person('Michael', 30)
person('Bob', 35, city='Beijing')
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)

# the order of all parameters in a function 
# is important
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

# for evry function, you can use it by form like
# func(*args, **kw)
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)