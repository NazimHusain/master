from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime

# Create your models here.

    # post Category
class Post_category(models.Model):
    title = models.CharField(max_length=500,blank=False,null=True,unique=True)

    def __str__(self):
        return self.title

# admit card, Result, Syllabus, Answer_key,
class Post_stage(models.Model):
    name = models.CharField(max_length=500,blank=False, null=True)

    def __str__(self):
        return self.name


# About Post
class Post_info(models.Model):
    category = models.ForeignKey(Post_category, on_delete=models.CASCADE)
    post_stage = models.ForeignKey(Post_stage, on_delete=models.CASCADE)
    post_provider_name = models.CharField(null=True,blank=True, max_length=100)
    post_title = models.CharField(max_length=200)
    total_post = models.IntegerField(default='0',blank=False,null=True)
    advt_number = models.TextField(null=True,blank=True)
    fee_desc = models.TextField(null=True,blank=True)
    post_dates = models.TextField(null=True,blank=True)
    post_last_date = models.DateField()
    age_desc = models.TextField(null=True,blank=True)
    post_detail_desc = models.TextField(null=True,blank=True)
    post_important_link = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.post_title


class Admission(models.Model):
    institute_name = models.CharField(null=True, blank=True, max_length=100)
    admission_title = models.CharField(max_length=200)
    unique_advt_number_primary_key = models.TextField(unique=True)
    fee_desc = models.TextField(null=True, blank=True)
    important_dates = models.TextField(null=True, blank=True)
    admission_detail_desc = models.TextField(null=True, blank=True)
    post_important_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.institute_name

class Certificate(models.Model):
    document_provider = models.CharField(max_length=200)
    document_name = models.CharField(null=True, blank=True, max_length=100)
    document_fee = models.TextField(null=True, blank=True)
    unique_advt_number_primary_key = models.TextField(unique=True)
    requirements = models.TextField(null=True, blank=True)
    document_detail_desc = models.TextField(null=True, blank=True)
    document_important_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.document_name


# important schemes
class Important(models.Model):
    provider_name = models.CharField(max_length=200)
    name_of_scheme = models.CharField(null=True, blank=True, max_length=200)
    fee_detail = models.TextField(null=True, blank=True)
    primary_key_name = models.TextField(unique=True)
    requirement_desc = models.TextField(null=True, blank=True)
    scheme_detail_desc = models.TextField(null=True, blank=True)
    scheme_important_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.provider_name


    # user profile structure
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=15,  null=True,blank=True)
    def __str__(self):
        return self.user


# comment structure
class Comment(models.Model):
    comment_post = models.ForeignKey(Post_info, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', related_name="replies", null=True,  on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} -by- {}'.format(self.comment_post.post_title, str(self.user.username))





