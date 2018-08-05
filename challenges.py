Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> >>> x,y,z = (3,4,5)
>>> my_tuple = (3,4,5)
print (x+y+z)
SyntaxError: invalid syntax
>>> x,y,z = (3,4,5)
>>> my_tuple = (3,4,5)
SyntaxError: multiple statements found while compiling a single statement
>>> x,y,z = (3,4,5)
>>> my_tuple = (3,4,5)
>>> print (x+y+z)
12
>>> print(my_tuple+my_tuple)
(3, 4, 5, 3, 4, 5)
>>> print(x*3)
9
>>> print(my_tuple*3)
(3, 4, 5, 3, 4, 5, 3, 4, 5)
>>> print(my_tuple[0]==x)
True
>>> print(x[0])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(x[0])
TypeError: 'int' object is not subscriptable
>>> my_tuple[0]=17
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    my_tuple[0]=17
TypeError: 'tuple' object does not support item assignment
>>> my_tuple[0]=17

>>> print(my_tuple)
SyntaxError: multiple statements found while compiling a single statement
>>> my_tuple[0]=17
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    my_tuple[0]=17
TypeError: 'tuple' object does not support item assignment
>>> print(my_tuple)
(3, 4, 5)
>>> x=17
>>> print (x)
17
>>> 
======================== RESTART: /home/student/rt.py ========================
type a number 1
Traceback (most recent call last):
  File "/home/student/rt.py", line 3, in <module>
    if count % 3 == 0 and count % 5 == 0 :
TypeError: not all arguments converted during string formatting
>>> 
======================== RESTART: /home/student/rt.py ========================
type all the numbers by these laws If a number is divisible by 3, instead of printing the number, print "fizz"!  If a   number is divisible by 5, instead of printing the number, print "buzz"! If it is divisible by 5 and 3, print "fizzbuzz"!
======================== RESTART: /home/student/rt.py ========================
