class Result(object):
    __TEST_FUNC   = "%-7s: Module: %-10s, function: %-10s"
    __TEST_DESC   = "%-7s: %s"
    __SUCCESS     = "SUCCESS"
    __FAILED      = "FAILED"
    __DEFAULT_MOD = "default"

    def __init__(self):
        self.__data = []
        self.__code = 0

    def ret_to_str(self, ret):
        if ret:
            ret_str = self.__SUCCESS
        elif ret is None:
            ret_str = self.__SUCCESS
        else:
            self.__code = 1
            ret_str = self.__FAILED

        return ret_str

    def generator(self, ret, mod_name=None, func_name=None):
        if not mod_name:
            mod_name = self.__DEFAULT_MOD

        line = self.__TEST_FUNC % (self.ret_to_str(ret), mod_name, func_name)
        self.__data.append(line)

    def test_desc(self, desc, ret):
        line = self.__TEST_DESC % (self.ret_to_str(ret), desc)
        self.__data.append(line)

    def test(self, func_name, func, mod_name=""):
        try:
            ret = func()
        except:
            ret = False

        self.generator(ret, mod_name, func_name)

    def show(self):
        for line in self.__data:
            print(line)

    @property
    def code(self):
        return self.__code