class classA:
         a = 10
         b = 20

         def method1():
                  return "ClassA"

class classB(classA):
         c = 30
         d = 40

         def method2():
                  return "i'm from class B"
class classC(classB):
         e = 50
         f = 60

         def method3():
                  return "class C"

obj = classC
print(obj.c)
print(obj.method3())
print(obj.method2())
print(obj.method1())
