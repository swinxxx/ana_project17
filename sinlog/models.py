from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class CountryModel(models.Model):
    type = models.CharField(blank=False, max_length=60)
    name = models.CharField(blank=False, max_length=60)


class DetailsModel(AbstractBaseUser):
    LtdL = 'Limited Liability'
    Part = 'Partnership'
    SolP = 'Sole Proprieter'
    Corp = 'Corporation'
    Type_Choices = (
        (LtdL, 'Limited Liability'),
        (Part, 'Partnership'),
        (SolP, 'Sole Proprieter'),
        (Corp, 'Corporation'),
    )
    type = models.CharField(blank=False, choices=Type_Choices, max_length=60)
    name = models.CharField(blank=False, max_length=60)
    email = models.EmailField(unique=True, blank=False, max_length=80)
    password = models.CharField(blank=False, validators=[MinLengthValidator(8)], max_length=100)
    objects = UserManager()
    is_created = models.BooleanField(default=False)
    country=models.ForeignKey(CountryModel,on_delete=models.CASCADE)
    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'email'
    def __self__(self):
        return "%s" % self.name
    def save(self, *args, **kwargs):
        if not self.is_created:
            self.set_password(self.password)
            self.is_created = True
            # self.save()
        return super(DetailsModel,self).save(*args,**kwargs)


















'''
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        print('HereAuth')
        print(Token.key)
'''