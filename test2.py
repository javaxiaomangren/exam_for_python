class Demo2():
    def __init__(self, user_name):
        self.user_name = user_name

    def __call__(self, *args, **kwargs):
        print self.__dict__


Demo2("yanghua").user_name

1.dir(Demo)
2.Demo.__dict__, __getattr__
3.inspect
4.help

# or: from rlcompleter import get_class_members
def get_class_members(klass):
    ret = dir(klass)
    if hasattr(klass,'__bases__'):
        for base in klass.__bases__:
            ret = ret + get_class_members(base)
    return ret


def uniq( seq ): 
    """ the 'set()' way ( use dict when there's no set ) """
    return list(set(seq))


def get_object_attrs( obj ):
    # code borrowed from the rlcompleter module ( see the code for Completer::attr_matches() )
    ret = dir( obj )
    ## if "__builtins__" in ret:
    ##    ret.remove("__builtins__")

    if hasattr( obj, '__class__'):
        ret.append('__class__')
        ret.extend( get_class_members(obj.__class__) )

        ret = uniq( ret )

    return ret
    
    
    http://docs.python.org/2/library/rlcompleter.html
