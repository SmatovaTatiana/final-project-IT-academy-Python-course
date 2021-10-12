from django.urls import path
from . import views

app_name = 'basis'
urlpatterns = [
    path('', views.all_education, name='all_education'),
    path('<slug:slug>/<int:graduated>', views.detailed_education, name='detailed_education'),
]
