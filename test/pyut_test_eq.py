from pyut import eq

def pyut_test_eq_val():
    eq(1,1)

def test_func1():
    return 1

def test_func2():
    return 1

def pyut_test_eq_func():
    eq(test_func1, test_func2)
