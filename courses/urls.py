from . import views
from django.urls import path




urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('kurslar',views.kurslar),
]
