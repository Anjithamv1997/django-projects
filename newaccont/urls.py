from django.urls import path
from . import views
urlpatterns = [
    path('', views.pro, name='index'),
    # path('',views.tax1),
    path('dummy/',views.dummy,name='dummy'),
    # path('dummy/new/', views.new, name='new')
    path('logout/',views.logout,name='logout'),
    path('register/', views.register, name='register'),

]