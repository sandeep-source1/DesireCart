from django.shortcuts import render

from user.models import product


def index(request):
    p=product.objects.all()[0:8]
    return render(request,'user/index.html',context={'p':p})


