#!/usr/bin/evn python
import itertools
import timeit

seq=range(1000)
price = 888
f1 = """
	temp_ids = []
	for rd in seq:
	    if price == rd:
	        temp_ids.append(str(rd))
"""
"0.00924301147461"
f2 = """ids = [ str(i) for i in itertools.ifilter(lambda x: x == price, seq)]"""
timeit.Timer(f2, "seq=range(1000); price=888")
print timeit.timeit()
seq = [1, 0, 2, 0]
for i in itertools.ifilter(x, seq):
	print i