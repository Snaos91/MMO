from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Message, Reaction


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['category', 'title', 'content', ]


class ReactionForm(ModelForm):
    class Meta:
        model = Reaction
        fields = ['text']


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
