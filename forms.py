
from django.contrib.auth.models import User
from django.forms import ModelForm, models

from farmproject.farmproject import settings
from .models import Signin


class SigninForm(ModelForm):

    class Meta:
        model = Signin
        fields = '__all__'

class update(SigninForm.ModelForm):

    class Meta:
        model = Signin
        fields = ['username', 'first_name', 'last_name', 'email',  'password']
