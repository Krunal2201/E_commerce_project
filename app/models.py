from django.db import models
from django.utils.safestring import mark_safe

class signupmodel(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    phone = models.BigIntegerField(unique=True)
    address = models.TextField()
    password = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name or "Unknown User"

class category(models.Model):
    catname = models.CharField(max_length=30)

    def __str__(self):
        return self.catname

class product(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    ]
    SIZE_CHOICES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ]
    name = models.CharField(max_length=30)
    catid = models.ForeignKey(category,on_delete=models.CASCADE)
    pimage = models.ImageField(upload_to='photos', null=True)
    pprice = models.FloatField()
    prentprice = models.FloatField()
    pcolor = models.TextField(max_length=20)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='M')
    desc = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    sellerid = models.ForeignKey(signupmodel,on_delete=models.CASCADE)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.pimage.url))

    admin_photo.allow_tags = True

    def __str__(self):
        return self.name

class cart(models.Model):
    userid = models.ForeignKey(signupmodel,on_delete=models.CASCADE)
    productid = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalamount = models.FloatField()
    orderstatus = models.IntegerField()
    orderid = models.IntegerField()

class ordermodel(models.Model):
   userid = models.ForeignKey(signupmodel, on_delete=models.CASCADE)
   finaltotal = models.FloatField()
   phone = models.BigIntegerField()
   address = models.TextField()
   paymode = models.CharField(max_length=40)
   timestamp = models.DateTimeField(auto_now_add=True)
   status = models.BooleanField(default=False)
   razorpay_order_id = models.CharField(max_length=255, null=True, blank=True)


class rental(models.Model):
    userid = models.ForeignKey(signupmodel, on_delete=models.CASCADE)
    productid = models.ForeignKey(product, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.IntegerField()
    total_rent = models.FloatField()
    payment_status = models.BooleanField(default=False)
    booking_date = models.DateTimeField(auto_now_add=True)
    razorpay_order_id = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"{self.userid.name} rented {self.productid.name}"

