Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 20*2
40
>>> 20**2
400
>>> 30*2
60
>>> 30**2
900
>>> x=2
>>> x+3
5
>>> y = 3
>>> x+y
5
>>> x+y
5
>>> x
2
>>> x=9
>>> x+y
12
>>> x
9
>>> _+y
12
>>> y
3
>>> name= 'youtube'
>>> name
'youtube'
>>> name+'rocks'
'youtuberocks'
>>> name+' youtube '
'youtube youtube '
>>> name = ' rocks'
>>> name[0]
' '
>>> name[1,2]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    name[1,2]
TypeError: string indices must be integers
>>> name[2]
'o'
>>> name[-1]
's'
>>> name[0:2]
' r'
>>> name[0:3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> name[0:3]
' ro'
>>> name[-5]
'r'
>>> name[1:4}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> name[1:4]
'roc'
>>> name[1:]
'rocks'
>>> my + name[3:]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    my + name[3:]
NameError: name 'my' is not defined
>>> 'my'+ name[3:]
'mycks'
>>> 'my '+name[3:]
'my cks'
>>> name = "jaypal"
>>> len(name)
6
>>> nums[25,12,36,95,14]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    nums[25,12,36,95,14]
NameError: name 'nums' is not defined
>>> nums = [25,12,36,95,14]
>>> nums
[25, 12, 36, 95, 14]
>>> nums[4]
14
>>> nums[2:]
[36, 95, 14]
>>> nums[-2:-4]
[]
>>> nums[-1]
14
>>> nums[-4:-2]
[12, 36]
>>> names = ['jp' ,'kiran','john']
>>> names
['jp', 'kiran', 'john']
>>> values = [9.5,'navin',25]
>>> mil = [nums,names]
>>> mil
[[25, 12, 36, 95, 14], ['jp', 'kiran', 'john']]
>>> mums.append(45)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    mums.append(45)
NameError: name 'mums' is not defined
>>> nums
[25, 12, 36, 95, 14]
>>> nums.append(45)
>>> nums
[25, 12, 36, 95, 14, 45]
>>> 
>>> 
>>> 


>>> 
>>> 


>>> 
>>> 

>>> 

>>> 

>>> 
>>> 


>>> 

>>> nums.insert(2,77)
>>> nums
[25, 12, 77, 36, 95, 14, 45]
>>> nums.remove(14)
>>> nums
[25, 12, 77, 36, 95, 45]
>>> nums.pop(1)
12
>>> nums
[25, 77, 36, 95, 45]
>>> nums.pop()
45
>>> nums
[25, 77, 36, 95]
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend([29,12,14,36])
>>> nums
[25, 77, 29, 12, 14, 36]
>>> min(nums)
12
>>> max(nums)
77
>>> sum(nums)
193
>>> nums.sort()
>>> nums
[12, 14, 25, 29, 36, 77]
>>> 