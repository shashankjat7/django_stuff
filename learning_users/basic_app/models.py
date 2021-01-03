from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    # this is done to add some more info to the model like the profile image, we use a one to one
    # relationship to not confuse the database about existing more than one same users.
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username



