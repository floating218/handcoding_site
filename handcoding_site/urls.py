"""handcoding_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.home,name='home'),
    path('<coder_id>/<screen_id>/',myapp.views.detail, name='detail'),
    path('<coder_id>/<screen_id>/update',myapp.views.update,name='update'),
    path('finish',myapp.views.finish,name='finish'),
    path('<game_name>/selection',myapp.views.selection,name='selection'),
    path('<game_name>/submit_coder',myapp.views.submit_coder,name='submit_coder'),
    path('<game_name>/input_coder',myapp.views.input_coder, name='input_coder')
]

###
# config/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)