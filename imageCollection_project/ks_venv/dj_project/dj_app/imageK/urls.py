from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='imageK-home'),
    path('category/<int:cid>/',views.category,name='imageK-category'),
    path('sfs/',views.sfs,name='imageK-sfs'),
    ]