import pytest


class Person:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        return self.name == other.name


# Case 1
# def test_classes_compare():
    # p1 = Person("Xiomara")
    # p2 = Person("Jacinto")
    # assert p1.name == p2.name


# Case 2
    # p3 = Person("Fidencio")
    # p4 = Person("Fidencio")
    # assert p3.name == p4.name


# Case 3
def test_classes_compare():
    p1 = Person("Amanda")
    p2 = Person("Amanda")
    assert p1==p2


# Compares two instances of the Person class, name is positional argument.

### Case 1 
# AssertionError: assert 'Xiomara' == 'Jacinto' 
    # Test fails

### Case 2 
# No AssertionErrors, test passed 

### Case 3 - Function outside class created for assert statement

# There is a way to update Person class def to pass Assertion test in this format 
    # using __eq__() method in the Person class, equality logic for comparing two objects