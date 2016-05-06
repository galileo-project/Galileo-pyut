# Galileo-pyut

[![Build Status](https://travis-ci.org/galileo-project/Galileo-pyut.svg?branch=dev)](https://travis-ci.org/galileo-project/Galileo-pyut)

Python unit test framework


## Python

* [x] python 2.6 
* [x] python 2.7 
* [x] python 3.x

## Build

    python setup.py install
    
## Usage

**project structure**

    |..
    |--project
    |--test
        |--__init__.py
        |--test.py
        |--pyut_some_module.py
        |--pyut_other_module.py

**test.py**
    
```python
from pyut import testing
from pyut import eq, it, desc


def pyut_test_eq():
    eq(1,1)

def pyut_test_it():
    it(True)
    #it(test_desc_true)

def test_desc_true():
    return True

if __name__ == "__main__":
    desc("test pyut desc true", test_desc_true)

    testing()
    
```

**pyut_some_module.py**

```python
from pyut import eq

def pyut_test_eq_val():
    eq(1,1)

def test_func1():
    return 1

def test_func2():
    return 1

def pyut_test_eq_func():
    eq(test_func1, test_func2)

```