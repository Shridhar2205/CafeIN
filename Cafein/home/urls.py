from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('ContactUs/',views.ContactUs,name='ContactUs'),
    path('productview/',views.ProductView,name='ProductView'),
    path('cart/',views.cart,name='Cart')
 ]   