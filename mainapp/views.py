from django.shortcuts import render

def index(request):
    context = {
        'title': 'GeekShop-Главная',
    }
    return render (request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'GeekShop-Каталог',
    }
    return render(request, 'mainapp/products.html', context)

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