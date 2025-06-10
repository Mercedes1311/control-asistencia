from django.shortcuts import render
from .models import Empleado, TipoAsistencia, RegistroAsistencia
from django.utils import timezone

def registrar_asistencia(request):
    empleados = Empleado.objects.all()
    tipos_evento = TipoAsistencia.objects.all()

    if request.method == 'POST':
        empleado_id = request.POST.get('empleado')
        tipo_id = request.POST.get('tipo_evento')
        descripcion = request.POST.get('descripcion') or ''

        now_utc = timezone.now()
        now_local = timezone.localtime(now_utc)

        fecha = now_local.date()
        hora = now_local.time()

        empleado = Empleado.objects.get(id_empleado=empleado_id)

        RegistroAsistencia.objects.create(
            empleado=empleado,
            tipo_id=tipo_id,
            fecha_registro=fecha,
            hora_registro=hora,
            descripcion=descripcion
        )

        return render(request, 'asistencia_exitosa.html', {
            'fecha': fecha,
            'hora': hora,
            'empleado': empleado
        })

    return render(request, 'formulario.html', {
        'empleados': empleados,
        'tipos_evento': tipos_evento
    })

def asistencia_exitosa(request):
    return render(request, 'asistencia_exitosa.html')