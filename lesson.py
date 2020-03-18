class Person(object):
    def __init__(self, name, hobby = 'car'):
        self.name = name
        self.hobby = hobby

    def say_something(self):
        print('I am {}. hello'.format(self.name))

# person = Person(name = 'Mike')
# person.say_something()

class People(object):
    def __init__(self, age=1):
        self.age = age
    
    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

class Baby(People):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)　#people(親クラス)のコンストラクタにage(1)を渡す
        else:
            raise ValueError

class Adult(People):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age) #people(親クラス)のコンストラクタにage(18)を渡す
        else:
            raise ValueError

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, people):
        people.drive()

car = Car()
car.ride(adult) #adultは親クラスPeopleのメソッドが使える(継承)