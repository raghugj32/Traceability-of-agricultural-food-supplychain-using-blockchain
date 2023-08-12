from django.shortcuts import render,redirect

# Create your views here.
from farmer.models import farmer_payment
from seed_seller.models import seedseller_reg, seed_upload


def seedseller_index(request):

    return render(request,'seed_seller/seedseller_index.html')

def seedseller_login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pswd = request.POST.get('password')
        try:
            check = seedseller_reg.objects.get(uname=uname, password=pswd)
            print(check)
            request.session['seedseller_id'] = check.id
            request.session['seedseller_name'] = check.uname
            return redirect('seedseller_home')
        except:
            pass
        return redirect('seedseller_login')
    return render(request,'seed_seller/seedseller_login.html')

def seedseller_register(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        seedseller_reg.objects.create(fullname=fullname, mobile=phone, gender=gender, location=location,
                                  uname=uname, password=password)
        return redirect('seedseller_login')
    return render(request,'seed_seller/seedseller_register.html')

def seedseller_home(request):
    if request.method == "POST" and request.FILES['product_image']:
        seed_name = request.POST.get('seed_name')
        number_pieces = request.POST.get('number_pieces')
        brand_name = request.POST.get('brand_name')
        price = request.POST.get('price')
        product_image = request.FILES['product_image']
        seed_upload.objects.create(seed_name=seed_name, number_pieces=number_pieces, brand_name=brand_name, price=price,
                               product_image=product_image)
    return render(request,'seed_seller/seedseller_home.html')

def sellerview_buyingdetails(request):
    seedbuying_details=farmer_payment.objects.all()

    return render(request,'seed_seller/sellerview_buyingdetails.html',{'seedbuying_details':seedbuying_details})