from django.shortcuts import render, HttpResponse,Http404,get_object_or_404
from .models import Product


# def display(request):
# m1=['home','about','contact']
# return render(request,'display.html',{'m2':m1})
# a=Product.objects.get(id=1)
# b = Product.objects.get(id=2)
# c = Product.objects.get(id=3)
# d = Product.objects.get(id=4)
# return render(request,'things.html',{'o':a,'p':b,'q':c,'r':d})


def play(request, id):
    # try:
        # obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404('delete')
    obj = get_object_or_404(Product, id=id)

    return render(request, 'things.html', {'objects': obj})
