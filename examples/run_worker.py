# -*- coding: utf-8 -*-
from viper import Worker
from viper import Strategy
from item import DzwwwItem, Item36kr
import settings

from multiprocessing import Pool, Process

def generate_process(i):
    start_urls = []
    strategy = Strategy(Strategy.BSF)
    template_item = DzwwwItem
    worker = Worker(start_urls=start_urls, strategy=strategy, settings=settings, template_cls=template_item)
    worker.run()

if __name__ == '__main__':
    #i = settings.WORKER_NUM 
    #if i is None:
    #    i = 5
    #p = Pool(5)
    #params = range(5)

    #debug
    p = Process(target=generate_process, args=(1,)) 
    p.start()
    p.join()
