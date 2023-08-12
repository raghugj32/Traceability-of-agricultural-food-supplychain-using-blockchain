from django.shortcuts import render,redirect

# Create your views here.
from distributor.models import distributor_payment1
from farmer.models import farmer_reg, farmer_payment, insurance_details, farmer_product
from insurance_company.models import insurance_company_register
from seed_seller.models import seed_upload
import datetime
import json
from os.path import dirname, join
import hashlib
import os
class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(nonce = 1, previous_hash = '0')

    def create_block(self, nonce, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'nonce': nonce,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_nonce):
        new_nonce = 1
        check_nonce = False
        while check_nonce is False:
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = True
            else:
                new_nonce += 1
        return new_nonce

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_nonce = previous_block['nonce']
            nonce = block['nonce']
            hash_operation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

def farmer_login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pswd = request.POST.get('password')
        try:
            check = farmer_reg.objects.get(uname=uname, password=pswd)
            print(check)
            request.session['farmer_id'] = check.id
            request.session['farmer_name'] = check.uname
            return redirect('farmer_home')
        except:
            pass
        return redirect('farmer_login')

    return render(request,'farmer/farmer_login.html')

def farmer_register(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        farmer_reg.objects.create(fullname=fullname, mobile=phone, location=location,
                                  uname=uname, password=password)
        return redirect('farmer_login')

    return render(request,'farmer/farmer_register.html')

def farmer_home(request):
    seed_details=seed_upload.objects.all()
    if request.method == "POST":
        cart_det = request.POST.getlist('cart_det[]')
        request.session['cart_det'] = cart_det
        print(cart_det)

        return redirect('view_cart')

    return render(request,'farmer/farmer_home.html',{'seed_details':seed_details})

def view_cart(request):
    farmerid=request.session['farmer_id']
    farmername=request.session['farmer_name']
    mm=0
    pname=''
    cart_det=request.session['cart_det']
    print(cart_det)
    cart_details=seed_upload.objects.filter(id__in=cart_det)
    for ca in cart_details:
        mm=mm+int(ca.price)
        pname=ca.seed_name+","+pname
        request.session['pname']=pname
        request.session['tprice']=mm
    print(mm)
    print(pname)
    if request.method == "POST":
        return redirect('payment')



    return render(request,'farmer/view_cart.html',{'cart_details':cart_details,'tprice':mm})


def payment(request):
    farmerid = request.session['farmer_id']
    farmername = request.session['farmer_name']
    pname=request.session['pname']
    total_price=request.session['tprice']
    blockchain = Blockchain()
    previous_block1 = blockchain.get_previous_block()
    previous_nonce1 = previous_block1['nonce']
    print(previous_nonce1)
    nonce1 = blockchain.proof_of_work(previous_nonce1)
    previous_hash1 = blockchain.hash(previous_block1)
    block1 = blockchain.create_block(nonce1, previous_hash1)
    atimestamp = str(datetime.datetime.now())
    apphash = farmer_payment.objects.all().count()
    print(apphash)
    if request.method == "POST":
        card_number = request.POST.get('card_number')
        cvv = request.POST.get('cvv')
        cname = request.POST.get('cname')
        card_validity = request.POST.get('card_validity')
        if apphash == 0:
            farmer_payment.objects.create(farmerid=farmerid, farmername=farmername, pname=pname,total_price=total_price,
                                          card_number=card_number,cvv=cvv,cname=cname,card_validity=card_validity,
                                          phash1=apphash,newhash1=previous_hash1,atimestamp=atimestamp)
            if pname.endswith(","):
                pname_list=pname.split(',')
                for pnames in pname_list:
                    seed_upload.objects.filter(seed_name=pnames).delete()
        else:
            ahash22 = farmer_payment.objects.all().last()
            aphash = ahash22.newhash1
            farmer_payment.objects.create(farmerid=farmerid, farmername=farmername, pname=pname,total_price=total_price,
                                          card_number=card_number,cvv=cvv,cname=cname,card_validity=card_validity, phash1=aphash,
                                          newhash1=previous_hash1,atimestamp=atimestamp)
            if pname.endswith(","):
                pname_list = pname.split(',')
                for pnames in pname_list:
                    seed_upload.objects.filter(seed_name=pnames).delete()

    return render(request,'farmer/payment.html',{'total_price':total_price,'pname':pname})



def apply_insurance(request):
    farmerid = request.session['farmer_id']
    farmername = request.session['farmer_name']
    insurance_company=insurance_company_register.objects.all()
    if request.method == "POST":
        insurance_company = request.POST.get('insurance_company')
        farmer_fullname = request.POST.get('farmer_fullname')
        door_number = request.POST.get('door_number')
        locality = request.POST.get('locality')
        village = request.POST.get('village')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        community = request.POST.get('community')
        farmer_category = request.POST.get('farmer_category')
        account_number = request.POST.get('account_number')
        bank_branch = request.POST.get('bank_branch')
        mobile = request.POST.get('mobile')
        survey_number = request.POST.get('survey_number')
        seed_name = request.POST.get('seed_name')
        status="pending"
        insurance_details.objects.create(farmerid=farmerid,farmername=farmername,farmer_fullname=farmer_fullname,door_number=door_number,
                                         locality=locality,village=village,district=district,pincode=pincode,community=community,
                                         farmer_category=farmer_category,account_number=account_number,bank_branch=bank_branch,
                                         mobile=mobile,survey_number=survey_number,seed_name=seed_name,insurance_company=insurance_company,
                                         status=status)
    return render(request,'farmer/apply_insurance.html',{'insurance_company':insurance_company})


def upload_product(request):
    farmerid = request.session['farmer_id']
    farmername = request.session['farmer_name']
    if request.method == "POST" and request.FILES['product_image']:
        quantity = request.POST.get('quantity')
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        location = request.POST.get('location')
        product_image = request.FILES['product_image']
        farmer_product.objects.create(farmerid=farmerid, farmername=farmername, product_name=product_name, quantity=quantity,
                               price=price,location=location,product_image=product_image)
    return render(request,'farmer/upload_product.html')

def view_distributorpayment(request):
    farmername = request.session['farmer_name']
    productbuying_details = distributor_payment1.objects.filter(farmer_name=farmername)
    return render(request,'farmer/view_distributorpayment.html',{'productbuying_details':productbuying_details})
