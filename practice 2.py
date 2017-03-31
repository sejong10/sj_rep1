Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Professor = "JinJin"
>>> print Professor
JinJin
>>> print if
SyntaxError: invalid syntax
>>> if = "JinJin"
SyntaxError: invalid syntax
>>> print"12'
SyntaxError: EOL while scanning string literal
>>> print12

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print12
NameError: name 'print12' is not defined
>>> print 12
12
>>> print "12+34"
12+34
>>> print 12+34
46
>>> First =7
>>> Second=8
>>> print First, Second, First+Second, First * Second
7 8 15 56
>>> Result = First - Second
>>> print Result
-1
>>> Another =Result
>>> print Another
-1
>>> print Result
-1
>>> Another = Anoter +10

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    Another = Anoter +10
NameError: name 'Anoter' is not defined
>>> Another = Another + 10
>>> print Another
9
>>> print Result
-1
>>> student_name = "Michel Foucault"
>>> survey-answer = "Nop!"
SyntaxError: can't assign to operator
>>> YourAnswer = "Yes"
>>> _my_cart = "full of stuff"
>>> 2017resolution = "Stop smoking"
SyntaxError: invalid syntax
>>> Title of Movie = "LA LA LAND"
SyntaxError: invalid syntax
>>> Total_number! = 300
SyntaxError: invalid syntax
>>> Width&Height = 30*10
SyntaxError: can't assign to operator
>>> Width&Height = 30 * 10
SyntaxError: can't assign to operator
>>> End... = "Happy ending"
SyntaxError: invalid syntax
>>> RIghtAnswer?="BIngo"
SyntaxError: invalid syntax
>>> FIrst = 10
>>> Second = 20
>>> First + Second
27
>>> First = '10'
>>> Second = '20'
>>> First + Second
'1020'
>>> Longstring = "I am a student. I have been enjoying my campus life.
SyntaxError: EOL while scanning string literal
>>> Longstring = """I am a student.
I have been enjoying my campus life.
I'm majoring in English Literature.
I'm learning programming language called Python."""
>>> print Longstring
I am a student.
I have been enjoying my campus life.
I'm majoring in English Literature.
I'm learning programming language called Python.
>>> a='10'
>>> b=10
>>> c=10.0
>>> type(a)
<type 'str'>
>>> type(b)
<type 'int'>
>>> type(c)
<type 'float'>
>>> a=10
>>> b=float(a)
>>> a
10
>>> b
10.0
>>> c=12.1
>>> d= int(c)
>>> c
12.1
>>> d
12
>>> e=12.9
>>> f=int(e)
>>> e
12.9
>>> f
12
>>> print int('23')
23
>>> print int('012')
12
>>> print int('JinJin')

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print int('JinJin')
ValueError: invalid literal for int() with base 10: 'JinJin'
>>> print float('JinJin')

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print float('JinJin')
ValueError: could not convert string to float: JinJin
>>> print str(23)
23
>>> print str('23')
23
>>> print str('23.01')
23.01
>>> print type(str(int('007')))
<type 'str'>
>>> 
