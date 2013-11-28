#/usr/bin/env python
#coding:utf8

import urllib2
from threading import Thread
from Queue import Queue
from bs4 import BeautifulSoup as bs
from bs4 import Tag

url_template = "http://www.qiushibaike.com/hot/page/%s"
thread_num = 5
task_queue = Queue()
img_queue = Queue()


def get_response(url):
    return urllib2.urlopen(url, timeout=120).read()


def parse_html(html, img_queue):
    root = bs(html)
    col = root.find("div", class_="col1")
    try:
        for c in col.children:
            if type(c) is Tag:
                bar = c.find("div", class_="bar")
                if bar:
                    _id = c["id"]
                    li = bar.find("li", class_="up")
                    vote = li.a.text
                    if int(vote) > 5000:
                        content = c.find("div", class_="content").text
                        print _id.rstrip() + content.rstrip()
                        thumb_div = c.find("div", class_="thumb")
                        if thumb_div:
                            img_url = thumb_div.img.attrs["src"]
                            if img_url:
                                img_queue.put((_id, img_url))
    except Exception:
        pass


def get_pages():
    try:
        root = bs(get_response("http://www.qiushibaike.com/hot"))
        page = root.find("div", class_="pagebar")
        plist = page.find_all("a")
        if len(plist) > 2:
            print "Get task size %d " % int(plist[-2: -1][0].text)
            return int(plist[-2: -1][0].text)
        return 1
    except Exception:
        return 1


def save_img(name, img):
    with open(name, "w") as f:
        f.write(img)


def download_img(i, img_queue):
    while True:
        url = img_queue.get()
        try:
            print "Thread-%d: Downloading image %s " % (i, url[1])
            img = get_response(url[1])
            if img:
                name = "images/%s.%s" % (url[0], url[1].rstrip().split(".").pop())
                save_img(name, img)
        except:
            print "Failed to handle task--->", url
        img_queue.task_done()


def fetch(i, task_queue):
    while True:
        print '%s: Looking for the next task' % i
        url = task_queue.get()
        if url:
            html = get_response(url)
            print 'Handle task %s' % url
            parse_html(html, img_queue)
        task_queue.task_done()


def generate_task(task_queue):
    for i in range(1, get_pages()):
        task_queue.put(url_template % i)


def main():
    generate_task(task_queue)

    for t in range(thread_num):
        worker = Thread(target=fetch, args=(t, task_queue, ))
        worker.setDaemon(True)
        worker.start()

    for t in range(thread_num, thread_num + 5):
        worker = Thread(target=download_img, args=(t, img_queue, ))
        worker.setDaemon(True)
        worker.start()

    task_queue.join()
    img_queue.join()


if __name__ == '__main__':
  main()