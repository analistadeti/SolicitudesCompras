# En compras/urls.py

from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('crear/', views.crear_solicitud, name='crear_solicitud'),
    path('<int:solicitud_id>/actualizar/', views.actualizar_solicitud, name='actualizar_solicitud'),
    path('<int:solicitud_id>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('<int:solicitud_id>/eliminar/', views.eliminar_solicitud, name='eliminar_solicitud'),
    path('lista/', views.lista_solicitudes, name='lista_solicitudes'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_departamento/', views.crear_departamento, name='crear_departamento'),
    path('departamentos/', views.lista_departamentos, name='lista_departamentos'),
    path('estados/', views.lista_estados, name='lista_estados'),
    path('estados/crear/', views.crear_estado, name='crear_estado'),
    path('estados/<int:estado_id>/actualizar/', views.actualizar_estado, name='actualizar_estado'),
    path('estados/<int:estado_id>/eliminar/', views.eliminar_estado, name='eliminar_estado'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', auth_views.LoginView.as_view(template_name='login.html')),  # Redirigir la raíz al login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]