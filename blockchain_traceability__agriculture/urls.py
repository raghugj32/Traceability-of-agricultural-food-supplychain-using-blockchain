"""blockchain_traceability__agriculture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from seed_seller import views as seedsellerviews
from blockchain_traceability__agriculture import settings
from insurance_company import views as insuranceviews
from farmer import views as farmerviews
from distributor import views as distributorviews
from retailers import views as retailerviews
from customer import views as customerviews
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',seedsellerviews.seedseller_index, name="seedseller_index"),
    url(r'^seedseller_login/$',seedsellerviews.seedseller_login, name="seedseller_login"),
    url(r'^seedseller_register/$',seedsellerviews.seedseller_register, name="seedseller_register"),
    url(r'^seedseller_home/$',seedsellerviews.seedseller_home, name="seedseller_home"),
    url(r'^sellerview_buyingdetails/$',seedsellerviews.sellerview_buyingdetails, name="sellerview_buyingdetails"),

    url(r'^insurance_login/$',insuranceviews.insurance_login, name="insurance_login"),
    url(r'^insurance_register/$',insuranceviews.insurance_register, name="insurance_register"),
    url(r'^company_home/$',insuranceviews.company_home, name="company_home"),
    url(r'^approve_status/(?P<pk>\d+)/$',insuranceviews.approve_status,name="approve_status"),
    url(r'^reject_status/(?P<pk>\d+)/$',insuranceviews.reject_status,name="reject_status"),

    url(r'^farmer_login/$',farmerviews.farmer_login, name="farmer_login"),
    url(r'^farmer_register/$',farmerviews.farmer_register, name="farmer_register"),
    url(r'^farmer_home/$',farmerviews.farmer_home, name="farmer_home"),
    url(r'^view_cart/$',farmerviews.view_cart, name="view_cart"),
    url(r'^payment/$',farmerviews.payment, name="payment"),
    url(r'^apply_insurance/$',farmerviews.apply_insurance, name="apply_insurance"),
    url(r'^upload_product/$',farmerviews.upload_product, name="upload_product"),
    url(r'^view_distributorpayment/$',farmerviews.view_distributorpayment, name="view_distributorpayment"),

    url(r'^distributor_login/$',distributorviews.distributor_login, name="distributor_login"),
    url(r'^distributor_register/$',distributorviews.distributor_register, name="distributor_register"),
    url(r'^distributor_home/$',distributorviews.distributor_home, name="distributor_home"),
    url(r'^distributor_view_cart/$',distributorviews.distributor_view_cart, name="distributor_view_cart"),
    url(r'^distributor_payment/$',distributorviews.distributor_payment, name="distributor_payment"),
    url(r'^distributor_uploadproduct/$',distributorviews.distributor_uploadproduct, name="distributor_uploadproduct"),
    url(r'^view_retailerpayment/$',distributorviews.view_retailerpayment, name="view_retailerpayment"),

    url(r'^retailer_login/$',retailerviews.retailer_login, name="retailer_login"),
    url(r'^retailer_register/$',retailerviews.retailer_register, name="retailer_register"),
    url(r'^retailer_home/$',retailerviews.retailer_home, name="retailer_home"),
    url(r'^retailer_view_cart/$', retailerviews.retailer_view_cart,name="retailer_view_cart"),
    url(r'^retailer_payment/$',retailerviews.retailer_payment, name="retailer_payment"),
    url(r'^retailer_uploadproduct/$',retailerviews.retailer_uploadproduct, name="retailer_uploadproduct"),
    url(r'^view_customerpayment/$',retailerviews.view_customerpayment, name="view_customerpayment"),

    url(r'^customer_login/$',customerviews.customer_login, name="customer_login"),
    url(r'^customer_register/$',customerviews.customer_register, name="customer_register"),
    url(r'^customer_home/$',customerviews.customer_home, name="customer_home"),
    url(r'^customer_view_cart/$', customerviews.customer_view_cart,name="customer_view_cart"),
    url(r'^customer_payment/$',customerviews.customer_payment, name="customer_payment"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

