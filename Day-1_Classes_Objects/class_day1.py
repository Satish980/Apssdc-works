'''class simple:
         a = 10
         def hi():
                  print('welcome to apssdc')
                  return'''

#addition operation

'''class simple:
         print('operations')

         def add():
                  a = 10
                  b = 20

                  return ('addtion of 2 numbers',a+b)'''

#Dynamic variables

'''class simple:
         print('Arithmetic oprations')

         def add(a,b):
                  return ('a+b',a+b)


a = int(input("a: "))
b = int(input("b: "))
obj = simple.add(a,b)
print(obj)
print(simple.add(a,b))'''

# objects

'''class hello:
         data = "welcome to apssdc"

         def hii():
                  return ('good')

obj = hello

print(obj)
print(dir(obj))

print(obj.data)
print(obj.hii())'''

# non-parametrized constructor
class hello:
         def __init__(self):
                  print('Non-Parametrized')

         def show(self,name):
                  return ('welcome',name)

obj = hello()
print(obj.show('Friend'))
                  
                  
