from django.db import models
from .choices import sex, state
from django.utils import timezone
from simple_history.models import HistoricalRecords
from werkzeug.security import check_password_hash


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.TextField(max_length=255, verbose_name='Descripcion')
    created = models.DateField(default=timezone.now)
    modified = AutoDateTimeField(default=timezone.now)
    state = models.CharField(max_length=1, choices=state , default='A', verbose_name='Estado')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['name']

class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    cedula = models.CharField(max_length=10, unique=True, verbose_name='Cédula')
    first_name = models.CharField(max_length=50, verbose_name='Primer Nombre')
    second_name = models.CharField(max_length=50, verbose_name='Segundo Nombre')
    father_last_name = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    mother_last_name = models.CharField(max_length=50, verbose_name='Apellido Materno')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Correo Electronico')
    password = models.CharField(max_length=255, verbose_name='Contraseña', unique=True)
    phone = models.CharField(max_length=10, verbose_name='Telefono')
    sex = models.CharField(max_length=1, choices=sex , default='M')
    address = models.CharField(max_length=255, verbose_name='Direccion')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Rol')
    created = models.DateField(default=timezone.now)
    modified = AutoDateTimeField(default=timezone.now)
    history = HistoricalRecords()
    last_session = models.DateTimeField(default=timezone.now)
    state = models.CharField(max_length=1, choices=state , default='A', verbose_name='Estado')

    def __str__(self):
        return self.first_name + ' ' + self.father_last_name + ' ' + self.mother_last_name

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id','cedula', 'first_name', 'father_last_name', 'mother_last_name','email', 'state']

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'
        ordering = ['name']

class RolPermission(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Rol')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, verbose_name='Permiso')

    def __str__(self):
        return self.rol.name + ' ' + self.permission.name

    class Meta:
        verbose_name = 'RolPermiso'
        verbose_name_plural = 'RolPermisos'
        ordering = ['rol', 'permission']



