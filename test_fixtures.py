import pytest 


# Marked to pytest as a fixture function
@pytest.fixture
def data_set():
    return (-111, -33.3, -5, 0, 0.67, 12, 25.02, 100, 'abc')

# Exercise 1 # add together all the positive numbers in an iterable, and return the total

def positive_numbers_sum(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total


# # Exercise 2 # Test function that includes fixture function data set in the parameter

def test_positive_numbers_sum(data_set):
    assert positive_numbers_sum(data_set) == 147.69


# Test function #
# running 'pytest test_fixtures.py' in git bash folder

# Test FAILED # Why? 
# TypeError: '>' not supported between instances of 'str' and 'int'
    # String data (non-numberic values) in the tuple return cause the error 