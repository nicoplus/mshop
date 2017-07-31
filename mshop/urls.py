"""mshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, static
from django.contrib import admin
from django.conf import settings

from mysite import views



urlpatterns = [
    url(r'^order/$', views.order),
    url(r'^myorders/$', views.my_orders),
    url(r'^removeitem/(\d+)/$', views.remove_from_cart, name='removeitem_id'),
    url(r'^api/cart_num/$', views.go_cart_num, name='cart_num'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^additem/(\d+)/(\d+)/$', views.add_to_cart, name = 'additem_id'),
    url(r'^api/add/(\d+)/(\d+)/$', views.go_add, name='go_add'),
    url(r'^product/(\d+)$', views.product, name='product_url'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^(\d*)$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^filer/', include('filer.urls')),
]
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
