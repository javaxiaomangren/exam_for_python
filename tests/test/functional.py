from operator import add

expr, res = "28+32+++32++39", 0
for t in expr.split("+"):
    if t != "":
        res += int(t)
print res

print sum(map(int, filter(bool, expr.split('+'))))
print reduce(add ,map(int, filter(bool, expr.split('+'))))

def fsum(f):
    def apply(a, b):
        return sum(map(f, range(a,b+1)))
    return apply

print fsum(lambda x: x*2)(1, 2)


ss = ["UA", "PyCon", "2012"]
print reduce(add, map(len, ss))