from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#custom form for new user registration
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] =  'form-control'
        self.fields['password1'].widget.attrs['class'] =  'form-control'
        self.fields['password2'].widget.attrs['class'] =  'form-control'

#custom form for login as a user
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username","class": "form-control"}), error_messages={'required': 'The username field is required.'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password","class": "form-control"}), error_messages={'required': 'The password field is required.'})
    remember_me = forms.BooleanField(required=False)