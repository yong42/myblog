from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def hello(request):
    return HttpResponse('欢迎使用Django!')


# def index(request):
    # sitename = 'Django中文网'
    # url = 'www.django.cn'
    # list=[
    #     '开发前的准备',
    #     '项目需求分析',
    #     '数据库设计分析',
    #     '创建项目',
    #     '基础配置',
    #     '欢迎页面',
    #     '创建数据库模型',
    #
    # ]
    # mydict={
    #     'name': 'A',
    #     'qq': '111',
    #     'wx': 'vipdjango',
    #     'email': '111@qq.com',
    #     'Q群': '111',
    # }
    # context={
    #     'sitename':sitename,
    #     'url':url,
    #     'list':list,
    #     'mydict':mydict,
    # }
    # return render(request,'index.html',context)

def index(request):
    allarticle=Article.objects.all()
    context={
        'allarticle':allarticle,
    }
    return render(request,'index.html',context)
