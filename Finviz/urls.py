from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView #new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('charts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',TemplateView.as_view( template_name = 'index.html' ), name = 'home')
    # path('',include('charts.urls')),#과거의 방식
]
