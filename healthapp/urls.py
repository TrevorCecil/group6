
from django.contrib import admin
from django.urls import path
from healthapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('inner_page/', views.inner_page),
]
