### Object Oriented Programming (OOP)

  - Object definition: An object is an instance of a class
    - For example, `str` is not an object, but in `word = 'hi'` word is an object (an instance of the `str` class)
    - Objects use allocated memory
    - A physically entity (digitally). You can't hold it, but an object is a thing. A class is an idea for how to make an object.
    - Characteristic/Attributes objects have
      - Identity
        - Each object has its own identity, such as a memory address. Two variables may reference the same object, but the identity is the memory address of the object.
      - State
        - The state is all the attributes of the object with values assigned to them. Such as a plane object having a fuel object. Anytime you change the fuel object, you change the plane object's state.
      - Behavior
        - Example: \_\_eq\_\_ method in `str`.
        - Always use behavior to access state (getter and setters), don't access directly.
  - Class definition: A class is the code that instructs a program how a particular object should be built.
    - A class is used to create many objects.
  - OOP Characteristics:
    - Encapsulation
      - Class, variable, getter, and setter all in one thing.
    ```
    class Cookie:
      def __init__(self):
        self.flavor = flavor

      def get_flavor(self):
        return self.flavor

      def set_flavor(self, flavor):
        self.flavor = flavor
    ```
    - Abstraction (user interface vs private interface)
      - `.sort()` does stuff, you make it easy, and you don't care how it does it (as long as it's reasonably efficient).
    - Inheritance
      - is-a relationship
      - Ferrari is-a Car
        - Can use methods of parent class, such as `__str__`, and add on to it with its own `__str__`.
    - Polymorphism
      - Always used with inheritance.
      - Overriding a parent class's method with a different method with different or extra functionality.
        - In the Ferrari class, `__str__()` overrides the Car `__str__()`, and can provide extra functionality, such as multiplying the cost to repair because it's a Ferrari.

### Classes 
- Magic methods (also called dunder methods) (override methods): 
  - If: `__eq__(), __gt__(), __ge__(), __lt__(), __le__(), __and__(), __or__()`
  - Math `__add__(), __abs__(), __ceil__(), __sub__(), __mod__(), __mul__(), __round__(), __floordiv__()`
- Make vars private by adding '__' to the beginning of the variable name
  - getters and setters are good, or you can make @property, @var_name.setter, etc functions
  ```
  # Acts as a getter, but is used for class_name.color
  @property
  def color(self):
    return self.__color
  
  @color.setter
  def color(self, value):
    self.color = value
  ```
- Inheritance
  - How to make inheritance in Python: `class Dog(Pet):  # Dog inherits from Pet`
  - Basic explanation of inheritance in OOP section.
- Arbitrary parameters
  - Arbitrary num of parameters for a function/method
  - Can use `*args` or `**kwargs` to get a tuple or dict with an arbitrary length
  - Variable name doesn't actually matter those names are standard, just number of asterisks *. 1 for tuple, 2 for dict.
  - Example:
```
def custom_sum(*args):
    total = 0
    for num in args:
        total += num
    return total
print(custom_sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
```
