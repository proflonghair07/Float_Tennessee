from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path(r'logout/', views.Logout.as_view(), name='logout'),
    # path(r'login/', views.Login.as_view(), name='login'),
    # path(r'home/', views.Home.as_view(), name='home'),
    # path(r'location/<str:name>/', views.Location.as_view(), name='location'),
]
