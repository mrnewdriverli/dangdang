from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from index.models import Classify, Book


def index(request):
    name = request.session.get('name')
    is_login = request.session.get("is_login")
    cate1 = Classify.objects.filter(level=1)
    cate2 = Classify.objects.filter(level=2)
    book = Book.objects.all().order_by('-publish_date')
    rec = Book.objects.all().order_by('-comment_num')
    salenum = Book.objects.all().order_by('-sale_num')[:5]
    list1 = [obj.price * obj.discount for obj in salenum][::-1]
    list11 = [obj.price * obj.discount for obj in salenum][::-1]
    list2 = [obj.price * obj.discount for obj in rec][::-1]
    list3 = [obj.price * obj.discount for obj in book][::-1]
    content = {
        'cate1': cate1,
        'cate2': cate2,
        'book': book,
        'rec': rec,
        'salenum': salenum,
        'list1': list1,
        'list11': list11,
        'list2': list2,
        'list3': list3,
        "is_login": is_login,
        'name': name,
    }
    return render(request, 'index.html', content)


def booklist(request):
    is_login = request.session.get("is_login")
    cate1 = Classify.objects.filter(level=1)
    cate2 = Classify.objects.filter(level=2)
    id = request.GET.get('id', "1")  # 获取前端传过来的id的值(Classify)
    version = request.GET.get("version", "1")
    num = request.GET.get('num', 1)  # 获取前端传过来的页数的值(页数，默认为第一页)
    level = request.GET.get('level', "1")  # 获取前端传过来的level的值(Classify)
    # cate = Classify.objects.filter(id=id)
    main = None
    cate = None

    books = None
    books1 = None
    books2 = None
    books3 = None

    if level == '1':  # 如果查询的是一级标题
        main = Classify.objects.filter(id=id)[0]

        if version == "1":
            books = Book.objects.filter(classify__sup_id=id)  # 对于2级标题的查询(所有Book中二级分类的id为通过GET方式获取的"id"的所有图书)
        elif version == "2":
            books1 = Book.objects.filter(classify__sup_id=id).order_by('-comment_num')
        elif version == "3":
            books2 = Book.objects.filter(classify__sup_id=id).order_by('-publish_date')
        else:
            books3 = Book.objects.filter(classify__sup_id=id).order_by('-price')

    if level == '2':
        cate = Classify.objects.filter(id=id)[0]
        main = Classify.objects.filter(id=cate.sup_id)[0]
        if version == "1":
            books = Book.objects.filter(classify_id=id)  # 对于2级标题的查询(所有Book中二级分类的id为通过GET方式获取的"id"的所有图书)
        elif version == "2":
            books1 = Book.objects.filter(classify_id=id).order_by('-comment_num')
        elif version == "3":
            books2 = Book.objects.filter(classify_id=id).order_by('-publish_date')
        else:
            books3 = Book.objects.filter(classify_id=id).order_by('-price')

    print(books, books1, books2, books3)
    paginator = None
    if books: paginator = Paginator(books, per_page=2)
    if books1: paginator = Paginator(books1, per_page=2)
    if books2: paginator = Paginator(books2, per_page=2)
    if books3: paginator = Paginator(books3, per_page=2)

    pages = paginator.num_pages
    page = paginator.page(num)
    name = request.session.get('name')
    content = {
        'cate1': cate1,
        'cate2': cate2,
        'books': books,
        'books1': books1,
        'books2': books2,
        'books3': books3,
        'page': page,
        'main': main,
        'cate': cate,
        'id': id,
        'level': level,
        'pages': pages,
        "is_login": is_login,
        'name': name,
    }
    return render(request, 'booklist.html', content)


def bookdetails(request):
    """
    :param request:
    :return:

        通过书的id获取它的一级分类和二级分类
     一级分类:
        Classify.objects.filter(id=book.classify.sup_id)
     二级分类:
        1. Classify.objects.filter(id=book.classify.id)
        2. er_id = book.classify.id
    """
    is_login = request.session.get("is_login")
    name = request.session.get('name')
    id = request.GET.get('id')
    book = Book.objects.get(id=id)
    list5 = [book.price * book.discount][::-1]
    b = Book.objects.get(id=id)
    a = b.classify
    main0 = a.id
    cate0 = a.sup_id
    main = Classify.objects.filter(id=main0)[0]
    cate = Classify.objects.filter(id=cate0)[0]
    content = {
        'book': book,
        'list5': list5[0],
        "id": id,
        "is_login": is_login,
        'name': name,
        "cate": cate,
        "main": main
    }
    return render(request, 'Book details.html', content)
