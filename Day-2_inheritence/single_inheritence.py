# single level inheritence
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

obj = classB
print(obj.c)
print(obj.a)
print(obj.method1())
