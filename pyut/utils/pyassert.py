from pyut.utils.exp import TestEQException, TestITException
from pyut.var import GLOBAL

def eq(lhs, rhs):
    is_func = hasattr(lhs, "__call__") and\
              hasattr(rhs, "__call__")

    if not type(lhs) is type(rhs):
        raise TestEQException()

    if is_func:
        if not lhs() == rhs():
            raise TestEQException()
        else:
            pass
    else:
        if not lhs == rhs:
            raise TestEQException()
        else:
            pass


def it(val):
    if hasattr(val, "__cal__"):
        ret = val()
        if not ret:
            raise TestITException()
        else:
            return ret
    else:
        if val:
            return val
        else:
            raise TestITException()

def desc(desc, test_func):
    try:
        ret = test_func()
    except:
        ret = False

    GLOBAL.result.test_desc(desc=desc, ret=ret)

    return ret