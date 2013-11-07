import types


class Demo2(object):
    def __init__(self, user_name=None, password=None):
        self.user_name = user_name
        self.password = password

    def get_user_name(self):
        return self.user_name

    def login(self):
        pass

    def __new__(cls, *args, **kwargs):
        it = object.__new__(cls)
        return it


class SpecialClass(object):
    @classmethod
    def removeVariable(cls, name):
        return delattr(cls, name)

    @classmethod
    def addMethod(cls, func):
        return setattr(cls, func.__name__, types.MethodType(func, cls))


d = Demo2('windy', 123456)
# print Demo2.__dict__


"""
function-rgx=??[a-z][A-Za-z0-9]{1,30}$
method-rgx=??[a-z][A-Za-z0-9]{1,30}$
attr-rgx=??[a-z][A-Za-z0-9]{1,30}$
argument-rgx=_?[a-z][A-Za-z0-9]{1,30}$
variable-rgx=_?[a-z][A-Za-z0-9]{1,30}$
inlinevar-rgx=_?[a-z][A-Za-z0-9]{1,30}$

http://pylint-messages.wikidot.com/messages:c0103

"""

#
# 1.dir(Demo)
# 2.Demo.__dict__, __getattr__
# 3.inspect
# 4.help

# # or: from rlcompleter import get_class_members
# def get_class_members(klass):
#     ret = dir(klass)
#     if hasattr(klass,'__bases__'):
#         for base in klass.__bases__:
#             ret = ret + get_class_members(base)
#     return ret
#
#
# def uniq( seq ):
#     """ the 'set()' way ( use dict when there's no set ) """
#     return list(set(seq))
#
#
# def get_object_attrs( obj ):
#     # code borrowed from the rlcompleter module ( see the code for Completer::attr_matches() )
#     ret = dir( obj )
#     ## if "__builtins__" in ret:
#     ##    ret.remove("__builtins__")
#
#     if hasattr( obj, '__class__'):
#         ret.append('__class__')
#         ret.extend( get_class_members(obj.__class__) )
#
#         ret = uniq( ret )
#
#     return ret
#
#
#     http://docs.python.org/2/library/rlcompleter.html


import copy

class SpecialClass(object):
    @classmethod
    def removeVariable(cls, name):
        return delattr(cls, name)

    @classmethod
    def addMethod(cls, func):
        return setattr(cls, func.__name__, types.MethodType(func, cls))

class Demo(object):

    def hello(self):
        print "hello"

    def init(self, *args, **kwargs):
        """inherited by subclass"""
        self.__init__(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        temp = cls.__dict__
        for t in temp:
            print t.capitalize(), "==>", temp[t]
        values = cls.__dict__.values()
        it = object.__new__(cls)

        it.init(*args, **kwargs)
        return it

    def world(self):
        pass
d = Demo()
# d.Hello()

