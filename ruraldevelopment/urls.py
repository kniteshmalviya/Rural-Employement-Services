"""ruraldevelopment URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from ruraldevelopment import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    # path('header/',views.header,name='header'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('supplier-register/',views.supplierregister,name="sr"),
    path('company-register/',views.companyregister,name="cr"),
    path('earthenware/',views.earthenware,name="earthenware"),
    path('stoneware/',views.stoneware,name="stoneware"),
    path('poreclain/',views.poreclain,name="poreclain"),
    path('kharif/',views.kharif),
    path('rabi/',views.rabi),
    path('zaid/',views.zaid),
    path('supplierprofile/',views.supplierprofile,name="supplierprofile"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('listofsupplier/<str:productName>',views.listofsupplier),
    path('<str:productname>/<str:suppliername>',views.viewsupplierprofile,name="viewsupplierprofile"),
    path('companyprofile/',views.companyprofile,name="companyprofile"),
    path('removeitems/',views.removeitems,name="removeitems"),
    path('request/<int:id>/<str:operation>',views.Request,name="Request"),
    
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
