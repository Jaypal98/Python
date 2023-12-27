Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 2.5
>>> type(num)
<class 'float'>
>>> num = 5
>>> type(num)
<class 'int'>
>>> num = 6+9j
>>> type(num)
<class 'complex'>
>>> a = 5.6
>>> b = int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> k = float(b)
>>> b
5
>>> k = float(b)
>>> k
5.0
>>> c = complex(b,k)
>>> c
(5+5j)
>>> b<k
False
>>> B<=k
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    B<=k
NameError: name 'B' is not defined
>>> b<=k
True
>>> b>=k
True
>>> b=k
>>> b==k
True
>>> int(True)
1
>>> int(False)
0
>>> lst = [25,36,14,26]
>>> type(lst)
<class 'list'>
>>> s = {25,36,14,25}
>>> s
{25, 36, 14}
>>> type(s)
<class 'set'>
>>> t = (25,36,4,57,12)
>>> type(t)
<class 'tuple'>
>>> str = "navin"
>>> st = 'a'
>>> type(st)
<class 'str'>
>>> type(str)
<class 'str'>
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> type(range(10))
<class 'range'>
>>> d = {}
>>> d = {'navin' : 'samsung','rahul':'Iphone','Kiran':'oneplus'}
>>> d
{'navin': 'samsung', 'rahul': 'Iphone', 'Kiran': 'oneplus'}
>>> d.keys()
dict_keys(['navin', 'rahul', 'Kiran'])
>>> d.values()
dict_values(['samsung', 'Iphone', 'oneplus'])
>>> d['rahul']
'Iphone'
>>> d.get('kiran')
>>> d.get('Kiran')
'oneplus'
>>> 