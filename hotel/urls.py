
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "Mister D's Hotel Staff"
admin.site.site_title = "Mister D's Hotel Admin Portal"
admin.site.index_title = "Welcome to Mister D's Hotel Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
]
