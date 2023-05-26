from django.shortcuts import render,HttpResponse
from .models import product

def index(request):
 products = product.objects.all() 
 print(products)
 n=len(products)
 params = {'no_of_products':n ,range:'1,n','product':products}
 return render(request,'index.html',params)

def about(request):
 return render(request,'about.html')

def ContactUs(request):
 return render(request,'contact.html')

def cart(request):
  return render(request,'cart.html')

def ProductView(request):
  return render(request,'productview.html')
