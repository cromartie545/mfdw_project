from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('index1',views.index1,name='index1'),
    path('', views.index, {'pagename': ''}, name='home'),
    path('contact', views.contact, name='contact'),
    path('<str:pagename>', views.index, name='index'),
]
