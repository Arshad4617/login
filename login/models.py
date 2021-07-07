from django.db import models

# Create your models here.


class Login(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    usr_password = models.CharField(max_length=50, null=True, blank=True)


# class CreateUser(models.Model):
#     user_name = models.CharField(max_length=500, null=True, blank=True)
#     password = models.CharField(max_length=50, null=True, blank=True)
#     re_password = models.CharField(max_length=50, null=True, blank=True)
