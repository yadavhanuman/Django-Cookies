
from django.contrib import admin
from django.urls import path
from facebook import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.setcookie),
    path('get/',views.getcookie),
    path('delete/',views.deletecookie), 
]
