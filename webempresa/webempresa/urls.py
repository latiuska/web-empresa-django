"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from services import views as services_views
from blog import views as blog_views
from core import views
from pages import views as pages_views



urlpatterns = [
    #Path del core
    path('', include('core.urls')),
    
    #Path de services
    path('services/', include('services.urls')),
    
    #Path de blogs
    path('blog/', include('blog.urls')),

    #Path de Pages
    path('page/', include('pages.urls')),

    #Path de Contacts
    path('contact/', include('contact.urls')),


    path('admin/', admin.site.urls),
    
]

###nos permite ver ficheros media en forma debug en el administrador###

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Custom tites for admin
admin.site.site_header = "La Caffetiera"
admin.site.index_title = "Panel de administrador"
admin.site.site_title = "La Caffetiera"
