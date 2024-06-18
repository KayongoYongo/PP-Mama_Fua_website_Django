from django.shortcuts import get_object_or_404 ,render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bookings_app.models import Booking
from bookings_app.forms.bookings_form import BookingsForm

# Create your views here.
@login_required
def user_dashboard(request):
    # Fetch bookings for the current user
    bookings = Booking.objects.filter(user=request.user).values('pickup_date', 'pickup_time', 'location', 'status')

    # Convert bookings to list of events
    events = []
    for booking in bookings:
        # Ensure date is formatted properly
        pickup_date = booking.get('pickup_date')
        if pickup_date:
            events.append({
                'title': f"{booking.get('location', 'No Location')} ({booking.get('status', 'No Status')})",
                'start': pickup_date.isoformat(),
                'description': booking.get('status', 'No Status')
            })

    # Pass bookings to the template
    return render(request, 'bookings_app/user_dashboard.html', {'events': events})

@login_required
def create_booking(request):
    if request.method == 'POST':

        # insttiate the form with post data
        form = BookingsForm(request.POST)

        # validate the form daata
        if form.is_valid():

            user = request.user
            pickup_date = form.cleaned_data['pickup_date']
            pickup_time = form.cleaned_data['pickup_time']
            location = form.cleaned_data['location']

            # create the booking object
            Booking.objects.create(user=user, pickup_date=pickup_date, pickup_time=pickup_time, location=location)

            # redirect the user to the home page
            return redirect('user_dashboard')
    else:
        form = BookingsForm()

    # render the bookings template with the form data
    return render(request, 'bookings_app/create_booking.html', {'form': form})

@login_required
def view_my_booking(request):
    # current user
    user = request.user

    # get the bookings from
    bookings = Booking.objects.filter(user=user).order_by('-created_at')

    return render(request, 'bookings_app/my_bookings.html', {'bookings': bookings})

@login_required
def edit_booking(request, id):
    # retrieve the booking object
    booking = get_object_or_404(Booking, id=id)

    # check if the request method is POST
    if request.method == 'POST':

        # instantiate the form with the dat submitted in the request
        form = BookingsForm(request.POST)

        # validate the form data
        if form.is_valid():

            # retrieve the cleaned data from the form
            pickup_date = form.cleaned_data['pickup_date']
            pickup_time = form.cleaned_data['pickup_time']
            location = form.cleaned_data['location']

            # update the bookings object
            booking.pickup_date = pickup_date
            booking.pickup_time = pickup_time
            booking.location = location

            # save the updated blog object ot the database
            booking.save()

            # display the success message to the user
            messages.success(request, 'Booking updated successfully')

            # redirect the user to the dashboard
            return redirect('user_dashboard')
        
    else:
        # if the request method is GET
        form = BookingsForm(instance=booking)

    # render the booking form with the form and bookings data
    return render(request, 'bookings_app/edit_booking.html', {'form': form, 'booking': booking})

@login_required
def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id)

    # delete the booking
    booking.delete()

    # send the user a message
    messages.success(request, 'Booking deleted successfully')

    # redirect the user to the user dashboard
    return redirect('user_dashboard')