from django.conf.urls import url
import views

urlpatterns=[
	url(r'^$', views.cart),
	url(r'^add(\d+)_(\d+)/$',views.add),
	# url(r'^list', views.list),
	url(r'^delete(\d+)',views.delete),
	url(r'^edit(\d+)_(\d+)/$',views.edit),
	]