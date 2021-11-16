from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


class Book():
    def __init__(self, title, price, position):
        self.title = title
        self.price = price
        self.position = position

    def __str__(self):
        return self.title + self.price + self.position


def index(request):
    name = "张三"
    age = 12
    grade = 91
    book_list = ["三国演义", "水浒传", "西游记", "红楼梦"]
    book1 = Book("许三观卖血记", 59.9, "菠萝出版社")
    book2 = Book("活着", 69.9, "西瓜出版社")
    book3 = Book("我们生活在巨大的差距里", 49.9, "香蕉出版社")
    book4 = Book("世事如烟", 55.9, "西瓜出版社")
    list_book = [book1, book2, book3, book4]
    return render(request, "app02/index.html", locals())


def order(request):
    return render(request, "app02/order.html")


def login(request):
    path = reverse("ind")
    return redirect(path)