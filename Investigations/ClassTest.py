class IterPerson(type):
    def __iter__(cls):
        return iter(cls._allPeople)


class Person(metaclass=IterPerson):
    _allPeople = {}

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person._allPeople[self._key()] = self

    def _key(self):
        return self.name

    def __del__(self):
        try:
            del Person._allPeople[self._key()]
            print("Destructor called")
        except:
            print(self.name)


if __name__ == '__main__':
    Jeff = Person("Jeff", 20, "1.6")
    Bob = Person("Bob", 39, "1.4")
    Helen = Person("Helen", 19, "1.3")

    del Helen

#    for person in Person:
#        print(person.name + " is " + str(person.age))

    print(Person._allPeople)

    print(Helen)

    input('alors?')