from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  #used for User Authentication
from django.contrib import messages #used to send a flash message



# Create your views here.

#renders login page
def loginPage(request):
    return render(request, 'base/loginPage.html')

def new(request):
    return render(request, 'base/new.html')

def login2(request):
    return render(request, 'base/login2.html')

#renders register page
def registerPage(request):
    return render(request, 'base/registerPage.html')

def portalPage(request):
    return render(request, 'base/portalPage.html')


def loginPage(request):
    if request.user.is_authenticated: #if the user is already logged in
        return redirect('portalPage') #send them to the portal
    else:
        if request.method == 'POST': #check if we get a post request
            username = request.POST.get('username') #send username to username varible
            password = request.POST.get('password') #send password to password varible
            user = authenticate(request, username=username, password=password)
            if user is not None: #If we can see if there is a valid user
                login(request, user) #Django login method from import
                return redirect('portalPage') #sends user to the portal
            else: #if there is not a valid user
                messages.info(request, 'Username OR password is incorrect') #print flash message
        context = {}
        return render(request, 'base/loginPage.html', context) #show the login page again so they can re enter the right credentials
