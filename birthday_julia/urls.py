from django.urls import path
from . import views

app_name = 'analysis_app'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('next',views.next, name = 'next'),
    path('next/plot', views.img_plot, name='img_plot')
]
