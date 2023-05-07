from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# from App_Dashboard.models import Country


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    # country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country_user_profile", default=None)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    contact = models.CharField(max_length=20, null=True)
    dob = models.DateField(blank=True, null=True)
    status_ = (
        (1, "Active"),
        (2, "Deactivate")
    )
    status = models.IntegerField(choices=status_, null=True)
    type_ = (
        (1, "Customer"),
        (2, "Designer")
    )
    type = models.IntegerField(choices=type_)

    def __str__(self):
        return self.full_name

