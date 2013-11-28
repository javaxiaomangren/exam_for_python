Exam_for_python
===============
1. 完成class Demo,使得以下条件满足:<br/>a = Demo() <br />b = Demo() <br />assert id(a) == id(b) <br />

    分析：id函数的作用是获取对象在内存中的地址，要使id(a) == id(b)，则对象a和b需要指向相同的内存地址。
    再看一下python创建对象的方式，python里的class会先调用__new__方法(There is no way to create a new instance without calling __new__)

    每个python对都继承了object，所以只要重写object 的__new__方法，改变其创建对象的方式。既然对Demo只能有一个内存地址，那么在创建对象的时候先判断
    Demo的实例是否存在，如果存在返回。
    
        class Demo(object):
            def __new__(cls, *args, **kwargs):
                it = cls.__dict__.get('__it__')
                if it is not None:
                    return it
                cls.__it__ = it = object.__new__(cls)
                it.init(*args, **kwargs)
                return it
                
            def init(*args, **kwargs):
                pass

    判断对象是否创建还有一些方式，hasattr(cls, '__self__'), setattr, getattr....
    gc.get_objects()
    ......


    思路２： metaclass 继承元类型, Any class whose instances are themselves classes, is a metaclass

        class defaultdict(dict):

            def __init__(self, default=None):
                dict.__init__(self)
                self.default = default

            def __getitem__(self, key):
                try:
                    return dict.__getitem__(self, key)
                except KeyError:
                    return self.default


    [参考文档](http://www.python.org/download/releases/2.2/descrintro/)<br />

2. 实现class Demo2,使得Demo2所有属性和方方法均自动变成CamelCase的形式。尽可能多写几种实现方式。<br />
    把原有的方法和属性复制一份，使用CamelCase形式命名
    [test2.py](https://github.com/javaxiaomangren/exam_for_python/blob/master/test2.py)

3. 你是水果店的老板,店里新推出了DIY水果篮子的服务,可以让用户任意搭配不同品种和数量的水果,搭配完后还提供各种不同的打折服务。请用用Python实现一个计价程序,方方便收银。提醒:水果的品种、价格和打折的幅度可能随时调整。
    [fruit_diy.py](https://github.com/javaxiaomangren/exam_for_python/blob/master/fruit_diy.py)

4. 用Python实现linux的用户和权限管理基本功能。

5. 写一个简单的爬虫,把糗事百科今天被顶超过5000的帖子子爬出来,注意考虑性能和图片显示。
    url_template: http://www.qiushibaike.com/hot
    使用两个队列，一个处理抓取任务，一个处理抓取图片，BeautifulSoup 解析html, 详见spider.py
    开启多个线程去处理队列

    出于好奇，我装了一个糗事百科的app,　在pc上装了一个finder,代理手机上网，拦截请求链接
        http://m2.qiushibaike.com/article/list/latest?page=2&count=30&rqcnt=7
       这个返回的结果是一个json，解析起来比较简单，但是翻页到60页以后很慢，翻到100的时候基本已经不行了


6. 用Django+Nginx+Redis+BootStrap开发一个BBS,要求支持用户,板块,图片,发/编辑/删帖,留言等功能。考虑到用户量激增的可能性,将这个BBS切分成几个服务,配置Nginx将请求转发到不同服务;使用Redis为可能成为性能瓶颈的数据做缓存。
可以用位运算做权限控制,判断帖子的状态，顶火？？

用tornado　+　bootcss + solr弄了个保险搜索的东西，开发中
[代码](https://github.com/javaxiaomangren/insurance)

[网站](http://110.75.189.239:8888/)
[后台](http://110.75.189.239:8889/admin)