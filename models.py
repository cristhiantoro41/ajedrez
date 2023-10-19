from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chess_score = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def update_chess_score(self, score_change):
        self.chess_score += score_change
        self.save()

    def set_profile_picture(self, image):
        self.profile_picture = image
        self.save()

    def update_last_login(self, login_time):
        self.last_login = login_time
        self.save()













