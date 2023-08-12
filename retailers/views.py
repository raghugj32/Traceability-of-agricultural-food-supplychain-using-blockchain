from django.shortcuts import render,redirect

# Create your views here.
from customer.models import customer_payment1
from distributor.models import distributor_product
from retailers.models import retailer_reg, retailer_payment1, retailer_product

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

def retailer_login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pswd = request.POST.get('password')
        try:
            check = retailer_reg.objects.get(uname=uname, password=pswd)
            print(check)
            request.session['retailer_id'] = check.id
            request.session['retailer_name'] = check.uname
            return redirect('retailer_home')
        except:
            pass
        return redirect('retailer_login')
    return render(request,'retailers/retailer_login.html')

def retailer_register(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        retailer_reg.objects.create(fullname=fullname, mobile=phone, gender=gender, location=location,
                                  uname=uname, password=password)
        return redirect('retailer_login')
    return render(request,'retailers/retailer_register.html')

def retailer_home(request):
    viewproduct = distributor_product.objects.all()
    if request.method == "POST":
        cart_det = request.POST.getlist('cart_det[]')
        request.session['cart_det'] = cart_det
        print(cart_det)

        return redirect('retailer_view_cart')
    return render(request,'retailers/retailer_home.html',{'viewproduct':viewproduct})


def retailer_view_cart(request):
    retailer_id=request.session['retailer_id']
    retailer_name=request.session['retailer_name']
    mm=0
    pname=''
    cart_det=request.session['cart_det']
    print(cart_det)
    cart_details=distributor_product.objects.filter(id__in=cart_det)
    for ca in cart_details:
        mm=mm+int(ca.price)
        pname=ca.product_name+","+pname
        request.session['pname']=pname
        request.session['tprice']=mm
        distributor_name=ca.distributor_name
        request.session['distributor_name']=distributor_name

    print(mm)
    print(pname)
    if request.method == "POST":

        return redirect('retailer_payment')



    return render(request,'retailers/retailer_view_cart.html',{'cart_details':cart_details,'tprice':mm})

def retailer_payment(request):
    retailer_id = request.session['retailer_id']
    retailer_name = request.session['retailer_name']
    distributor_name = request.session['distributor_name']
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
    apphash = retailer_payment1.objects.all().count()
    print(apphash)
    if request.method == "POST":
        card_number = request.POST.get('card_number')
        cvv = request.POST.get('cvv')
        cname = request.POST.get('cname')
        card_validity = request.POST.get('card_validity')
        if apphash == 0:
            retailer_payment1.objects.create(retailer_id=retailer_id, retailer_name=retailer_name,
                                                distributor_name=distributor_name,pname=pname,total_price=total_price,
                                          card_number=card_number,cvv=cvv,cname=cname,card_validity=card_validity,
                                          phash1=apphash,newhash1=previous_hash1,atimestamp=atimestamp)
            if pname.endswith(","):
                pname_list=pname.split(',')
                for pnames in pname_list:
                    distributor_product.objects.filter(product_name=pnames).delete()
        else:
            ahash22 = retailer_payment1.objects.all().last()
            aphash = ahash22.newhash1
            retailer_payment1.objects.create(retailer_id=retailer_id, retailer_name=retailer_name,
                                                distributor_name=distributor_name, pname=pname,total_price=total_price,
                                          card_number=card_number,cvv=cvv,cname=cname,card_validity=card_validity, phash1=aphash,
                                          newhash1=previous_hash1,atimestamp=atimestamp)
            if pname.endswith(","):
                pname_list = pname.split(',')
                for pnames in pname_list:
                    distributor_product.objects.filter(product_name=pnames).delete()

    return render(request,'retailers/retailer_payment.html',{'total_price':total_price,'pname':pname})

def retailer_uploadproduct(request):
    retailer_id = request.session['retailer_id']
    retailer_name = request.session['retailer_name']
    if request.method == "POST" and request.FILES['product_image']:
        quantity = request.POST.get('quantity')
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        location = request.POST.get('location')
        product_image = request.FILES['product_image']
        retailer_product.objects.create(retailer_id=retailer_id, retailer_name=retailer_name,
                                      product_name=product_name, quantity=quantity,price=price,location=location,
                                      product_image=product_image)
    return render(request,'retailers/retailer_uploadproduct.html')

def view_customerpayment(request):
    retailer_name = request.session['retailer_name']
    productbuying_details = customer_payment1.objects.filter(retailer_name=retailer_name)
    return render(request,'retailers/view_customerpayment.html',{'productbuying_details':productbuying_details})


