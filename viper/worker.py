# -*- coding: utf-8 -*-
'''
    author: assassinpig
    email: assassinpig@gmail.com
'''
import settings
import redis
from crawler import Crawler
from crawleritem import CrawlerItem
from StringIO import StringIO
import lxml.html as LH
from strategy import Strategy
from mylogger import get_logger
from datetime import *

import hashlib
import os

logger = get_logger(name="worker", file_name="worker.log")

class Worker(Crawler):

    def __init__(self, start_urls=None, template_cls=None, strategy=None, settings=None):
        super(Worker, self).__init__(start_urls=start_urls, template_cls=template_cls, strategy=strategy)
        logger.debug('Init Worker...')
        if settings is None:
            try:
                self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
                logger.debug('Connection local redis')
                if self.r is None:
                    raise redis.exceptions.ConnectionError 
            except (redis.exceptions.ConnectionError), e:
                raise e 
        else:
            self.settings = settings
            self.host = settings.REDIS_HOST
            self.port = settings.PORT

            self.QUEUE_TODO = settings.QUEUE_TODO
            self.QUEUE_VISITED = settings.QUEUE_VISITED
            self.QUEUE_FETCHED = settings.QUEUE_FETCHED

            self.r = redis.StrictRedis(host=self.host, port=self.port, db=0)
            logger.debug('Connectio %s:%d redis' % ( self.host, self.port ))
    
    def run(self):
        while True:
            #print 'run loop...'
            url = self.r.brpop(self.QUEUE_TODO)
            #suppose url is validate
            logger.debug('get %s' % url[1])
            self.strategy.append(url[1])

            if self.strategy.todo_count() != 0:
                item = self.template_cls(self.strategy.pop())
                item.fetch()
                logger.debug('crawl %s' % url[1])
                url_list = item.parse()
                
                #self.visited_list.append(item.url)
                #self.strategy.append(item.url)
                self.strategy.make_visited(item.url)

                #save
                self.save(item)
                
                for l in url_list:
                    self.r.lpush(self.QUEUE_FETCHED, l)
                    logger.debug('push %s' % l)

                #url_list process
                #self.strategy.extend_list(url_list)

    def save(self, item):
        m = hashlib.md5()
        m.update(item.url)
        file_name = m.hexdigest()
        full_path = os.path.join(os.getcwd(), 'data', file_name)
        with open(full_path, 'w+') as f:
            info = "version:%s\nurl:%s\n" % (self.settings.VERSION, item.url)
            f.write(info)

            dt = datetime.today()
            nowtime = "date:%d-%d-%d %d-%d-%d\n" % ( dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second )
            f.write(nowtime)
            
            f.write(item.getHeader())
            f.write('\n')

            f.write(item.getHtmlBody())
