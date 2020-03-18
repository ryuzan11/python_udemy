class Person(object):
    def __init__(self, name, hobby = 'car'):
        self.name = name
        self.hobby = hobby

    def say_something(self):
        print('I am {}. hello'.format(self.name))

person = Person(name = 'Mike')
person.say_something()