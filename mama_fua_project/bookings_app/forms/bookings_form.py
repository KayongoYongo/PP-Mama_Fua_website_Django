from bookings_app.models import Booking
from django import forms

class BookingsForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pickup_date', 'pickup_time', 'location']
        widgets = {
            'pickup_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'pickup_time': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'placeholder': 'location', 'class': 'form-control'}),
        }

    def clean_pickup_date(self):
        pickup_date = self.cleaned_data.get('pickup_date')

        if pickup_date is None:
            raise forms.ValidationError("The pickup date cannot remain empty")
        
        return pickup_date

    def clean_location(self):
        location = self.cleaned_data.get('location')

        if location is None or location.strip() == '':
            raise forms.ValidationError("The location cannot remain empty")
        
        return location