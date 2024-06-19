from bookings_app.models import Booking
from django import forms
from datetime import date, timedelta

class BookingsForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pickup_date', 'pickup_time', 'location']
        widgets = {
            'pickup_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'pickup_time': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'placeholder': 'location', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = date.today()
        self.fields['pickup_date'].widget.attrs['min'] = today.isoformat()
        self.fields['pickup_date'].widget.attrs['max'] = (today + timedelta(days=7)).isoformat()

    def clean_pickup_date(self):
        pickup_date = self.cleaned_data.get('pickup_date')

        if pickup_date is None:
            raise forms.ValidationError("The pickup date cannot remain empty")
        
        today = date.today()
        if pickup_date < today:
            raise forms.ValidationError("The pickup date cannot be in the past")
        if pickup_date > today + timedelta(days=7):
            raise forms.ValidationError("The pickup date cannot be more than 7 days in the future")
        
        return pickup_date

    def clean_location(self):
        location = self.cleaned_data.get('location')

        if location is None or location.strip() == '':
            raise forms.ValidationError("The location cannot remain empty")
        
        return location