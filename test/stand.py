 --*-- coding=UTF-8 --*--
import sys


if __name__ == '__main__':
    sys.path.append('/home/sarahzhou/pythontest')

print '=====contract======='
import contract
print contract.__doc__
print contract.name
print contract.hello()
