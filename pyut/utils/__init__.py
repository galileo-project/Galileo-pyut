from pyut.var import GLOBAL

def parse_pyut(name):
    if name[0:4] != GLOBAL.PYUT_FREFIX:
        return False, name
    else:
        return True, name[5:]