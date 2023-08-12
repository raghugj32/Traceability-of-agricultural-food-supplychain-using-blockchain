from django.shortcuts import render,redirect

# Create your views here.
from farmer.models import insurance_details
from insurance_company.models import insurance_company_register


def insurance_login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pswd = request.POST.get('password')
        try:
            check = insurance_company_register.objects.get(uname=uname, password=pswd)
            print(check)
            request.session['company_uid'] = check.id
            request.session['company_uname'] = check.uname
            request.session['company_name'] = check.company_name
            return redirect('company_home')
        except:
            pass
        return redirect('insurance_login')

    return render(request,'insurance_company/insurance_login.html')

def insurance_register(request):
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        insurance_company_register.objects.create(company_name=company_name, mobile=phone, location=location,
                                  uname=uname, password=password)
        return redirect('insurance_login')
    return render(request,'insurance_company/insurance_register.html')

def company_home(request):
    cuid=request.session['company_uid']
    cuname=request.session['company_uname']
    cname=request.session['company_name']
    farmer_insurance=insurance_details.objects.filter(insurance_company=cname)

    return render(request,'insurance_company/company_home.html',{'farmer_insurance':farmer_insurance})

def approve_status(request,pk):
    unresult=insurance_details.objects.get(id=pk)
    unid=unresult.id
    status="Accept"
    insurance_details.objects.filter(id=unid).update(status=status)

    return render(request,'insurance_company/approve_status.html')

def reject_status(request,pk):
    unresult = insurance_details.objects.get(id=pk)
    unid = unresult.id
    status = "Reject"
    insurance_details.objects.filter(id=unid).update(status=status)

    return render(request,'insurance_company/reject_status.html')
