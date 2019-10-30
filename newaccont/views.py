from django.shortcuts import render, HttpResponse,redirect
from .models import Products
from django.contrib.auth.models import auth,User
from django.contrib import messages


def pro(request):
    obj = Products.objects.all()
    return render(request, 'index.html', {'ob': obj})
def logout(request):
    auth.logout(request)
    return redirect('index')
def register(request):
    if request.method=='POST':
        a = request.POST['username']
        b = request.POST['password']
        c = request.POST['email']
        d = request.POST['conform password']
        if User.objects.filter(username==a).exist():
            messages.info(request, 'invalid')
            return redirect()
        user = User.objects.create_user(username=a, password=b, email=c)
        user.save()
        auth.login(request,user)
        return redirect('index')
    return render(request,'new.html')


# def tax1(request):
#     return render(request,'index.html')
def dummy(request):
    if request.method=='POST':
        a = request.POST['username']
        b = request.POST['password']
        user = auth.authenticate(username=a, password=b)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            # return render(request, 'dummy.html')
            messages.info(request,'invalid')

    return render(request, 'dummy.html')
def log(request):
    return render(request,'new.html')

# def new(request):
#     a = request.POST['username']
#     b = request.POST['password']
#     user = auth.authenticate(username=a, password=b)
#     if user is not None:
#         auth.login(request,user)
#
#     return render(request, 'new.html')
