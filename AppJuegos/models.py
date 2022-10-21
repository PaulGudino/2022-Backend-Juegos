from django.db import models
from .choices import sex, category, juego
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

# ==================================================================================================================
#
# Client Model

# Example taken from https://docs.djangoproject.com/en/4.0/ref/models/fields/

NONE = 'Ninguno'
ACTIVE = 'Activo'
INACTIVE = 'Inactivo'
DISABLED = 'Deshabilitado'

STATES = [
    (NONE, 'Ninguno'),
    (ACTIVE, 'Activo'),
    (INACTIVE, 'Inactivo'),
    (DISABLED, 'Desabilitado')
]

class Client(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    cedula = models.CharField(max_length=10, unique=True, verbose_name='Cédula')
    names = models.CharField(max_length=100, verbose_name='Nombres')
    surnames = models.CharField(max_length=100, verbose_name='Apellidos')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Correo Electronico')
    phone = models.CharField(max_length=10, verbose_name='Telefono')
    sex = models.CharField(max_length=1, choices=sex , default='N', verbose_name='Sexo')
    address = models.CharField(max_length=500, verbose_name='Direccion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    history = HistoricalRecords()
    state = models.CharField(max_length=100, choices=STATES, default='Ninguno', verbose_name='Estado')
    user_client_register = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario que registra', related_name='user_client_register')
    user_client_modify = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario que modifica', related_name='user_client_modify', null=True, blank=True)

    def __str__(self):
        return self.names + ' ' + self.surnames + ' - ' + self.email

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id', 'cedula', 'names', 'surnames','email', 'phone']

# ================================================================================================================== 

class Award(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.TextField(max_length=100, verbose_name='Descripcion')
    imagen = models.ImageField(upload_to='premios/', verbose_name='Imagen')
    initial_stock = models.IntegerField(verbose_name='Stock inicial')
    current_stock = models.IntegerField(verbose_name='Stock actual', default=0)
    prizes_awarded = models.IntegerField(verbose_name='Premios entregados', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    is_active = models.BooleanField(default=True)
    user_register = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario que registra', related_name='user_register')
    user_modify = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario que modifica', related_name='user_modify', null=True, blank=True)
    category = models.CharField(max_length=1, choices=category, default='C', verbose_name='Categoria')
    juego = models.CharField(max_length=1, choices=juego, default='T', verbose_name='Juego')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

    class Meta:
        verbose_name = 'Premio'
        verbose_name_plural = 'Premios'
        ordering = ['id','name','description', 'initial_stock', 'current_stock', 'prizes_awarded']


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


class ImagenesJuegos(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    imagen = models.ImageField(upload_to='imagenes_juegos/', verbose_name='Imagen')

    def __str__(self):
        return self.imagen

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

    class Meta:
        verbose_name = 'ImagenJuego'
        verbose_name_plural = 'ImagenesJuegos'
        ordering = ['imagen']



