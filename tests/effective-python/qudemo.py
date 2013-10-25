__author__ = 'yanghua'
# System modules
from Queue import Queue
from threading import Thread
import time

# Local modules

# Set up some global variables
num_fetch_threads = 2
enclosure_queue = Queue()

# A real app wouldn't use hard-coded data...
feed_urls = ['http://www.castsampler.com/cast/feed/rss/guest']


def downloadEnclosures(i, q):
    """This is the worker thread function.
    It processes items in the queue one after
    another.  These daemon threads go into an
    infinite loop, and only exit when
    the main thread ends.
    """
    while True:
        print '%s: Looking for the next enclosure' % i
        url = q.get()
        print '%s: Downloading:' % i, url
        # instead of really downloading the URL,
        # we just pretend and sleep
        time.sleep(i + 2)
        q.task_done()


# Set up some threads to fetch the enclosures
for i in range(num_fetch_threads):
    worker = Thread(target=downloadEnclosures, args=(i, enclosure_queue,))
    worker.setDaemon(True)
    worker.start()

# Download the feed(s) and put the enclosure URLs into
# the queue.
while 1:
    if enclosure_queue.qsize() < 2:
        enclosure_queue.put("http://www.baidu.com")
    #     response = feedparser.parse(url, agent='fetch_podcasts.py')
    #     for entry in response['entries']:
    # pass
#         for enclosure in entry.get('enclosures', []):
#             print 'Queuing:', enclosure['url']

# Now wait for the queue to be empty, indicating that we have
# processed all of the downloads.
print '*** Main thread waiting'
enclosure_queue.join()
print '*** Done'