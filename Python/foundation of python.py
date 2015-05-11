# IO : print and raw_input()
name = raw_input('Please enter your name : ')
print 'hello,', name

# Python can deal with integers how ever big they are

# float is nothing new

# string is surrounded by "" or ''
# multi-lines string 
print '''line
... line
... line '''

# boolean is True, False
# and or not instead of &&, ||, !

# None

# variable don't have to be declared

# Origin string 'abc' is in ASCII in Python
# To express Unicode, use u'xxx'
print u'中文'

# convent Unicode to UTF-8
u'ABC'.encode('utf-8')

# len() returns the length of the string
len(u'abc')

# convent string in utf-8 to Unicode
'abc'.decode('utf-8')

# format output %d %f %s %x
'Hello, %s' % 'world'
'Hi, %s, you have $%d' % ('Michael', 100000)

# can esacap % by %%

# Build-in data structrue list, like ArrayList
classmates = ['Michael', 'Bob', 'Tracy']
# You can append in list
classmates.append('Adam')
# You can insert in list
classmates.insert(1, 'Jack')
# delete is pop(i) in list, default pop()
# deletes the last element in list
classmates.pop()
classmates.pop(2)
# elements in list can be different datat type
s = ['python', 'java', ['asp', 'php'], 'scheme']
len(s)

# Build-in data structrue tuple, like Array
t = (1, 2)
t = (1,)
t=(1)		# different from t = (1,)
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'

# elif is else if
age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'

# for in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

sumx = 0
for x in range(101):
    sumx = sumx + x
print sumx

# raw_input() always return as string
birth = int(raw_input('birth: '))

# dictionary in Python like map in java
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

'Thomas' in d 		# d.hasKey('Thomas')
d.get('Thomas')		# if key doesn't exist, return None
d.pop('Bob')		# delete key-value

# set as usual
s = set([1, 2, 3])
s.add(4)
s.remove(4)

# Union and intersection
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s3 = s1 & s2
s4 = s1 | s2

