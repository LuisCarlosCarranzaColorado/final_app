from pyexpat import model
from django.db import models

class Customer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    isAdmin = models.BooleanField(default=False)

class Account(models.Model):
    number = models.IntegerField(primary_key=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    lastChangeDate = models.DateField()
    isActive = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, related_name='account', on_delete=models.CASCADE)

class usuario(models.Model):
    no_cedula = models.BigIntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=255, null=False)
    segundo_nombre = models.CharField(max_length=255)
    primer_apellido= models.CharField(max_length=255, null=False)
    segundo_apellido= models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=False)
    no_celular = models.CharField(max_length=255,null=False)
    rol = models.CharField(max_length=255,null=False)
    contrasena = models.CharField(max_length=255,null=False)
    fecha_nacimiento = models.DateField(max_length=255,null=False)
    ubicacion_gps_latitud = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    ubicacion_gps_longitud= models.DecimalField(max_digits=20, decimal_places=2, default=0)

class medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    no_cedula = models.ForeignKey(usuario, related_name='Usuario', on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, null = False)

class enfermero(models.Model):
    id_enfermero = models.AutoField(primary_key=True)
    no_cedula = models.ForeignKey(usuario, related_name='UsuarioEnf', on_delete=models.CASCADE)
    turno = models.CharField(max_length=50, null = False)
    especialidad = models.CharField(max_length=100, null = False)

class secretario(models.Model):
    id_secretario = models.AutoField(primary_key=True)
    no_cedula = models.ForeignKey(usuario, related_name='UsuarioSec', on_delete=models.CASCADE)
    turno = models.CharField(max_length=50, null = False)

class paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    no_cedula = models.ForeignKey(usuario, related_name='UsuarioPac', on_delete=models.CASCADE)
    id_medico = models.ForeignKey(medico, related_name='medicoPac', on_delete=models.CASCADE)
    id_enfermero = models.ForeignKey(enfermero, related_name='enfermeroPac', on_delete=models.CASCADE)

class acompanante(models.Model):
    id_acompanante = models.AutoField(primary_key=True)
    parentesco = models.CharField(max_length=50, null = False)
    no_cedula = models.ForeignKey(usuario, related_name='UsuarioAcom', on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(paciente, related_name='pacienteAcom', on_delete=models.CASCADE)

class historia_clinica(models.Model):
    id_historia = models.AutoField(primary_key=True)
    fecha_hora = models.DateTimeField(null=False)
    diagnostico = models.CharField(max_length=500, null = False)
    FC = models.IntegerField(null = False)
    TA = models.IntegerField(null = False)
    FR = models.IntegerField(null = False)
    Temp = models.IntegerField(null = False)
    Oxi = models.IntegerField(null = False)
    Recomendaciones = models.CharField(max_length=500, null = False)
    id_paciente = models.ForeignKey(paciente, related_name='Paciente_His', on_delete=models.CASCADE)