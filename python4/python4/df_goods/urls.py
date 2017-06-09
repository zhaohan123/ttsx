from django.conf.urls import url
import views

urlpatterns=[
    url('^$',views.index),
    url('^index2(\d+)/$',views.index2),
    # url('^list/$',views.list),
    # url('^detail/$',views.detail),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list),
    url(r'^(\d+)/$', views.detail),
    # url(r'^query/', views.query),
    url(r'^search/', views.MySearchView()),
]
