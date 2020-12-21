from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop-Главная',

    }
    return render (request, 'mainapp/index.html', context)

def products(request, id=None):
    context = {
        'title': 'GeekShop-Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', context=context)


def test_context(request):
    context = {
        'title': 'тест контент',
        'userName': 'Ksenia',
        'products': [
            {'name': 'Черное худи', 'price': '10 000 руб.'},
            {'name': 'Шорты', 'price': '5 000 руб.'}
        ],
        'promotion_products': [
            {'name': 'Платье', 'price': '7 000 руб.'},
        ],
    }
    return render(request, 'mainapp/context.html', context)


def main(request):
    title = 'главная'

    products = Product.objects.all()

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)
