# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/yFcocJbfS9Hs375NhE8Gbw
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/20 0:08 
@本段代码的视频说明     ：
'''

import office

office.image.add_watermark(file='./test_files/add_watermark/程序员晚枫-2.jpg',
                           mark='公众号：程序员晚枫',
                           output_path=r'./test_files/add_watermark/mark_img')
