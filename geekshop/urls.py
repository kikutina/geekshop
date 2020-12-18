
from django.urls import path, include
from django.contrib import admin
from mainapp import views as mainapp_views
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import include





urlpatterns = [
    path('', mainapp_views.index, name='index'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('admin/', admin.site.urls),
    path('test_context/', mainapp_views.test_context),
    path('auth/', include('authapp.urls',  namespace='auth')),

    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
