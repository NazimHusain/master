from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from post_app.models import *
from .forms import *  # Imported All Forms
from django.template.loader import render_to_string
import random
# from rembg import remove
# from PIL import Image


# Create your views here.
def index_view(request):
    post_category = Post_category.objects.all()
    all_post = Post_info.objects.order_by('-id')
    # random all post
    list_post = list(all_post)
    random_post = random.sample(list_post, 5)
    first = list_post[0]
    second = list_post[1]
    third = list_post[2]
    fourth = list_post[3]
    fifth = list_post[4]
    sixth = list_post[5]

    # all stage 
    all_stage = Post_stage.objects.all().order_by('id')[:4]  # no nay state excluded

    # admit card filter
    get_admit_card = Post_stage.objects.get(name='Admit_card')
    admit_card_filtered = Post_info.objects.filter(post_stage=get_admit_card)
    # result filter
    get_result = Post_stage.objects.get(name='Result')
    result_filtered = Post_info.objects.filter(post_stage=get_result)
    # syllabus filter
    get_syllabus = Post_stage.objects.get(name='Syllabus')
    syllabus_filtered = Post_info.objects.filter(post_stage=get_syllabus)

    # upcomming filter
    get_up_comming_post = Post_stage.objects.get(name='up_comming_post')
    up_comming_filtered = Post_info.objects.filter(post_stage=get_up_comming_post)

    # Answer key
    # upcomming filter
    get_answer_key_post = Post_stage.objects.get(name='Answer_key')
    answer_key_filtered = Post_info.objects.filter(post_stage=get_answer_key_post)
    # admission
    institute = Admission.objects.all()
    # documents
    documents = Certificate.objects.all()
    # important
    important = Important.objects.all()

    # random post

    data = {
        'category': post_category,
        'posts': all_post,
        'stages': all_stage,
        'admit_cards': admit_card_filtered,
        'results': result_filtered,
        'syllabus': syllabus_filtered,
        'up_comming': up_comming_filtered,
        'answer_key': answer_key_filtered,
        'institute': institute,
        'certificates': documents,
        'importants': important,
        'random_posts': random_post,
        'first':first,
        'second': second,
        'third': third,
        'fourth': fourth,
        'fifth': fifth,
        'sixth': sixth,



    }

    return render(request, 'index.html', data)


# post category view 
def post_category_view(request,name):
    get_category=Post_category.objects.get(title=name)
    filtered_cat_post=Post_info.objects.filter(category=get_category)
    all_category=Post_category.objects.all()
    all_stage = Post_stage.objects.all().order_by('id')[:4]

    data = {
        'posts':filtered_cat_post,
        'category':all_category,
        'stages': all_stage,
    }
    return render(request,'post_category.html',data)


# post view 
def post_info_view(request,post_id):
    post_category=Post_category.objects.all()
    all_stage = Post_stage.objects.all().order_by('id')[:4]
    get_post=Post_info.objects.filter(pk=post_id)
    get_comment_post = get_object_or_404(Post_info,id=post_id)
    comments = Comment.objects.filter(comment_post=post_id,reply=None).order_by('-id') 
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')   # getting content from forms
            reply_id = request.POST.get('comment_id')  # getting id from reply form
            print(reply_id)
            comment_reply = None
            if reply_id:
                comment_reply = Comment.objects.get(id=reply_id)    # getting matching reply_id from database
            comment = Comment.objects.create(comment_post=get_comment_post,user=request.user,content=content,reply=comment_reply)
            comment.save()
           
    else:
        comment_form = CommentForm()

    data = {
        'category':post_category,
        'posts': get_post,
        'comments': comments,
        'comment_form': comment_form,
        'stages': all_stage,
    }
    if request.is_ajax():
        html = render_to_string('comments.html', data, request=request)
        return JsonResponse({'form': html})
    return render(request,'post_info.html', data)


# admit card view
def admit_card_view(request,stage_name):
    all_stage = Post_stage.objects.all().order_by('id')[:4]
    get_admit_card_name = Post_stage.objects.get(name=stage_name)
    filtered_cat_post = Post_info.objects.filter(post_stage=get_admit_card_name)
    all_category = Post_category.objects.all()
    all_stage = Post_stage.objects.all().order_by('id')[:4]
    data = {
        'admit_cards': filtered_cat_post,
        'category':all_category,
        'stages': all_stage,
    }
    return render(request,'admit_card.html',data)


# Admission
def admission(request,adv_name):
    all_stage = Post_stage.objects.all().order_by('id')[:4]
    get_admission_post = Admission.objects.filter(unique_advt_number_primary_key=adv_name)
    all_category = Post_category.objects.all()
    data = {
        'admission': get_admission_post,
        'category':all_category,
        'stages': all_stage,
    }
    return render(request,'admission.html', data)


# Certificate
def document_view(request,document_name):
    all_stage = Post_stage.objects.all().order_by('id')[:4]
    get_document_post = Certificate.objects.filter(unique_advt_number_primary_key=document_name)
    all_category = Post_category.objects.all()
    data = {
        'certificates': get_document_post,
        'category':all_category,
        'stages': all_stage,
    }
    return render(request,'documents.html', data)


# Important
def important_view(request, primary_key_name):
    all_stage = Post_stage.objects.all().order_by('id')[:4]
    get_important_post = Important.objects.filter(primary_key_name=primary_key_name)
    all_category = Post_category.objects.all()
    data = {
        'importants': get_important_post,
        'category': all_category,
        'stages': all_stage,
    }
    return render(request, 'important_scheme.html', data)


# about_us view
def about_us(request):
    return render(request, 'image_bg_remove.html')




    
   