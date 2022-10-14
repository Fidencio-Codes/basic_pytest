# Case 1
# def func_retval():
#     some_int = 10
#     return some_int

# def test_func_retval():
#     assert func_retval() == 4

# This condition evaluates to False, since 10 does not equal 4. 
# Thus, an AssertionError is raised and the test fails


# Case 2
def test_sets_compare():
    set1 = set("abcd")
    set2 = set("aced")
    assert set1 == set2

# function creates two sets, and checks if they are equal
# In Terminal: pytest test_asserts -vv (even more verbose information)
# AssertionError, test fails