"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from project import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('apps.base.urls', namespace='base')),
    url(r'^legoteka/', include('apps.legoteka.urls', namespace='legoteka')),
    url(r'^humanitarian_aid/', include('apps.aid.urls', namespace='humanitarian_aid')),
    url(r'^library/', include('apps.library.urls', namespace='library')),
    url(r'^financial/', include('apps.financial.urls', namespace='financial')),
    url(r'^api/', include('api.urls')),
    url(r'^pages/(\S+)/$', 'apps.pages.views.pages_detail', name='pages_detail'),
    url(r'^redactor/', include('redactor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

