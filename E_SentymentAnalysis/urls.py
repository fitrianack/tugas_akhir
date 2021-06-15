from dashboard.views import dashboard
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # new
    path('landing_page/', include('landing_page.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('crawling/', include('crawling.urls')),
]
