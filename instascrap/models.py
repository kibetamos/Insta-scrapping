from django.db import models

# Create your models here.
# Create your models here.
class Instagram(models.Model):
    instagramuser = models.CharField(max_length=1000)
    imagelink = models.CharField(max_length=10000)
    username = models.CharField(max_length=1000)

    def __str__(self):
        return self.instagramuser