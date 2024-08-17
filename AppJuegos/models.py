from tracemalloc import start
from django.db import models
from .choices import *
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import AbstractUser,BaseUserManager
from datetime import datetime
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, rol=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico debe ser proporcionado')
        email = self.normalize_email(email)
        if rol is None:
            rol = Rol.objects.get_or_create(name='default_rol')[0]  # Obtener o crear un rol por defecto
        user = self.model(username=username, email=email, rol=rol, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, rol=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico debe ser proporcionado')
        email = self.normalize_email(email)
        if rol is None:
            rol = Rol.objects.get_or_create(name='default_rol')[0]  # Obtener o crear un rol por defecto
        user = self.model(username=username, email=email, rol=rol, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class Rol(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True, verbose_name='Nombre')
    description = models.TextField(max_length=100, verbose_name='Descripcion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    is_active = models.BooleanField(default=True)

    def _str_(self):
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
    sex = models.CharField(max_length=50, choices=SEX , default='Masculino', verbose_name='Sexo')
    address = models.CharField(max_length=100, verbose_name='Direccion')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Rol')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    history = HistoricalRecords()
    is_active = models.BooleanField(default=True)

     # Estos campos son necesarios para manejar los permisos en Django
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=datetime.now)

    first_name = None
    last_name = None
    groups = None
    user_permissions = None
    #is_staff = None
    #is_superuser = None
    last_login = None
    #date_joined = None

    objects = CustomUserManager()  # Asignar el CustomUserManager

    def _str_(self):
        return self.names + ' ' + self.surnames + ' - ' + self.email

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id','username','cedula', 'names', 'surnames','email', 'phone']

class Permission(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name='Nombre')

    def _str_(self):
        return self.name
    
    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'
        ordering = ['id']

class RolPermission(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Rol')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, verbose_name='Permiso')

    def _str_(self):
        return self.rol.name + ' ' + self.permission.name

    class Meta:
        verbose_name = 'RolPermiso'
        verbose_name_plural = 'RolPermisos'
        ordering = ['rol', 'permission']

class Client(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    cedula = models.CharField(max_length=10, unique=True, verbose_name='Cédula')
    names = models.CharField(max_length=100, verbose_name='Nombres')
    surnames = models.CharField(max_length=100, verbose_name='Apellidos')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Correo Electronico')
    phone = models.CharField(max_length=10, verbose_name='Telefono')
    sex = models.CharField(max_length=50, choices=SEX , default='Femenino', verbose_name='Sexo')
    address = models.CharField(max_length=500, verbose_name='Direccion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    history = HistoricalRecords()
    user_client_register = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario que registra', related_name='user_client_register')
    user_client_modify = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario que modifica', related_name='user_client_modify', null=True, blank=True)

    def _str_(self):
        return self.names + ' ' + self.surnames + ' - ' + self.email

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id', 'cedula', 'names', 'surnames','email', 'phone']


class Game(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    start_date = models.DateTimeField(verbose_name='Fecha inicio juego')
    end_date = models.DateTimeField(verbose_name='Fecha fin juego')
    modification_date = models.DateTimeField(verbose_name='Fecha  modificacion juego',null=True)
    name = models.CharField(max_length=50, choices=GAME_CHOICES, default="Tragamonedas",verbose_name='Nombre')
    players = models.IntegerField(default=0, verbose_name='Jugadores')
    state = models.CharField(max_length=100, default='Activado', choices=GAME_STATES)
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()

    def _str_(self):
        return self.name


    class Meta:
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'

class Award(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.TextField(max_length=100, verbose_name='Descripcion')
    imagen = models.ImageField(upload_to='premios/', verbose_name='Imagen')
    initial_stock = models.IntegerField(verbose_name='Stock inicial')
    condition_stock = models.IntegerField(verbose_name='Stock Condicionado', default=0)
    prizes_awarded = models.IntegerField(verbose_name='Premios entregados', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    is_active = models.BooleanField(default=True)
    user_register = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario que registra', related_name='user_register')
    user_modify = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario que modifica', related_name='user_modify', null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY, default='Comun', verbose_name='Categoria')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Juego')
    history = HistoricalRecords()

    def _str_(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

    class Meta:
        verbose_name = 'Premio'
        verbose_name_plural = 'Premios'
        ordering = ['id','name','description', 'initial_stock', 'prizes_awarded']

# Modelos de contraseña

class ForgotPassword(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    email = models.EmailField(max_length=100, unique=True, verbose_name='Correo Electronico')
    code = models.CharField(max_length=6, verbose_name='Codigo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')

    def _str_(self):
        return self.email

    class Meta:
        verbose_name = 'RecuperarContraseña'
        verbose_name_plural = 'RecuperarContraseñas'
        ordering = ['email', 'code']

# ================================================================================================================== 
class AwardCondition(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    award = models.ForeignKey(Award, on_delete=models.CASCADE, verbose_name='Premio')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Juego')
    start_date = models.DateTimeField(verbose_name='Fecha inicio premio')
    end_date = models.DateTimeField(verbose_name='Fecha fin premio')
    is_approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    user_register = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario que registra', related_name='user_register_award_condition')
    user_modify = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario que modifica', related_name='user_modify_award_condition', null=True, blank=True)
    history = HistoricalRecords()

    def _str_(self):
        return self.award.name

    class Meta:
        verbose_name = 'CondicionPremio'
        verbose_name_plural = 'CondicionPremios'
        ordering = ['id','award', 'game']

class Publicity_top(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    image = models.ImageField(upload_to='publicity_top/', null=False)


class Publicity_bottom(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    image = models.ImageField(upload_to='publicity_bottom/', null=False)


class Publicity_game(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    image = models.ImageField(upload_to='publicity_game', null=True)
    

class Probabilidad(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    percent_win = models.PositiveIntegerField('porcent_win',null=False,default=0)
    winners_limit = models.PositiveIntegerField('winners_limit',null=False,default=0)
    attempts_limit = models.PositiveIntegerField('numero de intentos',null=False,default=1)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE,verbose_name = 'Juego' )
   
    
    class Meta:
        verbose_name = 'Probabilidad'
        verbose_name_plural = 'Probabilidades'


class Publicity(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    time_display = models.IntegerField(verbose_name='Tiempo de vista ',null=False,default=4)

    class Meta:
        verbose_name = 'Publicity'
        verbose_name_plural = 'Publicities'


class Ticket(models.Model): # Entradas
    id = models.AutoField(primary_key=True, unique=True)
    invoice_number = models.CharField(max_length=255)
    qr_code_digits = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_ticket_played = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=100, choices=TICKET_STATES, default='Disponible')
    history = HistoricalRecords()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default='', related_name='ticket_client')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default='', related_name='ticket_game')
    user_register = models.ForeignKey(User, on_delete=models.CASCADE, default='', related_name='register_ticket')
    game_start = models.DateTimeField()
    game_end = models.DateTimeField()


class TicketConfiguration(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    logo = models.ImageField(upload_to='logo_ticket/', null=True)
    title = models.CharField(max_length=255, null=True, default='Gana premios jugando')
    description = models.CharField(max_length=255, null=True, default='Gana premios jugando')


class Match(models.Model): # Partida
    id = models.AutoField(primary_key=True, unique=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=False, related_name='match_ticket')
    award = models.ForeignKey(Award, on_delete=models.CASCADE, null=True, related_name='award')
    date_created = models.DateTimeField(auto_now_add=True)
    win_match = models.BooleanField(default=False,null=False,verbose_name="¿ganó la partida?")
    delivered = models.BooleanField(default=False,null=False,verbose_name="entrego el premio?")


class Audio(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    audio = models.FileField(upload_to='audio/', verbose_name='audio',  null=False)


class Styles(models.Model): # Partida
    id = models.AutoField(primary_key=True, unique=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE,verbose_name = 'Juego' )
    color_text = models.CharField(max_length=50,choices=BASIC_COLORS ,verbose_name = 'color texto',null=True)
    font_letter= models.CharField(max_length=50,choices=BASIC_FONTS ,verbose_name = 'Fuente Letra',null=True)
    color_background_game = models.CharField(max_length=50, choices=GAME_BACKGROUND_COLOR , default='Black', verbose_name='color de fondo')


    image_machine_game = models.ImageField(upload_to='design/',verbose_name = 'imagen máquina tragamonedas',null=True)
    image_box_watch = models.ImageField(upload_to='design/',verbose_name = 'imagen caja reloj',null=True)

    image_dice_face_one = models.ImageField(upload_to='design/',verbose_name = 'imagen dado cara uno',null=True)
    image_dice_face_two = models.ImageField(upload_to='design/',verbose_name = 'imagen dado cara dos',null=True)
    image_dice_face_three = models.ImageField(upload_to='design/',verbose_name = 'imagen dado cara tres',null=True)
    image_dice_face_four = models.ImageField(upload_to='design/',verbose_name = 'imagen dado cara cuatro',null=True)
    image_dice_face_five = models.ImageField(upload_to='design/',verbose_name = 'imagen dado cara cinco',null=True)
    image_dice_face_six = models.ImageField(upload_to='design/',verbose_name = 'imagen dado cara seis',null=True)

    image_door_left = models.ImageField(upload_to='design/',verbose_name = 'imagen puerta izquierda',null=True)
    image_door_center = models.ImageField(upload_to='design/',verbose_name = 'imagen puerta central',null=True)
    image_door_right = models.ImageField(upload_to='design/',verbose_name = 'imagen puerta derecha',null=True)

    image_logo_tragamonedas = models.ImageField(upload_to='design/',verbose_name = 'imagen logo juego Tragamonedas',null=True)
    image_logo_precision = models.ImageField(upload_to='design/',verbose_name = 'imagen logo juego Precisión',null=True)
    image_logo_dados = models.ImageField(upload_to='design/',verbose_name = 'imagen logo juego Dados',null=True)
    image_logo_puertas = models.ImageField(upload_to='design/',verbose_name = 'imagen logo juego Puertas',null=True)

    image_background_tragamonedas = models.ImageField(upload_to='design/',verbose_name = 'imagen fondo Tragamonedas',null=True)
    image_background_precision = models.ImageField(upload_to='design/',verbose_name = 'imagen fondo Precisión',null=True)
    image_background_dados = models.ImageField(upload_to='design/',verbose_name = 'imagen fondo Dados',null=True)
    image_background_puertas = models.ImageField(upload_to='design/',verbose_name = 'imagen fondo Puertas',null=True)

    image_background_kiosco = models.ImageField(upload_to='design/',verbose_name = 'imagen fondo Kiosco',null=True)
    image_logo_kiosco = models.ImageField(upload_to='design/',verbose_name = 'imagen logo Kiosco',null=True)

    video_screensaver = models.FileField(upload_to='screensaver/',verbose_name = 'video Salvapantallas',null=True)
    video_autoplay=models.BooleanField(default=True,verbose_name='video autoplay')
    video_loop=models.BooleanField(default=True,verbose_name='video loop')
    title_button_screensaver= models.CharField(max_length=100,verbose_name = 'título botón salvapantallas',null=True)

    scan_code_title=models.CharField(max_length=200,default='Escanear Código')
    scan_code_description=models.CharField(max_length=200,default='Puedes escanear el código QR de tu ticket')
  
    title_winner = models.CharField(max_length=150, verbose_name='título del ganador',null=True,default='¡JUEGA OTRA VEZ!')
    description_winner = models.CharField(max_length=200,verbose_name = 'descripción ganador juego',null=True,default='¡HAS GANADO!')
    image_winner = models.FileField(upload_to='design/',verbose_name = 'imagen ganador',null=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class GameImageUpload(models.Model):
    game_name = models.CharField(max_length=100)
    image_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to=f'media/{game_name}/')

    def __str__(self):
        return f'{self.game_name} - {self.image_type}'

# ================================================================================================================== 
# Log del juego enc curso, cliente que juega, en que maquina juega
# ================================================================================================================== 

class GameCurrentSession(models.Model):
    # Lista de campos, asegúrate de que `client_id` no esté aquí.
    kiosko_numero = models.CharField(max_length=100)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    game_id = models.CharField(max_length=100)  # Cambiado a CharField para almacenar un ID de juego como string
    gano = models.BooleanField(default=False,null=False,verbose_name="¿ganó la partida?")
    award_id = models.ForeignKey(Award, null=True, blank=True, on_delete=models.SET_NULL)
    fecha_hora_startgame = models.DateTimeField()
    fecha_hora_finalgame = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f'Partida {self.id} - Cliente {self.client} - Juego {self.game}'

    class Meta:
        verbose_name = 'Partida en Curso'
        verbose_name_plural = 'Partidas en Curso'
        ordering = ['id']
