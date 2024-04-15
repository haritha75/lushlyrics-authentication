from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth import login as auth_login, logout
from django.core.mail import send_mail

# Create your views here.

def home(request):
    # Your home view logic here
    return render(request, 'home.html') 

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get('next', '')  # Get the 'next' parameter from the URL
            if next_url:
                return redirect(next_url)  # Redirect to the 'next' URL after login
            else:
                return redirect('home')  # Redirect to a default URL if 'next' is not present
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Password recovery view
def password_recovery(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Generate a unique token (not implemented here)
            # Send email with token to the user
            send_mail(
                'Password Recovery',
                'Here is your password recovery token: [TOKEN]',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return redirect('password_reset_done')  # Redirect to password reset done page
    else:
        form = PasswordResetForm()
    return render(request, 'password_recovery.html', {'form': form})



def custom_password_reset_done(request):
    # Your custom logic here
    return render(request, 'custom_password_reset_done.html')


from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

@login_required
def my_secure_view(request):
    # Your view logic here
    return render(request, 'base.html')

@permission_required('app.change_model')
def my_authorized_view(request):
    # Your view logic here
    return render(request, 'login.html')

