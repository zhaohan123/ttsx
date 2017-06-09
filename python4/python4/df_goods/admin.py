#coding=utf-8
from django.contrib import admin
from models import *

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']
    actions_on_top = True
    actions_on_bottom = True
class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id','gtitle','gprice','gunit','gclick','gkucun','gtype']


 	
 	
admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)