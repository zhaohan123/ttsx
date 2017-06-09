#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from df_user import user_decorator
from django.http import JsonResponse
# from df_foods.models import *
# Create your views here.
@user_decorator.login
def cart(request):
	uid=request.session['user_id']
	print(uid)
	carts=CartInfo.objects.filter(user_id=uid)
	print(carts)
	context={
		'title':'购物车',
		'carts':carts,
		'page_name':1,
		'name':'购物车',


	}
	return render(request,'df_cart/cart.html',context)

@user_decorator.login

def add(request,gid,count):
	uid=request.session['user_id']
	gid=int(gid)
	count=int(count)
	carts=CartInfo.objects.filter(user_id=uid,goods_id=gid)
	if len(carts)>=1:
		cart=carts[0]
		cart.count=cart.count+count
	else:
		cart=CartInfo()
		cart.user_id=uid
		cart.goods_id=gid
		cart.count=count
	cart.save()



	if request.is_ajax():
		return JsonResponse({'count':CartInfo.objects.filter(user_id=request.session['user_id']).count(),'cart_id':cart.id})
   
  	else:
  		return redirect('/cart/')


@user_decorator.login
def delete(request,cart_id):
    try:
        cart=CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data={'ok':1}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)

@user_decorator.login
def edit(request,cart_id,count):
	count1=1
	try:
		cart=CartInfo.objects.get(pk=int(cart_id))
		count1=cart.count
		cart.count=int(count1)
		cart.save()
		data={'ok':0}
	except Exception as e:
		data={'ok':count1}
	return JsonResponse(data)
    






