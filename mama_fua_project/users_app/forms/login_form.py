from django import forms

class logInForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}), required=False)
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    def clean_email(self):
        email= self.cleaned_data.get('email')

        if email is None or email.strip() == '':
            raise forms.ValidationError("The username cannot remain empty")
        
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")

        if password is None or password.strip() == '':
            raise forms.ValidationError("The password cannot remain empty")
        
        return password