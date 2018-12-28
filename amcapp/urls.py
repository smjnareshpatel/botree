from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import handler404,handler500
# from django.contrib.auth import views
from . import views
from amcapp import register_view



urlpatterns = [

    # default url displays home page
    url(r'^$', views.customer, name='customer'),
    url(r'^register/$', register_view.register_view, name='register_view'),
    
    url(r'^customer$', views.customer, name='customer'),
    url(r'^product_log$', views.login, name='login'),
    url(r'^login$', views.login, name='login'),

    url(r'^customer-add$', views.customer_add, name='customer_add'),
    url(r'^(?P<id>\d+)/customer-update/', views.customer_update, name='customer_update'),
    url(r'^(?P<id>\d+)/customer-delete/', views.customer_delete, name='customer_delete'),
    url(r'^booking$', views.booking, name='booking'),
    url(r'^(?P<id>\d+)/booking-update/', views.booking_update, name='booking_update'),
    url(r'^booking-add$', views.booking_add, name='booking_add'),
    url(r'^(?P<id>\d+)/booking-delete/', views.booking_delete, name='booking_delete'),
    
    url(r'^cleaner$', views.cleaner, name='cleaner'),
    url(r'^cleaner-add$', views.cleaner_add, name='cleaner_add'),
    url(r'^(?P<id>\d+)/cleaner-update/', views.cleaner_update, name='cleaner_update'),
    

    url(r'^(?P<id>\d+)/cleaner-delete/', views.cleaner_delete, name='cleaner_delete'),
    
    url(r'^admin/', admin.site.urls),

    # url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    # url(r'^logout/$', views.logout, {'next_page': '/login'}),


   #-------------------login----------------------
   
   # url(r'^login$', blog_view.login, name='login'),


]

