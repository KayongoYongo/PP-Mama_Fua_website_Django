from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render, redirect
from users_app.forms.signup_form import signUpForm
from users_app.forms.login_form import logInForm

# Create your views here.
def home_page(request):
    return render(request, 'users_app/index.html')

# Define a method for traditional sign up
def sign_up(request):
    if request.method == 'POST':

        # Instantiate the form with POST data
        form = signUpForm(request.POST)

        if form.is_valid():
            # If the form data is valid, sanitize it
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            # Get the user model
            User = get_user_model()

            # Create a user instance in the database
            User.objects.create_user(username=username, email=email, password=password)

            # This is a success message that is sent upon succesfull signup
            messages.success(request, "Sign up successful! Please log in")

            return redirect('log_in')
    else:
        # if it is a GET request, we can render an empty form
        form = signUpForm()

    # Reder the sign up form either (either empty or with errors)
    return render(request, 'users_app/sign_up.html', {'form': form})

# Define a method for log in
def log_in(request):
    if request.method == 'POST':

        # Instantiate the form with POST data
        form = logInForm(request.POST)

        if form.is_valid():
            # if the form data is valid, sanitize the daata
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # check if the "remeber me" checkbox is checked
            remember_me = form.cleaned_data.get('remember_me')

            user = authenticate(request, email=email, password=password)

            if user is not None:

                # if authentication is successful, log the user in
                login(request, user)

                # set the remember me value
                if remember_me:
                    request.session.set_expiry(settings.SESSION_COOKIE_AGE)
                else:
                    request.session.set_expiry(0)

                # redirect the user
                return redirect('user_dashboard')
            
            else:
                # if the authentication failes, add a non field errr to the form
                form.add_error(None, "Invalid email or password")

    else:
        # if it is a GET request, render an empty form
        form = logInForm()

    # Render the log in page either(empty or with errors)
    return render(request, 'users_app/log_in.html', {'form': form})

# Define the method for rendering out the log in page
def logout_page(request):
    logout(request)
    return redirect('home_page')