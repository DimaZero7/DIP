from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('common.urls')),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('product/', include('products.urls')),
    path('manufacture/', include('manufacture.urls')),
    path('comments/', include('comments.urls')),
    path('auth/', include('authorization.urls')),  # авторизация
    path('basket_add/', include('orders.urls')), # добавление товаров в корзину
    path('basket/', include('basket.urls')), # корзину
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
