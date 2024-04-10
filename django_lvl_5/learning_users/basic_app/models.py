from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # We are using one to one as we already have User setup with the User class.(email, pw, fname, lname)
    # This is only used for additional information.

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(blank=True, upload_to='profile_pics')

    def __str__(self):
        return self.user.username
