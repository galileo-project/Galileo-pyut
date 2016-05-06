from pyut.var import GLOBAL
from pyut.utils import parse_pyut
import inspect
import sys
import pkgutil
import os

def testing():
    testfunctions = [(obj, name) for name, obj in inspect.getmembers(sys.modules["__main__"]) if inspect.isfunction(obj)]

    for testfunction in testfunctions:
        is_pyut_func, pyut_func_name = parse_pyut(testfunction[1])
        if is_pyut_func:
            GLOBAL.result.test(pyut_func_name, testfunction[0])

    path = list(inspect.getframeinfo(inspect.currentframe().f_back))[0]
    for loader, module_name, is_pkg in pkgutil.walk_packages(os.path.basename(path)):
        mod = loader.find_module(module_name).load_module(module_name)

        is_pyut_mod, pyut_mod_name = parse_pyut(module_name)
        if is_pyut_mod:
            for func_name in dir(mod):
                is_pyut_func, pyut_func_name = parse_pyut(func_name)
                if is_pyut_func:
                    func = getattr(mod, func_name)
                    GLOBAL.result.test(pyut_func_name, func, pyut_mod_name)


    GLOBAL.result.show()
    sys.exit(GLOBAL.result.code)