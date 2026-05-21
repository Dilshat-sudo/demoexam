from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Booking
from .forms import RegisterForm, BookingForm


def index(request):
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна!')
            return redirect('cabinet')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = RegisterForm()
    return render(request, 'booking/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('cabinet')
        else:
            messages.error(request, 'Неверный логин или пароль')
    return render(request, 'booking/login.html', {})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def cabinet(request):
    bookings = Booking.objects.filter(user=request.user)

    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        review = request.POST.get('review')
        if booking_id and review:
            booking = Booking.objects.get(id=booking_id, user=request.user)
            booking.review = review
            booking.save()
            messages.success(request, 'Спасибо за отзыв!')
            return redirect('cabinet')

    return render(request, 'booking/cabinet.html', {'bookings': bookings})


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Заявка отправлена!')
            return redirect('cabinet')
    else:
        form = BookingForm()

    rooms = Room.objects.all()
    return render(request, 'booking/create_booking.html', {'form': form, 'rooms': rooms})