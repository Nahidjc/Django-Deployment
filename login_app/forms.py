from django.contrib.auth.models import User
from django import forms
from login_app.models import UserInfo
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    username = forms.CharField(max_length=50)
    class Meta():
        model = User
        fields = ('username', 'email','password')

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('facebook_id','profile_pic')
