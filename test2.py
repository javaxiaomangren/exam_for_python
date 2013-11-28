import types


class SpecialClass(object):
    @classmethod
    def removeVariable(cls, name):
        return delattr(cls, name)

    @classmethod
    def addMethod(cls, func):
        return setattr(cls, func.__name__, types.MethodType(func, cls))


class Demo(object):
    test_value = "aaa"

    def get_hello(self):
        print "hello"

    def init(self, *args, **kwargs):
        """inherited by subclass"""
        self.__init__(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        it = object.__new__(cls)
        it.init(*args, **kwargs)
        for t in cls.__dict__:
            if not t.endswith("__"):
                attrs = t.split("_")
                if len(attrs) > 1:
                    camelName = attrs[0] + "".join(map(str.capitalize, t.split("_")[1:]))
                    old = cls.__dict__[t]
                    if hasattr(old, "__call__"):
                        setattr(it, camelName, types.MethodType(old, cls))
                    else:
                        setattr(it, camelName, old)

        return it

    def world(self):
        pass

d = Demo()
d.getHello()
print d.testValue

