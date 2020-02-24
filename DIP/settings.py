
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parents[1]

SECRET_KEY = '(@=3-)a0u-5h@7t((91o+2-v-b+k+07%j+g_3^_6zb1!ghteth'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'common.apps.CommonConfig',  # Приложение общее содержит то что не относится по сымслу к дргим приложениямы
    'catalog.apps.CatalogConfig',  # Приложение отвечающее за каталог товров
    'authorization.apps.AuthorizationConfig',  # Приложение отвечающее за авторизацию
    'django_cleanup',  # Подключаемая библиотека котороя удаляет фаилы при удалении родительской модели
    
]

MIDDLEWARE =  [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] 

ROOT_URLCONF = 'DIP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')  # Путь к главным шаблонам
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'catalog.utils.menu',  # Контекст для работы списка категорий
            ],
        },
    },
]

WSGI_APPLICATION = 'DIP.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # Путь к статичным файлам главных шаблонов
]

MEDIA_URL = '/media/'  # Url путь к медиа фаилам
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Путь к медиа фаилам (для сервера)

