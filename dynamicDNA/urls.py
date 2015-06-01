from django.conf.urls import include, patterns, url
from django.contrib import admin
from vizDNA import views
from django.conf import settings 
from django.conf.urls.static import static 

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        
urlpatterns = [
    # Examples:
    # url(r'^$', 'dynamicDNA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^vizDNA/', include('vizDNA.urls')),
]
