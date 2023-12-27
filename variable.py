Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 5
>>> id(num)
2169488763312
>>> nae = 'navjot'
>>> name = 'navjot'
>>> id(name)
2169530197552
>>> a = 10
>>> b = a
>>> a
10
>>> b
10
>>> id(a)
2169488763472
>>> id(b)
2169488763472
>>> id(a)
2169488763472
>>> a = 9
>>> id(a)
2169488763440
>>> b = 8
>>> id(b)
2169488763408
>>> PI 