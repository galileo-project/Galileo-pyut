from pyut import testing
from pyut import eq, it, desc


def pyut_test_eq():
    eq(1,1)

def pyut_test_it():
    it(True)

def test_desc_true():
    return True

if __name__ == "__main__":
    desc("test pyut desc true", test_desc_true)

    testing()