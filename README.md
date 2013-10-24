Exam_for_python
===============
1. 完成class Demo,使得以下条件满足:<br/>a = Demo() <br />b = Demo() <br />assert id(a) == id(b) <br />
    分析：id函数的作用是获取对象在内存中的地址，要使id(a) == id(b)，则对象a和b需要指向相同的内存地址。
    再看一下python创建对象的方式，python里的class会先调用__new__方法(There is no way to create a new instance without calling __new__)

    每个python对都继承了object，所以只要重写object 的__new__方法，改变其创建对象的方式。既然对Demo只能有一个内存地址，那么在创建对象的时候先判断
    Demo的实例是否存在，如果存在返回。(我靠，　这不是单例子模式吗？恍然大悟呀）
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

3. 你是水果店的老板,店里新推出了DIY水果篮子的服务,可以让用户任意搭配不同品种和数量的水果,搭配完后还提供各种不同的打折服务。请用用Python实现一个计价程序,方方便收银。提醒:水果的品种、价格和打折的幅度可能随时调整。

4. 用Python实现linux的用户和权限管理基本功能。

5. 写一个简单的爬虫,把糗事百科今天被顶超过5000的帖子子爬出来,注意考虑性能和图片显示。

6. 用Django+Nginx+Redis+BootStrap开发一个BBS,要求支持用户,板块,图片,发/编辑/删帖,留言等功能。考虑到用户量激增的可能性,将这个BBS切分成几个服务,配置Nginx将请求转发到不同服务;使用Redis为可能成为性能瓶颈的数据做缓存。


大标题  
===================================  
  大标题一般显示工程名,类似html的\<h1\><br />  
  你只要在标题下面跟上=====即可  
  
    
中标题  
-----------------------------------  
  中标题一般显示重点项,类似html的\<h2\><br />  
  你只要在标题下面输入------即可  
    
### 小标题  
  小标题类似html的\<h3\><br />  
  小标题的格式如下 ### 小标题<br />  
  注意#和标题字符中间要有空格  
  
### 注意!!!下面所有语法的提示我都先用小标题提醒了!!!   
  
### 单行文本框  
    这是一个单行的文本框,只要两个Tab再输入文字即可  
          
### 多行文本框    
    这是一个有多行的文本框  
    你可以写入代码等,每行文字只要输入两个Tab再输入文字即可  
    这里你可以输入一段代码  
  
### 比如我们可以在多行文本框里输入一段代码,来一个Java版本的HelloWorld吧  
    public class HelloWorld {  
  
      /**  
      * @param args  
   */  
   public static void main(String[] args) {  
   System.out.println("HelloWorld!");  
  
   }  
  
    }  
### 链接  
1.[点击这里你可以链接到www.google.com](http://www.google.com)<br />  
2.[点击这里我你可以链接到我的博客](http://guoyunsky.iteye.com)<br />  
  
###只是显示图片  
![github](http://github.com/unicorn.png "github")  
  
###想点击某个图片进入一个网页,比如我想点击github的icorn然后再进入www.github.com  
[![image]](http://www.github.com/)  
[image]: http://github.com/github.png "github"  
  
### 文字被些字符包围  
> 文字被些字符包围  
>  
> 只要再文字前面加上>空格即可  
>  
> 如果你要换行的话,新起一行,输入>空格即可,后面不接文字  
> 但> 只能放在行首才有效  
  
### 文字被些字符包围,多重包围  
> 文字被些字符包围开始  
>  
> > 只要再文字前面加上>空格即可  
>  
>  > > 如果你要换行的话,新起一行,输入>空格即可,后面不接文字  
>  
> > > > 但> 只能放在行首才有效  
  
### 特殊字符处理  
有一些特殊字符如<,#等,只要在特殊字符前面加上转义字符\即可<br />  