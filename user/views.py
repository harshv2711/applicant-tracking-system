from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User, auth 
from django.contrib.auth.decorators import login_required
from .form import UserUpdateForm
from .form import ProfileUpdateForm

from .models import Profile
from client import utils as clientAppUtils


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username'].replace(' ','_')
        email = request.POST['email'].replace(' ','')
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        
        # password and confirm password must be equal.
        if password == confirm_password:

            # username should not exists.
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username already taken.')
                return redirect('user-register')

            # check for email. if exists redirect to register page.
            else: 
                if User.objects.filter(email=email).exists():
                    messages.error(request, f"Email alread exists")
                    return redirect('user-register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    user_queryset = User.objects.filter(username=username).first()
                    profile = Profile(user=user_queryset)
                    profile.save()
                    messages.success(request, f'Account Created Sucessfully!')
                    return redirect('user-login')
        else:
            messages.error(request, f'Password Not Matching.')
            return redirect('user-register')

    return render(request, 'user/register.html', {'title': 'Sign Up'})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if clientAppUtils.isLoggedInUserIsClient(request.user):
                messages.error(request, f'Use client login page to login as a Client.')
                auth.logout(request)
                return redirect('user-login')
            
            messages.success(request, f'Welcome back {user.username}')
            return redirect('webpages-search')
        else:
            messages.error(request, f'Invalid credentials')
            return redirect('user-login')

    return render(request, 'user/login.html')

def logout(request):
    auth.logout(request)
    return redirect('user-login')
    # return render(request, 'user/logout.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        

    context = {
        'u_form' : u_form,
        'p_form'    : p_form
    }

    return render(request, 'user/profile.html', context)
