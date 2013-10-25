#coding:utf-8
READ = 1 << 0
WRITE = 1 << 1
CREATE = 1 << 2
DELETE = 1 << 3
ADMIN = 1 << 4

def checkPermission(pririvleges, action):
	return pririvleges & action == action

def addPermissino(pririvleges, action):
	return pririvleges | action

def delPermission(pririvleges, action):
	

auth = READ | WRITE | CREATE 

auth1 = WRITE | CREATE

if auth & READ and auth & WRITE and auth & CREATE:
	print 'have read privilege'

if auth1 & WRITE == 1:
	print "Can read"

if auth1 & DELETE:
	print "Can DELETE"
else:
	print "Can NOT DELETE"

if not auth & ADMIN:
	print "have not privilege"

"""
位运算的运算对象是二进制的位，速度快，效率高，而且节省存储空间，位运算做权限控制又相当地灵活。
但是，位运算也有很大的局限，因为在32位计算机上，位移不能超过32次，这就要求权限数量不超过32种。
-rwx-rwx-rwx   这个在linux中表示777，我们来看第一段7
x可执行1<< 0
w可写1<<1
r 可读 1<<2
2^0=1，相应2进数为”0001″(2的0次方，下同)
2^1=2，相应2进数为”0010″
2^2=4，相应2进数为”0100″
2^3=8，相应2进数为”1000″
要判断一个数在某些数范围内就可以使用 & 运算符(数值从上面的表中得来)
如：7=4|2|1　(可以简单理解成7=4+2+1)，用 & 来操作，可以知道7&4、7&2、7&1都是真的，而如果7&8则是假的。


权限运算采用位运算的方式，权限由系统预先定义，一个权限用2的N次冥表示,mysql的一个BIGINT类型占8个字节（8字节 * 8比特位 =64个比特位），则权限集可以表示64-1项权限.如下所示：

二进制：0001 表示权限1,整型值1

二进制：0010 表示权限2,整型值2

二进制：0100 表示权限3,整型值4

二进制：1000 表示权限4,整型值8

... ...
权限集：0011就表示权限1和权限2,则整型值就为3

权限的基本操作：

1 检测是否有权限： 权限验证采用与等运算(&=)
checkPermission(权限集值，权限项) {

       return 权限集值 & 权限项 == 权限项

}

2 增加权限项：权限增加采用和运算(+)

addPermission(权限集值, 权限项) {

      return 权限集值 + 权限项

}

3 删除权限项： 权限删除采用与非运算(&~)
deletePermission(权限集值，权限项){

      return 权限集值 & ~权限项

}
"""