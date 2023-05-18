from django.contrib import admin
from django.urls import path
from ads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.StartView.as_view()),
]
