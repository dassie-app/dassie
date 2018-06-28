from django.db import models
from django.contrib.auth.models import User

def profile_photo_upload_handler(self, filename):
    return 'static/images/%s/profile.jpg' % (self.user.username)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.ImageField(upload_to=profile_photo_upload_handler, blank=True)
