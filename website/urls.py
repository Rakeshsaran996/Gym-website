from django.contrib import admin
from django.urls import path , include

admin.site.site_header = "RAKESH FITNESS Admin"
admin.site.site_title = "RAKESH FITNESS Admin Portal"
admin.site.index_title = "Welcome to RAKESH FITNESS"

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('home.urls')),
     
]
