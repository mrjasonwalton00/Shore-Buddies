from django.shortcuts import render

# Create your views here.

def loginPage(request):
    return render(request, 'userReg/loginPage.html')

def registerPage(request):
    return render(request, 'userReg/registerPage.html')
