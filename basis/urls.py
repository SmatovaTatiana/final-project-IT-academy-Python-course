from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'basis'
urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('contacts/', views.contacts, name='contacts'),
    path('all_education/', views.all_education, name='all_education'),
    path('<slug:slug>/<int:graduated>', views.detailed_education, name='detailed_education'),
    path('all_experience/', views.all_experience, name='all_experience'),
    path('<slug:slug>/<str:company_name>/<str:position>', views.detailed_experience,
         name='detailed_experience'),
    path('contact_form/', views.contact_form, name="contact_form"),
    path('upload_documents/', views.document_form_upload, name='upload_documents'),
    path('all_portfolio/', views.all_portfolio, name='all_portfolio'),
 #   path('detailed_portfolio', views.detailed_portfolio, name='detailed_portfolio'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
