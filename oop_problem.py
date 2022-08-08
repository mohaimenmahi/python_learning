class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} talks")


name = input("> ")
person1 = Person(name)
person1.talk()

name2 = input("> ")
person2 = Person(name2)
person2.talk()
        