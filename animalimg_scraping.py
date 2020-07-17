#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:01:38 2020

@author: hajime.b
"""


from icrawler.builtin import BingImageCrawler
crawler = BingImageCrawler(storage={"root_dir": "/Users/hajime.b/Documents/animals/dogs"})
crawler.crawl(keyword="犬", max_num=100)

crawler = BingImageCrawler(storage={"root_dir": "/Users/hajime.b/Documents/animals/cats"})
crawler.crawl(keyword="猫", max_num=100)

crawler = BingImageCrawler(storage={"root_dir": "/Users/hajime.b/Documents/animals/gorillas"})
crawler.crawl(keyword="ゴリラ", max_num=100)

crawler = BingImageCrawler(storage={"root_dir": "/Users/hajime.b/Documents/animals/Giraffes"})
crawler.crawl(keyword="キリン", max_num=100)

crawler = BingImageCrawler(storage={"root_dir": "/Users/hajime.b/Documents/animals/Lions"})
crawler.crawl(keyword="ライオン", max_num=100)