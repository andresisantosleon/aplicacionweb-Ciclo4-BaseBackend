"""InventarioFabricaMuebles URL Configuration

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

"""
from django.contrib import admin
from django.urls import path
"""

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
from nuevosRegistros import views as viewsNuevosRegistros


urlpatterns = [
path('login/', TokenObtainPairView.as_view()),
path('refresh/', TokenRefreshView.as_view()),
path('user/', views.UserCreateView.as_view()),
path('user/<int:pk>/', views.UserDetailView.as_view()),
path('materiasPrimas/',viewsNuevosRegistros.materiaPrimaAPIView,name='materiasPrimas'),
path('proveedores/',viewsNuevosRegistros.proveedoresAPIView,name='proveedores'),
path('materiasPrimas/<int:pk>/',viewsNuevosRegistros.materiaPrima_detailsAPIView,name='materiaPrima_details'),
path('movimientos/',viewsNuevosRegistros.movimientosAPIView,name='movimientos'),
path('actualizar/<int:pk>/',viewsNuevosRegistros.proveedores_detail_APIView,name='actualizar'),
]

"""
urlpatterns = [
    path('admin/', admin.site.urls),
]
"""