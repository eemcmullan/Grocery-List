

from django.contrib import admin
from django.urls import path, include
from grocery_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('grocery_list.urls')),
]
