from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import TextInput, PasswordInput

class signUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "password1",
            "password2", 
        ]

        error_messages = {
            'username': {'required': ""},
            'email': {'required': ""},
            'password1': {'required': ""},
            'password2': {'required': ""},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove HTML form validation
        self.fields['username'].widget = TextInput(attrs={'placeholder': 'Username', 'class':'form-control'})
        self.fields['email'].widget = TextInput(attrs={'placeholder': 'Email address', 'class':'form-control'})
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Confirm Password', 'class':'form-control', 'cols' : 20})


        # Remove HTML form validation
        self.fields['email'].required = False
        self.fields['username'].required = False
        self.fields['password1'].required = False
        self.fields['password2'].required = False
    
    # Form validation
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email is None or email.strip() == '':
            raise forms.ValidationError("The email cannot remain empty")
        
        # Get the user model
        User = get_user_model()
        
        # Check if the email exists
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        
        return email
    
    def clean_username(self):
        username =  self.cleaned_data.get('username')

        if username is None or username.strip() == '':
            raise forms.ValidationError("The user name cannot remain empty")
        return username
  
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        if password1 is None or password1.strip() == '':
            raise forms.ValidationError("The password cannot remain empty")
        
        if len(password1) < 6:
            raise forms.ValidationError("The password cannot be less than 6 characters")
        
        return password1
    
    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")

        if password2 is None or password2.strip() == '':
            raise forms.ValidationError("The password cannot remain empty")
        
        return password2
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data