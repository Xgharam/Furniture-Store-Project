from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Items,ItemDetails,Cart
from .forms import Register,Login
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
#index
def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render({'request':request}))

#DiningTables
def Tables(request):
    template=loader.get_template('Tables.html')
    furniture=ItemDetails.objects.select_related('itemsid')
    return HttpResponse(template.render({'furniture':furniture,'request':request}))

#Details
def TablesDetails(request,id):
    template=loader.get_template('TablesDetails.html')
    furniture=ItemDetails.objects.select_related('itemsid').filter(id=id)
    context={
        'furniture':furniture,
        'request':request
    }
    return HttpResponse(template.render(context))

#Register
@csrf_exempt
def auth_register(request):
    template=loader.get_template('Register.html')
    form=Register()
    if request.method=="POST":
         form=Register(request.POST)
         if form.is_valid():
            form.save()
            return redirect('Login.html')
    context={'registerform':form}
    return HttpResponse(template.render(context=context))

#Login
@csrf_exempt
def auth_login(request):
    form=Login()
    if request.method=="POST":
         form=Login(data=request.POST)
         if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return render(request,'index.html')
    context={'form':form}
    return render(request,'Login.html',context)

#Logout
@csrf_exempt
def auth_logout(request):
    if request.method=="POST":
        logout(request)
        return redirect("/")

#Checkout
@login_required(login_url='/Login/')
def Checkout(request, id):
    template=loader.get_template('Checkout.html')
    currentuser=request.user
    print(currentuser.id)
    furniture=ItemDetails.objects.select_related('itemsid').filter(id=id)
    context={
        'furniture':furniture,
        'request':request
    }
    return HttpResponse(template.render(context)) 

#ِAdd To Cart
def add_to_cart(requset, id):
    currentuser=requset.user
    discount=3
    status=False
    furniture=ItemDetails.objects.select_related('itemsid').filter(id=id)
    count=0
    for item in furniture:
        net=item.total-discount
        count=count+1
    cart = Cart(
       id_product=item.id,
       id_user=currentuser.id,
       price=item.price,
       qty=item.qty,
       tax=item.tax,
       total=item.total,
       discount=discount,
       net=net,
       status=status
)
    currentuser=requset.user.id
    count=Cart.objects.filter(id_user=currentuser).count()
    print(count)
    cart.save()
    requset.session['countcart']=count
    return redirect("/Tables")
