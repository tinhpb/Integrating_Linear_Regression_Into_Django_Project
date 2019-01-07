from django.urls import path
from . import views
app_name='house'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('demo/', views.demo_page, name='demo_page'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('predict/', views.predict, name='predict'),
    path('load-house-data/', views.load_house_data, name='load_house_data'),
    path('chart/', views.chart, name='chart'),
]
