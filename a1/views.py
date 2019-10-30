from django.shortcuts import render,HttpResponse
def form(request):
    return render(request,'form.html')
def result(request):
        username=['anji','jinu','ashi']
        password=['111','222','333']
        a=request.POST['username']
        b=request.POST['password']
        print(request.POST)
        print(request.GET)
        if a in username:
            i=username.index(a)
            if b in password[i]:
                 return render(request,'result.html',{'un':a,'pw':b})
            else:
                return HttpResponse('invalid')
        else:
            return HttpResponse('invalid')




