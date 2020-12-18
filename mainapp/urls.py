from django.urls import path, include

import mainapp.views as mainapp



app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:id>/', mainapp.products, name='product'),
    path('auth/', include('authapp.urls', namespace='auth')),

]

