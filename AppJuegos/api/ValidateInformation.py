from AppJuegos.models import (
    User,
    Award,
    Client,
    AwardCondition,
    Game,
    Ticket
)
from datetime import datetime

class ValidateUserRelationships:
    def __init__(self, pk):
        self.pk = pk

    def validate(self):
        user_award_register = Award.objects.filter(user_register=self.pk).first()
        user_award_modify = Award.objects.filter(user_modify=self.pk).first()
        user_client_register = Client.objects.filter(user_client_register=self.pk).first()
        user_client_modify = Client.objects.filter(user_client_modify=self.pk).first()
        if user_award_register or user_award_modify or user_client_register or user_client_modify:
            return True
        return False

class ValidateUserinClient:

    message_user_in_client = list()

    def cedula(self, cedula):
        cedula_client = Client.objects.filter(cedula=cedula).first()
        if cedula_client:
            self.message_user_in_client.append('La cedula ya existe en la sección de clientes')
        print(self.message_user_in_client)

    def email(self, email):
        email_client = Client.objects.filter(email=email).first()
        if email_client:
            self.message_user_in_client.append('El email ya existe en la sección de clientes')
        print(self.message_user_in_client)

    def validate(self):
        if self.message_user_in_client:
           error_user_message = self.message_user_in_client.copy()
           self.message_user_in_client.clear()
           return error_user_message
        return False

class ValidateClientinUser:

    message_client_in_user = []

    def cedula(self, cedula):
        cedula_user = User.objects.filter(cedula=cedula).first()
        if cedula_user:
            self.message_client_in_user.append('La cedula ya existe en la sección de usuarios')

    def email(self, email):
        email_user = User.objects.filter(email=email).first()
        if email_user:
            self.message_client_in_user.append('El email ya existe en la sección de usuarios')

    def validate(self):
        if self.message_client_in_user:
           error_client_message = self.message_client_in_user.copy()
           self.message_client_in_user.clear()
           return error_client_message
        return False

class ValidateAwardRelationships:
    
        def __init__(self, pk):
            self.pk = pk

        def validate(self):
            award_condition = AwardCondition.objects.filter(award=self.pk).first()
            if award_condition:
                return True
            return False

# Logica Award y AwardCondition

class ReduceAwardInitialStock:

    message_stock_in_award = []

    def initial_stock(self, pk):
        award = Award.objects.filter(pk=pk).first()
        if award.initial_stock < 1:
            self.message_stock_in_award.append('No hay stock disponible para reservar')
            error_stock_message = self.message_stock_in_award.copy()
            self.message_stock_in_award.clear()
            return error_stock_message

        award.initial_stock = award.initial_stock - 1
        award.condition_stock = award.condition_stock + 1
        award.save()
        return None
        
class AddAwardInitialStock:

    def initial_stock(self, pk):
        award = Award.objects.filter(pk=pk).first()
        award.initial_stock = award.initial_stock + 1
        award.condition_stock = award.condition_stock - 1
        award.save()
        return None

class ValidateGameRelationships:
        def __init__(self, pk):
            self.pk = pk

        def validate(self):
            award = Award.objects.filter(game=self.pk).first()
            award_condition = AwardCondition.objects.filter(award=self.pk).first()
            if award_condition or award:
                return True
            return False    


class ValidateAwardConditionDateinGame:

    message_award_condition_date = []

    def validate(self, id_game,start_date, end_date):
        awards_conditions = AwardCondition.objects.filter(
            game_id=id_game,
            is_approved = True,
            )
        if len(start_date) == 19:
            start_date = datetime.strptime(start_date.replace('T', ' '), '%Y-%m-%d %H:%M:%S')
            end_date = datetime.strptime(end_date.replace('T', ' '), '%Y-%m-%d %H:%M:%S')
        else:
            start_date = datetime.strptime(start_date.replace('T', ' '), '%Y-%m-%d %H:%M')
            end_date = datetime.strptime(end_date.replace('T', ' '), '%Y-%m-%d %H:%M')

        for award_condition in awards_conditions:

            if start_date >= award_condition.start_date:
                self.message_award_condition_date.append('Hay una condición de premio que tiene una fecha de inicio menor a la fecha de inicio actual del juego')
                error_message = self.message_award_condition_date.copy()
                self.message_award_condition_date.clear()
                return error_message
            if end_date <= award_condition.end_date:
                self.message_award_condition_date.append('Hay una condición de premio que tiene una fecha de fin mayor a la fecha de fin actual del juego')
                error_message = self.message_award_condition_date.copy()
                self.message_award_condition_date.clear()
                return error_message
        return None

class ValidateTicketInvoice:

    message_ticket_invoice = []


    def validate(self, invoice, id_client):
        ticket = Ticket.objects.filter(
            invoice_number=invoice,
            state= "Disponible",
            client = id_client
            )
        print(ticket)
        print(self.message_ticket_invoice)
        if ticket:
            self.message_ticket_invoice.append('El cliente ya tiene resgistro ese número de factura')
            error_message = self.message_ticket_invoice.copy()
            print('Dentro del if')
            print(self.message_ticket_invoice)
            self.message_ticket_invoice.clear()
            return error_message
        return None
        


        

        
        
        



