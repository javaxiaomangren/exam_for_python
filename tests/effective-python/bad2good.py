#/usr/bin/env python
    if x != []:  
        x.doSth()  
    #优化：  
    if x:  
        x.doSth()  

python  False, [] ,0, null , None 都当作False

看一下执行效率：

>>> t = timeit.Timer("if x != []:pass", "x=[]")
>>> t.timeit()
0.04584908485412598
>>> 
>>> t = timeit.Timer("if x:pass", "x=[]")
>>> t.timeit()
0.032701969146728516
>>>

2.循环迭代

带索引循环：

[html] view plaincopy

    for i in range(len(seq)):  
       do(seq[i], i)  
    #-----  
    for i, item in enumerate(seq):  
        do(item, i)  

多个列表迭代：
[python] view plaincopy

    #--------Bad-----------------------------  
    for i in xrange(len(seq1)):  
        do(seq[i], seq2[i])  
    #--------Good----------------------------  
    for i, j in zip(seq1, seq2):  
        do(i, j)  
    #--------Good----------------------------  
    for i, j in itertools.izip(seq1, seq2):  
       do(i, j)  


[python] view plaincopy

    #--------Bad-----------------------------  
    for i in xrange(len(seq1)):  
        do(seq[i], seq2[i])  
    #--------Good----------------------------  
    for i, j in zip(seq1, seq2):  
        do(i, j)  
    #--------Good----------------------------  
    for i, j in itertools.izip(seq1, seq2):  
       do(i, j)  



反向循环：

[python] view plaincopy

    #--------Bad-----------------  
    for i in xrange(len(seq)-1, -1, -1):  
        print seq[i]  
      
    l = seq[:]  
    l.reverse()  
    for i in l:  
        print i  
    #--------Good----------------  
    for i in reversed(seq):  
        print i  

处理指定位置列表元素：

[python] view plaincopy

    def foo(seq, bgn, end):  
        i = 0  
        while bgn < end:  
            bar(seq[bgn], i)  
            bgn += 1  
            i += 1  
      
    def foo1(seq, bgn, end):  
        tmp_seq = seq[bgn:end]  
        for i, item in enumerate(tmp_seq):  
            bar(item, i)  
      
    #--------Good----------------  
    def foo2(seq, bgn, end):  
        for begin, i in itertools.izip(xrange(bgn, end), itertools.counts()):  
            bar(seq[begin], i)  


条件循环：

[python] view plaincopy

    #--------Bad-----------------  
    for i in seq:  
        if pre(i):  
            foo(i)  
    #--------Good----------------  
      
    for i in itertools.ifilter(pre, seq):  
        foo(i)  

字符链接：

[python] view plaincopy

    #--------Bad-----------------  
    s = ''  
    for i in seq:  
        s += chr(i)  
    #--------Good----------------  
    ''.join(map(chr, seq))  