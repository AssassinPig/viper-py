# -*- coding: utf-8 -*-
'''
    author: assassinpig
    email: assassinpig@gmail.com
'''
import signal, os
import time
import settings
import redis
import threading
from mylogger import get_logger 

logger = get_logger(name="master", file_name="master.log")

class Master(object): 

    @staticmethod
    def exit_handler(signum, frame):
        #print 'you press ctrl+c!'
        logger.debug('you press Ctrl+C!')
        pass

    def __init__(self, settings=None, start_urls=None, strategy=None):
        logger.debug('Init Master ...')
        if settings is None:
            try:
                logger.debug('Connect to local redis')
                self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
                if self.r is None:
                    raise redis.exceptions.ConnectionError 
            except (redis.exceptions.ConnectionError), e:
                raise e 
        else:
            self.host = settings.REDIS_HOST
            self.port = settings.PORT

            self.QUEUE_TODO = settings.QUEUE_TODO
            self.QUEUE_VISITED = settings.QUEUE_VISITED
            self.QUEUE_FETCHED = settings.QUEUE_FETCHED
            self.watermark = settings.WATERMARK

            self.r = redis.StrictRedis(host=self.host, port=self.port, db=0)
            logger.debug('Connect to %s:%d redis' % (self.host, self.port))

        signal.signal(signal.SIGINT, self.exit_handler)

        if start_urls is not None:
            self.todo_list = start_urls
        self.thread_running = False

        #Master._instance = this

    #@staticmethod
    #def instance():
    #    return self._instance

    def is_running(self):
        return self.thread_running

    def run(self):
        visited_list = [] 
        while True:
            watermark = self.watermark  

            while watermark > 0:
                watermark -= 1
                for l in self.todo_list:
                    logger.debug('push %s todo' % l)
                    self.r.lpush(self.QUEUE_TODO, l)  
                    i = self.todo_list.index(l)
                    #here should be a watermark
                    self.todo_list.pop(i)
                    break

            url = self.r.brpop(self.QUEUE_FETCHED) 
            logger.debug('fetch %s todo' % url[1])
            #simple stragtey 
            if url[1] not in visited_list:
                self.todo_list.append(url[1])
                visited_list.append(url[1])

    @staticmethod
    def put(master):
        while master.is_running():
            for l in master.todo_list:
                master.r.lpush(master.QUEUE_TODO, l)  
            time.sleep(1)

    @staticmethod
    def fetch(master):
        while master.is_running():
            url = master.r.brpop(master.QUEUE_FETCHED) 
            master.todo_list.append(url)
