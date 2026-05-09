from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import *
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache

def register(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        gender = request.POST.get('gender')

        if password1 != password2:
            return HttpResponse("Passwords do not match.")
            
        # password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

        # if not re.match(password_regex, password1):
        #     return HttpResponse(
        #         "Password is too weak. It must be at least 8 characters long, "
        #         "include an uppercase letter, a number, and a special character."
        #     )
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        if full_name:
            parts = full_name.split()
            user.first_name = parts[0]
            user.last_name = " ".join(parts[1:]) if len(parts) > 1 else ""
            user.save()

        Profile.objects.create(
            user=user,
            phone_number=phone_number,
            gender=gender
        )

    return render(request,"user/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:listitem')
        else:
            message = "Authentication Failed"
            return HttpResponse(message)

    return render(request,"user/login.html")

@never_cache
def logout_view(request):
    logout(request)
    return HttpResponse('You are now logged out') 
