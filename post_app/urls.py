# app Views
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('post_info/<int:post_id>/',views.post_info_view,name='post_info'),
    path('post_category/<name>/',views.post_category_view,name='post_category'),
    path('post_stage_status/<stage_name>/',views.admit_card_view,name='admit_card'),
    path('admission/<adv_name>/', views.admission, name='admission'),
    path('document/<document_name>/', views.document_view, name='documents'),
    path('important/<primary_key_name>/', views.important_view, name='important'),
    path('about_us/', views.about_us, name='about_us'),

]
