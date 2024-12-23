from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld', include('hello.urls')),
    path('helloworldhtml/', include('helloworldhtml.urls')),
    path('messageboard/', include('messageboard.urls')),
    path('responses/', include('responses.urls')),
]