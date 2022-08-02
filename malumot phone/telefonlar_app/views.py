from django.shortcuts import render
from .models import SmartphoneBrand, SmartphoneMadel, SmartphoneProduct

def index_page(request):
    queryset = SmartphoneBrand.objects.all().order_by('name')
    return render(request, 'index.html', {'sort_brand': queryset})

def get_madel(request, madel_id):
    queryset = SmartphoneMadel.objects.all().filter(brand=madel_id)
    brand = SmartphoneBrand.objects.get(id=madel_id)
    context = {'filter_madel': queryset, 'brand_name': brand}
    return render(request, 'madel_product.html', context)

def get_product(request,product_id, soni):
    queryset = SmartphoneProduct.objects.all().filter(madel=product_id)[:soni]
    madel = SmartphoneMadel.objects.get(id=product_id)
    context = {'madel_pro':queryset, 'madel':madel}
    return render(request, 'phone_product.html', context)