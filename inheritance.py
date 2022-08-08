class Mamal:
    def walk(self):
        print("walk")


class Dog(Mamal):
    def bark(self):
        print("Bark")


class Cat(Mamal):
    def annoying(self):
        print("Be Annoying")


dog1 = Dog()
cat1 = Cat()

dog1.walk()
dog1.bark()

cat1.walk()
cat1.annoying()