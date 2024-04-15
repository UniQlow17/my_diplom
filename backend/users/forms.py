from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image', 'first_name', 'last_name', 'email', 'username',]