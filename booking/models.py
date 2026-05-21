from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name


class Room(models.Model):
    ROOM_TYPES = (
        ('auditorium', 'Аудитория'),
        ('coworking', 'Коворкинг'),
        ('cinema', 'Кинозал'),
    )

    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    capacity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    STATUS = (
        ('new', 'Новая'),
        ('scheduled', 'Мероприятие назначено'),
        ('completed', 'Мероприятие завершено'),
    )

    PAY = (
        ('cash', 'Наличные'),
        ('card', 'Карта'),
        ('transfer', 'Перевод'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateTimeField()
    payment = models.CharField(max_length=20, choices=PAY)
    status = models.CharField(max_length=20, choices=STATUS, default='new')
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заявка {self.id} - {self.user.username}"