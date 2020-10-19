import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from car.cart import Cart, Books
from car.models import GoodsCar
from index.models import Book
from user.models import User
from indent.models import Addressee, List, BookList
import re,time



def indent(request):
    request.session["backcart"] = Cart()
    name = request.session.get('name')
    is_login = request.session.get("is_login")
    uid = request.session.get('id')
    address_list = request.GET.get('address_list')
    print(address_list)
    cart = Cart()
    address = Addressee.objects.filter(user_id=uid)
    print(address.count())
    address_list = Addressee.objects.filter(address=address_list)
    id1 = GoodsCar.objects.filter(user_id=uid)
    s = 0
    for i in id1:
        cart.add(i.book_id, i.num)
        book = Books(i.book_id, i.num)
        s += book.getTolPrice
    request.session['s'] = s
    request.session['order'] = cart
    content = {
        's': s,
        'cartlist': cart.book_list,
        'name': name,
        'is_login': is_login,
        'address': address,
        'address_list': address_list,
    }
    return render(request, 'indent.html', content)


def indent_logic(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    address_id = request.POST.get("address_id")
    post = request.POST.get('post')
    phone = request.POST.get('phone')
    tel = request.POST.get('tel')
    uid = request.session.get('id')
    user = User.objects.filter(id=uid)[0]
    if name:
        if address:
            if len(post) == 6:
                if re.findall(r'\(?0\d{2,3}[)-]?\d{7,8}', tel) or re.findall(r'^(1\d)\d{9}$', phone):
                    if not Addressee.objects.filter(id=address_id):
                        cur_address = Addressee.objects.create(name=name, address=address, telephone=tel,
                                                               cellphone=phone, post_code=post,
                                                               user=user)
                    else:
                        cur_address = Addressee.objects.filter(id=address_id)[0]

                    od = request.session.get('order')
                    bc = request.session.get('backcart')
                    for i in bc.book_list:
                        for j in od.book_list:
                            if i.id == j.id:
                                od.removeBook(j.id)
                    request.session['order'] = od
                    cost_sum = 0
                    for book in od.book_list:
                        cost_sum += book.getTolPrice
                    list = List.objects.create(code=int(time.time()), date=datetime.now(), store="当当网", user=user,
                                               adressee=cur_address,price=cost_sum)
                    request.session['orderlist']=list
                    for i in od.book_list:
                        cur_book = Book.objects.filter(id=i.id)[0]
                        BookList.objects.create(book=cur_book, list=list, num=i.count)

                    for cur_book in GoodsCar.objects.all(): cur_book.delete()
                    backbook = request.session.get('backcart')
                    for book in backbook.book_list:
                        cur_book = Book.objects.filter(id=book.id)[0]
                        GoodsCar.objects.create(user=user, book=cur_book, num=book.count)
                    request.session["backcart"] = Cart()
                    return HttpResponse("ok")
                else:
                    return HttpResponse("wrongphone")
            else:
                return HttpResponse("wrongpost")
        else:
            return HttpResponse("wrongaddress")
    else:
        return HttpResponse("wrongname")


def indent_ok(request):
    orderlist = request.session.get('orderlist')
    od = request.session.get('order')
    num = len(od.book_list)
    id = orderlist.adressee_id
    person = Addressee.objects.filter(id=id)[0]

    content = {
        'num':num,
        'person':person,
        'orderlist':orderlist,
    }
    return render(request, 'indent ok.html', content)


def address(request):
    id = request.POST.get('sel')
    ad = Addressee.objects.filter(id=id)[0]

    def default(u):
        if isinstance(u, Addressee):
            return {'id': u.id, 'name': u.name, 'address': u.address, 'telephone': u.telephone,
                    'cellphone': u.cellphone, 'post_code': u.post_code, 'user_id': u.user_id}

    json_str = json.dumps(ad, default=default)  # 将QuerySet对象转为list
    return HttpResponse(json_str)


def back_to_car(request):
    this = request.POST.get('book_id')
    uid = request.session.get("id")
    book = GoodsCar.objects.filter(book_id=this, user_id=uid)[0]
    cart = request.session.get("backcart")
    if not cart:
        cart = Cart()
    t = cart.add(book.book_id, book.num)
    request.session["backcart"] = cart
    if t == 1:
        print("no")
    else:
        print("Yes")
    print(cart.book_list, len(cart.book_list))
    # for i in cart.book_list:
    #     print(22222222222222, i.name)
    print(book.book_id)

    return HttpResponse('1')
