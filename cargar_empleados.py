# cargar_empleados.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'control_asistencia.settings')
django.setup()

from app.models import Empleado, TipoAsistencia

# Crear empleados
Empleado.objects.bulk_create([
    Empleado(nombres='Ademir', apellidos='Arredondo', dni=10000001, contrato='RRHH'),
    Empleado(nombres='Alexis', apellidos='Vasquez Conchatupa', dni=10000002, contrato='Planilla'),
    Empleado(nombres='Carlos Fernando', apellidos='Lozano Roman', dni=10000003, contrato='RRHH'),
    Empleado(nombres='Carlos Gabriel', apellidos='More Miranda', dni=10000004, contrato='Planilla'),
    Empleado(nombres='Claudia', apellidos='Aguilar', dni=10000005, contrato='RRHH'),
    Empleado(nombres='Cristopher', apellidos='Rufasto', dni=10000006, contrato='RRHH'),
    Empleado(nombres='David Eduardo', apellidos='Pauta Juarez', dni=10000007, contrato='Planilla'),
    Empleado(nombres='Edson', apellidos='Pavel Ipenza', dni=10000008, contrato='RRHH'),
    Empleado(nombres='Edwin', apellidos='Chaparro Ampa', dni=10000009, contrato='RRHH'),
    Empleado(nombres='Iris', apellidos='Oblitas La Rosa', dni=10000010, contrato='RRHH'),
    Empleado(nombres='Jean Leonardo', apellidos='Estrada Roque', dni=10000011, contrato='Planilla'),
    Empleado(nombres='Joel Edwin', apellidos='Llanos Mejico', dni=10000012, contrato='RRHH'),
    Empleado(nombres='Jonathan Oswaldo', apellidos='Azaña Ramos', dni=10000013, contrato='Planilla'),
    Empleado(nombres='Jordi Cesar Hernando', apellidos='Quezada Rosales', dni=10000014, contrato='RRHH'),
    Empleado(nombres='Jose Alberto', apellidos='Davila Paredes', dni=10000015, contrato='RRHH'),
    Empleado(nombres='Jose Angel', apellidos='Borda Hernandez', dni=10000016, contrato='Planilla'),
    Empleado(nombres='Jose Lino', apellidos='Solano Caqui', dni=10000017, contrato='Planilla'),
    Empleado(nombres='Jose Luis', apellidos='Gonzalez Romero', dni=10000018, contrato='Planilla'),
    Empleado(nombres='Julio Daniel', apellidos='Pañaherrera Orillo', dni=10000019, contrato='Planilla'),
    Empleado(nombres='Kevin Paul', apellidos='Sanchez', dni=10000020, contrato='Planilla'),
    Empleado(nombres='Marco Antonio Jose', apellidos='Garcia Galvan', dni=10000032, contrato='Planilla'),
    Empleado(nombres='Mercedes Anayely', apellidos='Durand Azurza', dni=10000021, contrato='RRHH'),
    Empleado(nombres='Pedro Luis', apellidos='Hernandez Reyes', dni=10000022, contrato='Planilla'),
    Empleado(nombres='Romulo', apellidos='Prieto', dni=10000023, contrato='RRHH'),
    Empleado(nombres='Ruben Dario', apellidos='Canicani Ccahuana', dni=10000024, contrato='RRHH'),
    Empleado(nombres='Saul', apellidos='Gamarra Quispe', dni=10000025, contrato='Planilla'),
    Empleado(nombres='Stalin', apellidos='Llulluy Ramón', dni=10000026, contrato='RRHH'),
    Empleado(nombres='Valery', apellidos='Celestino Begar', dni=10000027, contrato='RRHH'),
    Empleado(nombres='Willy Jhon', apellidos='Paco Deza', dni=10000028, contrato='RRHH'),
    Empleado(nombres='Wilmer', apellidos='Quispe Huaringa', dni=10000029, contrato='Planilla'),
    Empleado(nombres='Yuli', apellidos='Tarazona Aguirre', dni=10000030, contrato='RRHH'),
    Empleado(nombres='Zhihua Santiago', apellidos='Yong Sanchez', dni=10000031, contrato='Planilla'),
    
])

# Crear tipos de asistencia si no existen
tipos = [
    'Entrada', 'Salida', 'Inicio Almuerzo', 'Fin Almuerzo',
    'Entrada por comisión', 'Salida por comisión',
    'Entrada por otros', 'Salida por otros'
]
for nombre in tipos:
    TipoAsistencia.objects.get_or_create(nombre_asistencia=nombre)

print("Datos insertados correctamente.")
