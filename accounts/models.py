from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(r'^010[1-9]\d{7}$')], null=True )
    name = models.TextField(max_length=10, null=True)
    company = models.TextField(max_length=20, null=True)
    is_auth = models.IntegerField('회원권한', default=1)
