from django.db import models

from users.models import CustomUser


class Habbits(models.Model):
    user = models.ForeignKey(
        CustomUser,
        null=True,
        blank=True,
        related_name="habbits",
        on_delete=models.SET_NULL,
    )
    place = models.CharField(max_length=100, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    action = models.CharField(max_length=255)
    is_pleasant_habit = models.BooleanField(null=True, blank=True)
    connected_habbit = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.SET_NULL
    )
    periodicity = models.IntegerField(blank=True, null=True)
    award = models.CharField(max_length=255, blank=True, null=True)
    time_to_do = models.IntegerField(default=120)
    is_public = models.BooleanField(null=True, blank=True)
