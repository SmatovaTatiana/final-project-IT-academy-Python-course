from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'basis'
urlpatterns = [
    path('', views.all_education, name='all_education'),
]
urlpatterns += staticfiles_urlpatterns()
