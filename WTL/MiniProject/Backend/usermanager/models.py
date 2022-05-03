from django.db import models
from django.contrib.auth.models import User
import copy
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext_lazy as _


class AccountManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class Account(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=True,
                                  null=False)
    address = models.CharField('address', max_length=255, blank=True,
                                  null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    AUTH_PROVIDERS = [
                    ('customer', 'customer'), 
                    ('seller', 'seller'),
                    ('delivery_personnel', 'delivery_personnel')
                    ]

    category = models.CharField(max_length=255, blank=False, null=False, default='customer',choices=AUTH_PROVIDERS)

    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_UNIQUE_EMAIL = True
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_AUTHENTICATION_METHOD = 'email'

    SITE_ID = 1
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    

    def __str__(self):
        return self.first_name

    def tokens(self):
    #refresh = RefreshToken.for_user(self)
        if Token.objects.filter(user=self).exists():
            token=Token.objects.filter(user=self).first()
            return{
                'token' : token.key
            }
        token=Token.objects.create(user=self)    
        return{
                'token' : token.key
            }