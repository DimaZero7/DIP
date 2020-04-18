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
    path('order/', include('order.urls')), # создание заказов
    path('basket/', include('basket.urls')), # добавление товаров в корзину
    path('auth/', include('authorization.urls')), # регистрация
    path('account/', include('account.urls')), # профиль пользователя
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
