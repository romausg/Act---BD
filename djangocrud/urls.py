"""
URL configuration for mi_grupo_personal project.

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
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='inicio'),
    path('registro/',views.signup,name='registro'),
    path('actividades/',views.tasks,name='actividades'),
    path('actividades/crear/',views.create_task,name='crear_actividad'),
    path('actividades/completadas/',views.tasks_completed,name='actividades_completadas'),
    path('actividades/<int:task_id>/',views.task_detail,name='detalle_actividad'),
    path('actividades/<int:task_id>/completar',views.complete_task,name='completar_actividad'),
    path('actividades/<int:task_id>/eliminar',views.delete_task,name='eliminar_actividad'),
    path('cerrar-sesion/',views.signout,name='cerrar_sesion'),
    path('iniciar-sesion/',views.signin,name='iniciar_sesion'),
]
