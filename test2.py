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

def snake_to_camel_case(s):
    """
    Converts strings from 'snake_case' (Python code convention)
    to CamelCase
    """
    new_string = s

    leading_count = 0
    while new_string.find('_') == 0:
        new_string = new_string[1:]
        leading_count +=1
    
    trailing_count = 0
    while new_string.rfind('_') == len(new_string) - 1:
        new_string = new_string[:-1]
        trailing_count +=1
    
    new_string = ''.join([word.title() for word in new_string.split('_')])
    leading_underscores = '_' * leading_count
    trailing_underscores = '_' * trailing_count
    return leading_underscores + new_string[0].lower() + new_string[1:] + trailing_underscores
