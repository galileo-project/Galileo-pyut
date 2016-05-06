from pyut import it

def pyut_test_eq_val():
    it(True)

def test_func():
    return True

def pyut_test_eq_func():
    it(test_func)
