# Base user class with generic fields (username, email, first_name, last_name, staff_status)
from django.contrib.auth.models import User

from django import forms


# Creating a blueprint from forms
# Customized User class
class UserForm(forms.ModelForm):
    # Tells password is an input of type password
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:  # Information abut your class
        model = User
        fields = ['username', 'email', 'password']
