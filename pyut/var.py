class GlobalVar(object):
    PYUT_FREFIX = "pyut"

    def __init__(self):
        self.__data = {}

    @property
    def result(self):
        name = "result"

        if not self.__data.get(name):
            from pyut.testing.result import Result
            self.__data[name] = Result()
        return self.__data[name]


GLOBAL = GlobalVar()