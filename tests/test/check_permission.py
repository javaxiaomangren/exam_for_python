#!/usr/bin/env python
#coding: utf-8
#某些页面必须拥有某个权限才能访问

# class GroupUI(object):
# 	def new_topic(self, request):
# 		if self.group.can_post(request.user):
# 			return new_topic_ui(self.group)
# 		else:
# 			request.response.set_status(403, "Forbidden")
# 		return error_403_ui(msg="成为小组成员才能发帖")
# 	def join(self, request):
# 		if self.group.can_join(request.user):
# 			pass

class BadPermission(Exception):
	pass

class Group(object):
	def can_post(self, user):
		return "self.group.has_member(user)"
	def can_join(self, user):
		return not "self.group.has_banned(user)"

class check_permission(object):
	def __init__(self, action, msg=None):
		self.action = action
		self.msg = msg
	def __call__(self, func):
		def _(ui, req, *args, **kwargs):
			f = getattr(ui.perm_obj, 'can_' + self.action)
			if f(req.user):
				return func(ui, *args, **kwargs)
			raise BadPermission(ui.perm_obj, self.action,self.msg)
		return _

class GroupUI(object):
	
	@check_permission('post', msg="成为小组成员才能发帖")
	def new_topic(self, request):
		return "new_topic_ui(self.group)"

	@check_permission('join', msg="不能加入小组")
	def join(self, request):
		pass


class BadLogin(Exception):
	pass

class decorator_with_class(object):
	def __init__(self, username, passwd):
		self.username = username
		self.passwd = passwd

	def __call__(self, func):
		def _(a, *args, **kwargs):
			print "print in decorator func ",a * 10
			if self.username == "windy" and self.passwd == "windy" :
				return func(*args, **kwargs)
			raise BadLogin("username or password error!")
		return _

@decorator_with_class("windy", "windy")		
def test_login(a='1'):
	print "print in invoked func:", a
	return "login successed"

# print test_login("1")

