from django.contrib import admin
from .models import *

@admin.register(Post_info)
class Post_info_Admin(admin.ModelAdmin):
    list_display = ['post_title','category','post_provider_name','advt_number', 'id','post_stage']
    list_filter = ['category']
    # autocomplete_fields = ['posts']
    search_fields = ['id']

@admin.register(Post_stage)
class Post_stage_Admin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ['name','id']
    search_fields = ['id']

@admin.register(Admission)
class Post_stage_Admin(admin.ModelAdmin):
    list_filter = ['institute_name']
    list_display = ['admission_title','id']
    search_fields = ['id']


@admin.register(Certificate)
class Cirtificate_Admin(admin.ModelAdmin):
    list_filter = ['document_provider']
    list_display = ['document_name','id']
    search_fields = ['id']


@admin.register(Important)
class Important_admin(admin.ModelAdmin):
    list_filter = ['provider_name']
    list_display = ['name_of_scheme','id']
    search_fields = ['id']


# Register your models here.
admin.site.register(Post_category)
admin.site.register(Profile)
admin.site.register(Comment)
