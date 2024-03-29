"""POSBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from POSBackend import settings
from django.conf.urls.static import static
from app import views
from app import views_orders


from rest_framework_simplejwt.views import (TokenObtainPairView,)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/orders/', views_orders.orders),
    path('api/orders/<int:order_id>/', views_orders.order),
    path('', views.index),
    path('signin', views.login_view),

    #path('login', views.login_view),

] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
