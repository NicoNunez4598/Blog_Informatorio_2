"""
URL configuration for Blog_Online project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from GestionDeBlog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='inicio'),
    path('accounts/', include('django.contrib.auth.urls'), name="login"),
    path('logout/', views.exit, name="exit"),
    path('register/', views.register, name='register'),
    path('generales/', views.generales, name='generales'),
    path('tutoriales/', views.tutoriales, name='tutoriales'),
    path('tecnologia/', views.tecnologia, name='tecnologia'),
    path('programacion/', views.programacion, name='programacion'),
    path('videojuegos/', views.videojuegos, name='videojuegos'),
    path('Usuarios/', views.usuarios, name="usuarios"),
    path('registrarusuario/', views.registrarusuario, name="registrarusuario"),
    path('Usuarios/edicionusuario/<username>', views.edicionusuario, name="edicionusuario"),
    path('Usuarios/eliminarusuario/<username>', views.eliminarusuario, name="eliminarusuario"),
    path('editarusuario/', views.editarusuario, name="editarusuario"),
    path('Posts/', views.posts, name="posts"),
    path('registrarpost/', views.registrarpost, name="registrarpost"),
    path('Posts/edicionpost/<id>', views.edicionpost, name="edicionpost"),
    path('Posts/eliminarpost/<id>', views.eliminarpost, name="eliminarpost"),
    path('editarpost/', views.editarpost, name="editarpost"),
    path('Categorias/', views.categorias, name="categorias"),
    path('registrarcategoria/', views.registrarcategoria, name="registrarcategoria"),
    path('Categorias/edicioncategoria/<id>', views.edicioncategoria, name="edicioncategoria"),
    path('Categorias/eliminarcategoria/<id>', views.eliminarcategoria, name="eliminarcategoria"),
    path('editarcategoria/', views.editarcategoria, name="editarcategoria"),
    path('registrarcomentario/<int:pk>/', views.registrarcomentario, name="registrarcomentario"),
    path('<slug:slug>/', views.detallepost, name='detallepost'),
    path('eliminarcomentario/<id>/', views.eliminarcomentario, name='eliminarcomentario'),
]
