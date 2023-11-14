class Person:
    def __init__(self, name): # method is run as soon as an object is instantiated(i.e. created)
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Noble')
p.say_hi()

# Person('Noble').say_hi()