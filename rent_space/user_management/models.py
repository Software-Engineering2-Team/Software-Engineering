from django.contrib.auth.models import AbstractUser
from django.db import models
from rent_space.space_booking.models import Booking, AdSpace


# Create your models here.
class User(AbstractUser):
    saved_listings = models.ManyToManyField(AdSpace, related_name='saved_by')
    booking_history = models.ManyToManyField(Booking, related_name='user_bookings')
    spaces_owned = models.ManyToManyField(AdSpace, related_name='owners')
    # history of bookings made for this users spaces
    # Other fields like name, email, password (inherited from AbstractUser)
