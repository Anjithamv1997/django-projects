from django.urls import path
from . import views
urlpatterns = [
    # path('tax/',views.tax),
    # path('dummy/',views.tax,name='dummy')
     path('login/', views.log),
]