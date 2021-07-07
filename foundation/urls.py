from django.urls import path
from . import views
from django.conf import settings
urlpatterns=[
path('',views.index,name='Home'),
path('donate/submit/handlerequest/index.html',views.ret,name='Home'),
path('massage/',views.sendmessage,name='massage'),
path('donate/index.html/',views.ret),
path('donate/donate',views.dev),
path('donate/event',views.eve),
path('donate/bank',views.ban),
path('bank/index.html/',views.ret),
path('event/donate',views.dev),
path('event/bank',views.ban),
path('event/event',views.eve),
#path('donate/submit/handlerequest/',views.ret),
path('index.html/',views.ret),
path('bank/',views.bank),
path('event/',views.event),
path('case1/',views.case),
path('case2/',views.case2),
path('case3/',views.case3),
path('covid/',views.covid),
path('index/donate',views.dev),
path('donate/',views.devloper,name='dev'),
path('donate/submit/',views.submit,name='submit'),
path('covid/submit/',views.submit,name='submit'),
path('devloper/home/',views.index,name='home'),
path('donate/submit/handlerequest/',views.handlerequest,name='request'),
]
