
from django.shortcuts import redirect, render
from accounts.models import *
from django.contrib.auth.decorators import login_required
from .forms import *  # Imported All Forms
from django.contrib.auth.models import User, auth
from django.contrib import messages
import re
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password
from post_app.models import Profile
from django.http import HttpResponse
# Create your views here.


# form validation 
def form_validation(request,username,first_name,last_name,email,password1):
    if not username.isalnum():
        messages.error(request, 'Username Must contain alphanumeric  !')
        return redirect('registration')
    # First Name Validation
    if len(first_name) < 3:
        messages.error(request, 'First Name length should be greater than 3 character !')
        return redirect('registration')
    # Last Name Validation
    if len(last_name) < 3:
        messages.error(request, 'Last Name length should be greater than 3 character !')
        return redirect('registration')
    # First Password Validation
    password_pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    result = re.findall(password_pattern, password1)
    if not result:
        messages.error(request,'Password At least 8 characters,uppercase letters:\n A-Z,lowercase letters: a-z,numbers: 0-9,\nany of the special characters: @#$%^&+= !')
        return redirect('registration')
    # Email Validation
    email_pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  # /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    email_val = re.findall(email_pattern, email)
    if not email_val:
        messages.error(request, 'invalid  Email !')
        return redirect('registration')


# registration
def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
       
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already Taken ')
                return redirect('registration')
            else:
                error=form_validation(request,username,first_name,last_name,email,password1)  # validation function
                if not error:
                    user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1,)
                    user.save()
                    messages.info(request, 'User Created Successfully !')
                    return redirect('/')
                else:

                    return redirect('registration')
        else:
            messages.info(request, 'username or password did not matched !')
            return redirect('registration')

    else:
        return render(request, 'register.html')


# login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Login Successfully')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            messages.error(request, 'Invalid user credentials.')
            return redirect('registration')
    else:
        return render(request, 'register.html')


# log_out
@login_required
def logout_page(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = profile_form(data=request.POST, instance=request.user)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            messages.info(request, 'Profile Updated Successfully..')
            return redirect("/")
        else:
            form = profile_form(instance=request.user)
            return redirect('edit_profile')
    else:
        form = profile_form(instance=request.user)
    return render(request, 'profile.html', {'form': form})


@login_required
def about_profile_view(request):
    user = User.objects.all()
    data = {
        user: 'user'
    }
    return render(request,'about_profile.html',data)


# # forgot password view
# def forget_password(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         if User.objects.filter(email=email).exists():
#             uid = User.objects.get(email=email)
#             url = f'http://127.0.0.1:8000/change-password/{uid.profile.uuid}'
#             send_mail('Reset Password', url, settings.EMAIL_HOST_USER, [email], fail_silently=False,)
#             return redirect('/password_reset_send/')
#         else:
#             messages.error(request,'email address is not exist')
#     return render(request,'password_reset.html')

#
# # change password view
# def change_password(request, uid):
#     try:
#         if Profile.objects.filter(uuid=uid).exists():
#             if request.method == "POST":
#                 password1 = 'password' in request.POST and request.POST['password']
#                 password2 = 'confirm_password' in request.POST and request.POST['confirm_password']
#                 if password1 == password2:
#                     error = form_validation(request, password1)  # validation function
#                     if not error:
#                         p = Profile.objects.get(uuid=uid)
#                         u = p.user
#                         user = User.objects.get(username=u)
#                         user.password = make_password(password1)
#                         user.save()
#                         messages.success(request, 'Password has been reset successfully')
#                         return redirect('/')
#                     else:
#                         return redirect('change-password')
#                 else:
#                     messages.info(request, 'username or password did not matched !')
#                     return redirect('change-password')
#             else:
#                 return HttpResponse('Wrong URL')
#         else:
#             messages.info(request, 'Wrong Url !')
#             return redirect('change-password')
#     except:
#         return render(request, 'password_reset_confirm.html')
