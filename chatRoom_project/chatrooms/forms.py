from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SginupForm(UserCreationForm):
   
    class Meta:
        model=User
        fields=['username','password1','password2']

    def clean_username(self):
        username= self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already taken. Please choose another.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Make sure to type the same password twice.')

        return cleaned_data
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Type Username'
        self.fields['username'].help_text = ''
        self.fields['password1'].widget.attrs['placeholder'] = ' Type Password'
        self.fields['password1'].help_text = ''
        self.fields['password2'].widget.attrs['placeholder'] = 'Type Password one more time'
        self.fields['password2'].help_text = ''

    
