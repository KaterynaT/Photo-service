# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User
from rango.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
        
class DocumentForm(forms.Form):
    docfile = forms.ImageField(label='Select a file',)
    
class ParametresForm(forms.Form):
    x = forms.CharField(max_length=100)
    y = forms.CharField(max_length=100)
    angle = forms.CharField(max_length=100)
    width = forms.CharField(max_length=100)
    height = forms.CharField(max_length=100)