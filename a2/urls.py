from django.urls import path
from . import views
urlpatterns = [
    # path('home/',views.display),
    path('<int:id>/', views.play)

]