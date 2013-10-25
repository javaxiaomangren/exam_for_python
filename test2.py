class Demo2():
    def __init__(self, user_name):
        self.user_name = user_name

    def __call__(self, *args, **kwargs):
        print self.__dict__


Demo2("yanghua").user_name

