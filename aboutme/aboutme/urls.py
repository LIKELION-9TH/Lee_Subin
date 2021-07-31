from django.contrib import admin
from django.urls import path
from leesubin import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('hobby/', views.hobby, name="hobby"),
    path('movien/', views.movie, name="movie"),
    path('music/', views.music, name="music"),
    path('photo/', views.photo, name="photo"),
    path('<str:id>',views.detail,name="detail"),
    path('new/',views.new, name="new"),
    path('create/', views.create, name="create"),
    path('edit/<str:id>',views.edit, name="edit"),
    path('update/<str:id>', views.update, name="update"),
    path('delete/<str:id>', views.delete, name="delete"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)