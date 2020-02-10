from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .validators import phone_number_validator
from django.utils.translation import ugettext_lazy as _
from django_jalali.db import models as jmodels

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError('Users must have a phone number')

        user = self.model(
            phone=phone,
        )
        user.is_active = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# App User
class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()
    
    name = models.CharField(max_length=50, blank=True)
    
    phone = models.CharField(max_length=16, primary_key=True, validators=[phone_number_validator])
    
    email = models.EmailField(blank=True)

    attempts = models.IntegerField(blank=True, null=True, default=0)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    isInvestor = models.BooleanField('نماینده سرمایه گذار', default=False)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return self.name

    def get_short_name(self):
        """ Returns the short name for the user. """
        return self.first_name

    def get_attempts(self):
        """ Returns the short name for the user. """
        return self.attempts

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


# only will receive Emails from us!
class Subscriber(models.Model):
    ip = models.GenericIPAddressField(default='0.0.0.0')
    email = models.EmailField()
    dateRegistered = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Date Registered')

    class Meta:
        verbose_name = 'مشترک'
        verbose_name_plural = 'مشترکان خبرنامه'

