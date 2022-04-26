class ParentClass:
    def printHello(self):
        print('Hello, World!')

class ChildClass(ParentClass):
    def someNewMethod(self):
        print('ParentClass objects dont have this method.')

class GrandchildClass(ChildClass):
    def anotherNewMethod(self):
        print('Only GrandchildClass objects have this metod.')

print('Create a ParentClass object adn call its methods:')
parent = ParentClass()
parent.printHello()

print('Create a ChildClass object and call its methods:\n')
child = ChildClass()
child.printHello()
child.someNewMethod()

print('Create a GrandchildClass object adn call its methods:\n')
grandchild = GrandchildClass()
grandchild.printHello()
grandchild.someNewMethod()
grandchild.anotherNewMethod()

print('\nAn error:')
parent.someNewMethod()
