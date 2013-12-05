#/usr/bin/env python
#conding: utf8

import gc


class Demo(object):
    def __new__(cls, *args, **kwargs):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwargs)
        return it

    def init(self, *args, **kwargs):
        """inherited by subclass"""
        pass


class Demo1(object):
    def __new__(cls, *args, **kwargs):
        for obj in gc.get_objects():
            if isinstance(obj, Demo1):
                return obj
        return object.__new__(cls)


class Demo2(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Demo2, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# metaclass

class Demo3(dict):
    def __init__(self, default=None):
        dict.__init__(self)
        self.default = default

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.default


class Demo4():

    def __init__(self):
        pass

    @staticmethod    
    def instance():
        if not hasattr(Demo4, "_instance"):
            Demo4._instance = Demo4()
        return Demo4._instance


if __name__ == "__main__":
    assert id(Demo()) == id(Demo())
    assert id(Demo1()) == id(Demo1())
    assert id(Demo2()) == id(Demo2())
    dicA = Demo3(dict(i=1, j=2))
    dicB = Demo3(dict(x="a", y="b"))
    assert id(dicB) == id(dicB)
    assert id(Demo4.instance) == id(Demo4.instance)
    print "finished"

