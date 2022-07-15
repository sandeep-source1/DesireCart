from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
# Create your views here.
from user.models import product,contact as mycon,subcategory,signup,Cart,Product_Review,d_state
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout

def mens(request):
    p = product.objects.filter(category='Men')
    sub=[]
    for a in p:
        if a.subcategory not in sub:
            sub.append(a.subcategory)
    if request.GET.get('cid'):

        p=product.objects.filter(category='Men',subcategory=request.GET.get('cid'))

    return render(request,'user/mens.html',context={"men":p,'cat':sub})
def womens(request):
    p = product.objects.filter(category='Women')
    sub = []
    for a in p:
        if a.subcategory not in sub:
         sub.append(a.subcategory)
    if request.GET.get('cid'):

        p = product.objects.filter(category='Women', subcategory=request.GET.get('cid'))

    return render(request,'user/womens.html',context={'women':p,'cat':sub})


def contact(request):
    if request.method=="POST":
        cont=mycon(name=request.POST.get('name',''),email=request.POST.get('email',''),contact=request.POST.get('mobno',''),msg=request.POST.get('msg',''))
        cont.save()
        return render(request, 'user/contactus.html',context={"status":True})
    return render(request,'user/contactus.html',context={'status':False})


def kids(request):
    p = product.objects.filter(category='Kid')
    sub=[]
    for a in p:
        if a.subcategory not in sub:
            sub.append(a.subcategory)
    if request.GET.get('cid'):

        p = product.objects.filter(category='Kid', subcategory=request.GET.get('cid'))

    return render(request, 'user/kids.html', context={'kid': p, 'cat': sub})


def myoders(request):
    if request.user.is_authenticated:
       if request.GET.get('remove'):
           try:
               if Cart.objects.get(id=request.GET.get('remove'),odered=False):
                   cart_item=Cart.objects.get(id=request.GET.get('remove'))
                   cart_item.delete()
           except:
               print("Not Exists.")
           mycart =Cart.objects.filter(Owner=request.user,odered=True).order_by('-id')
           return render(request, 'user/myoders.html', {'mycart': mycart,'status':True})
       mycart =Cart.objects.filter(Owner=request.user,odered=True).order_by('-id')
       return render(request,'user/myoders.html',{'mycart':mycart,'status':True})
    return render(request,'user/myoders.html',{'mycart':'sign','status':False})




def myprofile(request):
    if request.user.is_authenticated:
        profile=signup.objects.filter(userid=request.user.username)
        mycart = Cart.objects.filter(Owner=request.user)
        return render(request,'user/myprofile.html',{'profile':profile,'mycart':mycart})
    return render(request,'user/myprofile.html')

def signin(request):

    if request.method=='POST':
        user=auth.authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            if request.POST['action']=='home':
                return HttpResponse('success and home')
            return HttpResponse("success")
        else:
            return HttpResponse("Failure")



def detail(request):
    if request.method=='POST':
        pid = request.POST.get('product')
        pr = product.objects.filter(id=pid).first()
        review=request.POST.get('review')
        user=signup.objects.filter(userid=request.user.username).first()
        save_review=Product_Review(Owner=user,Review=review,Product=pr)
        save_review.save()
        reviews=Product_Review.objects.filter(Product=pr)
        count=Product_Review.objects.filter(Product=pr).count()

        return render(request, 'user/description.html', context={'product': pr, 'status': True,'reviews':reviews,'count':range(1,count+1)})
    pid = request.GET.get('product')
    pr = product.objects.filter(id=pid).first()
    reviews = Product_Review.objects.filter(Product=pr)
    count = Product_Review.objects.filter(Product=pr).count()
    return render(request,'user/description.html',context={'product':pr,'status':True,'reviews':reviews,'count':range(1,count+1)})


def signUp(request):
    if request.method=='POST':
        data=signup(name=request.POST['name'],userid=request.POST['username'],email=request.POST['email'],
                    userpic=request.FILES['file'],address=request.POST['address'],password=request.POST['password'],mob=request.POST['mobno'])
        data.save()
        myuser=User.objects.create_user(request.POST.get('username'),request.POST.get('email'),request.POST.get('password'))
        myuser.save()
        return render(request, 'user/signup.html',{'status':True})
    return render(request,'user/signup.html',{'status':False})


def signout(request):
    logout(request)
    return HttpResponse('success')


def addtocart(request):  
    if request.user.is_authenticated:

        pid=request.GET.get('pid')
        pro=product.objects.filter(id=pid)
        cart_item=Cart(Owner=request.user,cartproduct=pro.first())
        cart_item.save()
        if cart_item in Cart.objects.filter(Owner=request.user):
              return HttpResponse("added successfuly")
        return HttpResponse("Something went.")


def orderdetails(request):
    if request.user.is_authenticated:
       pid=request.GET.get('product')
       pr=product.objects.get(id=pid)
       return render(request,'user/orderpage.html',context={'product':pr})
    return render(request,'user/signup.html')


def cartdata(request):
    cart_item=Cart.objects.filter(Owner=request.user).count()
    return HttpResponse(cart_item)

def removefromcart(request):
    if request.GET.get('remove'):
        id=request.GET.get('remove')
        cart_item = Cart.objects.filter(id=id).first()
        cart_item.delete()
        return  HttpResponse("Need refresh")
    return  HttpResponse("Somthing went wrong..")


def mycart(request):
    if request.user.is_authenticated:
       if request.GET.get('remove'):
           try:
               if Cart.objects.get(id=request.GET.get('remove')):
                   cart_item = Cart.objects.get(id=request.GET.get('remove'))
                   cart_item.delete()
           except:
               print("Not Exists.")
           mycart = Cart.objects.filter(Owner=request.user,odered=False).order_by('-id')
           return render(request, 'user/mycart.html', {'mycart': mycart, 'status': True})
       mycart = Cart.objects.filter(Owner=request.user,odered=False).order_by('-id')
       return render(request,'user/mycart.html',{'mycart':mycart,'status':True})
    return render(request,'user/mycart.html',{'mycart':'sign','status':False})


def uname(request):
    name=request.POST.get('username')

    user=signup.objects.filter(userid=name).first()
    if user is not None:
        print()
        return HttpResponse('failure')
    else:
        return HttpResponse('success')


def payment(request):
    if request.user.is_authenticated:
       return render(request,'user/payment.html',{'product':product.objects.get(id=request.POST.get('pid'))})
    return render(request,'user/signup.html')


def thanks(request):
    if request.user.is_authenticated:
     if request.method=="POST":
        pid=request.POST.get('pid')
        pro=product.objects.get(id=pid)
        my_cart=Cart.objects.filter(cartproduct=pro,Owner=request.user).first()
        if my_cart:
            my_cart.status=d_state.objects.get(id=1).status_value
            my_cart.odered=True
            my_cart.save()
            return render(request, 'user/thanks.html')
        my_order=Cart(Owner=request.user,cartproduct=pro,Datetime=datetime.now(),status=d_state.objects.get(id=1).status_value,odered=True)
        my_order.save()
        return render(request,'user/thanks.html')
     return render(request,'user/index.html')
    return render(request,'user/signup.html')


def track(request):
  order = Cart.objects.get(id=request.GET.get('product'))
  if request.user.is_authenticated:
    if order.Owner==request.user:
     if order.status=='Waiting to dispatch':
       return render(request,'user/orderstatus.html',{'order':order,'one':True})
     elif order.status=="Dispatching":
       return render(request,'user/orderstatus.html',{'order':order,'two':True})
     elif order.status=="Dispatched":
       return render(request,'user/orderstatus.html',{'order':order,'three':True})
     elif order.status=="Leaved for Your City":
       return render(request,'user/orderstatus.html',{'order':order,'four':True})
     elif order.status=="Leaved for Your City":
       return render(request,'user/orderstatus.html',{'order':order,'five':True})
     elif order.status=="On the Way to Your Door":
       return render(request,'user/orderstatus.html',{'order':order,'six':True})
     elif order.status=="Delivered":
       return render(request,'user/orderstatus.html',{'order':order,'eight':True})
    return render(request,'user/myoders.html')
  return render(request,'user/signup.html')


def editpro(request):
    if request.user.is_authenticated:
      user=signup.objects.filter(userid=request.user.username).first()
      return render(request,'user/editpro.html',{'pro':user})


def saveedit(request):
   if request.user.is_authenticated:
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        mob=request.POST['mobno']
        img=request.FILES['file']
        user=signup.objects.filter(userid=request.user.username).first()
        user.name=name
        user.email=email
        user.address=address
        user.mob=mob
        user.userpic=img
        user.save()
    profile = signup.objects.filter(userid=request.user.username)
    mycart = Cart.objects.filter(Owner=request.user)
    return render(request, 'user/myprofile.html', {'profile': profile, 'mycart': mycart})
   return render(request,'user/signup.html')


def forgetpassword(request):
    return render(request,'user/forgetpassword')


def data(request):
    if request.method=='GET':
      name=request.GET.get('data')
      prodata=product.objects.all()
      st=''
      for a in prodata:
          if a.name.startswith(name):
              st+=a.name+'!'+str(a.id)+'!'
      return HttpResponse(st)