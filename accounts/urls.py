
from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from django.views.generic import TemplateView


urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('edit_profile/', views.profile_view, name='edit_profile'),
    path('about_me/', views.about_profile_view, name='about_me'),
    # Password Reset handling
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = "password_reset.html"), name ='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name ="password_reset_send.html"), name ='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name ='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name ="password_reset_complete.html"), name='password_reset_complete'),


    # Password Change handling
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="password_change.html"),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"),
         name='password_change_done'),

]
