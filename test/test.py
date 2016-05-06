from pyut import testing
from pyut import eq, it, desc


def pyut_test_eq():
    eq(1,1)

def pyut_test_it():
    it(True)

def test_desc_true():
    return True

def test_desc_eq1():
    return 1

def test_desc_eq2():
    return 1

if __name__ == "__main__":
    desc("test pyut desc it", test_desc_true)
    desc("test pyut desc eq", test_desc_eq1, test_desc_eq2)

    testing()