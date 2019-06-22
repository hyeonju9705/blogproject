
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


import blogapp.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blogapp.urls')),
    
    path('',blogapp.views.home, name="home"),
    path('portfolio/',portfolio.views.portfolio, name="portfolio"),
    path('accounts/' , include('accounts.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
