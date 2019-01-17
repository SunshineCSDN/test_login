from django.urls import path
from ss import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('login/',views.login, name='login' ),
    path('register/', views.reg, name='register')
]