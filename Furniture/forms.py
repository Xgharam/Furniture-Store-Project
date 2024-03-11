from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class Register(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username', 'email', 'password1', 'password2')
        help_texts={
            'username':None,
        }
        
class Login(AuthenticationForm):
    class Meta:
        model=User
        fields=('username','password')