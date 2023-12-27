Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = {1:'Navin',2:'Kiran',4:'Harsh'}
>>> data
{1: 'Navin', 2: 'Kiran', 4: 'Harsh'}
>>> data[4]
'Harsh'
>>> data[1]
'Navin'
>>> data.get(1)
'Navin'
>>> data.get(3)
>>> print(data.get(3))
None
>>> data.get(1,'not found')'
SyntaxError: EOL while scanning string literal
>>> data.get(1,'not found')
'Navin'
>>> data.get(3,'not found')
'not found'
>>> keys = ['Navin','Kiran','Harsh']
>>> values = ['python','Java','Js']
>>> data = zip(keys,values)
>>> data
<zip object at 0x00000237EC1B9440>
>>> data = di(zip(keys,values))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    data = di(zip(keys,values))
NameError: name 'di' is not defined
>>> data = dict(zip(keys,values))
>>> data
{'Navin': 'python', 'Kiran': 'Java', 'Harsh': 'Js'}
>>> data[kiran]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data[kiran]
NameError: name 'kiran' is not defined
>>> data['kiran']
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    data['kiran']
KeyError: 'kiran'
>>> data['Kiran']
'Java'
>>> data['Monika'] = 'CS'
>>> data
{'Navin': 'python', 'Kiran': 'Java', 'Harsh': 'Js', 'Monika': 'CS'}
>>> del data['Harsh']
>>> data
{'Navin': 'python', 'Kiran': 'Java', 'Monika': 'CS'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> prog = {'JS':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
>>> 
>>> prog
{'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
>>> prog['JS']
'Atom'
>>> prog['python']
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    prog['python']
KeyError: 'python'
>>> prog['Python']
['Pycharm', 'Sublime']
>>> prog['Python'][1]
'Sublime'
>>> prog['Java']
{'JSE': 'Netbeans', 'JEE': 'Eclipse'}
>>> prog['Java'][2]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    prog['Java'][2]
KeyError: 2
>>> prog['Java']['JEE']
'Eclipse'
>>> 