from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from car.cart import Cart, Book
from car.models import GoodsCar
from user.models import User


def cart(request):
    name = request.session.get('name')
    is_login = request.session.get("is_login")
    id = request.POST.get("id")
    uid = request.session.get('id')
    if is_login:


        cart00 = Cart()
        id1 = GoodsCar.objects.filter(user_id=uid)
        for i in id1:
            cart00.add(i.book_id, i.num)
        content = {
            'cartlist': cart00.book_list,
            'name': name,
            'is_login': is_login,
        }
        return render(request, "car.html", content)
    else:
        cart = request.session.get("cart", Cart())
        content = {
            'cartlist': cart.book_list,
            'name': name,
            'is_login': is_login,

        }
        return render(request, "car.html", content)


def add_goods(request):
    id = request.POST.get("id")
    count = request.POST.get("count")
    num = request.POST.get("num", 1)
    is_login = request.session.get("is_login")
    if is_login:
        uid = request.session.get('id')
        cart0 = GoodsCar.objects.filter(user_id=uid, book_id=id)
        print(cart0)
        if not cart0:
            user = User.objects.filter(id=uid)[0]
            book = Book.objects.filter(id=id)[0]
            GoodsCar.objects.create(user=user, book=book, num=int(count))
        else:
            cart0 = cart0[0]
            cart0.num += int(count) * int(num)
            cart0.save()

    else:
        cart = request.session.get("cart")
        if not cart:
            cart = Cart()
        else:
            cart = request.session.get("cart")
        cart.add(id, int(count) * int(num))
        request.session["cart"] = cart
    return HttpResponse("")


def delete_goods(request):
    is_login = request.session.get("is_login")
    id = request.POST.get("id")
    uid = request.session.get('id')
    if is_login:
        cart00 = GoodsCar.objects.filter(user_id=uid, book_id=id)[0]
        cart00.delete()
    else:
        cart = request.session.get("cart")
        cart.removeBook(id)

        request.session["cart"] = cart
        print(len(request.session.get("cart")))
        return HttpResponse("1")
