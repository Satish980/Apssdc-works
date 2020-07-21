class classA:
         a = 10
         b = 20

         def method1():
                  return "ClassA"

class classB:
         c = 30
         d = 40

         def method2():
                  return "i'm from class B"
class classC(classA):
         e = 50
         f = 60

         def method3():
                  return "class C"
         def method2():
                  return "i'm from class C"

class classD(classC,classB):
         x,y = 30,40
         def method4():
                  return "class D"
         
obj = classD
print(obj.c)
print(obj.method3())
print(obj.method2())
print(obj.method1())
print(obj.method4())
