from django.shortcuts import render

def index(request):
    context = {
        'title': 'GeekShop-Главная',

    }
    return render (request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'GeekShop-Каталог',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 руб.',
             'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'img': '/static/vendor/img/products/Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб.',
             'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'img': '/static/vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 руб.',
             'text': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'img': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00 руб.',
             'text': 'Плотная ткань. Легкий материал.',
             'img': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00 руб.',
             'text': 'Гладкий кожаный верх. Натуральный материал.',
             'img': '/static/vendor/img/products/Black-Dr-Martens-shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00 руб.',
             'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'img': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},

        ]
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