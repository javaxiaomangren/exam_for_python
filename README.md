exam_for_python
===============

Examination for Python engineer
Python工工程师初级笔试题
1. 完成class Demo,使得以下条件满足:
a = Demo()
b = Demo()
assert id(a) == id(b)
2. 实现class Demo2,使得Demo2所有属性和方方法均自动变成CamelCase的形式。
尽可能多写几种实现方式。
3. 你是水果店的老板,店里新推出了DIY水果篮子的服务,可以让用户任意搭配不同
品种和数量的水果,搭配完后还提供各种不同的打折服务。请用用Python实现一个计
价程序,方方便收银。提醒:水果的品种、价格和打折的幅度可能随时调整。
4. 用Python实现linux的用户和权限管理基本功能。
5. 写一个简单的爬虫,把糗事百科今天被顶超过5000的帖子子爬出来,注意考虑性能
和图片显示。
6. 用Django+Nginx+Redis+BootStrap开发一个BBS,要求支持用户,板块,图片,
发/编辑/删帖,留言等功能。考虑到用户量激增的可能性,将这个BBS切分成几个服
务,配置Nginx将请求转发到不同服务;使用Redis为可能成为性能瓶颈的数据做缓
存。
