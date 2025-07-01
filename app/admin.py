from django.contrib import admin
from .models import *
# Register your models here.

class showsignup(admin.ModelAdmin):
    list_display = ('name','email','phone','address','password','role')

admin.site.register(signupmodel, showsignup)

class showcategory(admin.ModelAdmin):
   list_display = ('catname',)

admin.site.register(category, showcategory)

class showproduct(admin.ModelAdmin):
   list_display = ('name','catid','pprice','prentprice','pcolor','desc','status','sellerid','admin_photo')

admin.site.register(product, showproduct)

class showcart(admin.ModelAdmin):
   list_display = ('id','userid','productid','quantity','totalamount','orderstatus','orderid')

admin.site.register(cart, showcart)

class order(admin.ModelAdmin):
   list_display = ('userid','finaltotal','phone','address','paymode','timestamp','status','razorpay_order_id')

admin.site.register(ordermodel,order)

class showrentalmodel(admin.ModelAdmin):
    list_display = ('userid','productid','start_date','end_date','total_days','total_rent','payment_status','booking_date')

admin.site.register(rental,showrentalmodel)