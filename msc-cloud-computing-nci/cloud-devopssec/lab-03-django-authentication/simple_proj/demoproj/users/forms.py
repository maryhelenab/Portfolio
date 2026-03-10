from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email.endswith('@gmail.com'):
            raise forms.ValidationError(
                "Email must be a Gmail address."
            )

        return email