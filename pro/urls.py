"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('404',views.showpage),
    path('profile',views.showprofile),
    path("cart",views.showcart),
    path("",views.showhome),
    path("home71",views.showhome12),
    path("login",views.showloginpage),
    path("fetchsignupdata",views.fetchsignupdata),
    path("checklogin",views.checklogin),
    path('logout', views.logout),
    path('product1/<int:id>',views.showproduct1),
    path('addproduct',views.showaddproduct),
    path('categoryviseproduct/<int:id>',views.categoryviseproduct),
    path('fetchproduct',views.fetchproduct),
    path('insertintocart',views.insertintocart),
    path('showcart', views.showcart),
    path('manageproduct',views.manageproduct),
    path("deleteproduct/<int:id>", views.deleteproduct),
    path("editproduct/<int:id>",views.editproduct),
    path('deleteitem/<int:id>',views.deleteitem),
    path("updateproductdata",views.updateproductdata),
    path('increase/<int:id>',views.increase),
    path('decrease/<int:id>',views.decrease),
    path('placeorder', views.placeorder),
    path('payment-success', views.payment_success),
    path("yourorder",views.yourorders),
    path("yourorderdetail/<int:id>",views.yourorderdetails),
    path("cancelorder/<int:id>",views.cancelorder),
    path('rent/<int:pid>', views.rent_product, name='rent_product'),
    path('rental-summary/<int:rid>', views.rental_summary, name='rental_summary'),
    path('rental/payment/<int:rid>', views.rental_payment, name='rental_payment'),
    path('rental_paymenthandler/<int:rid>/', views.rental_paymenthandler, name='rental_paymenthandler'),
    path('my-rentals', views.rental_history, name='rental_history'),
    path('sellershoworder', views.sellershoworder, name='sellershoworder'),
    path('sellershowrentorder', views.sellershowrentorder, name='sellershowrentorder'),
    path('seller_rentals', views.seller_rentals, name='seller_rentals'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
