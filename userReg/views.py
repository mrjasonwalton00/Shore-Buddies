# -------------------------------------------------------------------------------------------------------------------------
# Imports
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm #used for our user creation form
from .forms import CreateUserForm #used for our user creation form
from django.contrib.auth import authenticate, login, logout  #used for User Authentication
from django.contrib.auth.decorators import login_required #this is so we can restrict pages if you are not a logged in user
from django.contrib import messages #used to send a flash message
from django.contrib.auth.models import Group #used to access our groups
from .models import Profile #import our profile model
#-------------------------------------------------------------------------------------------------------------------------



# Create your views here.
def testPage1(request):
    return render(request, 'userReg/testPage1.html')

def registerTurtle(request):
    return render(request, 'userReg/registerTurtle.html')


# def registerFreemium(request):
#     return render(request, 'userReg/registerFreemium.html')

def registerFreemium(request):
    if request.user.is_authenticated: #if the user is authenticated
        return redirect('testPage1') 
    else:
        form = CreateUserForm() #import our form
        if request.method == 'POST': #checking for a post request
            form = CreateUserForm(request.POST) #use our form
            if form.is_valid(): # if the regrestration is successfully filled out
                user = form.save() #save the information and store the created user object in a variable
                group = Group.objects.get(name='Freemium') #retrieve the gold group object
                user.groups.add(group) #add the user to the gold group
                username = user.username #get the username and store in variable username
                messages.success(request, 'Account was created for ' + username ) #sends flash message 
                
                
                return redirect('loginPage') # redirect user to login page
        context = {'form':form,} #context dictionary
        return render(request, 'userReg/registerFreemium.html', context)



@login_required(login_url='loginPage')
def logoutUser(request):
    logout(request) #logout method from Django import
    return redirect('loginPage') # redirect user to back login page when a user logs out










