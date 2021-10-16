from django.urls import path, reverse_lazy
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


class MyHackedView(auth_views.PasswordResetView):
    success_url = reverse_lazy('basis:password_reset_done')


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
    path('<slug:slug>/<str:project_name>', views.detailed_portfolio, name='detailed_portfolio'),
#    path('login/', views.custom_login, name='login'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_reset/', MyHackedView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('basis:password_reset_complete'),
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    path('register/', views.register, name='register'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
