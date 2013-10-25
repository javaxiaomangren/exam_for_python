class Fib:
    def __init__(self, max):
        self.max = max
        print "A"

    def __iter__(self):
        self.a = 0
        self.b = 1
        print "C"
        return self

    def next(self):
        """__next__() in py3"""
        print "D"
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

    def __enter__(self):
        print "B"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "E"
        pass

if __name__ == "__main__":
    # for n in Fib(1000):
    #     print n
    print list(Fib(100))

    # with Fib(100) as f:
    #     print list(f)