from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pastpaper/', views.pastpaper, name='pastpaper'),
    path('pastpapers/<str:level>/', views.select_university, name='select_university'),
    path('pastpapers/<str:level>/university/<int:university_id>/', views.select_faculty, name='select_faculty'),
    path('pastpaper_level/<str:level>/faculty/<int:faculty_id>/', views.pastpaper_level, name='pastpaper_level'),
    ]