from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cp = self.cleaned_data
        if cp['password'] != cp['password2']:
            raise forms.ValidationError('Hasła nie są identyczne.')
        return cp['password2']
