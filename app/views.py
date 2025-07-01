from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def showpage(request):
    return render(request,"404.html")

def showprofile(request):
    if 'log_id' in request.session:
        userid = request.session["log_id"]
        fetchdata = signupmodel.objects.get(id=userid)
        context = {
        'data':fetchdata
        }
        return render(request,"profile.html",context)
    else:
        return redirect('/login')
def showhome(request):
    fetchproduct = product.objects.all()
    fetchcatdata = category.objects.all()
    context = {
        "product": fetchproduct,
        "category": fetchcatdata
    }
    return render(request,"HOME.html",context)

def fetchsignupdata(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        add = request.POST.get("address")
        password = request.POST.get("password")
        role = request.POST.get("role")
        alreadyuser = signupmodel.objects.filter(email=request.POST['email'])
        if alreadyuser:
            messages.error(request, "this email is alredy registered..")
            return render(request, 'login_page.html')

        print("fetchsignupdata")

        insert_query = signupmodel(name=name, email=email, phone=phone, address=add, password=password, role=role)
        insert_query.save()
        print("save data")

        return render(request, "login_page.html")
    else:
        return render(request, "login_page.html")


def checklogin(request):
    useremail = request.POST.get("email")
    userpass = request.POST.get("password")
    print(useremail)
    print(userpass)


    # query to check data into model

    try:
        userdata = signupmodel.objects.get(email=useremail,password=userpass)
        print(userdata)
        print("success")

        # store data into session
        request.session["log_id"] = userdata.id
        request.session["log_name"] = userdata.name
        request.session["log_email"] = userdata.email
        request.session["log_role"] = userdata.role

        print("session name",request.session["log_name"])
    except:
        print("failure")
        userdata = None

    # navigation based on query result
    if userdata is not None:
        return redirect("/")
    else:
        print("invaild email and password")
        messages.error(request,"invaild email or password")

    return render(request,"login_page.html")

def logout(request):
    try:
        del request.session["log_id"]
        del request.session["log_name"]
        del request.session["log_email"]
        del request.session["log_role"]
    except:
        pass
    return render(request,"Home.html")

def insertintocart(request):
    pid = request.POST.get("pid")
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")

    userid = request.session["log_id"]
    totalamount = int(quantity) * float(price)

    try:
        fetchdata = cart.objects.get(userid=userid,productid=pid,orderstatus=1)
    except:
        fetchdata = None

    if fetchdata is not None:
        fetchdata.quantity += int(quantity)
        fetchdata.totalamount += int(totalamount)
        fetchdata.save()
    else:
        insertquery = cart(userid=signupmodel(id=userid),
                       productid=product(id=pid),
                       quantity=quantity,
                       totalamount=totalamount,
                       orderstatus=1,orderid=0)
        insertquery.save()

    return redirect("/")
def showcart(request):
    userid = request.session["log_id"]
    fetchdata = cart.objects.filter(userid=userid)
    context = {
        "data": fetchdata
    }
    return render(request,"cart_page.html",context)

def showhome12(request):
    return render(request,"HOME1-2.html")

def showloginpage(request):
    return render(request,"login_page.html")

def showproduct1(request,id):
    print(id)
    singledata = product.objects.get(id=id)
    fetchcatdata = category.objects.all()
    fetchproduct = product.objects.all()
    context = {
        "data": singledata,
        "category": fetchcatdata,
        "product":fetchproduct,

    }
    print("fetchcatdata sucsess")
    return render(request,"product_detail_1.html",context)

def showaddproduct(request):
    allcatdata = category.objects.all()
    context = {
        "catdata": allcatdata
    }
    return render(request,"addproduct.html",context)

def categoryviseproduct(request,id):
    fetchdata = product.objects.filter(catid=id)
    fetchcatdata = category.objects.all()
    context = {
        "data":fetchdata,
        "category":fetchcatdata,
    }
    return render(request,"shop_no_sidebar.html",context)

def fetchproduct(request):
    name = request.POST.get("productname")
    catid = request.POST.get("category")
    productimage = request.FILES['productImage']
    color = request.POST.get("productcolor")
    price = request.POST.get("price")
    desc = request.POST.get("desc")
    size = request.POST.get("size")
    status = request.POST.get("status")
    temp=float(request.POST.get("price"))
    rentp= round(temp * 0.10,2)

    #fech sellerid from session variable

    sellerid = request.session["log_id"]

    print("insertproduct")

    insert_query = product(name=name, catid=category(id=catid), pimage=productimage, pprice=price,prentprice=rentp,pcolor=color ,desc=desc, size=size,status=status, sellerid=signupmodel(id=sellerid))
    insert_query.save()
    messages.success(request, "product add successfully")
    print("savedata")

    return render(request,"addproduct.html")

def manageproduct(request):
    sellerid_loggedin = request.session["log_id"]
    fetchdata = product.objects.filter(sellerid=sellerid_loggedin)
    context = {
        "data":fetchdata
    }
    return render(request,"manageproduct.html",context)

def deleteproduct(request,id):
    print(id)
    # delete query
    # delete from tablename where id=id
    fetchdata = product.objects.get(id=id)
    fetchdata.delete()
    messages.success(request,"Product Deleted")
    return redirect("/manageproduct")

def editproduct(request,id):
    fetchdata = product.objects.get(id=id)
    fetchcat = category.objects.all()
    context = {
        "data":fetchdata,
        "category":fetchcat
    }
    return render(request,"editproduct.html",context)

def updateproductdata(request):
    name = request.POST.get("pname")
    catid = request.POST.get("pcat")
    color = request.POST.get("color")
    price = request.POST.get("price")
    size = request.POST.get("size")
    desc = request.POST.get("desc")
    status = request.POST.get("status")
    pid = request.POST.get("pid")

    # seller id from session
    sellerid = request.session["log_id"]

    # update table set name=name , price=price where id=pid
    fetchdata = product.objects.get(id=pid)
    fetchdata.name = name
    fetchdata.catid = category(id=catid)
    fetchdata.color = color
    fetchdata.pprice = price
    fetchdata.size = size
    fetchdata.desc = desc
    fetchdata.status = status
    fetchdata.sellerid = signupmodel(id=sellerid)
    if 'pimage' in request.FILES:
        file = request.FILES['pimage']
        object.pimage = file

    fetchdata.save()
    messages.success(request,"Data Updated")
    return redirect("/manageproduct")
def deleteitem(request,id):
    cart.objects.get(id=id).delete()
    return redirect("/showcart")

def decrease(request,id):
    fetchdata = cart.objects.get(id=id)
    fetchdata.quantity -= 1
    fetchdata.totalamount -= fetchdata.productid.pprice
    fetchdata.save()
    return redirect("/showcart")

def increase(request,id):
    fetchdata = cart.objects.get(id=id)
    fetchdata.quantity += 1
    fetchdata.totalamount += fetchdata.productid.pprice
    fetchdata.save()
    return redirect("/showcart")

import razorpay
from django.conf import settings


def placeorder(request):
   userid = request.session["log_id"]
   finaltotal = request.POST.get("total")
   phone = request.POST.get("phone")
   address = request.POST.get("address")
   payment = request.POST.get("payment")


   if payment=="Cash on Delivery":
       storedata = ordermodel(
           userid=signupmodel(id=userid),
           finaltotal=finaltotal,
           phone=phone,
           address=address,
           paymode=payment,
           status=True,
       )
       storedata.save()


       lastid = storedata.id


       fetchdata = cart.objects.filter(userid=userid,orderstatus=1)
       for i in fetchdata:
           i.orderstatus = 0
           i.orderid = lastid
           i.save()


       messages.success(request,"Order Placed Successfully")
   else:


       client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))
       order_amount = int(float(finaltotal) * 100)  # Razorpay needs amount in paise
       razorpay_order = client.order.create({
           "amount": order_amount,
           "currency": "INR",
           "receipt": f"order_rcptid_{userid}",
           "payment_capture": "1",
       })


       storedata = ordermodel(
           userid=signupmodel(id=userid),
           finaltotal=finaltotal,
           phone=phone,
           address=address,
           paymode="Online",
           status=True,
           razorpay_order_id=razorpay_order['id'],
       )
       storedata.save()


       lastid = storedata.id


       # Update Cart Items
       cart_items = cart.objects.filter(userid=userid, orderstatus=1)
       for item in cart_items:
           item.orderstatus = 0
           item.orderid = lastid
           item.save()


       return render(request, "payment.html", {
           "razorpay_order_id": razorpay_order['id'],
           "amount": order_amount,
           "key": settings.RAZORPAY_KEY_ID,
           "currency": "INR",
       })


   return redirect("/")


def payment_success(request):
 return redirect("/")

def showcart(request):
   userid = request.session["log_id"]
   fetchdata = cart.objects.filter(userid=userid,orderstatus=1)
   total = sum(item.totalamount for item in fetchdata)
   context = {
       "data":fetchdata,
       "total":total
   }
   return render(request,"cart_page.html",context)


from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime,date,time
def rent_product(request, pid):
    prod = get_object_or_404(product, id=pid)

    if request.method == 'POST':
        start = request.POST.get('start_date')
        end = request.POST.get('end_date')
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        end_date = datetime.strptime(end, "%Y-%m-%d").date()

        # Check if dates are valid
        if end_date <= start_date:
            messages.error(request, "End date must be after start date.")
            return redirect('rent_product', pid=pid)

        # Check overlapping bookings
        overlap = rental.objects.filter(
            productid=prod,
            start_date__lte=end_date,
            end_date__gte=start_date
        ).exists()

        if overlap:
            messages.error(request, "This product is already booked for the selected dates.")
            return redirect('rent_product', pid=pid)

        num_days = (end_date - start_date).days
        total = (prod.prentprice * 5)+( num_days * prod.prentprice)
        uid = request.session["log_id"]
        userdata =signupmodel.objects.get(id=uid)
        rent = rental.objects.create(
            userid=userdata,
            productid=prod,
            start_date=start_date,
            end_date=end_date,
            total_days=num_days,
            total_rent=total
        )

        return redirect('rental_summary', rid=rent.id)

    return render(request, 'rent_product.html', {'product': prod})

def rental_summary(request, rid):
    rent = rental.objects.get(id=rid)
    return render(request, 'rental_summary.html', {'rent': rent})

def rental_history(request):
    history = rental.objects.filter(userid__id=request.session["log_id"]).order_by('-booking_date')
    return render(request, 'rental_history.html', {'rentals': history})


def rental_payment(request, rid):
    rent = rental.objects.get(id=rid)
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))
    amount = int(rent.total_rent * 100)  # in paise

    order = client.order.create({
        'amount': amount,
        'currency': 'INR',
        'payment_capture': '1'
    })

    rent.razorpay_order_id = order['id']
    rent.save()

    context = {
        'rent': rent,
        'order_id': order['id'],
        'order_amount': amount,
        'razorpay_merchant_key': settings.RAZORPAY_KEY_ID,
        'callback_url': f'/rental_paymenthandler/{rent.id}/'

    }
    return render(request, 'rental_payment.html', context)


import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import redirect

@csrf_exempt
def rental_paymenthandler(request, rid):
    if request.method == "POST":
        try:
            rent = rental.objects.get(id=rid)

            # Only get and verify razorpay_order_id
            razorpay_order_id = request.POST.get('razorpay_order_id')

            # Optionally: you can skip verifying the signature if not storing it
            # But to ensure security, it's better to still verify
            razorpay_payment_id = request.POST.get('razorpay_payment_id')
            razorpay_signature = request.POST.get('razorpay_signature')

            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            }

            # Optional but recommended verification
            client.utility.verify_payment_signature(params_dict)

            # Mark payment successful
            rent.payment_status = True
            rent.razorpay_order_id = razorpay_order_id  # You’re already storing this
            rent.save()

            return redirect('rental_history')

        except razorpay.errors.SignatureVerificationError:
            return HttpResponse("Payment signature verification failed")

        except Exception as e:
            return HttpResponse(f"Payment Failed: {str(e)}")



def seller_rentals(request):
    seller = signupmodel.objects.get(id=request.session['log_id'])
    seller_products = product.objects.filter(sellerid=seller)
    rentals = rental.objects.filter(productid__in=seller_products).select_related('userid', 'productid')
    context = {
        'rentals': rentals
    }
    return render(request, 'seller_rentals.html', context)

def yourorders(request):
    userid = request.session["log_id"]
    fetchdata = ordermodel.objects.filter(userid=userid)
    context = {
        "data":fetchdata
    }
    return render(request,"yourorders.html",context)

def yourorderdetails(request,id):
    fetchdata = cart.objects.filter(orderid=id)
    context = {
        "data":fetchdata
    }
    return render(request,"yourorderdetail.html",context)

def cancelorder(request,id):
    fetchdata = ordermodel.objects.get(id=id)
    fetchdata.status = False
    fetchdata.save()
    messages.success(request,"your order is cancelled")
    return redirect("/yourorder")


def sellershoworder(request):
    uid = request.session['log_id']
    sellers_products = product.objects.filter(sellerid=signupmodel(id=uid))
    getdetails =  cart.objects.filter(productid__in = sellers_products , orderstatus=0)
    context = {
        "sellerorderdetails":getdetails
    }
    return render(request, 'manage_seller_order.html', context)


def sellershowrentorder(request):
    seller_id = request.session.get("log_id")  # Adjust key if needed
    if not seller_id:
        return redirect('login')  # Or handle unauthorized access

    rentals = rental.objects.filter(productid__sellerid__id=seller_id).order_by('-booking_date')

    return render(request, 'seller_rentalproduct.html', {'rentals': rentals})


