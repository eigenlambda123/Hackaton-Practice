from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            # If authentication failed 
            messages.error(request, 'Invalid Login')
            return redirect('login')
        else:
            # If authentication is successful
            login(request, user)
            return redirect('map')

    return render(request, 'user_authentication/login.html')