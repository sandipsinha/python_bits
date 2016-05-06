##class Human(object):
##    def __setattr__(self,name,value):
##        if name == 'sex':
##            if value in ('male','female'):
##                print 'I am here', value
##                self.sex = value
##            else:
##                raise AttributeError('Sex can only be male or female')
##
##
##b=Human()
##b.name='Mary'
##b.sex='female'
##print b.sex
##class A:
##    brothers=[]
##    def __init__(self,name):
##        self.name=name
##
##a=A('Richard')
##b=A('Eily')
##a.brothers.append('John')
##print a.name,a.brothers,b.name, b.brothers, id(a), id(b)

##import copy
##class A(object):
##    pass
##
##a=A()
##a.lst=[1,2,3]
##a.str='cats and dogs'
##b=copy.copy(a)
##a.lst.append(100)
##a.str='cats and mices'
##print b.lst
##print b.str
import random
##def func(type='s'):
##    if type == 's':
##        return 'Mark'
##    elif type == 'i':
##        return random.randint(0,1000)
##def dec(func,type_):
##    x = 8
##    def wrapper():
##        value=func(type_)
##        if isinstance(value,int):
##            return value * x
##        elif isinstance(value,basestring):
##            return 'Hi' + value
##    return wrapper
class A(object):
    def calc(self):
        return 7
    
class B(object):
    def calc(self):
        return 6
    
class C(A,B):
    pass

c=C()
print c.calc()

#print c(func,'i')()
