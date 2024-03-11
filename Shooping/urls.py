"""
URL configuration for Shooping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Furniture import views as v1
from Furniture2 import views as v2
from Furniture3 import views as v3
from Furniture4 import views as v4
urlpatterns = [
    path("",v1.index,name='index'),
    path('admin/', admin.site.urls),
    path('Tables/',v1.Tables,name='Tables'),
    path('TablesDetails/<int:id>/',v1.TablesDetails,name='TablesDetails'),
    path('Sofas/',v2.Sofas,name='Sofas'),
    path('SofasDetails/<int:id>/',v2.SofasDetails,name='SofasDetails'),
    path('LightingDecor/',v3.LightingDecor,name='LightingDecor'),
    path('ShowDetails/<int:id>/',v3.ShowDetails,name='ShowDetails'),
    path('Bedrooms/',v4.Bedrooms,name='Bedrooms'),
    path('BedroomsDetails/<int:id>/',v4.BedroomsDetails,name='BedroomsDetails'),
    path('Register/',v1.auth_register,name='Register'),
    path('Login/',v1.auth_login,name='Login'),
    path('Logout/',v1.auth_logout,name='auth_logout'),
    path('Checkout/<int:id>/',v1.Checkout,name='Checkout'),
    path('add_to_cart/<int:id>/',v1.add_to_cart,name='add_to_cart')

]