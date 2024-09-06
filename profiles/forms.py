 # 2024/07/18 課題
from django import forms
from django.forms import ModelForm

from profiles.models import Profile


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('self_introduction', )
        widgets = {
          'self_introduction': forms.Textarea(attrs={'rows': 5}),
        }