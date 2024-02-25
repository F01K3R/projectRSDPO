from django.urls import path
from . import views

urlpatterns = [
    path('', views.bd_home, name='bd_home'),
    path('histogram/', views.histogram_view, name='histogram'),
    path('pie_chart/', views.pie_chart_view, name='pie_chart'),
    path('score_range_histogram/', views.score_range_histogram_view, name='score_range_histogram'),
]