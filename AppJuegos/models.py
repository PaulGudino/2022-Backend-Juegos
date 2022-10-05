from django.db import models
from .choices import sex
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import AbstractUser


class Rol(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True, verbose_name='Nombre')
    description = models.TextField(max_length=100, verbose_name='Descripcion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['name']

class User(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True)
    cedula = models.CharField(max_length=10, unique=True, verbose_name='Cédula')
    names = models.CharField(max_length=100, verbose_name='Nombres')
    surnames = models.CharField(max_length=100, verbose_name='Apellidos')
    username = models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Correo Electronico')
    password = models.CharField(max_length=255, verbose_name='Contraseña')
    phone = models.CharField(max_length=10, verbose_name='Telefono')
    sex = models.CharField(max_length=1, choices=sex , default='M', verbose_name='Sexo')
    address = models.CharField(max_length=100, verbose_name='Direccion')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Rol')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    history = HistoricalRecords()
    last_session = models.DateTimeField(auto_now=True, verbose_name='Ultima sesion')
    is_active = models.BooleanField(default=True)

    first_name = None
    last_name = None
    groups = None
    user_permissions = None
    is_staff = None
    is_superuser = None
    last_login = None
    date_joined = None

    def __str__(self):
        return self.names + ' ' + self.surnames + ' - ' + self.email

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id','username','cedula', 'names', 'surnames','email', 'phone']

class Permission(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'
        ordering = ['id']

class RolPermission(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Rol')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, verbose_name='Permiso')

    def __str__(self):
        return self.rol.name + ' ' + self.permission.name

    class Meta:
        verbose_name = 'RolPermiso'
        verbose_name_plural = 'RolPermisos'
        ordering = ['rol', 'permission']


# Modelos de contraseña

class ForgotPassword(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    email = models.EmailField(max_length=100, unique=True, verbose_name='Correo Electronico')
    code = models.CharField(max_length=6, verbose_name='Codigo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'RecuperarContraseña'
        verbose_name_plural = 'RecuperarContraseñas'
        ordering = ['email', 'code']


