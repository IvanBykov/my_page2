from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('type/', views.get_types),
    path('kianu/', views.get_kianu),
    path('guines/', views.get_guinness_world_records),
    path('beautiful_table/', views.get_beautiful_table),
    path('type/<str:element>', views.get_elements, name='type-name'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('<int:month>/<int:day>/', views.get_info_about_sign_zodiac_by_date),
]
