# coding=utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from cart.cart import Cart
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.contrib import messages

from mysite import models, forms

from datetime import date

# Create your views here.

def index(request, cat_id=0):
    all_products = None
    if cat_id > 0:
        try:
            category = models.Category.objects.get(id = cat_id)
        except :
            category = None
        if category:
            all_products = models.Product.objects.filter(category=category)

    if not all_products:
        all_products = models.Product.objects.all()

    all_categories = models.Category.objects.all()
    paginator = Paginator(all_products, 5)
    p = request.GET.get('p')
    try:
        products = paginator.page(p)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'index.html', locals())

def product(request, product_id, quantity=1):
    try:
        product = models.Product.objects.get(id=product_id)
    except Exception as e:
        product = None
    return render(request, 'product.html', locals())

@login_required(login_url='accounts/login/')
def cart(request):
    all_categories = models.Category.objects.all()
    cart = Cart(request)
    return render(request, 'cart.html', dict(cart=cart))

@login_required(login_url='accounts/login/')
def add_to_cart(request, product_id, quantity):
    try:
        product = models.Product.objects.get(id = product_id)
        
    except Exception as e:
        messages.add_message(request, messages.WARNING, 'no product that id is {}'.format(product_id))
        print e
        return redirect(index)
    else:
        cart = Cart(request)
        cart.add(product, product.price, quantity)
        messages.add_message(request, messages.SUCCESS, 'product has benn added to cart')
        return redirect(index)

def go_add(request, product_id=0, quantity=1):
    '''api, 使用ajax添加商品'''
    if request.method == 'GET' and request.is_ajax():
        try:
            product = models.Product.objects.get(id = product_id)
            
        except Exception as e:
            messages.add_message(request, messages.WARNING, 'no product that id is {}'.format(product_id))
            print e
        else:
            cart = Cart(request)
            cart.add(product, product.price, quantity)        

    return JsonResponse(dict(cart_num=cart.count()))

def go_cart_num(request):
    '''api, 使用ajax获取cart总数'''
    if request.method == 'GET' and request.is_ajax():
        return JsonResponse(dict(cart_num = Cart(request).count()))

@login_required(login_url='accounts/login/')
def  remove_from_cart(request, product_id):
    try:
        product = models.Product.objects.get(id = product_id)
            
    except Exception as e:
        messages.add_message(request, messages.WARNING, 'no product that id is {}'.format(product_id))
        print e
    else:
        cart_ins = Cart(request)
        cart_ins.remove(product)   
    
    return redirect(cart)

@login_required(login_url='accounts/login/')
def order(request):
    all_categories = models.Category.objects.all()
    cart = Cart(request)

    if request.method == 'POST':
        user = User.objects.get(username = request.user.username)
        new_oreder = models.Order(user = user)
        order_form = forms.OrderForm(request.POST, instance = new_oreder)

        if order_form.is_valid():
            order = order_form.save()
            messages.add_message(request, messages.SUCCESS, 'order has been built')
            for item in cart:
                models.OrderItem.objects.create(order = order,
                                        product = item.product,
                                        price = item.product.price,
                                        quantity = item.quantity)
            cart.clear()
            return redirect(my_orders)

    else:
        order_form = forms.OrderForm()

    return render(request, 'order.html',locals())


@login_required(login_url='accounts/login/')
def my_orders(request):
    all_categories = models.Category.objects.all()
    orders = models.Order.objects.filter(user = request.user)
    for _ in orders:
        print(_)

    return render(request, 'myorders.html', locals())
    



