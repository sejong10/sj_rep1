Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print "Hello Sejong!"
Hello Sejong!
>>> print 2*3
6
>>> print 2+3*4
14
>>> print 2+3-4-5
-4
>>> print 2+3*4-5
9
>>> print 12345678901234567890 * 98765432109876543210
1219326311370217952237463801111263526900
>>> print "cat" + "dog"
catdog
>>> print "Love"*20
LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
>>> print "hello again" + 1

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print "hello again" + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> print 'Hello Sejong'
Hello Sejong
>>> print " I love pizza!"
 I love pizza!
>>> print "pizza"*20
pizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizza
>>> print "yum" * 40
yumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyumyum
>>> print "I'm full"
I'm full
>>> import random
secret = random.randint(1, 99)     
guess = 0
tries = 0
print "AHOY!  I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99.  I'll give you 6 tries. "

while guess != secret and tries < 6:                
    guess = input("What's yer guess? ")  
    if guess < secret:
        print "Too low, ye scurvy dog!"
    elif guess > secret:
        print "Too high, landlubber!"

    tries = tries + 1                      

if guess == secret:                        
    print "Avast! Ye got it!  Found my secret, ye did!"
else:
    print "No more guesses!  Better luck next time, matey!"
    print "The secret number was", secret
    
>>> professor = "JinJin"
>>> print professor
JinJin
>>> print if
SyntaxError: invalid syntax
>>> if = "JinJin"
SyntaxError: invalid syntax
>>> print "12"
12
>>> print 12
12
>>> print "12 + 34"
12 + 34
>>> print 12 + 34
46
>>> First = 7
>>> Second = 8
>>> print First, Second, First + Second,First * Second
7 8 15 56
>>> Result = First - Second
>>> print Result
-1
>>> Another = Result
>>> print Another
-1
>>> Another = Another + 10
>>> print Another
9
>>> print Result
-1
>>> First = 10
>>> Second = 20
>>> First + Second
30
>>> Longstring = """I am a student. 
I have been enjoying my campus life.
I'm majoring in English Literature.
I'm learning programming language called Python."""
>>> print Longstring
I am a student. 
I have been enjoying my campus life.
I'm majoring in English Literature.
I'm learning programming language called Python.
>>> a = '10'
>>> b = 10
>>> c = 10.0
>>> type(a)
<type 'str'>
>>> type(b)
<type 'int'>
>>> type(c)
<type 'float'>
>>> a = 10
>>> b = float(a)
>>> a
10
>>> b
10.0
>>> c=12.1
>>> d = int(c)
>>> c
12.1
>>> e = 12.9
>>> f = int(e)
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
  File "<pyshell#57>", line 1, in <module>
    print int('JinJin')
ValueError: invalid literal for int() with base 10: 'JinJin'
>>> print float('JinJin')

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print float('JinJin')
ValueError: could not convert string to float: JinJin
>>> print str(23)
23
>>> print str('23')
23
>>> print str(23.01')
	  
SyntaxError: EOL while scanning string literal
>>> print str('23.01')
23.01
>>> print type(str(int('007')))
<type 'str'>
>>> 
