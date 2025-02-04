from rest_framework import serializers
from AppJuegos.models import User, ForgotPassword
from rest_framework_simplejwt.tokens import RefreshToken


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = User.objects.get(id=self.user.id)
        return data

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'names', 'surnames')

        
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        RefreshToken(self.token).blacklist()


class ForgotPasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForgotPassword
        exclude = ('created','code',)


class ResetForgotPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    code = serializers.CharField(required=True)


