from operator import truediv
from django.db import models
from django.forms import SlugField
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser


# Clients and Reservations //////////////////////////////////////////////// 

class Clients(models.Model):
    client_document = models.ManyToManyField('Document', related_name='clients', blank=True)
    client_contact = models.ManyToManyField('Contact', related_name='clients', blank=True)
    client_address = models.ManyToManyField('Address', related_name='clients', blank=True)
    client_reservation = models.ManyToManyField('Reservations', related_name='clients', blank=True)
    name = models.CharField(max_length=255)
    birthdate = models.DateField(max_length=255)
    vat = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        ordering = ['created_at',]

    def __str__(self):
        return self.name or ''

class Document(models.Model):
    number = models.PositiveBigIntegerField()
    expiration_date = models.DateField(max_length=255)
    doctype = models.CharField(max_length=255)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.slug or ''

class Contact(models.Model):
    email = models.EmailField(max_length=255)
    phone = models.PositiveBigIntegerField()
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.slug or ''

class Address(models.Model):
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = CountryField()
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.slug or ''
    
class Reservations(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    active_status = models.CharField(max_length=255)
    confirmation_id = models.CharField(max_length=255)
    checkin_date = models.DateField(max_length=255)
    checkin_time = models.TimeField(default='00:00:00')
    checkout_date = models.DateField(max_length=255)
    checkout_time = models.TimeField(default='00:00:00')
    reservation_guests = models.ManyToManyField('Guests', related_name='reservations', blank=True)
    room_type = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255)
    payment_information = models.ManyToManyField('Payment', related_name='reservations', blank=True)
    policies = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.slug or ''

class Guests(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age_group = models.CharField(max_length=255)
    reservation = models.ForeignKey(Reservations, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.slug or ''
    
class Payment(models.Model):
    method = models.CharField(max_length=255)
    card = models.ManyToManyField('Card', related_name='payments', blank=True)
    reservation = models.ForeignKey(Reservations, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.slug or ''
    
class Card(models.Model):
    number = models.CharField(max_length=255)
    expiration_date = models.DateField(max_length=255)
    vendor = models.CharField(max_length=255)
    reservation = models.ForeignKey(Reservations, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField( )

    def __str__(self):
        return self.slug or ''


# USERS //////////////////////////////////////////////////////////////////

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_currency = models.CharField(default='EUR', max_length=255)
    user_language = models.CharField(default='en', max_length=255)
    user_timezone = models.CharField(default='UTC', max_length=255)