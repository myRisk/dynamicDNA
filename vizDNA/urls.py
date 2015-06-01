from django.conf.urls import patterns, url
from vizDNA import views
#from django.conf import settings 
#from django.conf.urls.static import static 



#if not settings.DEBUG:
       # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^contact/$', views.contact, name='contact'),
        url(r'^risk/$', views.risk, name='risk'),
        url(r'^risk2/$', views.risk2, name='risk2'),
        url(r'^risk3/$', views.risk3, name='risk3'),
        url(r'^risk4/$', views.risk4, name='risk4'),
        url(r'^risk5/$', views.risk5, name='risk5'),
        url(r'^risk6/$', views.risk6, name='risk6'),
        url(r'^risk7/$', views.risk7, name='risk7'),
        url(r'^risk8/$', views.risk8, name='risk8'),
        url(r'^viz1/$', views.viz1, name='viz1'),
        url(r'^viz2/$', views.viz2, name='viz2'),
        url(r'^viz3/$', views.viz3, name='viz3'),
        url(r'^feedback/$', views.feedback, name='feedback'),
        #url(r'^add_category/$', views.add_category, name='add_category'),
        #url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        #url(r'^register/$', views.register, name='register'),
        #url(r'^login/$', views.user_login, name='login'),
        #url(r'^goto/$', views.track_url, name='goto'),)
]
