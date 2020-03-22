#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render #返回一个网页给用户

def home(request):#request固定，代表用户请求，也就是前面的urls里匹配到模式后调用这个函数的行为
    #return 'hello' #示例，实际上是不能给用户返回'hello'的，要引入django模块
    return render(request,'home.html')
    #创建一个网页，一般设置一个template文件夹放网页模板
    #同时要去setting.py里找到TEMPLATES，设置指定目录寻找网页
def count(request):
    user_text =request.GET['text'] #得到text文本框里的内容
    total_count = len( user_text ) #得到长度

    #制作一个统计各个字符个数的字典
    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    #对各个字符的统计结果排个序（降序）
    sorted_dict = \
        sorted(word_dict.items(), key= lambda w: w[1], reverse =True )
    #字典本身是不可迭代的 匿名函数传入item的tuple，以值排序

    return render(request,'count.html',
                  {'count': total_count , 'text': user_text ,
                   'dict': word_dict , 'sorted': sorted_dict })
    #以字典的方式传递给html  字典里面可以放字典
