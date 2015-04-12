# -*- coding: utf-8 -*-
'''
    author: assassinpig
    email: assassinpig@gmail.com
'''
import requests
class CrawlerItem(object):
    url = None
    html_body = None
    refer = None
    headers = None

    def __init__(self, url):
        self.url = url
        self.refer = url.split('/')[2] 

    def fetch(self):
        try:
            res = requests.get(self.url)
            content_type = res.headers.get('Content-type')

            #todo add filter
            if content_type == 'text/html':
                self.html_body = res.content 
                self.headers = ''
                for key in res.headers:
                    self.headers += ( '%s: %s\n' % (key, res.headers[key]))
        except:
            print 'exception occurs when fetching %s' % self.url
        finally:
            if self.html_body is None:
                self.html_body = ''
            if self.headers is None:
                self.headers = ''

    def parse(self):
        pass

    def getHtmlBody(self):
        return self.html_body

    def getHeader(self):
        return self.headers

