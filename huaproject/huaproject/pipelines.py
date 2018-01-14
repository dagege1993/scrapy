# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib


class HuaprojectPipeline(object):
    def __init__(self):
        # 重写构造方法,在这儿打开文件
        self.fp = open('spider.json', 'w', encoding='utf-8')

    def open_spider(self, spider):
        pass

    # 在这里处理每一个item
    def process_item(self, item, spider):
        # 将对象转换为字典
        obj = dict(item)

        # 本地的路径
        dirpath = r'/home/hlz/Desktop/huaproject/huaproject/images'
        # 获取图片后缀名
        # 分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作
        suffix = os.path.splitext(obj['image_url'])[-1]

        # 拼接文件名
        filename = obj['like'] + obj['name'] + suffix
        # 将文件路径和文件名拼接的文件全路径
        filepath = os.path.join(dirpath, filename)
        # 下载图片
        #urlretrieve() 方法直接将远程数据下载到本地。urlretrieve(url, filename=None,)
        #参数 finename 指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
        urllib.request.urlretrieve(obj['image_url'], filepath)

        # 将obj转换为字符串
        #dumps是将dict转化成str格式
        string = json.dumps(obj, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    # 重写这个方法,在关闭spider的时候将文件资源关闭
    def close_spider(self, spider):
        self.fp.close()
