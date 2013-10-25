#!/usr/bin/env python
#coding: utf-8
#==============================================================
#使用消息队列异步调用函数
import sys
import cPickle
import Queue


class MessageQueue(object):
	def __init__(self):
		self.queue = Queue.Queue()

	def put(self, message):
		self.queue.put(message)

	def get(self):
		if not self.queue.empty():
			return self.queue.get()
	def size(self):
		return self.queue.qsize()

mq = MessageQueue()


def async(func):
	mod = sys.modules[func.__module__]
	fname = "origin_" + func.__name__
	mod.__dict__[fname] = func

	def _(*a, **kw):
		body = cPickle.dumps((mod.__name__, fname, a, kw))
		mq.put(body)
	return _


def async_worker():
	modname, fname, a, kw = cPickle.loads(mq.get())
	__import__(modname)
	mod = sys.modules[modname]
	mod.__dict__[fname](*a, **kw)

def make_email_body(fromaddr, email, subject, body):
	return "%s\n%s\n%s\n%s" % (fromaddr, email, subject, body)

@async
def send_notification_mail(email, subject, body):
	fromaddr = 'no-reply@douban.com'
	email_body = make_email_body(fromaddr, email, subject, body)
	print email_body

send_notification_mail("email@12131.com", "Test function", "This is a Test body")
print mq.size()
async_worker()
