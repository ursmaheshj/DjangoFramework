from django.shortcuts import render,redirect
from crudwithfbv.forms import UserModelForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from crudwithfbv.models import User
from django.contrib.auth.decorators import login_required
#settings for mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse

from crudwithfbv.emailconf import send_activation_email
# Create your views here.

@login_required
def home(request):
    return render(request,'crudwithfbv/home.html')

@login_required
def dashboard(request):
    return render(request,'crudwithfbv/dashboard.html')

def loginview(request):
    if request.user and request.user.is_authenticated:
        if request.user.is_seller:
            return render(request,'crudwithfbv/dashboard.html',context={'usertype':"Seller"})
        elif request.user.is_customer:
            return render(request,'crudwithfbv/dashboard.html',context={'usertype':"Customer"})
        return redirect('home')
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            messages.error(request,"Require both fields")
            return redirect('login')

        user = authenticate(request,email=email,password=password)

        
        if user is None:
            messages.error(request, "Invalid email or password")
            return redirect('login')

        if not user.is_active:
            messages.error(request, "User is not activated yet")
            return redirect('login')
        
        login(request, user)

        if user.is_seller:
            return render(request, 'crudwithfbv/dashboard.html', context={'usertype': "Seller"})
        elif user.is_customer:
            return render(request, 'crudwithfbv/dashboard.html', context={'usertype': "Customer"})
        return redirect('home')
    
    return render(request,'crudwithfbv/login.html')

def register(request):
    if request.method == "POST":
        form = UserModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            role = form.cleaned_data['role']
            if role == 'seller':
                user.is_seller = True
                user.is_customer = False
            if role == 'customer':
                user.is_customer = True
                user.is_seller = False

            user.is_active = False
            user.save()
            print(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = reverse('activate',kwargs={'uidb64':uidb64,'token':token})
            activation_url = f"{settings.SITE_DOMAIN}{activation_link}"
            try:
                send_activation_email(user.email, activation_url)
            except Exception as e:
                messages.error(request, f"Issue sending activation mail: {e}")
                return redirect('login')

            messages.success(request, "Registration successful! Please check your email to activate account")
            return redirect('login')
    else:
        form = UserModelForm()
    return render(request,'crudwithfbv/register.html',{'form':form})

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if user.is_active:
            messages.warning(
                request,"This account is already active"
            )
            return redirect('login')
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(
                request,"Your account has been activated"
            )
            return redirect('login')
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        messages.error(request,"Invalid activation link")   
        return redirect('login')