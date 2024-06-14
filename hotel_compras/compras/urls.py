# En compras/urls.py

from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('crear/', views.crear_solicitud, name='crear_solicitud'),
    path('', TemplateView.as_view(template_name='index.html'), name='inicio'),
    path('<int:solicitud_id>/actualizar/', views.actualizar_solicitud, name='actualizar_solicitud'),
    path('<int:solicitud_id>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('<int:solicitud_id>/eliminar/', views.eliminar_solicitud, name='eliminar_solicitud'),
    path('lista/', views.lista_solicitudes, name='lista_solicitudes'),
    # Otras URLs necesarias
]
