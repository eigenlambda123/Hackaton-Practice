from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            # If authentication failed 
            messages.error(request, 'Invalid Login')
            return redirect('authentication:login')
        else:
            # If authentication is successful
            login(request, user)
            return redirect('map')
    return render(request, 'user_authentication/login.html')


def user_register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        # Check if the user already exists
        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username already exists')
            return redirect('authentication:register')
        
        # Create A new User Object with the provided Info
        user = User.objects.create_user(first_name=first_name,
                                        last_name=last_name,
                                        username=username,
                                        password=password,
                                        email=email)
        # Save user password and object
        user.set_password(password)
        user.save()

        messages.info(request, 'Account Created Successfully!')
        return redirect('map')
    
    return render(request, 'user_authentication/register.html')

def user_logout(request):
    logout(request)
    return redirect('authentication:login')