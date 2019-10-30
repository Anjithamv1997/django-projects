# from django.shortcuts import render,HttpResponse
# def tax(request):
#     return render(request,'template.html')


from django.shortcuts import render,redirect
def log(request):
    if request.method=='POST':
        a = request.POST['username']
        b = request.POST['password']
        print(a,b)
        return redirect('login')
    else:
        return render(request,'form.html')
