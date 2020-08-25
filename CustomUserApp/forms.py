from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=240)
    display_name = forms.CharField(max_length=20, required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    homepage = forms.URLField(required=False)
    age = forms.IntegerField()