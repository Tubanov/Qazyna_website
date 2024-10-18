from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import ModelForm
from market.models import Article


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-group'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-group'}))

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'price', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-group'}),
            'content': forms.Textarea(attrs={'class': 'form-group'}),
            'price': forms.NumberInput(attrs={'class': 'form-group'}),
            'image': forms.FileInput(attrs={'class': 'form-group'}),
        }