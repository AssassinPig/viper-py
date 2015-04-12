##schedule
------
1. 更新feature
    1. 爬取dzwww
    2. 处理特定链接：
        1. 空网站
        2. 打不开的页面
        3. 链接之中有猫 如
            ```html
            <a href="javascript:;" id="weixin">关注微信</a>
            ```
            mailto:xxxx@gmail.com
            处理各种Content-type, 比如各种.apk .mp3等等

    3.模块化 
2. 研究python lib打包
3. 更新文档说明


##bloom filter
------
原理:
    开辟一块空间，作为bit数组使用
    当接受到input数据的时候，使用几个hash函数，求的几个数字，然后在bit数组中对应标识
    当验证的时候，也是通过hash函数求的几个数字，然后判断是否在bit数组中存在

key问题:
    hash函数要足够快
    [murmur](https://sites.google.com/site/murmurhash/)
    [fnv](http://isthe.com/chongo/tech/comp/fnv/)
    [Jenkins Hashes](http://www.burtleburtle.net/bob/hash/doobs.html)

    要存多少元素        标记为n
    要开辟多大的bit数组       m
    要多少hash散列函数        k
    k: (m/n)ln(2) 

准确率
    false positive rate will be approximately (1-e-kn/m)k

[](http://www.zhihu.com/question/20899988)
[](http://billmill.org/bloomfilter-tutorial/)

##reference
------
[](http://python-rq.org/)
[](https://github.com/nvie/rq)
[](http://www.rabbitmq.com/)

[DSpark解析](http://qinxuye.me/category/distributed_computing/)

[huey](http://xiaorui.cc/2014/09/09/%E4%BD%BF%E7%94%A8python%E7%9A%84%E5%88%86%E5%B8%83%E5%BC%8F%E4%BB%BB%E5%8A%A1%E9%98%9F%E5%88%97huey%E5%AE%9E%E7%8E%B0%E4%BB%BB%E5%8A%A1%E7%9A%84%E5%BC%82%E6%AD%A5%E5%8C%96/)

[cola分布式框架](http://qinxuye.me/article/cola-a-distributed-crawler-framework/)

[DSpark](https://github.com/jackfengji/test_pro/wiki)

[article extractor](https://github.com/grangier/python-goose)
