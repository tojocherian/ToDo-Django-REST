
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import login, logout_then_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('accounts/logout/', logout_then_login, name='logout'),
    path('accounts/login/', login, name='login'),
]
