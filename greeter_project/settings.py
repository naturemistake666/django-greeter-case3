"""
Настройки Django для проекта greeter_project.

Сгенерировано командой 'django-admin startproject' (Django 6.1.1).

Подробнее об этом файле:
https://docs.djangoproject.com/en/6.1/topics/settings/

Полный список настроек:
https://docs.djangoproject.com/en/6.1/ref/settings/
"""

from pathlib import Path

# Пути внутри проекта строятся так: BASE_DIR / 'подпапка'
BASE_DIR = Path(__file__).resolve().parent.parent


# Настройки для разработки - для боевого сервера не подходят
# https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/

# ВНИМАНИЕ: секретный ключ должен храниться в секрете на проде!
SECRET_KEY = 'django-insecure-fzkl0yijx3d_oui^-*l0x_l5pl92q5$olnz-(3utt6i^$5&!q%'

# ВНИМАНИЕ: не запускать с DEBUG = True на проде!
DEBUG = True

ALLOWED_HOSTS = []


# Список приложений

INSTALLED_APPS = [
    'greeter',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'greeter_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'greeter_project.wsgi.application'


# База данных
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Проверка паролей
# https://docs.djangoproject.com/en/6.1/ref/settings/#auth-password-validators

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


# Интернационализация
# https://docs.djangoproject.com/en/6.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Статические файлы (CSS, JS, картинки)
# https://docs.djangoproject.com/en/6.1/howto/static-files/

STATIC_URL = 'static/'
