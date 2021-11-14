import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template


def index(request):
    # # 获取模板文件
    # template = get_template("index.html")
    # # 获取数据
    # context = {"name": "main"}
    # # 渲染
    # html = template.render(context, request)
    # print(":::", html)
    # return HttpResponse(html)
    return render(request, "index.html", {"name": "zhangsan"})


class Book():
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return "作品：" + self.title + "\t\t价格：" + self.price


def auth(request):
    name = "root"
    age = 22
    is_married = "否"
    book_list = ["三国演义", "水浒传", "西游记", "红楼梦"]
    zhangsan = {"name": "张三", "age": 33}
    book1 = Book("许三观卖血记", "59.9")
    book2 = Book("活着", "69.9")
    book3 = Book("我们生活在巨大的差距里", "49.9")
    list_book = [book1, book2, book3]
    return render(request, "auth.html", locals())


def filter(request):
    book1 = Book("许三观卖血记", "59")
    book2 = Book("活着", "69")
    book3 = Book("我们生活在巨大的差距里", "49")
    list_book = [book1, book2, book3]
    nowtime = datetime.datetime.now()
    booksize = 15555555
    speak = "i love you ~"
    context = "<script>alert(123)</script>"
    return render(request, "filter.html", locals())


def me_filter(request):
    """自定义过滤器 filters"""
    moblie_number = "13312345678"
    return render(request, "mefilter.html", locals())
