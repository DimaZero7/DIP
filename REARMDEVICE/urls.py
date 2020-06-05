from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', include('common.urls')),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('comments/', include('comments.urls')),
    path('basket/', include('basket.urls')), # добавление товаров в корзину
    path('authorization/', include('authorization.urls')),
    path('account/', include('account.urls')), # профиль пользователя
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()