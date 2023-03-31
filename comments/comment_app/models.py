from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    # add additional fields in here
    age=models.CharField(max_length=3)
    address=models.TextField()
    phone_number=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.username

class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    Comment=models.TextField()
    created_date=models.DateTimeField(auto_now_add =True)
    def __str__(self):
        return self.user.first_name