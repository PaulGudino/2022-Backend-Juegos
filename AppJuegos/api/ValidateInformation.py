from email import message
from AppJuegos.models import (
    User,
    Award,
    Client,
    AwardCondition,
)

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

class ReduceAward:

    message_stock_in_award = []

    def current_stock(self, amount, pk):
        print(amount)
        award = Award.objects.filter(pk=pk).first()
        if award.current_stock < amount:
            self.message_stock_in_award.append('El stock por reservar en la condición no puede ser menor al stock actual')
            error_stock_message = self.message_stock_in_award.copy()
            self.message_stock_in_award.clear()
            return error_stock_message

        award.current_stock = award.current_stock - amount
        award.save()
        return None
        
        
        
        



