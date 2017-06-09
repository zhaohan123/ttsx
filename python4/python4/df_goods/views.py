#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import *
from django.core.paginator import Paginator,Page
from df_cart.models import *


# Create your views here.
def index(request):
    t1_click= GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[0:3]
    t1_new=GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[0:4]
    t1_click1= GoodsInfo.objects.filter(gtype_id=4).order_by('-gclick')[0:3]
    t1_new1=GoodsInfo.objects.filter(gtype_id=4).order_by('-id')[0:4]
    


    context={'title':'首页',
             't1_click':t1_click,'t1_new':t1_new,
             't1_click1':t1_click1,'t1_new1':t1_new1,
             'cart_count':cart_count(request)


             }
    return render(request,'df_goods/index.html',context)

def index2(request,tid):
    
    t1_click= GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')[0:3]
    t1_new=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')[0:4]
    
    click_list=[]
    for click in t1_click:
        click_list.append({'id':click.id,'title':click.gtitle})
    
    new_list=[]
    for new in t1_new:
        new_list.append({'id':new.id,'title':new.gtitle,'price':new.gprice,'pic':new.gpic.name})








    
    context={'click_list':click_list,'new_list':new_list}
    return JsonResponse(context)


def list(request,tid,pindex,sort):
    typeinfo=TypeInfo.objects.get(pk=int(tid))
    news=typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort=='1':

        goods_list=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort=='2':
        goods_list=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    elif sort=='3':
        goods_list=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')  
    paginator=Paginator(goods_list,10)
    page=paginator.page(int(pindex))
    context={
        'title':typeinfo.ttitle,
        'guest_cart':1,
        'page':page,
        'paginator':paginator,
        'typeinfo':typeinfo,
        'sort':sort,
        'news':news,
        'cart_count':cart_count(request)
        }

    return render(request,'df_goods/list.html',context)




def detail(request,id):
    goods=GoodsInfo.objects.get(pk=int(id))
    goods.gclick=goods.gclick+1
    goods.save()

    news=goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context={
        'title':goods.gtype.ttitle,
        'g':goods,
        'news':news,
        'id':id,
        'cart_count':cart_count(request)
    }

    
    response=render(request,'df_goods/detail.html',context)
    goods_ids=request.COOKIES.get('goods_ids','')
    goods_id='%d'%goods.id
    if goods_ids!='':
        goods_ids1=goods_ids.split(',')
        if goods_ids1.count(goods_id)>=1:
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0,goods_id)
        if len(goods_ids1)>=6:
            del goods_ids1[5]
        goods_ids=','.join(goods_ids1)
    else:
        goods_ids=goods_id
    response.set_cookie('goods_ids',goods_ids)

    return response

def cart_count(request):
    if request.session.has_key('user_id'):
        return CartInfo.objects.filter(user_id=request.session['user_id']).count()
    else:
        return 0

from haystack.views import SearchView
class MySearchView(SearchView):
    def extra_context(self):
        context = super(MySearchView, self).extra_context()
        context['title']= '搜索'
        # context['guest_cart']=1
        context['cart_count']=cart_count(self.request)
        return context
























