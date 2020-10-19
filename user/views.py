import re
import string
import random
from captcha.image import ImageCaptcha
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from car.cart import Cart
from car.models import GoodsCar
from index.models import Book
from user.models import User


def login(request):
    name = request.COOKIES.get("name")
    password = request.COOKIES.get("pwd")
    d = User.objects.filter(name=name, password=password)  # cookie中存姓名密码自动登录

    level = request.GET.get('level')
    id = request.GET.get('idd')
    num = request.GET.get('num')
    idd = request.GET.get('id')  # 从跳转前页面的Ajax中获得参数 再传递到login页面实现跳转

    location = request.GET.get('location')  # 实现页面跳转的参数“从哪来回哪去”
    request.session['location'] = location  # 将参数写入session其他views函数可以使用
    content = {
        'level': level,
        'id': id,
        'num': num,
        'idd': idd
    }
    if d:
        request.session["is_login"] = True
        return redirect("index:index")  # 自动登陆后记录登陆状态重定向到主页
    return render(request, 'login.html', content)  # 主页的渲染


def login_logic(request):
    name = request.POST.get('name')
    a = User.objects.filter(name=name)[0]
    id = a.id  # 先获得用户id和name，以便之后记录用户id和name并存入session
    password = request.POST.get('password')
    d = User.objects.filter(name=name, password=password)  # 登录逻辑验证用户名密码是否匹配
    captcha = request.POST.get('code')
    code = request.session.get('code')  # 实现验证码功能 前端输入框中的内容和get_captcha函数中存入session的内容做对比
    location = request.session.get('location')  # 取出login函数中的参数 实现“从哪来回哪去”
    autologin = request.POST.get('autologin')  # 记住密码的勾选框
    if d and captcha.lower() == code.lower():  # 前端输入框中的内容和get_captcha函数中存入session的内容做对比
        request.session["is_login"] = True
        request.session["name"] = name
        request.session["id"] = id  # 记录用户id和name以及是否记住密码 并存入session 其他页面登陆状态和购物时都需要显示用户信息

        if location == 'booklist':
            run1 = HttpResponse("ok_booklist")
            if autologin:
                run1.set_cookie("name", name)
                run1.set_cookie("pwd", password)
                cart = request.session.get("cart", Cart())  # 从session中读取相应的购物车对象

                for a in cart.book_list:
                    uid = request.session.get('id')
                    cart0 = GoodsCar.objects.filter(user_id=uid, book_id=id)
                    if not cart0:
                        user = User.objects.filter(id=uid)[0]
                        book = Book.objects.filter(id=a.id)[0]
                        GoodsCar.objects.create(user=user, book=book, num=a.count)
                    else:
                        cart0 = cart0[0]
                        cart0.num += a.count
                        cart0.save()
                cart.book_list = []
                request.session['cart'] = cart
                return run1
            cart = request.session.get("cart", Cart())  # 从session中读取相应的购物车对象

            for a in cart.book_list:
                uid = request.session.get('id')
                cart0 = GoodsCar.objects.filter(user_id=uid, book_id=id)
                if not cart0:
                    user = User.objects.filter(id=uid)[0]
                    book = Book.objects.filter(id=a.id)[0]
                    GoodsCar.objects.create(user=user, book=book, num=a.count)
                else:
                    cart0 = cart0[0]
                    cart0.num += a.count
                    cart0.save()
            cart.book_list = []
            request.session['cart'] = cart
            return run1


        elif location == 'bookdetails':
            run2 = HttpResponse("ok_bookdetails")
            if autologin:
                run2.set_cookie("name", name)
                run2.set_cookie("pwd", password)
                cart = request.session.get("cart", Cart())  # 从session中读取相应的购物车对象

                for a in cart.book_list:
                    uid = request.session.get('id')
                    cart0 = GoodsCar.objects.filter(user_id=uid, book_id=id)
                    if not cart0:
                        user = User.objects.filter(id=uid)[0]
                        book = Book.objects.filter(id=a.id)[0]
                        GoodsCar.objects.create(user=user, book=book, num=a.count)
                    else:
                        cart0 = cart0[0]
                        cart0.num += a.count
                        cart0.save()
                cart.book_list = []
                request.session['cart'] = cart
                return run2
            cart = request.session.get("cart", Cart())  # 从session中读取相应的购物车对象

            for a in cart.book_list:
                uid = request.session.get('id')
                cart0 = GoodsCar.objects.filter(user_id=uid, book_id=id)
                if not cart0:
                    user = User.objects.filter(id=uid)[0]
                    book = Book.objects.filter(id=a.id)[0]
                    GoodsCar.objects.create(user=user, book=book, num=a.count)
                else:
                    cart0 = cart0[0]
                    cart0.num += a.count
                    cart0.save()
            cart.book_list = []
            request.session['cart'] = cart
            return run2


        elif location == 'indent':
            run3 = HttpResponse("ok_indent")
            if autologin:
                run3.set_cookie("name", name)
                run3.set_cookie("pwd", password)
                cart = request.session.get("cart", Cart())  # 从session中读取相应的购物车对象

                for a in cart.book_list:
                    uid = request.session.get('id')
                    cart0 = GoodsCar.objects.filter(user_id=uid, book_id=id)
                    if not cart0:
                        user = User.objects.filter(id=uid)[0]
                        book = Book.objects.filter(id=a.id)[0]
                        GoodsCar.objects.create(user=user, book=book, num=a.count)
                    else:
                        cart0 = cart0[0]
                        cart0.num += a.count
                        cart0.save()
                cart.book_list = []
                request.session['cart'] = cart
                return run3
            cart = request.session.get("cart", Cart())  # 从session中读取相应的购物车对象

            for a in cart.book_list:
                uid = request.session.get('id')
                cart0 = GoodsCar.objects.filter(user_id=uid, book_id=id)
                if not cart0:
                    user = User.objects.filter(id=uid)[0]
                    book = Book.objects.filter(id=a.id)[0]
                    GoodsCar.objects.create(user=user, book=book, num=a.count)
                else:
                    cart0 = cart0[0]
                    cart0.num += a.count
                    cart0.save()
            cart.book_list = []
            request.session['cart'] = cart
            return run3


        else:
            run4 = HttpResponse("ok_index")
            if autologin:
                run4.set_cookie("name", name)
                run4.set_cookie("pwd", password)
                cart = request.session.get("cart", Cart())  # 从session中读取相应的购物车对象

                for a in cart.book_list:
                    uid = request.session.get('id')
                    cart0 = GoodsCar.objects.filter(user_id=uid, book_id=id)
                    if not cart0:
                        user = User.objects.filter(id=uid)[0]
                        book = Book.objects.filter(id=a.id)[0]
                        GoodsCar.objects.create(user=user, book=book, num=a.count)
                    else:
                        cart0 = cart0[0]
                        cart0.num += a.count
                        cart0.save()
                cart.book_list = []
                request.session['cart'] = cart
                return run4
            cart = request.session.get("cart", Cart())  # 从session中读取相应的购物车对象

            for a in cart.book_list:
                uid = request.session.get('id')
                cart0 = GoodsCar.objects.filter(user_id=uid, book_id=id)
                if not cart0:
                    user = User.objects.filter(id=uid)[0]
                    book = Book.objects.filter(id=a.id)[0]
                    GoodsCar.objects.create(user=user, book=book, num=a.count)
                else:
                    cart0 = cart0[0]
                    cart0.num += a.count
                    cart0.save()
            cart.book_list = []
            request.session['cart'] = cart
            return run4

    elif not d:
        return HttpResponse('用户名或密码错误')
    else:
        return HttpResponse('验证码错误')  # 登陆失败后向前端页面Ajax传递的内容


def register(request):
    return render(request, 'register.html')


def register_logic(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    captcha = request.POST.get('code')
    code = request.session.get('code')
    agreement = request.POST.get('agreement')
    repassword = request.POST.get('repassword')
    print(agreement)
    d = User.objects.filter(name=name)
    if agreement == 'true':
        if captcha.lower() == code.lower():
            if repassword == password:
                if not d:
                    User.objects.create(name=name, password=password)
                    return HttpResponse("注册成功")
                else:
                    return HttpResponse("注册失败!用户名已存在!")
            else:
                return HttpResponse('密码不一致')
        return HttpResponse("验证码错误")
    else:
        return HttpResponse("请勾选“我同意”")


def get_captcha(request):
    code_list = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 4)
    code = ''.join(code_list)
    print(code)
    img = ImageCaptcha()
    data = img.generate(code)
    request.session['code'] = code
    return HttpResponse(data)


# def check_name(request):
#     name = request.POST.get('name')
#     user_name = User.objects.values('name')
#     print(user_name)
#     for a in user_name:
#         if a['name'] == name:
#             print(1)
#             return HttpResponse('该用户存在')
#     else:
#         return HttpResponse('该用户不存在')

def check_name(request):
    name = request.POST.get('name')
    user_name = User.objects.filter(name=name)
    if '@' in name and '.' in name or len(name) == 11:
        if user_name:
            return HttpResponse('该用户存在')
        else:
            return HttpResponse('该用户不存在')
    else:
        return HttpResponse('请输入正确的手机号或邮箱')


def check_password(request):
    password = request.POST.get('password')
    if 6 > len(password) > 0:
        return HttpResponse('1')
    elif len(password) >= 6 and password.isdigit():
        return HttpResponse('2')
    elif len(password) >= 6 and bool(re.search('[a-z]', password)):
        return HttpResponse('3')


def register_ok(request):
    name = User.objects.all()
    num = name.count()
    result = name[num - 1:num][0]
    r = result.name
    print(result)
    return render(request, 'register ok.html', {'r': r})


def logout(request):
    request.session.flush()
    response = redirect('user:login')  # 改成重定向等都可以
    response.delete_cookie('name')
    response.delete_cookie('password')
    return response
