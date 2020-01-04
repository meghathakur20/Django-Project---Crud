from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from passlib.hash import pbkdf2_sha256

# Create your models here.


class Signin(AbstractUser):
    first_name = models.CharField(max_length=20, blank=True,null=True)
    last_name = models.CharField(max_length=20, blank=True,null=True)
    email= models.EmailField(max_length=255, unique=True,blank=True,null=True)
    username = models.CharField(max_length=20, default='',unique=True, blank=True,null=True )
    password = models.CharField(max_length=256, blank=True,null=True )
    objects = UserManager()
    search_fields = ('email', 'first_name','username')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
    class Meta:
        db_table = 'Signin'

