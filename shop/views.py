from django.shortcuts import render
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        print(request)
        name =  request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id','')
        print(order_id)
        email = request.POST.get('email','')
        print(email)
        try:
            order = Orders.objects.filter(order_id = order_id,email = email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    print(item.timestamp)
                    updates.append({'text':item.update_desc,'time':item.timestamp})

                    response = json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')

        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})



def checkout(request):
    if request.method =='POST':
        item_json = request.POST.get('itemJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount','')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '') + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone', '')
        order = Orders(item_json=item_json, name=name, email=email, address=address, city=city, zip_code=zip_code,
                       state=state, phone=phone,amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id,update_desc='The order has been placed')
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')
