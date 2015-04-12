# -*- coding: utf-8 -*-

from viper import Master 

import settings

if __name__ == '__main__':
    #start_urls = [ 'http://www.woaidu.org/' ]
    #start_urls = [ 'http://36kr.com/' ]
    start_urls = [ 'http://www.dzwww.com/' ]
    master = Master(settings=settings, start_urls=start_urls)
    master.run()
