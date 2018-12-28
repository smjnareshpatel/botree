"""dpisite URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
# from amcapp.register_view import register_view

from django.contrib.auth import views
from django.contrib.auth import views as auth_views

from amcapp.forms import LoginForm
from amcapp.forms import Password_reset,Set_Password

from django.conf.urls import handler404,handler500


urlpatterns = [
    url(r'', include("amcapp.urls")),


    url(r'^login/$', views.login, {'template_name': 'authentication/login.html', 'authentication_form': LoginForm}),
    # url(r'^register/$', register_view.register_view, name='register_view'),
   
    url(r'^logout/$', views.logout, {'next_page':'/login'}),

    # url(r'^password_reset/$', auth_views.password_reset,{'template_name': 'authentication/password_reset_form.html'}),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, 
    #     {'template_name': 'authentication/password_reset_done.html'},name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    # url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    # url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset',
    #    {'post_reset_redirect' : 'django.contrib.auth.views.password_reset_done'},
    #     name="password_reset"),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    # url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url(r'^admin/', admin.site.urls),
    
]
if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
