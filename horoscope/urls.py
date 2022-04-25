from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.get_types),
    path('type/<str:element>', views.get_elements, name='type-name'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name')
]
