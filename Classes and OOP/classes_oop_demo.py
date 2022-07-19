from dog import Dog  # Imports class from other python file (dog.py)
from cat import Cat

# dog1 and dog2 are variables holding reference to instance of Dog in heap
dog1 = Dog(color='blue')
dog2 = Dog(weight=15.7)
dog3 = Dog(breed='beagle', weight=15.7)

# Calls __str__()
print(dog1)
print(dog2)

# Calls __eq__()
print(dog1 == dog2)

# Also calls __eq__()
print(dog1 != dog2)

dog1.name = 'snow'
print(dog1.color)

dog1.name = 'light'
print(dog1.color)

# Is type "class '__main__.Dog'"
print(type(dog1), type(dog2))

# You can do these, but you shouldn't. It's not good for OOP
# Commenting out because it's a mess
# dog1.breath = 'bad'
# print(dog1.breath)
# for attribute in dir(dog1):
#     print(f'{attribute}: {dog1.__getattribute__(attribute)}')

num1 = 42
num2 = 99
if num1 == num2:
    print('Equal')
else:
    print('Not equal')

print(dog2)
print(dog3)

print(dog2 == dog3)

dog1.do_something(item='newspaper')

# Cat
print()
cat1 = Cat(color='heliotrope')
print(cat1)
cat1.laser()
cat1.make_noise()
print()


# Other stuff
def get_full_name(*args):  # Can be any name, as long as it starts with *.
    full_name = ''
    for name in args:
        full_name += name + ' '
    return full_name[:-1]


print(get_full_name('super', 'cali', 'fragilistic', 'expialidocious'))
