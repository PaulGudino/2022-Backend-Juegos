# Generated by Django 4.1.1 on 2023-01-18 20:21

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('audio', models.FileField(upload_to='audio/', verbose_name='audio')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField(max_length=100, verbose_name='Descripcion')),
                ('imagen', models.ImageField(upload_to='premios/', verbose_name='Imagen')),
                ('initial_stock', models.IntegerField(verbose_name='Stock inicial')),
                ('condition_stock', models.IntegerField(default=0, verbose_name='Stock Condicionado')),
                ('prizes_awarded', models.IntegerField(default=0, verbose_name='Premios entregados')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('Legendaria', 'Legendaria'), ('Épica', 'Épica'), ('Rara', 'Rara'), ('Común', 'Común')], default='Comun', max_length=50, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Premio',
                'verbose_name_plural': 'Premios',
                'ordering': ['id', 'name', 'description', 'initial_stock', 'prizes_awarded'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cédula')),
                ('names', models.CharField(max_length=100, verbose_name='Nombres')),
                ('surnames', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo Electronico')),
                ('phone', models.CharField(max_length=10, verbose_name='Telefono')),
                ('sex', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], default='Femenino', max_length=50, verbose_name='Sexo')),
                ('address', models.CharField(max_length=500, verbose_name='Direccion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['id', 'cedula', 'names', 'surnames', 'email', 'phone'],
            },
        ),
        migrations.CreateModel(
            name='ForgotPassword',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo Electronico')),
                ('code', models.CharField(max_length=6, verbose_name='Codigo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'RecuperarContraseña',
                'verbose_name_plural': 'RecuperarContraseñas',
                'ordering': ['email', 'code'],
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateTimeField(verbose_name='Fecha inicio juego')),
                ('end_date', models.DateTimeField(verbose_name='Fecha fin juego')),
                ('modification_date', models.DateTimeField(null=True, verbose_name='Fecha  modificacion juego')),
                ('name', models.CharField(choices=[('Tragamonedas', 'Tragamonedas')], default='Tragamonedas', max_length=50, verbose_name='Nombre')),
                ('players', models.IntegerField(default=0, verbose_name='Jugadores')),
                ('state', models.CharField(choices=[('Activado', 'Activado'), ('Desactivado', 'Desactivado')], default='Activado', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Juego',
                'verbose_name_plural': 'Juegos',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Permiso',
                'verbose_name_plural': 'Permisos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Publicity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('time_display', models.IntegerField(default=4, verbose_name='Tiempo de vista ')),
            ],
            options={
                'verbose_name': 'Publicity',
                'verbose_name_plural': 'Publicities',
            },
        ),
        migrations.CreateModel(
            name='Publicity_bottom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='publicity_bottom/')),
            ],
        ),
        migrations.CreateModel(
            name='Publicity_game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(null=True, upload_to='publicity_game')),
            ],
        ),
        migrations.CreateModel(
            name='Publicity_top',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='publicity_top/')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(max_length=100, verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TicketConfiguration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('logo', models.ImageField(null=True, upload_to='logo_ticket/')),
                ('title', models.CharField(default='Gana premios jugando', max_length=255, null=True)),
                ('description', models.CharField(default='Gana premios jugando', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cédula')),
                ('names', models.CharField(max_length=100, verbose_name='Nombres')),
                ('surnames', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo Electronico')),
                ('password', models.CharField(max_length=255, verbose_name='Contraseña')),
                ('phone', models.CharField(max_length=10, verbose_name='Telefono')),
                ('sex', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], default='Masculino', max_length=50, verbose_name='Sexo')),
                ('address', models.CharField(max_length=100, verbose_name='Direccion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('is_active', models.BooleanField(default=True)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppJuegos.rol', verbose_name='Rol')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['id', 'username', 'cedula', 'names', 'surnames', 'email', 'phone'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('invoice_number', models.CharField(max_length=255)),
                ('qr_code_digits', models.PositiveIntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_ticket_played', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(choices=[('Disponible', 'Disponible'), ('Reclamado', 'Reclamado')], default='Disponible', max_length=100)),
                ('game_start', models.DateTimeField()),
                ('game_end', models.DateTimeField()),
                ('client', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='ticket_client', to='AppJuegos.client')),
                ('game', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='ticket_game', to='AppJuegos.game')),
                ('user_register', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='register_ticket', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Styles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('color_text', models.CharField(choices=[('Black', 'black'), ('White', 'white'), ('Blue', 'blue'), ('Brown', 'brown'), ('Grey', 'grey'), ('Green', 'green'), ('Purple', 'purple'), ('Red', 'red'), ('Yellow', 'yellow')], max_length=50, null=True, verbose_name='color texto')),
                ('font_letter', models.CharField(choices=[('Arial', 'Arial'), ('Times New Roman', 'Times New Roman'), ('Helvetica', 'Helvetica'), ('Cambria', 'Cambria'), ('Century Gothic', 'Century Gothic'), ('Didot', 'Didot'), ('Bodoni', 'Bodoni'), ('Candara', 'Candara'), ('Optima', 'Optima'), ('Quicksand', 'Quicksand'), ('Courier New', 'Courier New'), ('Rockwell', 'Rockwell'), ('Copperplate', 'Copperplate')], max_length=50, null=True, verbose_name='Fuente Letra')),
                ('image_machine_game', models.ImageField(null=True, upload_to='design/', verbose_name='imagen maquina tragamonedas')),
                ('image_background_game', models.ImageField(null=True, upload_to='design/', verbose_name='imagen fondo juego')),
                ('image_logo_game', models.ImageField(null=True, upload_to='design/', verbose_name='imagen logo juego')),
                ('color_background_game', models.CharField(choices=[('Black', 'Black'), ('White', 'White')], default='Black', max_length=50, verbose_name='color de fondo')),
                ('video_screensaver', models.FileField(null=True, upload_to='screensaver/', verbose_name='video Salvapantallas')),
                ('video_autoplay', models.BooleanField(default=True, verbose_name='video autoplay')),
                ('video_loop', models.BooleanField(default=True, verbose_name='video loop')),
                ('title_button_screensaver', models.CharField(max_length=100, null=True, verbose_name='titulo boton salvapantallas')),
                ('scan_code_title', models.CharField(default='Escanear Codigo', max_length=200)),
                ('scan_code_description', models.CharField(default='Puedes escanear el codigo QR de tu ticket', max_length=200)),
                ('title_winner', models.CharField(default='JUEGA OTRA VEZ!', max_length=150, null=True, verbose_name='titulo del ganador')),
                ('description_winner', models.CharField(default='HAS GANADO!', max_length=200, null=True, verbose_name='descripcion ganador juego')),
                ('image_winner', models.FileField(null=True, upload_to='design/', verbose_name='imagen ganador')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppJuegos.game', verbose_name='Juego')),
            ],
        ),
        migrations.CreateModel(
            name='RolPermission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppJuegos.permission', verbose_name='Permiso')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppJuegos.rol', verbose_name='Rol')),
            ],
            options={
                'verbose_name': 'RolPermiso',
                'verbose_name_plural': 'RolPermisos',
                'ordering': ['rol', 'permission'],
            },
        ),
        migrations.CreateModel(
            name='Probabilidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('percent_win', models.PositiveIntegerField(default=0, verbose_name='porcent_win')),
                ('winners_limit', models.PositiveIntegerField(default=0, verbose_name='winners_limit')),
                ('attempts_limit', models.PositiveIntegerField(default=1, verbose_name='numero de intentos')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppJuegos.game', verbose_name='Juego')),
            ],
            options={
                'verbose_name': 'Probabilidad',
                'verbose_name_plural': 'Probabilidades',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('win_match', models.BooleanField(default=False, verbose_name='gano la partida?')),
                ('delivered', models.BooleanField(default=False, verbose_name='entrego el premio?')),
                ('award', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='award', to='AppJuegos.award')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_ticket', to='AppJuegos.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('cedula', models.CharField(db_index=True, max_length=10, verbose_name='Cédula')),
                ('names', models.CharField(max_length=100, verbose_name='Nombres')),
                ('surnames', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('username', models.CharField(db_index=True, max_length=50, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(db_index=True, max_length=100, verbose_name='Correo Electronico')),
                ('password', models.CharField(max_length=255, verbose_name='Contraseña')),
                ('phone', models.CharField(max_length=10, verbose_name='Telefono')),
                ('sex', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], default='Masculino', max_length=50, verbose_name='Sexo')),
                ('address', models.CharField(max_length=100, verbose_name='Direccion')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('is_active', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('rol', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='AppJuegos.rol', verbose_name='Rol')),
            ],
            options={
                'verbose_name': 'historical Usuario',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTicket',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('invoice_number', models.CharField(max_length=255)),
                ('qr_code_digits', models.PositiveIntegerField(default=0)),
                ('date_created', models.DateTimeField(blank=True, editable=False)),
                ('date_ticket_played', models.DateTimeField(blank=True, editable=False)),
                ('state', models.CharField(choices=[('Disponible', 'Disponible'), ('Reclamado', 'Reclamado')], default='Disponible', max_length=100)),
                ('game_start', models.DateTimeField()),
                ('game_end', models.DateTimeField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='AppJuegos.client')),
                ('game', models.ForeignKey(blank=True, db_constraint=False, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='AppJuegos.game')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_register', models.ForeignKey(blank=True, db_constraint=False, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ticket',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalGame',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('start_date', models.DateTimeField(verbose_name='Fecha inicio juego')),
                ('end_date', models.DateTimeField(verbose_name='Fecha fin juego')),
                ('modification_date', models.DateTimeField(null=True, verbose_name='Fecha  modificacion juego')),
                ('name', models.CharField(choices=[('Tragamonedas', 'Tragamonedas')], default='Tragamonedas', max_length=50, verbose_name='Nombre')),
                ('players', models.IntegerField(default=0, verbose_name='Jugadores')),
                ('state', models.CharField(choices=[('Activado', 'Activado'), ('Desactivado', 'Desactivado')], default='Activado', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Juego',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalClient',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('cedula', models.CharField(db_index=True, max_length=10, verbose_name='Cédula')),
                ('names', models.CharField(max_length=100, verbose_name='Nombres')),
                ('surnames', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('email', models.EmailField(db_index=True, max_length=100, verbose_name='Correo Electronico')),
                ('phone', models.CharField(max_length=10, verbose_name='Telefono')),
                ('sex', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], default='Femenino', max_length=50, verbose_name='Sexo')),
                ('address', models.CharField(max_length=500, verbose_name='Direccion')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_client_modify', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que modifica')),
                ('user_client_register', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que registra')),
            ],
            options={
                'verbose_name': 'historical Cliente',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAwardCondition',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('start_date', models.DateTimeField(verbose_name='Fecha inicio premio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha fin premio')),
                ('is_approved', models.BooleanField(default=False)),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('award', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='AppJuegos.award', verbose_name='Premio')),
                ('game', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='AppJuegos.game', verbose_name='Juego')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_modify', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que modifica')),
                ('user_register', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que registra')),
            ],
            options={
                'verbose_name': 'historical CondicionPremio',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAward',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField(max_length=100, verbose_name='Descripcion')),
                ('imagen', models.TextField(max_length=100, verbose_name='Imagen')),
                ('initial_stock', models.IntegerField(verbose_name='Stock inicial')),
                ('condition_stock', models.IntegerField(default=0, verbose_name='Stock Condicionado')),
                ('prizes_awarded', models.IntegerField(default=0, verbose_name='Premios entregados')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('Legendaria', 'Legendaria'), ('Épica', 'Épica'), ('Rara', 'Rara'), ('Común', 'Común')], default='Comun', max_length=50, verbose_name='Categoria')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('game', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='AppJuegos.game', verbose_name='Juego')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_modify', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que modifica')),
                ('user_register', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que registra')),
            ],
            options={
                'verbose_name': 'historical Premio',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='client',
            name='user_client_modify',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_client_modify', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que modifica'),
        ),
        migrations.AddField(
            model_name='client',
            name='user_client_register',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_client_register', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que registra'),
        ),
        migrations.CreateModel(
            name='AwardCondition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateTimeField(verbose_name='Fecha inicio premio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha fin premio')),
                ('is_approved', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppJuegos.award', verbose_name='Premio')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppJuegos.game', verbose_name='Juego')),
                ('user_modify', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modify_award_condition', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que modifica')),
                ('user_register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_register_award_condition', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que registra')),
            ],
            options={
                'verbose_name': 'CondicionPremio',
                'verbose_name_plural': 'CondicionPremios',
                'ordering': ['id', 'award', 'game'],
            },
        ),
        migrations.AddField(
            model_name='award',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppJuegos.game', verbose_name='Juego'),
        ),
        migrations.AddField(
            model_name='award',
            name='user_modify',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modify', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que modifica'),
        ),
        migrations.AddField(
            model_name='award',
            name='user_register',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_register', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que registra'),
        ),
    ]
