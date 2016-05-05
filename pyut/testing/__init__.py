import inspect
import sys
import pkgutil
import os





def testing():
    testfunctions = [(obj, name) for name, obj in inspect.getmembers(sys.modules["__main__"]) if inspect.isfunction(obj)]


    for testfunction in testfunctions:
        print(testfunction)

    path = list(inspect.getframeinfo(inspect.currentframe().f_back))[0]

    for loader, module_name, is_pkg in pkgutil.walk_packages(os.path.basename(path)):
        mod = loader.find_module(module_name).load_module(module_name)

        for func in dir(mod):
            if "pyut" in func:
                ret = getattr(mod, func)
                print("ret = ", module_name, ret)

