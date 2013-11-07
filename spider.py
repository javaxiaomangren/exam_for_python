"""http://m2.qiushibaike.com/article/list/week?page=1&count=30&rqcnt=8
http://m2.qiushibaike.com/article/list/suggest?page=1&count=30&rqcnt=5
http://m2.qiushibaike.com/article/list/latest?page=1&count=30&rqcnt=6
http://m2.qiushibaike.com/article/list/latest?page=2&count=30&rqcnt=7
http://m2.qiushibaike.com/article/list/nearby10?page=1&count=30&n=10&rqcnt=8
http://m2.qiushibaike.com/article/list/nearby10?page=2&count=30&n=10&rqcnt=9

http://m2.qiushibaike.com/article/list/day?page=1&count=30&rqcnt=10
http://m2.qiushibaike.com/article/list/day?page=2&count=30&rqcnt=11

http://m2.qiushibaike.com/appinfo?rqcnt=25
http://m2.qiushibaike.com/article/list/suggest?page=1&count=30&rqcnt=26
http://m2.qiushibaike.com/article/list/suggest?page=2&count=30&rqcnt=27


http://www.douban.com/group/topic/44446641/
"""
import json
import urllib2
import thread


def get_response(url, coding='utf-8'):
  try:
    urllib2.urlopen(url, coding, timeout=120).read()
  except:
    pass
  
def get_img(url):
  pass

class FetchArticle(Thread):
  pass

def main():
  pass

if __name__ == '__main__':
  main()