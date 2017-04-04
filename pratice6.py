Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import easygui
>>> easygui.msgbox('This is a basic message box','Title Goes Here')
'OK'
>>> import easygui
>>> user_response=easygui.msgbox('This is a basic message box.','Title Goes Here')
>>> print user_response
OK
>>> import easygui
>>> easygui.buttonbox('Click on your favorite flavor.','Favorite Flavor',('Chocolate','Vanilla','Strawberry'))
'Chocolate'
>>> import easygui
>>> user_response = easygui.buttonbox('Click on your favorite flavor.','Favorite Flavor', ('Chocolate','Vanilla','Strawberry'))
>>> print user_response
Strawberry
>>> import easygui
>>> user_response = easygui.buttonbox('Click what you like.','Favorite color',('yellow','green','white','red','blue','black'))
>>> print user_response
white
>>> import easygui
>>> flavor = easygui.choicebox('What is your favorite flavor.',choices=['Chocolate','Vanilla','Strawberry'])
>>> easygui.msgbox('You picked ' + flavor)
'OK'
>>> 
=============== RESTART: C:/Users/yuu/Desktop/NumGuessGame.py ===============
>>> import easygui
>>> flavor = easygui.choicebox('What is your favorite flavor.',choices = ['Chocolate','Vanilla','Strawberry'])
>>> easygui.msgbox('You picked ' +flavor)
'OK'
>>> 
