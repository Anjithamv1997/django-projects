from django.urls import path
from . import views
urlpatterns = [
    path('',views.p),
    path('blog/',views.p1,name='blog'),

]