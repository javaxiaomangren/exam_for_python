#!/usr/bin/env python
#coding: utf-8
# cache函数运行结果(SQL, 复杂运算, etc)

import inspect

mc = {}
def exc_sql(sql):
	print "exe Mysql....................."
	return "max_id"

def get_latest_review_id():
	review_id = mc.get('latest_review_id')
	if review_id is None:
		review_id = exc_sql("select max(id) from review")
		mc['latest_review_id'] = review_id
	return review_id

def cache(key):
	def deco(func):
		def _(*args, **kwargs):
			r = mc.get(key)
			if r is None:
				r = func(*args, **kwargs)
				mc[key] = r
			return r
		return _
	return deco

def gen_key_factory(key_partten, arg_names, defaults):
	return 

@cache('latest_review_id')
def get_latest_review_id():
	return exc_sql("select max(id) from review")

# print get_latest_review_id()
# print get_latest_review_id()


def cache(key_partten, expire=0):
	def deco(func):
		arg_names, varargs, varkw, defaults = inspect.getargspec(func)
		if varargs or varkw:
			#动态参数不支持
			raise Exception("not support varargs")
		# gen_key = gen_key_factory(key_pattern, arg_names, defaults)
		def _(*args, **kwargs):
			# key = gen_key(*args, **kwargs)
			key = key_partten % {"id":args[0]}
			r = mc.get(key)
			if r is None:
				r = func(*args, **kwargs)
				mc[key] = r+"_"+str(expire)
			return r
		return _
	return deco

@cache("review:%(id)s", 12)
def review(id):
	return "122131"

print review("123213131L")
print review("123213131L")
print review("123213131L")