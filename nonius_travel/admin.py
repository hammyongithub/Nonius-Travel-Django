from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

class ContactInline(admin.TabularInline):
    model = Contact 
class DocumentInline(admin.TabularInline):
    model = Document
class AddressInline(admin.TabularInline):
    model = Address
class ReservationsInline(admin.TabularInline):
    model = Reservations
class ClientsAdmin(admin.ModelAdmin):
    inlines = [ContactInline, DocumentInline, AddressInline, ReservationsInline]
    list_display = ('name', 'birthdate', 'created_at')
    prepopulated_fields = {'slug': ('name',)}


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'user_currency', 'user_language', 'user_timezone')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserAdmin.fieldsets[0][1]['fields'] + ('user_currency', 'user_language', 'user_timezone')

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_currency', 'user_language', 'user_timezone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'user_currency', 'user_language', 'user_timezone')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)



admin.site.register(Clients, ClientsAdmin)
admin.site.register(Document)
admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(Reservations)
admin.site.register(Guests)
admin.site.register(Payment)
admin.site.register(Card)