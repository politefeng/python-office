# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/yFcocJbfS9Hs375NhE8Gbw
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/15 0:40 
@本段代码的视频说明     ：
'''

import popdf

popdf.pdf2docx(file_path=r'./test_files/pdf2docx/程序员晚枫（作品合集）.pdf',
               output_path=r'./test_files/pdf2docx/output')
