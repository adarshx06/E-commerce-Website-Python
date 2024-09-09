from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category

# Create your views here.
def home(request):
    #return HttpResponse("Hello, World!")
    products = Product.get_all_products()
    categorys = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    print(products)
    print(categorys)
    data = {}
    data['product'] = products
    data['category'] = categorys
    print(data)
    return render(request, 'home.html', data)


def signup(request):
    return render(request, 'signup.html')