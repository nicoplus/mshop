#_*_ coding: utf-8 _*_

from django import forms
from django.forms import ModelForm

from mysite import models


class OrderForm(ModelForm):
	class Meta:
		model = models.Order
		fields = ['full_name', 'address', 'phone']

	def __init__(self, *args, **kws):
		super(OrderForm , self).__init__(*args, **kws)
		self.fields['full_name'].label = '收件人'
		self.fields['phone'].label = '联系电话'
		self.fields['address'].label = '收件地址'
