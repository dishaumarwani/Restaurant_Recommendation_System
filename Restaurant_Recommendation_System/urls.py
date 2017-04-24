from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from restaurant.views import index, detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^restaurant/', include('restaurant.urls')),

]

