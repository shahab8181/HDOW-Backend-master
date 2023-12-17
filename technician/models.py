from django.db import models
from core.models import User


class Technician(models.Model):

    GENDER_CHOICES = (
    (1, 'Male'),
    (2, 'Female'),
    )

    account = models.OneToOneField(User,blank=True, null=True,on_delete=models.CASCADE, related_name='technicians')
    address = models.CharField(max_length=150,blank=True,null=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES,blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    birthdate = models.DateField(blank=True,null=True)

    def __str__(self) -> str:
        return self.account.first_name + self.account.last_name