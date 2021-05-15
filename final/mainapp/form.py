from django import forms

from django.utils.safestring import mark_safe







class signUpForm(forms.Form):
    CHOICES=[('Basic','Basic'),('Advanced','Advanced'),('Extra','Extra')]
    fname = forms.CharField(max_length=100 , label=mark_safe('<br />') , widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    lname = forms.CharField(max_length=100 , label=mark_safe('<br />') , widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    cell = forms.CharField(max_length=100 , label=mark_safe('<br />') , widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
    address = forms.CharField(max_length=400 , label=mark_safe('<br />') , widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    email =  forms.CharField(max_length=100 , label=mark_safe('<br />'),widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    password =  forms.CharField(max_length=100 , label=mark_safe('<br />'), widget=forms.PasswordInput(attrs={'placeholder': 'New password'}))
    plan = forms.CharField(max_length=400 , label=mark_safe('<br />') , widget=forms.TextInput(attrs={'placeholder': 'Plan'}))


class logInForm(forms.Form):
    email =  forms.CharField(max_length=100 , label='Email ',widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    password =  forms.CharField(max_length=100 , label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))

class contactForm(forms.Form):         
    name = forms.CharField(max_length=100 , label=mark_safe('<br />'), widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    cell = forms.CharField(max_length=100 , label=mark_safe('<br />'),  widget=forms.TextInput(attrs={'placeholder': 'Cell phone'}))
    email =  forms.CharField(max_length=100 ,label=mark_safe('<br />'),widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    message =  forms.CharField(max_length=1000 , label=mark_safe('<br />'), widget=forms.Textarea(attrs={'placeholder': 'Your messgae'}))
