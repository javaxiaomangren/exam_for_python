from __future__ import print_function


class ItemDescriptor(object):
    def __init__(self):
        self._data = []

    def __get__(self, instance, type = None):
        if len(self._data) == 1:
            tmp = self._data[0]

            class Wrapper(tmp.__class__): # 注意它的父类
                def __iter__(obj):
                    # 这里使用的是 obj 不是 self，因为 self 已经被用了
                    return self._data.__iter__()
                def next(obj):
                    return self._data.next()
            return Wrapper(tmp)
        return self._data

    def __set__(self, obj, val):
        if isinstance(val, list):
            self._data = val
            return
        self._data = [val]