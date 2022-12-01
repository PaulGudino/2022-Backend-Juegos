# Generated by Django 4.1 on 2022-09-02 18:46

from django.db import migrations
from django.contrib.auth.hashers import make_password
from datetime import date




class Migration(migrations.Migration):

    dependencies = [
        ('AppJuegos', '0001_initial'),
    ]

    def insert_data(apps, schema_editor):
        Permission = apps.get_model('AppJuegos', 'Permission')
        Rol = apps.get_model('AppJuegos', 'Rol')
        User = apps.get_model('AppJuegos', 'User')
        RolPermission = apps.get_model('AppJuegos', 'RolPermission')
        Game = apps.get_model('AppJuegos', 'Game')
        Styles = apps.get_model('AppJuegos', 'Styles')
        Publicity = apps.get_model('AppJuegos', 'Publicity')

		# ==================================================================================================================
		# Client permissions
        
        client_create_permission = Permission(name='Crear Cliente')
        client_view_permission = Permission(name='Ver Cliente')
        client_edit_permission = Permission(name='Editar Cliente')
        client_delete_permission = Permission(name='Eliminar Cliente')

        # ==================================================================================================================
		# Award permissions

        award_create_permission = Permission(name='Crear Premio')
        award_view_permission = Permission(name='Ver Premio')
        award_edit_permission = Permission(name='Editar Premio')
        award_delete_permission = Permission(name='Eliminar Premio')

		# ==================================================================================================================
        # Ticket permissions

        ticket_create_permission = Permission(name='Crear Ticket')
        ticket_view_permission = Permission(name='Ver Ticket')
        ticket_edit_permission = Permission(name='Editar Ticket')
        ticket_delete_permission = Permission(name='Eliminar Ticket')

        # ==================================================================================================================
        # AwardCondition permissions

        award_condition_create_permission = Permission(name='Crear Condicion de Premio')
        award_condition_view_permission = Permission(name='Ver Condicion de Premio')
        award_condition_edit_permission = Permission(name='Editar Condicion de Premio')
        award_condition_delete_permission = Permission(name='Eliminar Condicion de Premio')

                
        client_create_permission.save()
        client_view_permission.save()
        client_edit_permission.save()
        client_delete_permission.save()

        award_create_permission.save()
        award_view_permission.save()
        award_edit_permission.save()
        award_delete_permission.save()

        ticket_create_permission.save()
        ticket_view_permission.save()
        ticket_edit_permission.save()
        ticket_delete_permission.save()

        award_condition_create_permission.save()
        award_condition_view_permission.save()
        award_condition_edit_permission.save()
        award_condition_delete_permission.save()
        

        
		# ==================================================================================================================
        
        
        admin_rol = Rol(name='Administrador', description='Administrador del sistema')
        admin_rol.save()

        admin_user = User(
            username='admin',
            cedula='0000000000',
            names='Administrador',
            surnames='Sistema',
            email = 'admin@admin.com',
            password=make_password('admin'),
            phone='0000000000',
            sex='M',
            address='Administrador',
            rol= admin_rol
        )
        admin_user.save()

        # Creating a Game

        game_tragamonedas = Game(
            start_date =  "2022-11-08T00:00:00",
            end_date = "2029-12-13T12:12:00",
        )

        game_tragamonedas.save()

        #Create default Styles
        
        default_styles = Styles(
            game_id = Game.objects.all().first(),
            color_text = 'White',
            font_letter ='Arial',
            title_button_screensaver='Click para Jugar'
            
        )
        default_styles.save()

        #Create defaul publicity
        default_publicity_top = Publicity(
            created = date.today()
        )
        default_publicity_bottom = Publicity(
            created = date.today()
        )
        default_publicity_top.save()
        default_publicity_bottom.save()


        
        RolPermission_1 =  RolPermission(rol_id=admin_rol.id, permission_id=client_create_permission.id)
        RolPermission_2 =  RolPermission(rol_id=admin_rol.id, permission_id=client_view_permission.id)
        RolPermission_3 =  RolPermission(rol_id=admin_rol.id, permission_id=client_edit_permission.id)
        RolPermission_4 =  RolPermission(rol_id=admin_rol.id, permission_id=client_delete_permission.id)

        RolPermission_5 =  RolPermission(rol_id=admin_rol.id, permission_id=award_create_permission.id)
        RolPermission_6 =  RolPermission(rol_id=admin_rol.id, permission_id=award_view_permission.id)
        RolPermission_7 =  RolPermission(rol_id=admin_rol.id, permission_id=award_edit_permission.id)
        RolPermission_8 =  RolPermission(rol_id=admin_rol.id, permission_id=award_delete_permission.id)

        RolPermission_9 = RolPermission(rol_id=admin_rol.id, permission_id=ticket_create_permission.id)
        RolPermission_10 = RolPermission(rol_id=admin_rol.id, permission_id=ticket_view_permission.id)
        RolPermission_11 = RolPermission(rol_id=admin_rol.id, permission_id=ticket_edit_permission.id)
        RolPermission_12 = RolPermission(rol_id=admin_rol.id, permission_id=ticket_delete_permission.id)

        RolPermission_13 = RolPermission(rol_id=admin_rol.id, permission_id=award_condition_create_permission.id)
        RolPermission_14 = RolPermission(rol_id=admin_rol.id, permission_id=award_condition_view_permission.id)
        RolPermission_15 = RolPermission(rol_id=admin_rol.id, permission_id=award_condition_edit_permission.id)
        RolPermission_16 = RolPermission(rol_id=admin_rol.id, permission_id=award_condition_delete_permission.id)

		# ==================================================================================================================

        RolPermission_1.save()
        RolPermission_2.save()
        RolPermission_3.save()
        RolPermission_4.save()

        RolPermission_5.save()
        RolPermission_6.save()
        RolPermission_7.save()
        RolPermission_8.save()

        RolPermission_9.save()
        RolPermission_10.save()
        RolPermission_11.save()
        RolPermission_12.save()

        RolPermission_13.save()
        RolPermission_14.save()
        RolPermission_15.save()
        RolPermission_16.save()

		# ==================================================================================================================
    
    
    operations = [
        migrations.RunPython(insert_data),
    ]