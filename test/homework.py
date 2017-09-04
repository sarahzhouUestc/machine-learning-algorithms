# encoding=utf-8

#请将字符串的小写字符改成大写，大写字符改成小写
a = "fdALDFssAsdweEJLDM2fd88fdEW,CNVeowljs"
#  #  print a.swapcase()
#
#  print ''.join([x for x in a if x.isdigit()])
#
#  print [type(x) for x in a if x.isdigit()]
#
#  #统计每个字符出现的次数，生成字典
#  print dict([(x,a.count(x)) for x in a])
#
#  #对字符换去重，保留原来的顺序
#  c = set(a)
#  d = list(c)
#  d.sort(key=a.index)
#  print d
#
#  print "========================"
#  print list(set(a)).sort(key=a.index)
#
#
#  #将字符串反转
#  print a
#  print "-------------------------------"
#  print a[::-1]
#  f = list(a)
#  f.reverse()
#  print str(f)
#
#  print a[::-1]


#去除字符串的数字，并且将剩余的字符排序，AaBb
#  print "\n------------------------\n"
#  print a
#  b = [x for x in a if x.isalpha()]
#  print b
#  lower_alpha = set([x for x in b if x.islower()])
#  upper_alpha = set([x for x in b if x.isupper()])
#  lower_alpha_list = list(lower_alpha)
#  upper_alpha_list = list(upper_alpha)
#  lower_alpha_list.sort()
#  upper_alpha_list.sort()
#  print lower_alpha_list
#  print upper_alpha_list
#
#  #判断boy每个字母是不是都出现在a中
#  u = set(a)
#  a_len = len(u)
#  u.update('boy')
#  b_len = len(u)
#  print a_len
#  print b_len
#  if a_len == b_len:
#      print 'The original string contains "boy" sub string'
#  else:
#      print 'The original string does not contain "boy" sub string'
#


#输出a中输出频率最高的字符
#  b = [(x,a.count(x)) for x in set(a)]
#  print b
#  b.sort(key=lambda x:x[1],reverse=True)
#  print b
#  max_count = b[0][1]
#  for x in b:
#      if x[1] == max_count:
#          print x[0]
#      else:
#          break

#输入import os之后出现的文档里，统计出现be is than的次数
#  import os
#  m = os.popen('python -m this').read()
#  m = m.replace('\n','')
#  m = m.split(' ')
#  n = [(x,m.count(x)) for x in ['be','is','than']]
#  print n

#计算102324123499123的kb和mb的大小
#  b = 102324123499123
#  print "%s kb" % (b >> 10)
#  print "%s mb" % (b >> 20)
#

#请计算[1,2,3,6,8,9,10,14,17]转换为字符串
c = [1,2,3,6,8,9,10,14,17]
print str(c)
d = str(c)
print d[1:-1]
print d[1:-1].replace(', ','')








