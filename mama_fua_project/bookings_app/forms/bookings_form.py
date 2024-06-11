from bookings_app.models import Booking
from django import forms

class BookingsForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['picked_at', 'location', ]
        widgets = {
            'picked_at': forms.HiddenInput(),
            'location': forms.TextInput(attrs={'placeholder': 'location', 'class': 'form-control'}),
        }

    def clean_picked_at(self):
        picked_at = self.cleaned_data.get('picked_at')

        if picked_at is None or picked_at.strip() == '':
            raise forms.ValidationError("The picked date cannot remain empty")
        
        return picked_at

    def clean_location(self):
        location = self.cleaned_data.get('location')

        if location is None or location.strip() == '':
            raise forms.ValidationError("The location cannot remain empty")
        
        return location