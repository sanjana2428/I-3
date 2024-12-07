from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser,Review, ProviderResponse

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

class LoginForm(AuthenticationForm):
    pass

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']

class ProviderResponseForm(forms.ModelForm):
    class Meta:
        model = ProviderResponse
        fields = ['response_text']
