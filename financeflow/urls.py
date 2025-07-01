from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenses/', include('expenses.urls')),
    path('', views.home, name='home'), 
    path('accounts/', include('users.urls')),
    path('budgets/', include('budgets.urls')),
    path('goals/', include('savings.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

