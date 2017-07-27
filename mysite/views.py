# coding=utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.contrib import messages

from mysite import models

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
    '''使用ajax添加商品'''
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
    '''使用ajax获取cart总数'''
    if request.method == 'GET' and request.is_ajax():
        return JsonResponse(dict(cart_num = Cart(request).count()))

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

    



