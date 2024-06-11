from django.shortcuts import render, redirect
from bookings_app.models import Booking
from bookings_app.forms.bookings_form import BookingsForm

# Create your views here.
def home_page(request):
    return render(request, 'bookings_app/index.html')

def create_booking(request):
    if request.method == 'POST':

        # insttiate the form with post data
        form = BookingsForm(request.POST)

        # validate the form daata
        if form.is_valid():

            # retrieve the cleaned data from the form
            location = form.cleaned_data['location']
            picked_at = form.cleaned_data['picked_at']

            # create the booking
            Booking.objects.create(location=location, picked_at=picked_at)

            # redirect the user to the home page
            return redirect('home_page')
    else:
        form = BookingsForm()

    # render the bookings template with the form data
    return render(request, 'bookings_app/index.html', {'form': form})