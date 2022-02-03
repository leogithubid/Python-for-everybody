#fruit
fruit = 'banana'
#loop through and iterate
for letter in fruit:
    print(letter)
#substring
print(fruit[2:])
#in operator
print('m' in fruit)
print('n' in fruit)
if ('n' in fruit):
    print('yes')
# string operations
print(dir(fruit))
print(fruit.capitalize())
print(fruit.upper())
#quiz - I wrote them in the terminal
""" >>> str1 = "Hello"
>>> str2 = 'there'
>>> bob = str1 + str2
>>> print(bob)
Hellothere
>>> x = '40'
>>> y = int(x) + 2
>>> print(y)
42
>>> x = 'From marquard@uct.ac.za'
>>> 
>>> print(x[7])
r
>>> 
>>> print(x[8])
q
>>> x = 'From marquard@uct.ac.za'
>>> print(x[14:17])
uct
>>> 
>>> print(x[15:18])
ct.
>>> print(len('banana')*7)
42
>>> greet = 'Hello Bob'
>>> print(greet.upper())
HELLO BOB
>>> data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> pos = data.find('.')
>>> print(data[pos:pos+3])
.ma
>>>  """