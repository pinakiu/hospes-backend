from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

class GuestProfile(models.Model):
    # guest_account = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.IntegerField(null=True, blank=True)
    origin_country = models.IntegerField(null=True, blank=True)
    language = models.IntegerField(null=True, blank=True)
    target_dates = models.JSONField(default=dict, null=True, blank=True)
    target_price = models.FloatField(null=True, blank=True)
    profile_photo = models.ImageField(max_length=50)
    dietary_restrictions = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=2000)

