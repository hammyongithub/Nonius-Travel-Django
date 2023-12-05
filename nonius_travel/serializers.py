from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import CustomUser

from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class GuestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class ReservationsSerializer(serializers.ModelSerializer):
    guests = GuestsSerializer(many=True)
    payment = PaymentSerializer(many=True)
    card = CardSerializer(many=True)
    class Meta:
        model = Reservations
        fields = '__all__'

class ClientsSerializer(serializers.ModelSerializer):
    client_document = DocumentSerializer(many=True)
    client_contact = ContactSerializer(many=True)
    client_address = AddressSerializer(many=True)
    client_reservation = ReservationsSerializer(many=True)

    class Meta:
        model = Clients
        fields = '__all__'

# LOGIN ///////

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'username', 'password', 'email')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

class InfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'user_language', 'user_currency', 'user_timezone')
        read_only_fields = ('id',)