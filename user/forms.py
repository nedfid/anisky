from django import forms
from django.contrib.auth.models import User
from user.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    email = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UpdateProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    user_avatar = forms.ImageField()
    user_poster = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['bio', 'user_avatar', 'user_poster']