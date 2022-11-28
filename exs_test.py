class Mixin:
    attr = 0
    def mixin_method(self):
        print("Mixin method")


class Class1(Mixin):
    def method1(self):
        print("Class1 method")

class Class2(Class1, Mixin):
    def method2(self):
        print("Class2 method")


c1 = Class1()
c1.method1()
c1.mixin_method()
print()

c2 = Class2()
c2.method2()
c2.method1()
c2.mixin_method()