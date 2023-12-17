from django.db import models
from core.models import User


class Supervisor(models.Model):
    account = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True, related_name='account_set+')
    abbreviated_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.abbreviated_name