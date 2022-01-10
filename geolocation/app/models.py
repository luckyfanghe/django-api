from django.db import models
from django.utils import timezone

class GeoLocation(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, null=False)
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)
    accuracy = models.FloatField(blank=False, null=False)
    address = models.CharField(max_length=120, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'user_location'