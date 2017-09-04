# encoding=utf-8

#  a = {'a':"xixi",'d':'hehe','b':'hoho','e':'gigi'}
#
#  for x,y in a.items():
#      print x,y
#
#
#  l = list(a.items())
#  print l
#  l.sort(key=lambda x:x[0])
#  print l
#
#  print a.values()
#  print a.keys()
#  print a.items()
#

#演示翻译表 translate table
import string
table = string.maketrans('wek','*$@')
a = 'dlsetmdljiwerelbafdflkdsfisaslf'
b = a.translate(table,'fga')
print a,'\n',b



