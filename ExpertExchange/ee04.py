import datetime
import json
import ctypes
import uuid

print(uuid.uuid4())
print(uuid.uuid4())
print(uuid.uuid4())
print(uuid.uuid4())
print(uuid.uuid4())
print(uuid.uuid4())


def time_this(original_function):
    def new_function(*args, **kwargs):
        import datetime
        before = datetime.datetime.now()
        x = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print("Elapsed Time = {0}".format(after - before))
        return x
    return new_function


class Toto:
    def __init__(self, name):
        self.name = name


class Person:
    index = {}

    def __new__(cls, name, surname, birthdate, address, telephone, email, toto):
        if name:
            return super(Person, cls).__new__(cls)
        else:
            raise ValueError

    def __init__(self, name, surname, birthdate, address, telephone, email, toto):

        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self.toto = toto


    def age(self):
        today = datetime.date.today()
        birth = datetime.date.fromisoformat(self.birthdate)
        age = today.year - birth.year

        if today < datetime.date(today.year, birth.month, birth.day):
            age -= 1

        return age


@time_this
def convert_to_dict(obj):
    """
    A function takes in a custom object and returns a dictionary representation of the object.
    This dict representation includes meta data such as the object's module and class names.
    """

    #  Populate the dictionary with object meta data
    obj_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }

    #  Populate the dictionary with object properties
    # obj_dict.update(obj.__dict__)
    for k, v in obj.__dict__.items():
        if hasattr(v, '__dict__'):
            obj_dict[k] = convert_to_dict(v)
        else:
            obj_dict[k] = v

    return obj_dict

# ♣ ♢ ♡ ♠


@time_this
def dict_to_obj(our_dict):
    """
    Function that takes in a dict and returns a custom object associated with the dict.
    This function makes use of the "__module__" and "__class__" metadata in the dictionary
    to know which object type to create.
    """
    if "__class__" in our_dict:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = our_dict.pop("__class__")

        # Get the module name from the dict and import it
        module_name = our_dict.pop("__module__")

        # We use the built in __import__ function since the module name is not yet known at runtime
        module = __import__(module_name)

        # Get the class from the module
        class_ = getattr(module, class_name)

        # Use dictionary unpacking to initialize the object
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj


@time_this
def func_a(stuff):
    import time
    time.sleep(3)

func_a(1)
exit(0)


func_a(1)
#strange = Toto('Kasimir')

person = Person(
    "Jane",
    "Doe",
    datetime.date(1961, 8, 11).isoformat(),
    "No. 12 Short Street, Greenville",
    33.0676429876,
    "jane.doe@example.com",
    None
)


print(person.__dict__)


toto = json.dumps(person, default=convert_to_dict, indent=4, sort_keys=True)

print(toto)
#toto = convert_to_dict(person)
#print(json.dumps(toto, indent=4, sort_keys=True))

new_object = json.loads(toto, object_hook=dict_to_obj)

print(new_object.__hash__())
print(person.__hash__())

#print(hex(id(person)))
#print(ctypes.cast(id(person), ctypes.py_object).value)

print(json.dumps(new_object, default=convert_to_dict, indent=4, sort_keys=True))


print(person.toto)
print(new_object.toto)


