from pyut.utils.exp import TestEQException, TestITException
from pyut.var import GLOBAL

def eq(lhs, rhs):
    is_func = hasattr(lhs, "__call__") and\
              hasattr(rhs, "__call__")

    if not type(lhs) is type(rhs):
        raise TestEQException()

    if is_func:
        try:
            lhs_ret = lhs()
            rhs_ret = rhs()
        except:
            raise TestEQException()

        if not lhs_ret == rhs_ret:
            raise TestEQException()
        else:
            return True
    else:
        if not lhs == rhs:
            raise TestEQException()
        else:
            return True

def it(val):
    if hasattr(val, "__cal__"):
        try:
            ret = val()
        except:
            raise TestITException()

        if ret is True:
            return True
        else:
            raise TestITException()
    else:
        if val is True:
            return True
        else:
            raise TestITException()

def desc(desc, lhs_func, rhs_func = None):
    try:
        if rhs_func is None:
            ret = it(lhs_func)
        else:
            ret = eq(lhs_func, rhs_func)
    except:
        ret = False

    GLOBAL.result.test_desc(desc=desc, ret=ret)

    return ret