from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Product, Farm

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'detail']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Ime'
        self.fields['category'].label = 'Kategorija'
        self.fields['detail'].label = 'Detaljno'


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label=_("Email adresa"), widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=_("Lozinka"), strip=False, widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Lozinka', widget=forms.PasswordInput)
    
    ime = forms.CharField(label='Ime', max_length=30)
    prezime = forms.CharField(label='Prezime', max_length=30)
    naziv_opg = forms.CharField(label='Naziv OPG-a', max_length=100)
    adresa = forms.CharField(label='Adresa', max_length=255)
    telefon = forms.CharField(label='Telefon', max_length=20)
    email = forms.EmailField(label='Email')
    email_potvrda = forms.EmailField(label='Potvrdi email')
    lozinka = forms.PasswordInput()
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        del self.fields['password2'] 

    class Meta:
        model = User
        fields = ('ime', 'prezime', 'naziv_opg', 'adresa', 'telefon', 'email', 'email_potvrda', 'password1')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        email_potvrda = cleaned_data.get('email_potvrda')

        if email and email_potvrda and email != email_potvrda:
            self.add_error('email_potvrda', "Emails must match")

        return cleaned_data

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)      #NAPISATI README, 
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user_profile = Farm.objects.create(
                user=user,
                ime=self.cleaned_data['ime'],
                prezime=self.cleaned_data['prezime'],
                naziv_opg=self.cleaned_data['naziv_opg'],
                adresa=self.cleaned_data['adresa'],
                telefon=self.cleaned_data['telefon'],
                email_potvrda=self.cleaned_data['email_potvrda']
            )
        return user


class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['ime', 'prezime', 'naziv_opg', 'adresa', 'telefon']
