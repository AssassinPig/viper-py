# -*- coding: utf-8 -*-
import settings

from viper import Crawler
from viper import CrawlerItem
from viper import Strategy
from viper import get_logger

import hashlib
import os
from datetime import *

import lxml.html as LH
from StringIO import StringIO

logger = get_logger(name="worker", file_name="worker.log")

class DzwwwItem(CrawlerItem):
    def __init__(self, url):
        super(DzwwwItem, self).__init__(url)

    def parse(self):
        url_list = []
        if len(self.html_body) <= 0:
            return url_list

        strHtml = StringIO(self.html_body)
        tree = LH.parse(strHtml)
        l = tree.xpath('//a[@href]/@href')

        for i, elem  in enumerate(l):
            if l[i].find('http:') == 0:
                url_list.append(l[i])
            else:
                #filte invalidate href 
                if l[i].find('mailto') == 0:
                    continue

                url = 'http://%s%s' % (self.refer, l[i])
                url_list.append(url)

        return url_list


class Item36kr(CrawlerItem):
    def __init__(self, url):
        super(Item36kr, self).__init__(url)

    def parse(self):
        strHtml = StringIO(self.html_body)
        tree = LH.parse(strHtml)
        l1 = tree.xpath('//article/div/h1/a[@href]/@href')
        l2 = tree.xpath('//li[@class=\'next_page\']/a[@href]/@href')

        url_list = []
        for i, elem  in enumerate(l1):
            if l1[i].find('http:') == 0:
                url_list.append(l1[i])
            else:
                url = 'http://%s%s' % (self.refer, l1[i])
                #print 'new url: %s' % url
                url_list.append(url)

        for i, elem in enumerate(l2):
            print 'next page %s' % l2[i]
            if l2[i].find('http:') == 0:
                url_list.append(l2[i])
            else:
                url = 'http://%s%s' % (self.refer, l2[i])
                print 'new url: %s' % url
                url_list.append(url)

        return url_list


class WoaiduCrawlerItem(CrawlerItem):
    def __init__(self, url):
        super(WoaiduCrawlerItem, self).__init__(url)

    def parse(self):
        strHtml = StringIO(self.html_body)
        tree = LH.parse(strHtml)
        url_list = []
        for i, elem  in enumerate(l1):
            l1 = tree.xpath('//div[@class=\'wudongqiank\']/a[@href]/text()')
            l2 = tree.xpath('//div[@class=\'wudongqiank\']/a[@href]/@href')
            #print elem.encode('utf8')
            #print l2[i].encode('utf8')
            if l2[i].find('http:') == 0:
                url_list.append(l2[i])
            else:
                url = 'http://%s%s' % (self.refer, l2[i])
                #print 'new url: %s' % url
                url_list.append(url)

        #print url_list
        return url_list
