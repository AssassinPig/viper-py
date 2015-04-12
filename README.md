##viper-py
----------
    viper-py is a crawler framework written by python
here are more detail info: [schedule](https://github.com/AssassinPig/viper-py/blob/master/schedule.md)

###target
    1. 分布式爬虫
    2. 每个worker节点拥有bsf/dsf策略
    3. 添加保存页面功能
###usage
    1. 需要在master上安装redis
    2. 在worker上修改配置settings.py
    3. open example then write your self's XXXCrawlerItem class which inherit from class CrawlerItem 
    4. 
        ``` 	
    	mkdir data
    	python run_master.py
    	python run_worker.py
	```

##distributed crawler implemented with redis
------
    <br>
    ```
                            master 
                            /     \              
                           /       \
                          /         \
                     put /           \  get
                        /             \
                       /    redis      \
                      /     /   \       \
                myspider.todo    myspider.fetched   
                     \                  / 
                      \                /
                       \              /
                    get \            / put
                         \          /  
                          \        /
                           \      /
                            woker1 worker2 ... workern
    ```

    1. master put url node to todo list
    2. worker get url noode from todo list
    3. worker fetch and parse page
    4. worker put new url node to fetched list
    5. master get url node from fetched list 
    6. repeat from 1

##todo
------
1. bloom filter
2. avoid ban
3. watermark for worker
4. save page to separate file autoly
