from django.shortcuts import render, get_object_or_404, redirect
from .models import SolicitudCompra, EstadoCompra
from .forms import SolicitudCompraForm, EstadoCompraForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def lista_solicitudes(request):
    solicitudes = SolicitudCompra.objects.all()
    return render(request, 'lista_solicitudes.html', {'solicitudes': solicitudes})

def detalle_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudCompra, pk=solicitud_id)
    estados = EstadoCompra.objects.filter(solicitud=solicitud)
    return render(request, 'detalle_solicitud.html', {'solicitud': solicitud, 'estados': estados})

# Otras vistas para crear, actualizar y eliminar solicitudes y estados
@login_required
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudCompraForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.solicitante = request.user
            solicitud.save()
            # Crear el primer estado de la solicitud (ej. Solicitado)
            EstadoCompra.objects.create(solicitud=solicitud, estado='Solicitado', actualizado_por=request.user)
            return redirect('lista_solicitudes')
    else:
        form = SolicitudCompraForm()
    
    return render(request, 'crear_solicitud.html', {'form': form})

@login_required
def actualizar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudCompra, pk=solicitud_id)
    
    if request.method == 'POST':
        form = EstadoCompraForm(request.POST)
        if form.is_valid():
            estado_nuevo = form.save(commit=False)
            estado_nuevo.solicitud = solicitud
            estado_nuevo.actualizado_por = request.user
            estado_nuevo.save()
            # Actualizar el estado en la solicitud principal también (opcional)
            solicitud.estado = estado_nuevo.estado
            solicitud.save()
            return redirect('detalle_solicitud', solicitud_id=solicitud.id)
    else:
        form = EstadoCompraForm()
    
    return render(request, 'actualizar_solicitud.html', {'form': form, 'solicitud': solicitud})

# En compras/views.py



@login_required
def eliminar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudCompra, pk=solicitud_id)
    
    if request.method == 'POST':
        solicitud.delete()
        messages.success(request, 'La solicitud se ha eliminado correctamente.')
        return redirect('lista_solicitudes')
    
    return render(request, 'eliminar_solicitud.html', {'solicitud': solicitud})
